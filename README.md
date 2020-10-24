# pharo-watts-strogatz-test
this is a watts-strogatz circular lattice testcode on Pharo/Roassal2.
Pharo:
Pharo 9.0.0
Build information: Pharo-9.0.0+build.732.sha.6af0583f14b12f143ba4522feaccaabf048ed635 (64 Bit)
![alt text](https://github.com/cobwebkanamachi/pharo-watts-strogatz-test/blob/main/demo.png?raw=true "Demo Screen")
I inspired Serge Stinckwich's "Visualization of Regular Lattice with Pharo & Roassal" shown bellow, so made this.
[link to his demo movie on youtube](https://www.youtube.com/watch?v=kkFa4t5isYQ)
test.py would your watts-strogatz network as graph image and text like shown bellow.
1 -> 2 ,1 -> 50 ,1 -> 3 ,1 -> 49 ,1 -> 36 ,2 -> 3 ,2 -> 4 ,2 -> 50 ,3 -> 4 ,3 -> 5 ,4 -> 5 ,4 -> 6 ,5 -> 6 ,5 -> 7 ,6 -> 7 ,6 -> 8 ,7 -> 8 ,7 -> 9 ,8 -> 9 ,8 -> 10 ,9 -> 10 ,9 -> 11 ,9 -> 24 ,10 -> 11 ,10 -> 12 ,11 -> 12 ,11 -> 13 ,12 -> 13 ,12 -> 14 ,13 -> 14 ,13 -> 15 ,14 -> 15 ,14 -> 16 ,15 -> 16 ,15 -> 17 ,16 -> 17 ,16 -> 18 ,17 -> 18 ,17 -> 23 ,18 -> 19 ,18 -> 20 ,19 -> 20 ,19 -> 21 ,20 -> 21 ,20 -> 22 ,21 -> 22 ,21 -> 23 ,22 -> 23 ,22 -> 24 ,23 -> 24 ,23 -> 25 ,24 -> 26 ,25 -> 26 ,25 -> 27 ,26 -> 27 ,26 -> 28 ,27 -> 28 ,27 -> 29 ,28 -> 29 ,28 -> 30 ,29 -> 30 ,29 -> 31 ,30 -> 31 ,30 -> 32 ,31 -> 32 ,31 -> 33 ,32 -> 33 ,32 -> 34 ,33 -> 34 ,33 -> 35 ,34 -> 35 ,34 -> 36 ,35 -> 36 ,35 -> 37 ,36 -> 37 ,37 -> 38 ,37 -> 39 ,38 -> 39 ,38 -> 40 ,39 -> 40 ,39 -> 41 ,40 -> 41 ,40 -> 42 ,41 -> 42 ,41 -> 43 ,42 -> 43 ,42 -> 44 ,43 -> 44 ,43 -> 45 ,44 -> 45 ,44 -> 46 ,45 -> 46 ,45 -> 47 ,46 -> 47 ,46 -> 48 ,47 -> 48 ,47 -> 49 ,48 -> 49 ,48 -> 50 ,49 -> 50
Needed to express edges to edges as nodes, and smalltalk notification of edges to edges is like 1->2.
You could rewrite these with vi, emacs, notepad.exe, or you like.
Then you could embed these to test.st with yourself.

I have no idea other than Atlas3 and python to combine pharo with python3.
I have no idea to get python's output other than inspector invokation.
Sorry for inconvinient.
