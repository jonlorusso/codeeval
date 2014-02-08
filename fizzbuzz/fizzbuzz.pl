#!/usr/bin/env perl

sub fizzbuzz {
    my ( $a, $b, $n ) = @_;

    for ( 1 .. $n ) {
        my $fizz = $_ % $a == 0;
        my $buzz = $_ % $b == 0;

        print "FB" if ($fizz && $buzz);
        print "F" if ($fizz && !$buzz);
        print "B" if (!$fizz && $buzz);
        print $_ if (!$fizz && !$buzz);
        print " " if $_ < $n;
    }

    print "\n";
}

open FILE, "<", $ARGV[0] or die $!;
map { fizzbuzz(split / /) } <FILE>;
