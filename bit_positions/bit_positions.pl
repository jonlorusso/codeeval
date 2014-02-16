#!/usr/bin/env perl

use POSIX qw(pow);

sub bit_positions {
    my ( $n, $p1, $p2 ) = split /,/;

    my $x = ( $n & pow(2, $p1 - 1) ) >> ( $p1 - 1 );
    my $y = ( $n & pow(2, $p2 - 1) ) >> ( $p2 - 1 );
    
    print "true\n" if $x == $y;
    print "false\n" if $x != $y;
}

open FILE, "<", $ARGV[0] or die $!;
map { bit_positions } <FILE>;
