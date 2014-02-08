#!/usr/bin/env perl

use List::Util qw(sum);

open FILE, "<", $ARGV[0] or die $!;
map { print(sum(split //)."\n") } <FILE>;
