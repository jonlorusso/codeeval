#!/usr/bin/env perl

sub process {
    chomp;
    my @numbers;
    my @words;
    for (split /,/) {
        push @words, $_ if /[:alpha:]+/ ;
        push @numbers, $_ if /\d+/ ;
    }
    print join(',', @words);
    print "|" if @numbers and @words;
    print join(',', @numbers);
    print "\n" if @numbers or @words;;
}

open FILE, "<", $ARGV[0] or die $!;
map { process } <FILE>;
