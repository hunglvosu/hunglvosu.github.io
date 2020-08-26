
- **A Unified and Fine-Grained Approach for Light Spanners**
  <br>
**Hung Le** and Shay Solomon
  <br>
  Preprint
  <br>[[PDF](https://arxiv.org/pdf/2008.10582.pdf)]<br>
  <details><summary style="color:#7C4700">Abstract</summary>
  <font color = "7C4700">
  Seminal works on light spanners from recent years provide near-optimal tradeoffs between the stretch and lightness of spanners in general graphs, minor-free graphs and doubling metrics.   In FOCS'19 the authors provided a <i>``truly optimal''</i> tradeoff (i.e., including the $\epsilon$-dependency, where $\epsilon$ appears in both the stretch and lightness) for Euclidean low-dimensional spaces. Some of these papers employ inherently different techniques than others (e.g., the technique of Chechik and Wulff-Nilsen [SODA20] requires large stretch while others are naturally suitable to stretch $1+\epsilon$). Moreover, the runtime of these constructions is rather high.<br>
  
  In this work we present a unified and fine-grained approach for light spanners.
  Besides the obvious theoretical importance of unification, we demonstrate the power of our approach in obtaining (1) stronger lightness bounds, and (2) faster construction times. Our results include:
  <ul><li> $K_r$-minor-free graphs:
  <ul> <li> <i>A <b> truly optimal</b> spanner.</i> We provide a  $(1+\epsilon)$-spanner with lightness $\tilde{O}_{r,\epsilon}( \frac{r}{\epsilon} + \frac{1}{\epsilon^2})$, where $\tilde{O}_{r,\epsilon}$ suppresses $\mathsf{polylog}$ factors of $1/\epsilon$ and $r$, improving the lightness bound $\tilde{O}_{r,\epsilon}( \frac{r}{\epsilon^3})$ of Borradaile, Le and Wulff-Nilsen [FOCS17]. We complement our upper bound with a highly nontrivial lower bound construction, for which any $(1+\epsilon)$-spanner must have lightness $\Omega(\frac{r}{\epsilon} + \frac{1}{\epsilon^2})$.</li>
  <li><i>A <b> fast </b> construction.</i> Increasing the lightness bound by an additive term of $O(\frac{1}{\epsilon^4})$ allows us to achieve a runtime of $\tilde{O}_r(n r \alpha(nr, n))$, where $\alpha(.,.)$ is the inverse Ackermann function. The previous state-of-the-art runtime is  $O(n^2 r)$.</li>
  </ul>
  </li>
  <li>General graphs:
  <ul><li> <i>A <b>truly optimal</b> spanner--- almost</i>. We provide a $(2k-1)(1+\epsilon)$-spanner (for any $k \geq 2, \epsilon < 1$) with lightness $O(\frac{g(n,k)}{\epsilon})$, where $g(n,k)$ is the minimum sparsity of $n$-vertex graphs with girth $2k+1$. (Recall that $g(n,k) = O(n^{1/k})$  and Erdos' girth conjecture is that $g(n,k) = \Theta(n^{1/k})$.)  The previous state-of-the-art lightness by Chechik and Wulff-Nilsen [SODA20] is $O(n^{1/k}\epsilon^{-(3+\frac{1}{k})})$.</li>
  <li><i> A <b>fast</b> construction.</i> A $(2k-1)(1+\epsilon)$-spanner with lightness $O_{\epsilon}(n^{1/k})$ can be constructed in $O_{\epsilon}(m \alpha(m,n))$ time; the lightness bound is optimal up to the $\epsilon$-dependency and assuming Erdos' girth conjecture. In particular, when $m = \Omega(n \log^* n)$, the runtime is <i>linear</i> in $m$. The previous state-of-the-art runtime of such a spanner is super-quadratic in $n$.</li>
  </ul>
  </li>
  <li>Low dimensional Euclidean spaces: For any point set in $\mathbb{R}^d$ and constant $d\geq 3$, we construct a Euclidean $(1+\epsilon)$-spanner with lightness $\tilde{O}_{\epsilon}(\epsilon^{-(d+1)/2})$  using \emph{Steiner points}. Our result implies that Steiner points help in reducing the lightness of Euclidean $(1+\epsilon)$-spanners almost quadratically. Previously, this fact was only known for point sets with small spread [LS,ESA20].</li>
  <li>High dimensional Euclidean and normed spaces:
  We provide a construction of spanners that improves the previous state-of-the-art lightness and size.</li>
  </ul>
  </font>
  </details>


- **On Light Spanners, Low-treewidth Embeddings and Efficient Traversing in Minor-free Graphs**
  <br>
Vincent Cohen-Addad and  Arnold Filtser and Philip N. Klein and **Hung Le**
  <br>
  To appear in the 61st Annual Symposium on Foundations of Computer Science. **FOCS 2020**.
  <br>[PDF coming soon]<br>
  <details><summary style="color:#7C4700">Abstract</summary>
  <font color = "7C4700">Understanding the structure of minor-free metrics, namely shortest path metrics obtained
      over a weighted graph excluding a fixed minor, has been an important research direction
      since the fundamental work of Robertson and Seymour. A fundamental idea that helps both to understand the structural properties of these metrics     and lead to strong algorithmic results is to construct a ``small-complexity''      graph that approximately preserves distances between pairs of points of the metric. We show the two following structural results for minor-free metrics:<br>
      <ul><li>Construction of a <i>light</i> subset spanner. Given a  subset of vertices called terminals, and $\epsilon$,  in polynomial time we construct a subgraph that
      preserves all pairwise distances between terminals up to a multiplicative $1+\epsilon$ factor, of total weight at most $O_{\epsilon}(1)$ times the weight of the minimal Steiner tree spanning the terminals.</li>
      <li>Construction of a stochastic metric embedding into low treewidth graphs with expected additive distortion $\epsilon D$. Namely, given a minor free graph $G=(V,E,w)$ of diameter $D$, and parameter $\epsilon$, we construct a distribution $\mathcal{D}$ over dominating metric embeddings into  treewidth-$O_{\epsilon}(\log n)$ graphs such that $\forall u,v\in V$, $\mathbb{E}_{f\sim\mathcal{D}}[d_H(f(u),f(v))]\le d_G(u,v)+\epsilon D$.</li>
      </ul>
    One of our important technical contributions is a novel framework that allows us to reduce <i>both problems</i> to problems on simpler graphs of <i>bounded diameter</i> that we solve using a new decomposition. Our results have the following algorithmic consequences: (1) the first efficient approximation scheme for subset TSP in minor-free metrics; (2) the first approximation scheme for vehicle routing with bounded capacity in minor-free metrics; (3) the first efficient approximation scheme for vehicle routing with bounded capacity on bounded genus metrics.
      En route to the latter result, we design the first FPT approximation scheme for vehicle routing with  bounded capacity on bounded treewidth graphs (parameterized by the treewidth). </font>
  </details>

- **Light Euclidean Spanners with Steiner Points.**
  <br>
  **Hung Le** and Shay Solomon
  <br>
  To appear in the 28th Annual European Symposium on Algorithms. **ESA 2020**.
  <br>[[PDF](https://arxiv.org/pdf/2007.11636.pdf)][[Official version](https://drops.dagstuhl.de/opus/frontdoor.php?source_opus=12933)][[Slides](http://hunglvosu.github.io/files/ESA20-talk.pdf)]<br>
  <details><summary style="color:#7C4700">Abstract</summary>
  <font color = "#7C4700">The FOCS'19 paper of Le and Solomon, culminating a long line of research on Euclidean spanners, proves that the lightness  (normalized weight) of the greedy $(1+\epsilon)$-spanner in $\mathbb{R}^d$ is   $\tilde{O}(\epsilon^{-d})$ for any $d = O(1)$ and any $\epsilon = \Omega(n^{-\frac{1}{d-1}})$  (where $\tilde{O}$ hides polylogarithmic factors of $\frac{1}{\epsilon}$),  and also shows the existence of point sets in $\mathbb{R}^d$ for which any $(1+\epsilon)$-spanner must have lightness $\Omega(\epsilon^{-d})$. Given this tight bound on the lightness, a natural arising question is whether a better lightness bound can be achieved using <i>Steiner points</i>.<br><br>

  Our first result is a construction of Steiner spanners  in $\mathbb{R}^2$ with lightness $O(\epsilon^{-1} \log \Delta)$, where $\Delta$ is the spread of the point set. In the regime 
  of $\Delta \ll 2^{1/\epsilon}$, this provides an improvement over the lightness bound of Le and Solomon [FOCS 2019]; 
  this regime of parameters is of practical interest, as point sets arising in real-life applications 
  (e.g., for various random distributions) have polynomially bounded spread, while in spanner applications $\epsilon$ often controls the precision, and it sometimes needs to be much smaller than $O(1/\log n)$. Moreover, for spread polynomially bounded in $1/\epsilon$, this upper bound 
  provides a quadratic improvement over the non-Steiner bound of Le and Solomon [FOCS 2019], We then demonstrate that such a light spanner can be constructed in $O_{\epsilon}(n)$ time for polynomially bounded spread, where $O_{\epsilon}$ hides a factor of $\mathrm{poly}(\frac{1}{\epsilon})$. Finally, we extend the construction to higher dimensions, proving a lightness upper bound of $\tilde{O}(\epsilon^{-(d+1)/2} + \epsilon^{-2}\log \Delta)$ for any $3\leq d = O(1)$ and any $\epsilon = \Omega(n^{-\frac{1}{d-1}})$.</font>
  </details>
  
- **A PTAS for Subset TSP in Minor-free Graphs.**
  <br>
  **Hung Le**
  <br>
   The 31st Annual ACM-SIAM Symposium on Discrete Algorithms. **SODA 2020**.
  <br>[[PDF](https://arxiv.org/pdf/1804.01588.pdf)]<br>
  <details><summary style="color:#7C4700"> Abstract</summary>
  <font color = "#7C4700">We give the first polynomial time approximation scheme (PTAS) for the subset Traveling Salesperson Problem (TSP) in minor-free graphs.  This resolves a long standing open problem in a long line of work on designing PTASes for TSP in minor-closed families initiated by Grigni, Koutsoupias, and  Papadimitriou [FOCS'95]. The main technical ingredient in our PTAS is a  construction of a nearly light subset $(1+\epsilon)$-spanner for any given edge-weighted minor-free graph. This construction is based on a necessary and sufficient condition given by <i>sparse spanner oracles</i>: light subset spanners exist if and only if sparse spanner oracles exist. This relationship allows us to obtain two new results:
    <ul> <li>A $(1+\epsilon)$-spanner with lightness $O(\epsilon^{-d+2})$ for any doubling metric of constant dimension $d$. This improves the earlier lightness bound $\epsilon^{-O(d)}$ obtained by Borradaile, Le and Wulff-Nilsen [SODA`19].</li>
    <li>A $(1+\epsilon)$-spanner with sublinear lightness for any metric of constant correlation dimension. Previously, no spanner with non-trivial lightness was known.</li>
    </ul></font>
  </details>
  

- **Truly Optimal Euclidean Spanners.**
    <br>**Hung Le** and Shay Solomon
    <br> The 60th Annual IEEE Symposium on Foundations of Computer Science. **FOCS 2019**.
    <br>[[PDF](https://arxiv.org/pdf/1904.12042.pdf)][[ICERM Talk](https://icerm.brown.edu/video_archive/?play=1909)][[FOCS Talk](https://www.youtube.com/watch?v=W1_ORIqZGFE&list=PL3DbynX8gwfLXOsziSLaVmiLKKjedlvks&index=73)][[Oded's choices](http://www.wisdom.weizmann.ac.il/~oded/MC/281.html)]<br>[<font color = "red"><b>Invited to SICOMP Special Issue</b></font>][<font color = "red"><b>Invited to HALG 2020</b></font>]
    <details><summary style="color:#7C4700">Abstract</summary>
    <font color = "#7C4700">Euclidean spanners are important geometric structures, having found numerous applications over the years. Cornerstone results in this area from the late 80s and early 90s state that for any $d$-dimensional $n$-point Euclidean space, there exists a $(1+\epsilon)$-spanner with $ O(n\epsilon^{-d+1})$ edges and lightness (normalized weight) $O(\epsilon^{-2d})$. Surprisingly, the fundamental question of whether or not these dependencies on $\epsilon$ and $d$ for small $d$ can be improved  has remained elusive, even for $d = 2$.
    This question naturally arises in any application of Euclidean spanners where precision is a necessity (thus $\epsilon$ is tiny). In the most extreme case $\epsilon$ is inverse polynomial in $n$, and then one could potentially improve the size and lightness bounds by factors that are polynomial in $n$. <br><br>

    The state-of-the-art bounds $O(n\epsilon^{-d+1})$  and $O(\epsilon^{-2d})$ on the size and lightness of spanners are realized by the <i> greedy</i> spanner.
    In 2016, Filtser and Solomon [PODC 16] proved that, in low dimensional spaces, the greedy spanner is ``near-optimal''; informally, their result states that the greedy spanner for dimension $d$ is just as sparse and light as any other spanner <i>but for dimension larger by a constant factor</i>. Hence the question of whether the greedy spanner is truly optimal remained open to date.<br><br>

    The contribution of this paper is two-fold.
    <ul>
    <li> We resolve these longstanding questions by nailing down the exact dependencies on $\epsilon$ and $d$ and showing that the greedy spanner is truly optimal.
    Specifically, for any $d= O(1), \epsilon = \Omega({n}^{-\frac{1}{d-1}})$:
    <ul>
    <li> We show that any $(1+\epsilon)$-spanner must have $\Omega(n\epsilon^{-d+1})$ edges,  implying that the greedy (and other) spanners achieve the optimal size. </li>
    <li> We show that any $(1+\epsilon)$-spanner must have lightness $\Omega(\epsilon^{-d})$,
    and then improve the upper bound on the lightness of the greedy spanner from $O(\epsilon^{-2d})$   to $O(\epsilon^{-d}\log \frac{1}{\epsilon})$.</li>
    </ul></li>
    <li> We then complement our negative result for the size of spanners with a  rather counterintuitive positive result: Steiner points lead to a quadratic improvement in the size of spanners! Our bound for the size of Steiner spanners is tight as well (up to lower-order terms). </li>
    </ul></font>
    </details>
 
- **Engineering a PTAS for Minimum Feedback Vertex Set in Planar Graphs**
  <br>
  Glencora Borradaile and **Hung Le** and Baigong Zheng
  <br>The 17th International Symposium on Experimental Algorithms. **SEA 2019**.
  <br>[[PDF](https://link.springer.com/chapter/10.1007/978-3-030-34029-2_7)]<b>
  <details><summary style="color:#7C4700">Abstract</summary>
  <font color = "#7C4700"> We investigate the practicality of approximation schemes for optimization problems in planar graphs based on balanced separators.  The first polynomial-time approximation schemes (PTASes) for problems in planar graphs were based on balanced separators, wherein graphs are recursively decomposed into small enough pieces in which optimal solutions can be found by brute force or other methods.  However, this technique was supplanted by the more modern and (theoretically) more efficient approach of decomposing a planar graph into graphs of bounded treewidth, in which optimal solutions are found by dynamic programming.  While the latter approach has been tested experimentally, the former approach has not.<br><br>

   To test the separator-based method, we examine the minimum feedback vertex set (FVS) problem in planar graphs.  We propose a new, simple $O(n \log n)$-time approximation scheme for FVS using balanced separators and a {\em linear kernel}.  The linear kernel reduces the size of the graph to be linear in the size of the optimal solution.  In doing so, we correct a reduction rule in Bonamy and Kowalik's linear kernel for FVS.  We implemented this PTAS and evaluated its performance on large synthetic and real-world planar graphs.  Unlike earlier planar PTAS engineering results, our implementation guarantees the theoretical error bounds on all tested graphs.</font>
  </details>


- **Greedy Spanners are Optimal in Doubling Metrics**
   <br> Glencora Borradaile and **Hung Le** and Christian Wulff-Nilsen
  <br> The 30th ACM-SIAM Symposium on Discrete Algorithms. **SODA 2019**.
  <br>[[PDF](https://arxiv.org/pdf/1712.05007.pdf)]<br>
  <details><summary style="color:#7C4700">Abstract</summary>
  <font color = "#7C4700">We show that the greedy spanner algorithm constructs a $(1+\epsilon)$-spanner of weight $\epsilon^{-O(d)}w(\mathrm{MST})$ for a point set in metrics of doubling dimension $d$, resolving an open problem posed by Gottlieb [FOCS 15]. Our result generalizes the result by Narasimhan and Smid who showed that a point set in $d$-dimension Euclidean space has a $(1+\epsilon)$-spanner of weight at most $\epsilon^{-O(d)}w(\mathrm{MST})$. Our proof only uses  the packing property of doubling metrics and greatly simplifies the proof of the same result in Euclidean space. </font>
  </details>
 
- **Local Search is a PTAS for Feedback Vertex Set in Minor-free Graphs**
  <br>**Hung Le** and Baigong Zheng
  <br> The 25th International Computing and Combinatorics Conference. **COCOON 2019**.
  <br>[[PDF](https://arxiv.org/pdf/1804.06428.pdf)][[TCS](https://www.sciencedirect.com/science/article/pii/S0304397520302747)][<font color = "red"><b>Invited to TCS Special Issue!</b></font>]
   <details><summary style="color:#7C4700">Abstract</summary>
   <font color = "#7C4700">We show that an extremely simple local search gives a PTAS for the Feedback Vertex Set (FVS) problem in minor-free graphs. It keeps exchanging a constant number of vertices to improve the current solution until a local optimum is reached. The previous PTAS by Fomin, Lokshtanov, Raman and Saurabh, despite theoretical efficiency, is much more complicated in the sense that it combines many advanced algorithmic tools  such as contraction decomposition framework by Demaine and Hajiaghayi, Courcelle's theorem and the Robertson and Seymour decomposition. <br><br>

     Our main technical contribution is to show that the local optimum only differs the global optimum by a $(1+\epsilon)$ factor. We do so by introducing Steiner points, those who are not in the local and optimal solutions,  to the standard analysis of local search. We believe that our technique is of independent interest. </font>
    </details>


- **Minor-free Graphs have Light Spanners**
  <br> Glencora Borradaile and **Hung Le** and Christian Wulff-Nilsen
  <br> The 58th Annual IEEE Symposium on Foundations of Computer Science. **FOCS 2017**.
  <br> [[PDF](https://arxiv.org/pdf/1711.00821.pdf)]<br>
  <details><summary style="color:#7C4700">Abstract</summary>
  <font color = "#7C4700">We show that every $H$-minor-free graph has a light (1+ε)-spanner, resolving an open problem of Grigni and Sissokho and proving a conjecture of Grigni and Hung. Our lightness bound is:
   $$O(\frac{|V(H)\sqrt{\log |V(H)|}|}{\epsilon^3}\log\frac{1}{\epsilon})$$
   That is, it has a practical dependency on the size of the minor H. Our result also implies that the polynomial time approximation scheme (PTAS) for the Travelling Salesperson Problem (TSP) in H-minor-free graphs by Demaine, Hajiaghayi and Kawarabayashi is an efficient PTAS whose running time is $2^{\mathrm{poly}(\frac{1}{\epsilon})}n^{O(1)}$ Our techniques significantly deviate from existing lines of research on spanners for H-minor-free graphs, but build upon the work of Chechik and Wulff-Nilsen for spanners of general graphs.</font>
  </details>


- **Embedded-width: A Variant of Treewidth for Plane Graphs.**
  <br> Glencora Borradaile and Jeff Erickson and **Hung Le** and Robbie Weber
  <br> Manuscript.
  <br>[[PDF](https://arxiv.org/pdf/1703.07532.pdf)]<br>
  <details><summary style="color:#7C4700">Abstract</summary>
  <font color = "#7C4700">We define a special case of tree decompositions for planar graphs that respect a given embedding of the graph. We study the analogous width of the resulting decomposition we call the <i>embedded-width</i> of a plane graph. We show both upper bounds and lower bounds for the embedded-width of a graph in terms of its treewidth and describe a fixed parameter tractable algorithm to calculate the embedded-width of a plane graph. To do so, we give novel bounds on the size of matchings in planar graphs.</font>
  </details>


- **A Better Bound on the Largest Induced Forests in Triangle-free Planar Graphs.**
  <br> **Hung Le**
  <br> Graphs and Combinatorics.
  <br>[[PDF](https://arxiv.org/pdf/1611.04546.pdf)][[Code](http://web.engr.oregonstate.edu/~lehu/res/lp_final.lp)]<br>
  <details><summary style="color:#7C4700">Abstract</summary>
  <font color = "#7C4700">It is well-known that there exists a triangle-free planar graph of $n$ vertices such that the largest induced forest has order at most $\frac{5n}{8}$. Salavatipour proved that there is a forest of order at least $\frac{5n}{9.41}$ in any triangle-free planar graph of $n$ vertices.  Dross, Montassier and Pinlou improved Salavatipour's bound to $\frac{5n}{9.17}$. In this work, we further improve the bound to  $\frac{5n}{9}$. Our technique is inspired by the recent ideas from Lukot'ka, Mazak and Zhu.</font>
  </details>


- **Large Induced Acyclic and Outerplanar Subgraphs of Low-treewidth Planar Graphs.**
  <br> Glencora Borradaile and **Hung Le** and Melissa Sherman-Bennett
  <br> Graphs and Combinatorics.
  <br>[[PDF](https://arxiv.org/pdf/1711.00212.pdf)]<br>
  <details><summary style="color:#7C4700">Abstract</summary>
  <font color = "#7C4700">Albertson and Berman conjectured that every planar graph has an induced forest on half of its vertices. The best known lower bound, due to Borodin, is that every planar graph has an induced forest on two fifths of its vertices. In a related result, Chartran and Kronk, proved that the vertices of every planar graph can be partitioned into three sets, each of which induce a forest.<br><br>
  
   We show tighter results for $2$-outerplanar graphs. We show that every $2$-outerplanar graph has an induced forest on at least half the vertices by showing that its vertices can be partitioned into two sets, each of which induces a forest. We also show that every $2$-outerplanar graph has an induced outerplanar graph on at least two-thirds of its vertices.</font>
  </details>


- **Light Spanners for Bounded Treewidth Graphs Imply Light Spanners for H-minor-free Graphs.**
  <br> Glencora Borradaile and **Hung Le**
  <br> Manuscript
  <br>[[PDF](https://arxiv.org/pdf/1703.10633.pdf)]<br>
  <details><summary style="color:#7C4700">Abstract</summary>
  <font color = "#7C4700">Grigni and Hung conjectured that $H$-minor-free graphs have $(1 + \epsilon)$-spanners that are light, that is, of weight $g(|H|,\epsilon)$ times the weight of the minimum spanning tree for some function $g$. This conjecture implies the efficient polynomial-time approximation scheme (PTAS) of the traveling salesperson problem in $H$-minor free graphs; that is, a PTAS whose running time is of the form $2^{f(\epsilon)}n^{O(1)}$ for some function f. The state of the art PTAS for TSP in H-minor-free- graphs has running time $n^{\mathrm{poly}(1/\epsilon)}$. We take a further step toward proving this conjecture by showing that if the bounded treewidth graphs have light greedy spanners, then the conjecture is true. We also prove that the greedy spanner of a bounded pathwidth graph is light and discuss the possibility of extending our proof to bounded treewidth graphs.</font>
  </details>


- **An Optimal Dynamic Program for r-Dominating Set over Tree Decompositions.**
  <br> Glencora Borradaile and **Hung Le**
  <br> The 11th International Symposium on Parameterized and Exact Computation. **IPEC 2016**.
  <br>[[PDF](https://arxiv.org/pdf/1502.00716.pdf)][[IPEC](http://drops.dagstuhl.de/opus/volltexte/2017/6919/pdf/LIPIcs-IPEC-2016-8.pdf)]<br>
  <details><summary style="color:#7C4700">Abstract</summary>
  <font color = "#7C4700">There has been recent progress in showing that the exponential dependence on treewidth in dynamic programming algorithms for solving NP-hard problems are optimal under the Strong Exponential Time Hypothesis (SETH). We extend this work to $r$-domination problems. In $r$-dominating set, one wished to find a minimum subset S of vertices such that every vertex of $G$ is within $r$ hops of some vertex in $S$. In connected $r$-dominating set, one additionally requires that the set induces a connected subgraph of $G$. We give a $O((2r + 1)^{\mathrm{tw}}n)$ time algorithm for $r$-dominating set and a $O((2r + 2)^{\mathrm{tw}}n^{O(1)})$ time algorithm for connected $r$-dominating set in $n$-vertex graphs of treewidth $\mathrm{tw}$. We show that the running time dependence on $r$ and $\mathrm{tw}$ is the best possible under SETH. This adds to earlier observations that a "+1" in the denominator is required for connectivity constraints.</font>
  </details>

