#!/usr/bin/env swipl
:- use_module(library(dcg/basics)).
:- use_module(library(dcg/high_order)).
:- use_module(library(ugraphs)).
/*
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
*/

:- initialization(main, main).

main([]) :-
    format("missing input file~n", []).

main([File|_]) :- 
    bag_options(File, V),
    length(V, N),
    succ(R, N), % subtract 1 since reachable counts start vertex
    format("~w~n", [R]).

bag_options(File, V) :-
    phrase_from_file(sequence(bag_desc, "\n", G), File),
    %vertices_edges_to_ugraph([], Bags, G), % the DCG emits a graph already!
    transpose_ugraph(G, Gi),
    reachable('shiny gold', Gi, V).
    
bag_desc(Color-Sbcs) --> bag(Color), " contain ", sub_bags(Sbcs, _).
bag(Color) --> string(Colorc), " bags", !, {atom_codes(Color, Colorc)}.
sub_bags([], []) --> "no other bags.", !.
sub_bags([C], [N]) --> num_bag(C, N), ".".
sub_bags([C|Cs], [N|Ns]) --> num_bag(C, N), ", ", sub_bags(Cs, Ns).
% I'm sure there is a more clean way to do the below, but this works so /shrug
num_bag(C, 1) --> "1 ", string(Cc), " bag", !, {atom_codes(C, Cc)}.
num_bag(C, N) --> integer(N), " ", bag(C).
