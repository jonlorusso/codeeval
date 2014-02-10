#!/usr/bin/env perl

open FILE, "<", $ARGV[0] or die $!;
map { print } <FILE>;
