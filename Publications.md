- **Low Treewidth Embeddings of Planar and Minor-Free Metrics**
  <br>
  Arnold Filtser and **Hung Le**
  <br>
  Preprint.
  <br>[[PDF](https://arxiv.org/pdf/2203.15627.pdf)]<br>
  <details><summary style="color:#7C4700">Abstract</summary>
  <font color = "7C4700">
  Cohen-Addad, Filtser, Klein and Le [FOCS'20] constructed a stochastic embedding of minor-free graphs of diameter $D$ into graphs of treewidth $O_{\epsilon}(\log n)$ with expected additive distortion $+\epsilon D$. Cohen-Addad  et al. then used the embedding  to design the first quasi-polynomial time approximation scheme (QPTAS) for the capacitated vehicle routing problem. Filtser and Le [STOC'21] used the embedding (in a different way) to design a QPTAS for the metric Baker's problems in minor-free graphs. In this work, we devise a new embedding technique to improve the treewidth bound of  Cohen-Addad  et al. exponentially to $O_{\epsilon}(\log\log n)^2$. As a corollary, we obtain the first efficient PTAS for the capacitated vehicle routing problem in minor-free graphs. We also significantly improve the running time of the QPTAS for the metric Baker's problems in minor-free graphs from   $n^{O_{\epsilon}(\log(n))}$ to  $n^{O_{\epsilon}(\log\log(n))^3}$.<br><br>
  
  Applying our embedding technique to planar graphs, we obtain a deterministic embedding of planar graphs of diameter $D$ into graphs of treewidth $O((\log\log n)^2)/\epsilon)$ and  additive distortion $+\epsilon D$ that can be constructed in nearly linear time.  Important corollaries of our result  include a bicriteria PTAS for metric Baker's problems and a PTAS for the vehicle routing problem with bounded capacity in planar graphs, both run in almost-linear time. The running time of our algorithms is significantly better than previous algorithms that require quadratic time.<br><br>
  
  A key idea in our embedding is the construction of an (exact) emulator  for tree metrics with treewidth $O(\log\log n)$ and hop-diameter $O(\log \log n)$. This result may be of independent interest.
  
  </font>
  </details>
  
- **Locality-Sensitive Orderings and Applications to Reliable Spanners**
  <br>
  Arnold Filtser and **Hung Le**
  <br>
  To appear in the 54th Annual ACM Symposium on Theory of Computing. **STOC 2022**.
  <br>[[PDF](https://arxiv.org/pdf/2101.07428.pdf)][[Slides](http://hunglvosu.github.io/files/Reliable-Spanners.pdf)]<br>
  <details><summary style="color:#7C4700">Abstract</summary>
  <font color = "7C4700">
  Chan, Har-Peled, and Jones [2020] recently developed locality-sensitive ordering (LSO), a new tool that allows one to reduce problems in the Euclidean space $\mathbb{R}^d$ to the $1$-dimensional line. They used LSO's to solve a host of problems.  Later, Buchin, Har-Peled, and Oláh [2019,2020] used the LSO of Chan et al. to construct very sparse reliable spanners for the Euclidean space. A highly desirable feature of a reliable spanner is its ability to withstand a massive failure: the network remains functioning even if 90\% of the nodes fail.  In a follow-up work, Har-Peled, Mendel, and Oláh [2021] constructed reliable spanners for general and topologically structured metrics. Their construction used a different approach, and is based on sparse covers.<br><br>
  
  In this paper, we develop the theory of LSO's to non-Euclidean metrics by introducing new types of LSO's suitable for general and topologically structured metrics. We then construct such LSO's, as well as constructing considerably improved LSO's for doubling metrics. Afterwards, we use our new LSO's to construct reliable spanners with improved stretch and sparsity parameters.  Most prominently, we construct $\tilde{O}(n)$-size reliable spanners for trees and planar graphs with the optimal stretch of $2$. Along the way to the construction of LSO's and reliable spanners, we introduce and construct ultrametric covers, and construct $2$-hop reliable spanners for the line.
  </font>
  </details>
  
- **Sparse Euclidean Spanners with Tiny Diameter: A Tight Lower Bound**
  <br>
  **Hung Le** and Lazar Milenkovic and Shay Solomon
  <br>
  To appear in the 38th International Symposium on Computational Geometry. **SoCG 2022**
  <br>[[PDF](https://arxiv.org/pdf/2112.09124.pdf)]<br>
  <details><summary style="color:#7C4700">Abstract</summary>
  <font color = "7C4700">
  In STOC'95 Arya et al. showed that any set of $n$ points in $\mathbb R^d$ admits a $(1+\epsilon)$-spanner with hop-diameter at most 2 (respectively, 3) and $O(n \log n)$ edges (resp., $O(n \log \log n)$ edges). They also gave a general upper bound tradeoff of hop-diameter at most $k$ and $O(n \alpha_k(n))$ edges, for any $k \geq 2$.
  
  The function $\alpha_k$ is the inverse of a certain Ackermann-style function at the $\lfloor k/2 \rfloor$th level of the primitive recursive hierarchy, where $\alpha_0(n) = \lceil n/2 \rceil$, $\alpha_1(n) = \left\lceil \sqrt{n} \right\rceil$, $\alpha_2(n) = \lceil \log{n} \rceil$, $\alpha_3(n) = \lceil \log\log{n} \rceil$, $\alpha_4(n) = \log^* n$, $\alpha_5(n) = \lfloor \frac{1}{2} \log^*n \rfloor, \ldots$. Roughly speaking, for $k \geq 2$ the function $\alpha_{k}$ is close to $\lfloor \frac{k-2}{2} \rfloor$-iterated log-star function, i.e., $\log$ with $\lfloor \frac{k-2}{2} \rfloor$ stars.<br><br>
  
  Whether or not this tradeoff is tight has remained open, even for the cases $k = 2$ and $k = 3$. Two lower bounds are known: The first applies only to spanners with stretch 1 and the second is sub-optimal and applies only to sufficiently large (constant) values of $k$. In this paper we prove a tight lower bound for any constant $k$: For any fixed  $\epsilon > 0$, any $(1+\epsilon)$-spanner for the uniform line metric with hop-diameter at most $k$ must have at least $\Omega(n \alpha_k(n))$ edges.
  
  </font>
  </details>
  

- **A Unified Framework of Light Spanners II: Fine-Grained Optimality**
  <br>
  **Hung Le** and Shay Solomon
  <br>
  Preprint
  <br>[[PDF](https://arxiv.org/pdf/2111.13748.pdf)]<br>
  <details><summary style="color:#7C4700">Abstract</summary>
  <font color = "7C4700">
  Seminal works on light spanners over the years provide spanners with optimal lightness in various graph classes, such as in general graphs, Euclidean spanners and minor-free graphs. Three shortcomings of previous works on light spanners are: (1) The techniques are ad hoc per graph class, and thus can't be applied broadly.  (2) The runtimes of these constructions are almost always sub-optimal, and usually far from optimal. (3) These constructions are optimal in the standard and crude sense, but not in a refined sense that takes into account a wider range of involved parameters.<br><br>
  
  This work aims at addressing these shortcomings by presenting  a unified framework of light spanners in a variety of graph classes. Informally, the framework boils down to a  transformation from sparse spanners to light spanners; since the state-of-the-art for sparse spanners is much more advanced than that for light spanners, such a transformation is powerful. Our framework is developed in two papers. The current paper is the second of the two ---  it  builds on the basis of the unified framework laid in the first paper,  and then strengthens it to achieve more refined optimality bounds for several graph classes, i.e., the bounds remain optimal when taking into account a wider range of involved parameters, most notably $\epsilon$, but also others such as the dimension (in Euclidean spaces) or the minor size (in minor-free graphs).  Our new constructions are significantly better than the state-of-the-art {\em for every examined graph class}. Among various applications and implications of our framework, we highlight the following:<br><br>
  
  For $K_r$-minor-free graphs, we provide a  $(1+\epsilon)$-spanner with lightness $\tilde{O}_{r,\epsilon}( \frac{r}{\epsilon} + \frac{1}{\epsilon^2})$, where $\tilde{O}_{r,\epsilon}$ suppresses $\mathsf{polylog}$ factors of $1/\epsilon$ and $r$, improving the lightness bound $\tilde{O}_{r,\epsilon}( \frac{r}{\epsilon^3})$ of Borradaile, Le and Wulff-Nilsen. We complement our upper bound with a highly nontrivial lower bound construction, for which any $(1+\epsilon)$-spanner must have lightness $\Omega(\frac{r}{\epsilon} + \frac{1}{\epsilon^2})$. Interestingly, our lower bound is realized by a geometric graph in $\mathbb{R}^2$. We note that the quadratic dependency on $1/\epsilon$ we proved here is surprising, as the prior work suggested that the dependency on $\epsilon$ should be around $1/\epsilon$.  Indeed, for minor-free graphs there is a known upper bound of lightness $O(\log(n)/\epsilon)$, whereas subclasses of minor-free graphs, primarily graphs of genus bounded by $g$, are long known to admit spanners of lightness $O(g/\epsilon)$.  
  </font>
  </details>
  
- **Dynamic Matching Algorithms Under Vertex Updates**
  <br>
  **Hung Le** and Lazar Milenkovic and Shay Solomon and Virginia Vassilevska Williams
  <br>
  To appear in The 13th Innovations in Theoretical Computer Science. **ITCS 2022**
  <br>[[Official version](https://drops.dagstuhl.de/opus/volltexte/2022/15692/pdf/LIPIcs-ITCS-2022-96.pdf)][[Video by Lazar](https://www.youtube.com/watch?v=nHOW2PnAdzg)]<br>
  <details><summary style="color:#7C4700">Abstract</summary>
  <font color = "7C4700">
  Dynamic graph matching algorithms have been extensively studied, but mostly under  edge updates. This paper concerns dynamic matching algorithms under vertex updates, where in each update step a single vertex is either inserted or deleted along with its incident edges.  <br><br>
  
  A basic setting arising in online  algorithms and studied by Bosek et al. [FOCS'14] and Bernstein et al. [SODA'18] is that of dynamic approximate maximum cardinality matching (MCM) in bipartite graphs in which one side is fixed and vertices on the other side either arrive or depart via vertex updates. In the BASIC-incremental setting, vertices only arrive, while in the BASIC-decremental setting vertices only depart. When vertices can both arrive and depart, we have the BASIC-dynamic setting. In this paper we also consider the setting in which both sides of the bipartite graph are dynamic. We call this the MEDIUM-dynamic setting, and MEDIUM-decremental is the restriction when vertices can only depart. The GENERAL-dynamic setting is when the graph is not necessarily bipartite and the vertices can both depart and arrive. <br><br>
  
  Denote by $K$ the total number of edges  inserted and deleted to and from the graph throughout the entire update sequence. A well-studied measure, the  recourse of a dynamic matching algorithm is the number of changes made to the matching per step. <bt><br> 
  
  We largely focus on Maximal Matching (MM) which is a $2$-approximation to the MCM. Our main results are as follows.
    
  
  <ul> <li>In the BASIC-dynamic setting, there is a straightforward algorithm for maintaining a MM, with a total runtime of $O(K)$ and constant worst-case recourse. In fact, this algorithm never removes an edge from the matching; we refer to such an algorithm as irrevocable. </li>
  <li>For the MEDIUM-dynamic setting we give a strong conditional lower bound that even holds in the MEDIUM-decremental setting: if for any fixed $\eta>0$, there is an irrevocable decremental MM algorithm with a total runtime of $O(K \cdot n^{1-\eta})$, this would refute the OMv conjecture; a similar (but weaker) hardness result can be achieved via a reduction from the Triangle Detection conjecture. </li>
  <li>Next, we consider the GENERAL-dynamic setting, and  design an MM algorithm with a total runtime of $O(K)$ and constant worst-case recourse. We achieve this result via a 1-revocable algorithm, which may remove just one edge per update step. As argued above, an irrevocable algorithm with such a runtime is not likely to exist.</li>
  <li>Finally, back to the BASIC-dynamic setting, we present an algorithm with a total runtime of $O(K)$, which provides an $(\frac{e}{e-1})$-approximation to the MCM.  To this end, we build on the classic "ranking" online algorithm by Karp et al. [STOC'90]. </li>
  </ul>
  Beyond the concrete results, our work draws connections between the areas of dynamic graph algorithms and online algorithms, and it proposes several open questions that seem to be overlooked thus far. <br>
  </font>
  </details>

- **Near-Optimal Spanners for General Graphs in (Nearly) Linear Time**
  <br>
  **Hung Le** and Shay Solomon
  <br>
  The 33rd Annual ACM-SIAM Symposium on Discrete Algorithms. **SODA 2022**.
  <br>[[PDF](https://arxiv.org/pdf/2108.00102.pdf)]<br>
  <details><summary style="color:#7C4700">Abstract</summary>
  <font color = "7C4700"> 
  Let $G = (V,E,w)$ be a weighted undirected graph on $|V| = n$ vertices and $|E| = m$ edges, let $k \ge 1$ be any integer, and let $\epsilon < 1$ be any parameter. We present the following results on fast constructions of spanners with {near-optimal} sparsity and lightness,\footnote{The sparsity (respectively, lightness) is a normalized notion of size (resp., weight), where we divide the size (resp., weight)  by the size $n-1$ of a spanning tree (resp., the weight $w(\mathrm{MST})$ of a minimum spanning tree $\mathrm{mst}$).} which culminate a long line of work in this area. (By  near-optimal we mean optimal under Erdos' girth conjecture and disregarding the $\epsilon$-dependencies.)<br>
  
  <ul> <li>There are (deterministic) algorithms for constructing $(2k-1)(1+\epsilon)$-spanners for $G$ with a near-optimal sparsity of $O(n^{1/k} \cdot \log(1/\epsilon)/\epsilon))$. The first algorithm can be implemented in the pointer-machine model within time $O(m\alpha(m,n) \cdot \log(1/\epsilon)/\epsilon) + \mathrm{SORT}(m))$, where $\alpha(\cdot,\cdot)$ is the two-parameter inverse-Ackermann function and $\mathrm{SORT}(m)$ is the time needed to sort $m$ integers. The second algorithm can be implemented  in the \rdrm model  within time $O(m \log(1/\epsilon)/\epsilon))$. </li>
  <li>There is a (deterministic)  algorithm for constructing a $(2k-1)(1+\epsilon)$-spanner for $G$ that achieves a near-optimal bound of $O(n^{1/k} \cdot \mathrm{poly}(1/\epsilon))$ on both sparsity and lightness. This algorithm can be implemented in the pointer-machine model within time $O(m\alpha(m,n) \cdot \mathrm{poly}(1/\epsilon) + \mathrm{SORT}(m))$ and in the \rdrm model within time $O(m \alpha(m,n) \cdot \mathrm{poly}(1/\epsilon))$.</li>
  </ul>
  
  The previous fastest constructions of $(2k-1)(1+\epsilon)$-spanners with near-optimal sparsity incur a runtime of is $O(\min\{m(n^{1+1/k}) + n\log n,k \cdot n^{2+1/k}\})$, even regardless of the lightness.  Importantly, the  greedy spanner for stretch $2k-1$ has sparsity $O(n^{1/k})$ --- with no $\epsilon$-dependence whatsoever, but its runtime is $O(m(n^{1+1/k} + n\log n))$. Moreover, the   state-of-the-art lightness bound of any $(2k-1)$-spanner (including the greedy spanner) is poor, even regardless of the sparsity and runtime.
  </font>
  </details>
  

- **Can't See The Forest for the Trees: Navigating Metric Spaces by Bounded Hop-Diameter Spanners**
  <br>
  Omri Kahalon and **Hung Le** and Lazar Milenkovic and Shay Solomon
  <br>
  Preprint
  <br>[[PDF](https://arxiv.org/pdf/2107.14221.pdf)]<br>
  <details><summary style="color:#7C4700">Abstract</summary>
  <font color = "7C4700">
  Spanners for metric spaces have been extensively studied, both in general metrics and in restricted classes, perhaps most notably in low-dimensional Euclidean spaces--- due to their numerous applications.   Euclidean spanners can be viewed as means of compressing the $\binom{n}{2}$ pairwise distances of a $d$-dimensional Euclidean space into $O(n) = O_{\epsilon,d}(n)$ spanner edges, so that the spanner distances preserve the original distances to within a factor of $1+\epsilon$, for any $\epsilon > 0$. Moreover, one can compute such spanners in optimal $O(n \log n)$ time. Once the spanner has been computed, it serves as a "proxy" overlay network, on which the computation can proceed, which gives rise to huge savings in space and other important quality measures. <br><br>
  
  On the negative side, by working on the spanner rather than the original metric, one loses the key property of being able to efficiently "navigate" between pairs of points. While in the original metric, one can go from any point  to any other via a direct edge, it is unclear how to efficiently navigate in the spanner: How can we translate the existence of a "good" path into an efficient algorithm finding it?  Moreover, usually by "good" path we mean a path whose weight approximates the original distance between its endpoints --- but a priori the number of edges (or "hops") in the path could be huge.  To control the hop-length of paths, one can try to upper bound the spanner's hop-diameter, but naturally bounded hop-diameter spanners are more complex than spanners with unbounded hop-diameter, which might render the algorithmic task of efficiently finding good paths more challenging.<br><br>
  
  The original metric enables us to navigate optimally --- a single hop (for any two points) with the exact distance, but the price is high --- $\Theta(n^2)$ edges. Is it possible to efficiently navigate, on a sparse spanner, using $k$ hops and approximate distances, for $k$ approaching 1 (say $k=2$)? Surprisingly, this fundamental question has been overlooked despite the long line of work on spanners in metric spaces.<br><br>
  
  We answer this question in the affirmative via a surprisingly simple observation on bounded hop-diameter spanners for tree metrics, which we apply on top of known {\em tree cover theorems}. Beyond its simplicity, the strength of our approach is two-fold:
  
  <ul> <li>Applicable: We present a variety of applications of our efficient navigation scheme, including a 2-hop routing scheme in Euclidean spaces with stretch $1+\epsilon$ using $O(\log^2 n)$ bits of memory for labels and routing tables --- to the best of our knowledge, all known routing schemes prior to this work use $\Omega(\log n)$ hops.</li>
  <li>General: Our results extend beyond Euclidean spaces to doubling, planar and general metrics.</li>
  </ul>
  </font>
  </details>

- **Greedy Spanners in Euclidean Spaces Admit Sublinear Separators**
  <br>
  **Hung Le** and Cuong Than
  <br>
  The 33rd Annual ACM-SIAM Symposium on Discrete Algorithms. **SODA 2022**.
  <br>[[PDF](https://arxiv.org/pdf/2107.06490.pdf)]<br>[<font color = "red"><b>Invited to TALG Special Issue</b></font>]
  <details><summary style="color:#7C4700">Abstract</summary>
  <font color = "7C4700">
  The greedy spanner in a low dimensional Euclidean space is a fundamental geometric construction that has been extensively studied over three decades as it possesses the two most basic properties of a good spanner: constant maximum degree and constant lightness.  Recently, Eppstein and Khodabandeh showed that the greedy spanner in $\mathbb{R}^2$ admits a sublinear separator in a strong sense: any subgraph of $k$ vertices of the greedy spanner in $\mathbb{R}^2$ has a separator of size $O(\sqrt{k})$.  Their technique is inherently planar and is not extensible to higher dimensions. They left  showing the existence of a small separator for the greedy spanner  in $\mathbb{R}^d$ for any constant $d\geq 3$  as an open problem. <br><br>
  
  In this paper, we resolve the problem of Eppstein and Khodabandeh by showing that any subgraph of  $k$ vertices of the greedy spanner in $\mathbb{R}^d$ has a separator of size $O(k^{1-1/d})$. We introduce a new technique that gives a simple characterization for any geometric graph to have a sublinear separator that we dub \emph{$\tau$-lanky}: a geometric graph is  $\tau$-lanky if any ball of radius $r$ cuts at most $\tau$ edges of length at least $r$ in the graph. We show that any $\tau$-lanky geometric graph of $n$ vertices in $\mathbb{R}^d$ has a separator of size $O(\tau n^{1-1/d})$. We then derive our main result by showing that the greedy spanner is $O(1)$-lanky. We indeed obtain a more general result that applies to unit ball graphs and point sets of low fractal dimensions in $\mathbb{R}^d$.<br><br>
  
  Our technique naturally extends to doubling metrics. We use the $\tau$-lanky characterization to show that there exists a $(1+\epsilon)$-spanner for doubling metrics of dimension $d$ with a constant maximum degree and  a separator of size $O(n^{1-\frac{1}{d}})$;  this result resolves an open problem posed by Abam and Har-Peled a decade ago. We then introduce another simple characterization for a graph in doubling metrics of dimension $d$ to have a sublinear separator. We use the new characterization to show that the greedy spanner of an $n$-point metric space of doubling dimension $d$  has a separator of  size $O((n^{1-\frac{1}{d}}) + \log\Delta)$ where $\Delta$ is the spread of the metric; the factor $\log(\Delta)$ is tightly connected to the fact that, unlike its Euclidean counterpart, the greedy spanner in doubling metrics has unbounded maximum degree. Finally, we discuss algorithmic implications of our results.
  </font>
  </details>
  
- **A Unified Framework of Light Spanners I: Fast (Yet Optimal) Constructions**
  <br>
  **Hung Le** and Shay Solomon
  <br>
  Preprint
  <br>[[PDF](https://arxiv.org/pdf/2106.15596.pdf)][[Solving Open Problem 22](https://people.scs.carleton.ca/~michiel/SpannerBook/openproblems.html)]<br>
  <details><summary style="color:#7C4700">Abstract</summary>
  <font color = "7C4700">
  Seminal works on light spanners over the years provide spanners with optimal lightness in various graph classes, such as in general graphs, Euclidean spanners and minor-free graphs. Three shortcomings of previous works on light spanners are: (1) The techniques are ad hoc per graph class, and thus can't be applied broadly.  (2) The runtimes of these constructions are almost always sub-optimal, and usually far from optimal. (3) These constructions are optimal in the standard and crude sense, but not in a refined sense that takes into account a wider range of involved parameters.<br><br>
  
  This work aims at addressing these shortcomings by presenting  a unified framework of light spanners in a variety of graph classes. Informally, the framework boils down to a transformation from sparse spanners to light spanners; since the state-of-the-art for sparse spanners is much more advanced than that for light spanners, such a transformation is powerful. Our framework is developed in two papers. The current paper is the first of the two --- it   lays the basis of the unified framework and then applies it to design fast constructions with optimal lightness for several graph classes.  Our new constructions are significantly faster than the state-of-the-art for every examined graph class; our runtimes are near-linear and usually optimal.<br><br> 
  
  Among various applications and implications of our framework, we highlight here the following (for simplicity assume $\epsilon> 0$ is fixed):
  
  <ul> <li>In low-dimensional Euclidean spaces, we present an $O(n\log n)$-time construction  of $(1+\epsilon)$-spanners with lightness and degree both bounded by constants in the algebraic computation tree (ACT) (or real-RAM) model, which is the basic model used in Computational Geometry. The previous state-of-the-art runtime in this model for constant lightness (even for unbounded degree) was $O(n \log^2 n / \log\log n)$, whereas $O(n \log n)$-time spanner constructions with constant degree (and  $O(n)$ edges) are known for years. Our construction is optimal with respect to all the involved quality measures --- runtime, lightness and degree --- and it resolves a major problem in the area of geometric spanners, which was open for three decades. </li>
  <li>In general graphs, we present a nearly linear-time algorithm for constructing light spanners. Specifically, for any $k \ge 2$, we construct a $(2k-1)(1+\epsilon)$-spanner with lightness $O(n^{1/k})$  in $O(m \alpha(m,n))$ time, where $\alpha(\cdot,\cdot)$ is the inverse-Ackermann function; the lightness bound is optimal assuming Erd\H{o}s' girth conjecture (up to the $\epsilon$-dependency). Since $O(m\alpha(m,n)) = O(m + n\log^{*}(n)$, the runtime is linear in $m$ when ${m = \Omega(n \log^{*}n)}$. The previous state-of-the-art runtime of such a spanner is super-quadratic in $n$. This result for light spanners in general weighted graphs is   surprising, as it outperforms the analog one for sparse spanners.</li>
  </ul>
  </font>
  </details>
  
  
- **Optimal Approximate Distance Oracle for Planar Graphs**
  <br>
  **Hung Le** and Christian Wulff-Nilsen
  <br>
  To appear in the 62st Annual Symposium on Foundations of Computer Science. **FOCS 2021**.
  <br>[[PDF](https://arxiv.org/pdf/2111.03560.pdf)][[Talk](https://www.youtube.com/watch?v=GpjHrJoSI8k)]<br>
  <details><summary style="color:#7C4700">Abstract</summary>
  <font color = "7C4700">
  A $(1+\epsilon)$-approximate distance oracle of an edge-weighted graph is a data structure that returns an approximate shortest path distance between any two query vertices up to a $(1+\epsilon)$ factor. Thorup (FOCS 2001, JACM 2004) and Klein (SODA 2002) independently constructed a $(1+\epsilon)$-approximate distance oracle with $O(n\log n)$ space, measured in number of words, and $O(1)$ query time when $G$ is an undirected planar graph with $n$ vertices and $\epsilon$ is a fixed constant. Many follow-up works gave $(1+\epsilon)$-approximate distance oracles with various trade-offs between space and query time. However, improving $O(n\log n)$ space bound without sacrificing query time remains an open problem for almost two decades. In this work, we resolve this problem affirmatively by constructing a $(1+\epsilon)$-approximate distance oracle with optimal $O(n)$ space and $O(1)$ query time for undirected planar graphs and fixed $\epsilon$.
  
  We also make substantial progress for planar digraphs with non-negative edge weights. For fixed $\epsilon > 0$, we give a $(1+\epsilon)$-approximate distance oracle with space $o(n\log(Nn))$ and $O(\log\log(Nn)$ query time; here $N$ is the ratio between the largest and smallest positive edge weight. This improves Thorup's (FOCS 2001, JACM 2004) $O(n\log(Nn)\log n)$ space bound by more than a logarithmic factor while matching the query time of his structure. This is the first improvement for planar digraphs in two decades, both in the weighted and unweighted setting.
  </font>
  </details>  
  

- **Clan Embeddings into Trees, and Low Treewidth Graphs**
    <br>
    Arnold Filtser and **Hung Le**
    <br>
    The 53rd Annual ACM Symposium on Theory of Computing. **STOC 2021**.
    <br>[PDF](https://arxiv.org/pdf/2101.01146.pdf)<br>
    <details><summary style="color:#7C4700">Abstract</summary>
    <font color = "7C4700">
    In low distortion metric embeddings, the goal is to embed a host "hard" metric space into a "simpler" target space while approximately preserving pairwise distances. A highly desirable target space is that of a tree metric. Unfortunately, such embedding will result in a huge distortion.  A celebrated bypass to this problem is stochastic embedding with logarithmic expected distortion. Another bypass is Ramsey-type embedding, where the distortion guarantee  applies only to a subset of the points.  However, both these solutions fail to provide an embedding into a single tree with a worst-case distortion guarantee on all pairs. In this paper, we propose a novel third bypass called \emph{clan embedding}. Here each point $x$ is mapped to a subset of points $f(x)$, called a \emph{clan}, with a special \emph{chief} point $\chi(x)\in f(x)$. The clan embedding has multiplicative distortion $t$ if for every pair $(x,y)$ some copy $y'\in f(y)$ in the clan of $y$ is  close to the chief of $x$: $\min_{y'\in f(y)}d(y',\chi(x))\le t\cdot d(x,y)$. Our first result is a clan embedding into a tree with multiplicative distortion $O(\frac{\log n}{\epsilon})$ such that each point has $1+\epsilon$ copies (in expectation). In addition, we provide a  "spanning" version of this theorem for graphs  and use it to devise the first compact routing scheme with constant size routing tables.<br><br>

    We then focus on minor-free graphs of diameter prameterized by $D$, which were known to be stochastically embeddable into bounded treewidth graphs with expected additive distortion $\epsilon D$. We devise  Ramsey-type embedding and clan embedding analogs of the stochastic embedding. We use these embeddings to construct the first (bicriteria quasi-polynomial time) approximation scheme for the metric $\rho$-dominating set and metric $\rho$-independent set problems in minor-free graphs.     
    </font>
    </details>

- **On Light Spanners, Low-treewidth Embeddings and Efficient Traversing in Minor-free Graphs**
  <br>
Vincent Cohen-Addad and  Arnold Filtser and Philip N. Klein and **Hung Le**
  <br>
  The 61st Annual Symposium on Foundations of Computer Science. **FOCS 2020**.
  <br>[[PDF](https://arxiv.org/abs/2009.05039)]<br>
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
  <br>[[PDF](https://arxiv.org/pdf/2007.11636.pdf)][[Official version](https://drops.dagstuhl.de/opus/frontdoor.php?source_opus=12933)][[Slides](http://hunglvosu.github.io/files/ESA20-talk.pdf)][[Talk video](https://www.youtube.com/watch?v=mg-GFukfhUQ)]<br>
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

