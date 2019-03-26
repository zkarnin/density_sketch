### Suggested modifcations edits
* unify n and m if possible
* Add a generalization like result for ERM on the coreset
* Add many citation (all from the reviews) plus Bernard Chazelle's book.
* Add more discussion on the compactors (is the page limit really 12 pages?)
* Answer TODO questions below
* Discuss the algorithm explicitly
* Are there other results on additive coresets that we are missing? 
* How does the matrix column subsets selection compare to BSS?



### Interesting paper with new but simple techniques. References and comparisons are missing


The paper does not offer new bound on the Rademacher complexity. It suggests a new measure of complexity. Namely, the Class Discrepancy. The two quantities are contrasted and compared for discussion and intuition building. In fact, the new bound don’t hold for sampling but rather for algorithmic selection of coresets only.  

Regarding additive coresets, indeed, coresets are more often discussed in the context of multiplicative approximation. The authors will make sure to emphasize that this is not the case here. It is important to note that additive bounds for coresets and sketches are quite common. One could argue that additive error bounds are more important because they give smaller coresets while still allowing generalization results.

Regarding running time, the algorithm is actually not exponential but rather relies on constructive version of Banaszczyk’s theorem [1]. The authors will add that discussion into the paper.


It is not clear to the authors how one would obtain these results by extending results for 1-mean and low rank.  Regarding the suggested references. The authors will include those and explain the connections to the current work. 

[1] Nikhil Bansal, Daniel Dadush, Shashwat Garg, Shachar Lovett:
The gram-schmidt walk: a cure for the Banaszczyk blues. STOC 2018: 587-597

Algorithm 1 is not an optimal discrepancy solution but rather a “neat trick” which works well in practice (experiments omitted because it’s not the focus of the paper). While 1/eps^2 coresets are indeed achievable for Frank Wolfe Algorithms (see Philips et al.) this algorithm is different, straight forward, and elegant. See actual python code for it below

```python
def split(vectors, kernel):
    set1 = []; set2 = []
    for v in vectors:
        sum1 = sum([kernel(v,o) for o in set1])
        sum2 = sum([kernel(v,o) for o in set2])
        if sum1 < sum2:
            set1.append(v)
        else:
            set2.append(v)                
    return (set1,set2) 
```

### nice, elegant contribution


The review is very thoughtful and thorough, thank you. We would only like to point out that the presented result actually do give generalization bounds. In fact, class discrepancy of sqrt(d)/m immediately translates to generalization of the form 
R < R* + O(sqrt(d)/m)
Where R is the Risk of the model obtained by ERM on an optimal coreset of size m.
The authors thought it was not worth including in paper but would be happy to include in the final version. 

### reasonable paper but a bit incremental 


* The given result does not depend on the Gaussian kernel parameter.
* Theorem 16 indeed “plays with notation” mainly in order to make the vector balancing lemma (14) standalone. 
* It is not clear what the reviewer is saying wrt to R. For clarity, the radius of convergence does not depend on the input set of points. The bounds hold universality for any set of points. 
* The improved merge-and-reduce hold for _all_ queries exactly like previous constructions. The analysis goes through a single query high probability bound and union bound which might be the source of confusion.
* Regarding the novelty, the author never claim to be the first to identify any connection between coresets, machine learning, and discrepancy. Some of these connections are literally text book material. For example, Machine Learning and coresets received a whole chapter in Bernard Chazelle’s classic text book “the discrepancy method”. Nevertheless, the presented connection is new, especially elegant, and very useful as a framework. This is made clear by achieving a large set of new results in one fell swoop. These include Gaussian KDE which received intensive research.

##### Answers to questions
*In Corollary 21, there is the assumption that the norm of x-q is bounded. Is this assumption also made in the prior work?*

TODO
 
*Does prior work assume gamma to be constant?*
 
TODO


*Why do Corollaries 17 and 18 follow from the previous Theorem for ||q|| <=1?*

TODO


*How does the paper compare to earlier work? What are the novel ideas?*

The core of the paper is based on three contribution all of which are new

1. A new measure of complexity for function classes, the class discrepancy.
2. New generalization results, coresets, and streaming algorithms based on the class discrepancy. Offline coresets constructions are indeed trivial and provided for completeness (which is clearly stated and not “over sold”). The streaming algorithms are new and improve on prior results.
3. Tight bound on the class discrepancy of several well studied problems (which require some mathematically involved lemmas)




### Interesting general framework, but comparison and presentation are not compelling


*sec 4 focuses on the special case of Kernel density estimation, which is the only case presented where the proposed framework leads to a new algorithm* 

Section 4 does _not_ include an algorithm based on this framework but rather a standalone result. The framework produces algorithms for all of the stated problems including all analytic functions of the dot product or the squared distance. The algorithm is based on new constructive version of Banaszczyk’s Lemma.

[1] Nikhil Bansal, Daniel Dadush, Shashwat Garg, Shachar Lovett:
The gram-schmidt walk: a cure for the Banaszczyk blues. STOC 2018: 587-597

*The technical tools used to obtain the results are well known* 

We highly contest this statement. The result is not only new and mathematically involved, it also improves on several recent papers one of which appeared in STOC as recently as last year. 

The authors will take under advisement the add more survey material on frameworks for coresets and streaming algorithms (such the Braverman et al). These, however, do not compare directly for two main reasons. First, they consider multiplicative approximation and we consider additive approximation. Second, they are mostly sensitivity and sampling based and the bounds they achieve are not stated using similar quantities. 

*How related are CD and RC in reality? Can we really convert RC bounds into CD bounds?*

RC and CD are connected conceptually connected but require completely different tools for analyzing them. The only formal connection is that CD<RC which is both trivial and uninteresting. It is analogous to saying that random sampling is a valid algorithm for choosing coreset. The paper shows that careful selection of a coreset is asymptotically better (CD = o(RC)).

No. To the best of knowledge, RC bounds cannot be converted to CD bounds.

*How much of the machinery from RC analysis can be converted for CD analysis? How much has this been done in the current proofs?*

See above answer, while we reviewed the literature and techniques for bounding RC, these did not carry through to CD (except for standard transitions using Cauchy-Swartz etc.) 


*3.A) The reported complexity d/eps in regression problems is for multiplicative error bounds, which are harder. What are existing additive bounds for this problem?* 

We are not aware of additive bounds for regression coresets.

*3.B) Similarly, bounds for multiplicative error in matrix column subset selection are of the order of d/eps. Here we achieve d^(1/2)/eps, but for additive bound. How does this result compares to existing work e.g. in spectral graph sparsification.*

We have corresponded about this topic with experts in these areas including Christopher Musco, Nikhil Srivastava, and Nikhil Bansal. These appear to be new results that don’t quite stack against existing work due to the different kind of bounds (additive) they produce.  They do, however, greatly overperform matrix concentration-based sampling results (which is unsurprising and therefore not boasted in the paper)

*If there are computationally efficient (i.e. at least poly(n)) algorithms that could be extracted from this framework, it should be discussed in the paper, at least at the level of conjectures.* 

The authors can add such statements to the paper. General algorithms require running the result of Bansal, Dadush, Garg, and Lovett which is, indeed, polynomial. The authors, however, acknowledge that above approach is not attractive enough for practitioners and leave it to future research to find more efficient algorithms that achieve the presented bounds. 


*Quadratic complexity becomes quickly unfeasible as n grows.*

We agree with the reviewer. An o(n^2) algorithm would indeed be more desirable. This is subject to further research.

*What is the actual computational comparison between the proposed approach and existing poly(n) methods?*

These provide asymptotically different results. If the question is about experimental results, we can report that that O(n^2) algorithm produces much better coresets than sampling. We did not, however, code the solver for the general problem. This is left for future work.

*The appendix contains an interesting discussion*

The reviewer is correct, the authors will add more information regarding compactors in the body of the paper. 

Regarding the “duality” of ‘n’ and ‘m’. The authors agree and will do their best to unify those.



































# V2

General notes:

We'd like to thank the reviewers for their thoughtful feedbacks. A few general comments
* missing citations: Thank you for pointing out missing citations. Below we address the connections to these papers and we will add this discussion to the paper.
* run time: The results of section 3 prove the existence of an algorithm achieving a coreset for analytical functions. While a naive implementation is exponential, we in fact do conjecture there is a polynomial time algorithm given the constructive version of Banaszczyk's theorem [1]. We will add a discussion about this.
* Algorithm 1 is indeed similar to the Frank-Wolfe algorithm given in Philips et al., yet is conceptually simpler, easier to implement, and has smaller constants in its run-time. The novelty here is the simplification.
* Regarding the novelty, the author never claim to be the first to identify any connection between coresets, machine learning, and discrepancy. Some of these connections are literally text book material. For example, Machine Learning and coresets received a whole chapter in Bernard Chazelle's classic text book the discrepancy method. Nevertheless, the presented connection is new, especially elegant, and very useful as a framework. This is made clear by achieving a large set of new results in one fell swoop. These include Gaussian KDE which received intensive research.


[1] Nikhil Bansal, Daniel Dadush, Shashwat Garg, Shachar Lovett:
The gram-schmidt walk: a cure for the Banaszczyk blues. STOC 2018: 587-597


AnonReviewer2

We wanted to point out that the paper does not provide new bounds for Radamacher complexity nor does it hold for randomly sampled points. The result brings a new complexity measure, namely Class Discrepancy, that measures the generalization bound for an actively chosen, rather than randomly chosen, set.

Regarding the merge-reduce algorithms: The main novelty of the paper is in setting up the problem so that existing merge-reduce techniques can be applied in order to achieve a streaming coreset. In particular we combine the general merge-reduce trick with the concept of compactors using variable length coresets. Since the tools are standard we feel that the proofs and algorithm should be in the appendix

We are not sure about the connection to 1-mean queries and low-rank approximations. We'll try to see if one can be drawn and if so, add a small discussion about it

[10] indeed provide coresets for the Gaussian Kernel but it is weak, multiplicative and larger in size compared to ours. Since we provide an additive bound the results are not comparable


Program Committee Member1

The review is very thoughtful and thorough, thank you. We would only like to point out that the presented result actually do give generalization bounds. In fact, class discrepancy of sqrt(d)/m immediately translates to generalization of the form 
R < R* + O(sqrt(d)/m)
Where R is the Risk of the model obtained by ERM on an optimal coreset of size m.
The authors thought it was not worth including in paper but would be happy to include in the final version. 



Program Committee Member3

* We indeed depend on a scaling parameter unlike the result of Philips et al. Still, the contribution is a new view and the application of kernel density estimation is one of many
* Corollaries 17,18 follow from observing the Taylor expansion of the functions they apply to. We will note this in the paper
* Theorem 16 indeed ��plays with notations�� mainly in order to make the vector balancing lemma (14) standalone. It applies for compact sets, in particular of radius R. We will make this clearer
* The improved merge-and-reduce hold for *all* queries exactly like previous constructions. The analysis goes through a single query high probability bound and union bound which might be the source of confusion.

"the main ideas have been already used": We respectfully disagree. Indeed the connection between discrepancy and coresets has been drawn in the past but the way we do so, using Banaszczyk's theorem, is completely new. The rest of the tricks such as halving and merge-reduce were not claimed to be our own and are presented as tricks rather than a major novelty in the paper.

*In Corollary 21, there is the assumption that the norm of x-q is bounded. Is this assumption also made in the prior work?*
Some works do not need that assumption. The bounded norm is indeed an issue to be addressed. We will emphasize this in our paper
 
*Does prior work assume gamma to be constant?*
 Some do not


*How does the paper compare to earlier work? What are the novel ideas?*

The core of the paper is based on three contribution all of which are new
1. A new measure of complexity for function classes, the class discrepancy.
2. New generalization results, coresets, and streaming algorithms based on the class discrepancy. Offline coresets constructions are indeed trivial and provided for completeness (which is clearly stated and not “over sold”). The streaming algorithms are new and improve on prior results.
3. Tight bound on the class discrepancy of several well studied problems (which require some mathematically involved lemmas)




AnonReviewer1

*sec 4 focuses on the special case of Kernel density estimation, which is the only case presented where the proposed framework leads to a new algorithm* 

Section 4 does _not_ include an algorithm based on this framework but rather a standalone result. The framework produces algorithms for all of the stated problems including all analytic functions of the dot product or the squared distance, albeit of exponential complexity. We claim that the mere existence of these algorithms is an interesting result. Finding an efficient version is a problem we believe is feasible due to [1] yet leave for future work. 

[1] Nikhil Bansal, Daniel Dadush, Shashwat Garg, Shachar Lovett:
The gram-schmidt walk: a cure for the Banaszczyk blues. STOC 2018: 587-597

*The technical tools used to obtain the results are well known* 

We highly contest this statement. The result is not only new and mathematically involved, it also improves on several recent papers one of which appeared in STOC as recently as last year. 

The authors will take under advisement the add more survey material on frameworks for coresets and streaming algorithms (such the Braverman et al). These, however, do not compare directly for two main reasons. First, they consider multiplicative approximation and we consider additive approximation. Second, they are mostly sensitivity and sampling based and the bounds they achieve are not stated using similar quantities. 

*How related are CD and RC in reality? Can we really convert RC bounds into CD bounds?*

RC and CD are connected conceptually but require completely different tools for analyzing them. The only formal connection is that CD<RC which is both trivial and uninteresting. It is analogous to saying that the best active set achieves as good a generalization bound as a random set. The interesting question is how much better can an actively selected set do compared to a random one. The fact that CD=o(RC) translates to the answer "assymptotically better"

*How much of the machinery from RC analysis can be converted for CD analysis? How much has this been done in the current proofs?*

There is little to no connection, as far as we can tell, between the machinery for RC to that of CD. We'll mention this in the paper.


*3.A) The reported complexity d/eps in regression problems is for multiplicative error bounds, which are harder. What are existing additive bounds for this problem?* 

We are not aware of additive bounds for regression coresets.

*3.B) Similarly, bounds for multiplicative error in matrix column subset selection are of the order of d/eps. Here we achieve d^(1/2)/eps, but for additive bound. How does this result compares to existing work e.g. in spectral graph sparsification.*

We have corresponded about this topic with experts in these areas including Christopher Musco, Nikhil Srivastava, and Nikhil Bansal. These appear to be new results that don't quite stack against existing work due to the different kind of bounds (additive) they produce.  They do, however, greatly overperform matrix concentration-based sampling results (which is unsurprising and therefore not boasted in the paper)

*If there are computationally efficient (i.e. at least poly(n)) algorithms that could be extracted from this framework, it should be discussed in the paper, at least at the level of conjectures.* 

We conjecture the existence of polynomial algorithms but leave that to future work.


*Quadratic complexity becomes quickly unfeasible as n grows.*

We agree with the reviewer. An o(n^2) algorithm would indeed be more desirable. This is subject to further research.

*What is the actual computational comparison between the proposed approach and existing poly(n) methods?*

These provide asymptotically different results. If the question is about experimental results, we can report that that O(n^2) algorithm produces much better coresets than sampling. We did not, however, code the solver for the general problem. This is left for future work.

*The appendix contains an interesting discussion*

The reviewer is correct, the authors will add more information regarding compactors in the body of the paper. 

Regarding the duality of n and m, the authors agree and will do their best to unify those.

