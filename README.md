# Leander
Leandergames challenge

This program is the results of the Leandergames interview challenge. The statement is copied below:

_Python Test
Consider the following game:
From one deck of poker cards (52 cards) you place cards face up in a ring of 12 positions. The 13th card is placed
in the middle of the ring. If an Ace was put on the first position (“place one”) or a deuce on “place two” and so
on (a king on “place 13”) you have a match. You simply skip that place on the next lap and continue to place
cards on top of the cards not corresponding to their positions.
Every time you have a new match you pick up the cards on that certain position and place them in the bottom of
your deck and leave the matched card on its position in the ring. You continue this procedure until you either
run out of cards or have all 13 positions matched.
You win if you have all 13 positions matched.
What is the probability of winning the game?
Please provide the answer together with simulation code in Python._


![Results obtained](Img/prob.png)

Attempts  | Test 1   |	 Test 2 	|  Test 3	  |  Test 4	  |  Test 5
:-------: | :------: | :--------: | :-------: | :-------: | :------: 
1000      |	 12.4    |  	11.5    | 	 12.1   |	  10.4	  |   12.2
10000     |  11.49	 |   11.59    |    11.34	|   11.82   | 	11.81
100000    |  11.72	 |   11.93    |    11.58	|   11.94   | 	11.59
1000000   |  11.66	 |   11.67	  |    11.66	|   11.66	  |   11.65
10000000  |  11.69	 |   11.69    |    11.67	|   11.68	  |   11.69
100000000 |	         |            |           |           |   11.68

