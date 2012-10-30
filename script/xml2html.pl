#!/usr/bin/env perl
#author:terrencehan(hanliang1990@gmail.com)
#This script is used to extract datas from .xml
#and .spec files and generate the responding .html
#files. If you find any bug, PLEASE report is to
#my email :)

use XML::Twig;
use Data::Dump qw/dump/;
use File::Slurp;
use File::Spec;
use File::Find qw/find/;
use strict;
use warnings;
use 5.010;

my $delete_en = 0;

my $layout = read_file('./layout/default.html');
my $app    = "";
my %spec;

my @erldocs_index;

my @xml_files;

sub wanted {
    push @xml_files, $File::Find::name if $File::Find::name =~ /\.xml$/;
}
find \&wanted, './xml_doc/';

handle_a_file($_) for sort @xml_files;

my $erldocs_index_str = dump \@erldocs_index;
$erldocs_index_str =~ s/"(.*?)"/[$1]/g;
write_file( './js/erldocs_index.js',
    "var index = " . $erldocs_index_str . ";" );

#script ends here, the followings are definitions of functions

sub handle_a_file {
    my ($xml_file) = @_;
    my @path_pieses = split '/', $xml_file;

    $app = $path_pieses[ $#path_pieses - 1 ];
    my $temp = "'app', '$app', '$app', '[application]'";
    push( @erldocs_index, $temp ) unless $temp ~~ @erldocs_index;

    #generate spec file path by $xml_file
    my $spec_file =
      File::Spec->catfile( 'specs',
        @path_pieses[ $#path_pieses - 1 .. $#path_pieses ] );
    my $html_file =
      File::Spec->catfile( @path_pieses[ $#path_pieses - 1 .. $#path_pieses ] );
    $spec_file =~ s/xml/spec/;
    $html_file =~ s/xml/html/;

    my $spec_text = read_file($spec_file);
    my @specs = split /\n\n/, $spec_text;
    undef %spec;    #reset %spec for every file
    for (@specs) {
        if (/name:(?<name>.*?)\ndef:(?<def>.*?)($|(\ntypes:\n(?<types>.*)))/s) {
            $spec{ $+{name} }->{def}   = $+{def};
            $spec{ $+{name} }->{types} = $+{types} if defined $+{types};
        }else{die 'spec regexp not match'}
    }
    my $res      = $layout;
    my $xml_html = xml_to_html($xml_file);

    $res =~ s/{{content}}/$xml_html/;

    write_file( $html_file, $res );
}

sub xml_to_html {
    my $xml_file = shift;
    my $t = XML::Twig->new( pretty_print => 'indented' );
    $t->parsefile($xml_file);
    my $root = $t->root;
    $root->set_tag('div');
    $root->set_att( style => "margin:0px; padding:10px 20px" );

    my $module = $root->first_child('module');
    if ($module) {
        $module->set_tag('h1');
        my $temp = "'mod', '$app', '${\$module->text}', []";
        push( @erldocs_index, $temp ) unless $temp ~~ @erldocs_index;
    }

    if ( my $header = $root->first_child('header') ) {
        $header->delete;
    }

    if ( my $modulesummary = $root->first_child('modulesummary') ) {
        $modulesummary->set_tag('h2');
        $modulesummary->set_att( class => "modsummary" );
    }

    ##################
    #simple repalce
    for my $block (qw/note warning/) {
        for ( $root->getElementsByTagName($block) ) {
            $_->set_tag('div');
            $_->set_att( class => $block );
            my $new_node = XML::Twig::Elt->new('h2');
            $new_node->set_inner_xml("${\ucfirst($block)}:<br/>");
            $new_node->paste($_);
        }
    }

    $_->set_att( class => 'english' ) for ( $root->getElementsByTagName('p') );
    $_->set_tag('p') for ( $root->getElementsByTagName('p_zh') );

    if ($delete_en) {
        for ( $root->getElementsByTagName('p') ) {
            $_->delete;
        }
    }

    $_->set_tag('span') for ( $root->getElementsByTagName('input') );
    $_->set_tag('dt')   for ( $root->getElementsByTagName('tag') );

    for ( $root->getElementsByTagName('code') ) {
        $_->set_tag('pre');
        $_->del_atts;
    }
    $_->set_tag('code') for $root->getElementsByTagName('c');

    ##################

    if ( my $description = $root->first_child('description') ) {
        $description->set_tag('div');
        $description->set_att( class => "description" );
    }

    if ( my $funcs = $root->first_child('funcs') ) {
        $funcs->set_tag('div');
        $funcs->set_att( class => "functions" );

        my $new_node = XML::Twig::Elt->new('hr');
        $new_node->paste($funcs);

        $new_node = XML::Twig::Elt->new('h4');
        $new_node->set_inner_xml("Functions:");
        $new_node->paste($funcs);

        for my $func ( $funcs->children('func') ) {

            #if reach here, $func must be defined.dont need to check
            $func->set_tag('div');
            $func->set_att( class => "function" );

            #if ( my $name = $func->first_child('name') ) {
            for my $name ( $func->children('name') ) {
                if (    $name->att_exists('arity')
                    and $name->att_exists('name') )
                {
                    my $name_name  = $name->att('name');
                    my $name_arity = $name->att('arity');

                    if ( $spec{ $name_name . '/' . $name_arity }->{def} ) {
                        my $str =
                          $spec{ $name_name . '/' . $name_arity }->{def};
                        $name->set_inner_xml($str);
                        $name->set_att( id => $name_name . '/' . $name_arity );
                        if ( $spec{ $name_name . '/' . $name_arity }->{types} )
                        {
                            $new_node = XML::Twig::Elt->new('div');
                            $str =
                              $spec{ $name_name . '/' . $name_arity }->{types};
                            $str =~ s/\n/<br\/>/g;
                            $new_node->set_inner_xml($str);
                            $new_node->paste( after => $name );
                            $new_node->set_att( class => 'type_desc' );
                        }
                    }
                    my $temp =
"'fun', '$app', '${\$module->text}:$name_name/$name_arity', []";
                    push( @erldocs_index, $temp )
                      unless $temp ~~ @erldocs_index;
                }
                else {    #extract name and type in xml file directely
                    my $type = $func->first_child('type');
                    if ( $name->text =~ /(?<fun_name>.*?)\s*\((?<args>.*?)\)/ )
                    {
                        my $id = $+{fun_name} . '/' . scalar split /,/,
                          $+{args};
                        $name->set_att( id => $id );
                        my $temp = "'fun', '$app', '${\$module->text}:$id', []";
                        push( @erldocs_index, $temp )
                          unless $temp ~~ @erldocs_index;
                    }
                    if ($type) {
                        for ( $type->children('v') ) {
                            $_->set_tag('div');
                            $_->set_att( class => 'type_desc' );
                        }
                    }
                }

                $name->set_tag('h3');
            }

            if ( my $fsummary = $func->first_child('fsummary') ) {
                $fsummary->delete;
            }

            if ( my $desc = $func->first_child('desc') ) {
                $desc->set_tag('div');
                $desc->set_att( class => 'discription' );

            }

        }
    }

    my $res_str;
    open my $str_fd, ">", \$res_str;
    $root->print($str_fd);
    $res_str;
}
