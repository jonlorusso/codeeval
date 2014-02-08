#!/usr/bin/env perl

use Math::Complex;

sub prime {
    my $x = shift;
    my $s = sqrt($x);

    return 1 if $x == 2;

    for ( 2 .. ( $s + 1 ) ) {
        return 0 if $x % 2 == 0;
        return 0 if $x % $_ == 0;
    }

    return 1;
}

my $i = 2;
my $count = 0;
my $sum = 0;
while ( $count < 1000 ) {
    if ( prime($i) ) {
        $sum += $i;
        $count += 1;
    }
    $i += 1;
} 

print "$sum\n";
