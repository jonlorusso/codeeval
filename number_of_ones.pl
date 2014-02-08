#!/usr/bin/env perl

use feature qw(say);
use List::Util qw(sum);

open FILE, "<", $ARGV[0] or die $!;
map { my $x = $_; say sum(map { ( $x & (2**$_) ) >> $_ } (0..15)) } <FILE>;
