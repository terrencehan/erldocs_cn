#!/usr/bin/env perl 

#author: terrencehan(hanliang1990@gmail.com)
#you are welcome to report bugs about this
#script to my email above. :)

#The script is disigned for single .erl file. 
#If you have some files to maintain try: 
#'find path/to/.erl files -exec path/to/tiis/script {} path/to/target/dir'

use 5.010;
use File::Slurp;
use File::Basename qw/basename/;
use File::Spec;
use File::Find qw/find/;
use Data::Dump q/dump/;
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
/-spec\s*\(?(?<def>(?<fun_name>\w+)\s*\((?<args>.*?)\)\s*->\s*(?<return>.*?\)?))\s*(?<when_zone>when(?<types>.*?\)?))?\)?\.\n/gcs
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
            #$fun->{types} =~ s/\s+/ /g;
            $fun->{types} =~ s/::/=/g;
        }
        $fun->{spec} = $&;
        push @res, $fun;
    }
    \@res;
}

sub handle {
    my ( $file, $tar_dir ) = @_;

    my $specs = get_specs_from_file $file;

    open my $out, ">", $tar_dir . basename( $file, '.erl' ) . '.spec';

    for ( sort { $a->{name} cmp $b->{name} } @$specs ) {
        print $out 'name:',
          $_->{name} . '/' . scalar split( ',', $_->{args} ), "\n";
        print $out 'def:', $_->{def}, "\n";
        print $out 'types:', $_->{types}, "\n" if $_->{types};
        print $out "\n";
    }

}

my ( $src, $tar_dir ) = @ARGV;

handle $src, $tar_dir;
print "done\n";
