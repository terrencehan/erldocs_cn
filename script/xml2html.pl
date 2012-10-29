#!/usr/bin/env perl

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
my %spec;
my $erldocs_index = ""

my @xml_files;
sub wanted {
    push @xml_files, $File::Find::name if $File::Find::name =~ /\.xml$/;
}
find \&wanted, './xml_doc/';

handle_a_file($_) for @xml_files;

#script ends here, the followings are definitions of functions

sub handle_a_file {
    my ($xml_file) = @_;
    my @path_pieses = split '/', $xml_file;
    my $spec_file =
      File::Spec->catfile( 'specs',
        @path_pieses[ $#path_pieses - 1 .. $#path_pieses ] )
      ;    #generate spec file path by $xml_file
    $spec_file =~ s/xml/spec/;
    my $html_file =
      File::Spec->catfile( @path_pieses[ $#path_pieses - 1 .. $#path_pieses ] )
      ;    #generate html file path by $xml_file
    $html_file =~ s/xml/html/;

    my $spec_text = read_file($spec_file);
    my @specs = split /\n\n/, $spec_text;

    undef %spec;    #reset %spec for every file
    for (@specs) {
        if (/name:(?<name>.*?)\ndef:(?<def>.*?)\n(types:\n(?<types>.*))?/s) {
            $spec{ $+{name} }->{def}   = $+{def};
            $spec{ $+{name} }->{types} = $+{types};
        }
    }
    my $res      = $layout;
    my $xml_html = xml_to_html($xml_file);

    $res =~ s/{{content}}/$xml_html/;

    write_file( $html_file, $res );
}

sub xml_to_html {
    my $t = XML::Twig->new( pretty_print => 'indented' );
    my $xml_file = shift;
    $t->parsefile($xml_file);
    my $root = $t->root;
    $root->set_tag('div');
    $root->set_att( style => "margin:0px; padding:10px 20px" );

    my $module = $root->first_child('module');
    if ( defined $module ) {
        $module->set_tag('h1');
    }

    my $header = $root->first_child('header');
    if ( defined $header ) {
        $header->delete;
    }

    my $modulesummary = $root->first_child('modulesummary');
    if ( defined $modulesummary ) {
        $modulesummary->set_tag('h2');
        $modulesummary->set_att( class => "modsummary" );
    }

    my $description = $root->first_child('description');
    if ( defined $description ) {
        $description->set_tag('div');
        $_->set_tag('p') for $description->children('p_zh');

        for ( $description->children('p') ) {
            $_->set_tag('code') for $_->children('c');
        }
        $description->set_att( class => "description" );

        #$description->print;
    }

    my $funcs = $root->first_child('funcs');
    if ( defined $funcs ) {
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

            my $name = $func->first_child('name');
            if ( defined $name ) {
                if (    $name->att('arity')
                    and $name->att('name') )
                {
                    my $name_name  = $name->att('name');
                    my $name_arity = $name->att('arity');

                    #$name->delete;
                    my $str = $spec{ $name_name . '/' . $name_arity }->{def};
                    $name->set_inner_xml($str);
                    $name->set_att( id => $name_name . '/' . $name_arity );
                    $new_node = XML::Twig::Elt->new('div');
                    $str = $spec{ $name_name . '/' . $name_arity }->{types};
                    $str =~ s/\n/<br\/>/g;
                    $new_node->set_inner_xml($str);
                    $new_node->paste( after => $name );
                    $new_node->set_att( class => 'type_desc' );
                }
                else {    #extract name and type in xml file directely
                    my $type = $func->first_child('type');
                    if ( $name->text =~ /(?<fun_name>.*?)\s*\((?<args>.*?)\)/ )
                    {
                        my $id = $+{fun_name} . '/' . scalar split /,/,
                          $+{args};
                        $name->set_att( id => $id );
                    }
                    for ( $type->children('v') ) {
                        $_->set_tag('div');
                        $_->set_att( class => 'type_desc' );
                    }
                }

                $name->set_tag('h3');
            }

            my $fsummary = $func->first_child('fsummary');
            $fsummary->delete if defined $fsummary;

            my $desc = $func->first_child('desc');
            if ( defined $desc ) {
                $desc->set_tag('div');
                $desc->set_att( class => 'discription' );

                for ( $desc->children('code') ) {
                    $_->set_tag('pre');
                    $_->del_atts;
                }

                for ( $desc->children('pre') ) {
                    for ( $_->children('input') ) {
                        $_->set_tag('span');
                    }
                }

                eval { $_->delete for $desc->children('p') }
                  if $delete_en;

                $_->set_att( class => 'english' ) for $desc->children('p');
                $_->set_tag('p') for $desc->children('p_zh');
                for ( $desc->children('p') ) {
                    $_->set_tag('code') for $_->children('c');
                }

                for ( $desc->children('warning') ) {
                    $_->set_att( class => 'english' ) for $_->children('p');
                    eval { $_->delete for $_->children('p') }
                      if $delete_en;
                    $_->set_tag('div');
                    $_->set_att( class => 'warning' );
                    my $new_node = XML::Twig::Elt->new('h2');
                    $new_node->set_inner_xml("Warning:<br/>");
                    $new_node->paste($_);
                    $_->set_tag('p') for $_->children('p_zh');
                }

                for ( $desc->children('note') ) {
                    eval { $_->delete for $_->children('p') }
                      if $delete_en;
                    $_->set_tag('div');
                    $_->set_att( class => 'note' );
                    my $new_node = XML::Twig::Elt->new('h2');
                    $new_node->set_inner_xml("Note:<br/>");
                    $new_node->paste($_);
                    $_->set_tag('p') for $_->children('p_zh');
                }

            }

        }
    }

    my $res_str;
    open my $str_fd, ">", \$res_str;
    $root->print($str_fd);
    $res_str;
}
