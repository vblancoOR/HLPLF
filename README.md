# Probability Datasets for Hub Location with Protection under Inter-Link Failures

We make available here the different probability matrices used in the computacional experiments carried out for our paper "Hub Location with Protection under Inter-Hub Link Failures" by V. Blanco, E. Fernández, and Y. Hinojosa.

Two different types of files are generated:
- ProbNnPp_it.txt: nxn matrices of random uniform probabilities in [0, p_0] with p0<=p. it instances are generated.
- ProbGroupsNn_it.txt: nxn matrices with probabilities in {0.1, 0.2, 0.3}. The matrices are symmetric, and the assignment (i,j)/(j,i) pair to the probability is randomly performed.

The file GenProb.py has the functions used to generate these files:

- ProbGenerationGroups(n, maxit): generates the files "ProbGroupsNn_it.txt" for it =1, ..., maxit
- ProbGenerationRandom(n, maxit, P): generates the files "ProbNnPp_it.txt" for it =1, ..., maxit for each p in P (we use P={0.1, 0.2, 0.3, 0.4, 0.5}).

The data for the three dataset that we consider in our experiments were downloaded from:

- _CAB_ (O’Kelly ME (1987) A quadratic integer program for the location of interacting hub facilities. European Journal of Operational Research 32(3):393–404) and _AP_ (Ernst AT, Krishnamoorthy M (1996) Efficient algorithms for the uncapacitated single allocation p-hub median problem. Location Science 4(3):139 – 154.) datasets: http://people.brunel.ac.uk/~mastjjb/jeb/orlib/
- _TR_ dataset (Tan PZ, Kara BY (2007) A hub covering model for cargo delivery systems. Networks: An International Journal 49(1):28–39.):  https://ie.bilkent.edu.tr/~bkara/dataset.php
