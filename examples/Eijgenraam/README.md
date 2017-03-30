# Dike Heightening - Eijgenraam Model

Eijgenraam et al. (2012) extended Van Dantzig's dike heightening model by allowing a series of
dike heightenings over the 300 year planning horizon.  The goal is to maintain a low
failure probability for each dike ring in the Netherlands.

## Replicating the Eijgenraam Study

The file `eijgenraam.py` replicates the results of Eijgenraam et al. (2012) within Rhodium.
The problem aims to identify a series of dike heightenings over a 300 year planning horizon.

Within Rhodium, a naive way to represent this problem is to utilize a single lever, an array of
length 300, storing the heightenings for each year.  A solution would thus look like:

```
    H = 0, 0, 0, 75, 0, 0, 0, 0, 0, 0, 0, 0, 75, 0, 0, 0, ...
```

This indicates a dike heightening would occur at year 4 and year 13.  It turns out this
representation is quite inefficient, as the optimization process must attempt to optimize 300
decision variables, most of which end up set to 0.

A better representation is to encode specific actions.  For this problem, we want to increase
the dike height by some amount after a given number of years.  We can represent this as a pair,
`(t_i, h_i)`, where `t_i` is the number of years since the last dike heightening and `h_i`
is the heightening amount.  For example, the following encoding:

```
    [(4, 75), (9, 75)]
```

would be equivalent to the previous example.  We have two dike heightenings: the first increases
the dike by 75 cm on year 4; the second increases the dike by 75 cm on year 9+4=13.

In addition to efficiency, this representation also has another advantage: it can represent a
variable number of dike heightenings.  For this problem, we have a 300 year planning horizon.
We first set a maximum number of dike heightenings we'll allow over the entire planning horizon,
say 6.  Each `t_i` can range from 0 to 300.  Any heightenings occuring after 300 years are
ignored.  For example, the following heightenings:

```
    [(50, 75), (100, 75), (100, 75), (100, 75), (100, 75), (100, 75)]
```

would result in 3 heightenings during our 300 year planning horizon, at years 50, 150, and 250.

## References

> Eijgenraam, C., R. Brekelmans, D. den Hertog, and K. Roos (2012),
  "Flood Prevention by Optimal Dike Heightening", Working Paper,
  http://feweb.uvt.nl/pdf/TICOPT/flood-prevention.pdf.