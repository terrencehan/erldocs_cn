#!/use/bin/env perl

use XML::Twig;
use Data::Dump qw/dump/;
use File::Slurp;
use File::Find qw/find/;
use strict;
use warnings;

my $delete_en = 1;


my $layout   = read_file('./layout.html');
my $res      = $layout;
my $xml_html = xml_to_html('./lists.xml');

$res =~ s/{{content}}/$xml_html/;

write_file( 'lists.html', $res );

#script ends here, the followings are definitions of functions

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
            if ( defined $name and defined $name->att('name') ) {
                my $name_name  = $name->att('name');
                my $name_arity = $name->att('arity');
            }
            $name->delete if defined $name;

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

                eval { $_->delete for $desc->children('p') } if $delete_en;

                $_->set_tag('p') for $desc->children('p_zh');
                for ( $desc->children('p') ) {
                    $_->set_tag('code') for $_->children('c');
                }

                for ( $desc->children('warning') ) {
                    eval { $_->delete for $_->children('p') } if $delete_en;
                    $_->set_tag('div');
                    $_->set_att( class => 'warning' );
                    my $new_node = XML::Twig::Elt->new('h2');
                    $new_node->set_inner_xml("Warning:<br/>");
                    $new_node->paste($_);
                }

                for ( $desc->children('note') ) {
                    eval { $_->delete for $_->children('p') } if $delete_en;
                    $_->set_tag('div');
                    $_->set_att( class => 'note' );
                    my $new_node = XML::Twig::Elt->new('h2');
                    $new_node->set_inner_xml("Note:<br/>");
                    $new_node->paste($_);
                }

            }

        }
    }

    my $res_str;
    open my $str_fd, ">", \$res_str;
    $root->print($str_fd);
    $res_str;
}

