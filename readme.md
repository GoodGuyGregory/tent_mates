# Assignment

## Tentmates

The following problem is posed by Dennis Sasha in the August 1998 Dr. Dobb's Journal: Given a bunch of campers that need to be packed into tents, and preferences of these campers for tent-mates, find an optimally-happy packing. [The article](http://drdobbs.com/184410645) Links to an external site. provides the details. (If you can't reach this article for some reason, message me for a copy.) The generalized decision problem has been proven to be NP-complete, so search is the only known way.

The instance data you will need is available as tents-prefs.csv and tents-sizes.csv on our Github at [CS_Ai_Course_Mini_Projects](https://github.com/pdx-cs-ai/miniproject-data-fall2023Links) to an external site.. `tents-prefs.csv` just contains the preferences listed in the post. `tents-sizes.csv` gives a name and capacity for each tent.

Use state-space search to find a good matching and score for the given instance. Just do the basic problem: ignore the bonus problem where the happiness is reduced by four. You may use any complete or local method. The runtime for your search should be under three minutes on your box. If you cannot manage a score of _175_ (should be straightforward), give the best score over _165_ you can.

Your program should open tents-prefs.csv and tents-sizes.csv for the relevant data, or hardcode it in. Output should be the score followed by the mapping of people to tent numbers: for example

```
172
nick: e
alan: a
olivia: b
kris: d
emily: d
larry: c
dave: c
petra: b
gwenyth: d
isaac: c
bob: e
hillary: d
mike: a
felicia: b
jack: e
carol: e
```

**Hints:**

I wrote a simple local search of about 50 lines in a couple of hours that worked in a couple of seconds. The "obvious" way to do local search is to start with a random assignment and swap pairs of people that are in different tents. Use short local searches and a lot of restarts.

Assigning tents to people is way easier than the other way around.
