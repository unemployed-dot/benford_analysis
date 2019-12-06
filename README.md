# benford_analysis
Benford analysis applied to national election in Italy on the 03/04/2018

You can find data for every district in CSV extension on Ministero degli interni website:

https://dait.interno.gov.it/elezioni/open-data/dati-elezioni-politiche-4-marzo-2018

Those are the results:

First Digit Probabilities:
1: observed: 0.298 expected: 0.301
2: observed: 0.172 expected: 0.176
3: observed: 0.125 expected: 0.125
4: observed: 0.099 expected: 0.097
5: observed: 0.082 expected: 0.079
6: observed: 0.069 expected: 0.067
7: observed: 0.060 expected: 0.058
8: observed: 0.050 expected: 0.051
9: observed: 0.046 expected: 0.046

Chi Squared Test Statistic: 2.855
Critical value at P-value of 0.05 is 15,51
Observed distributions matches expected distributions

The high amount of data (nearly 8000) gave us a good correspondence with Benford Model. 
