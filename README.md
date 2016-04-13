# tile_game
Rearranging letter tiles game.  Made in about three days as a CodingDojo final project.

Most of the work is done client-side, with Angular and jQuery UI sortables.  The wordlist is saved server-side (node.js); every time the tiles are moved, an AJAX call checks if any words are formed.

This uses the SOWPODS wordlist (the international Scrabble list).  To get the set of tiles, it chooses four words of the appropriate lengths from a list of the 10,000 most commonly used English words (based on the Google corpus, see [here](https://github.com/first20hours/google-10000-english)), to guarantee that every game has at least one solution using familiar words.

The point-value of each letter is based on based on [Peter Norvig's letter-frequency calculations](http://norvig.com/scrabble-letter-scores.html).
