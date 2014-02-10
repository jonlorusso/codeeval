#!/usr/bin/env perl

sub output {
    my ( $count, $curr, $first, $last ) = @_;

    print ' ' unless $first;
    print "$count $curr";
    print "\n" if $last;
}


sub compress_sequence {
    my @nums = split / /;

    my $count = 0;
    my $curr = 0;
    my $first = 1;

    for ( @nums ) {
        if ( !$curr ) {
            $curr = $_;
            $count = 1;
        }
        elsif ( $_ != $curr ) {
            output( $count, $curr, $first, 0 );
            $first = 0;
            $curr = $_;
            $count = 1;
        }
        else {
            $count += 1;
        }
    }
    output( $count, $curr, $first, 1 );
}

open FILE, "<", $ARGV[0] or die $!;
map { compress_sequence chomp } <FILE>;
