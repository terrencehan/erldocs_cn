#!/usr/bin/env perl 

#author: terrencehan(hanliang1990@gmail.com)
#you are welcome to report bugs about this 
#script to my email above. :)

use 5.010;
use File::Slurp;
use File::Basename qw/basename/;
use File::Find qw/find/;
use Data::Dump q/dump/;
use Cwd;
use strict;
use warnings;

#this script is used to extract 'spec's from 
#erlang module source files. you should give 
#a directory containing .erl files and a existing 
#target directory which will be filled with 
#.spec files.

sub get_specs_from_file {
    my $file = shift;
    my $src  = read_file($file);

    my @res;

    while ( $src =~
/-spec\s*(?<def>(?<fun_name>\w+)\s*\((?<args>.*?)\)\s*->\s*(?<return>.*?))\s*(?<when_zone>when(?<types>.*?))?\.\n/gcs
      )

#Attention: here is a bug, we cannot match strings like "-spec funname(fun((T)->boolean()|{true, X}), [T])->List."
    {
        my $fun;
        $fun->{name}   = $+{'fun_name'};
        $fun->{args}   = $+{'args'};
        $fun->{return} = $+{'return'};
        $fun->{def}    = $+{'def'};
        if ( defined $+{'types'} ) {
            $fun->{types} = $+{'types'};
            $fun->{types} =~ s/\s+/ /g;
            $fun->{types} =~ s/::/=/g;
        }
        $fun->{spec} = $&;
        push @res, $fun;
    }
    \@res;
}

sub get_specs_from_files {
    my ( $src_dir, $tar_dir ) = @_;

    our @files;

    sub wanted {
        my $file = $File::Find::name;
        return unless $file =~ /\.erl$/;
        push @files, $file;

    }
    find \&wanted, $src_dir;

    for my $file (@files) {

        my $specs = get_specs_from_file $file;

        open my $out, ">",
          './specs/stdlib/' . basename( $file, '.erl' ) . '.spec';

        for ( sort { $a->{name} cmp $b->{name} } @$specs ) {
            print $out 'name:',
              $_->{name} . '/' . scalar split( ',', $_->{args} ), "\n";
            print $out 'def:', $_->{def}, "\n";
            print $out 'types:', $_->{types}, "\n" if $_->{types};
            print $out "\n";
        }
    }

}

get_specs_from_files '/home/terrence/tar/otp_src_R15B/lib/stdlib/src/',
  './specs/stdlib/';
print "done\n";
