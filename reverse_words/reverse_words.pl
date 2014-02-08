#!/usr/bin/env perl

open FILE, "<", $ARGV[0] or die $!;

while (<FILE>) {
    chomp;
    print join(' ', reverse(split / /));
    print "\n";
}
