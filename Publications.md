My research has been generously supported by two NSF grants:  [CCF-2121952](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2121952) and [CCF-2237288](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2237288)

- **Approximate Light Spanners in Planar Graphs**
  <br>**Hung Le** and Shay Solomon and Cuong Than and Csaba D. Tóth and Tianyi Zhang.
  <br>[[PDF](https://arxiv.org/abs/2505.24825)]
  <br>Manuscript.
  <details><summary style="color:#7C4700">Abstract</summary>
  <font color = "7C4700">
  In their seminal paper, Alth\"{o}fer   et al.\ (DCG~1993) introduced the greedy spanner and showed that, for any weighted planar graph $G$, the weight of the greedy $(1+\epsilon)$-spanner is at most $(1+\frac{2}{\epsilon}) \cdot w(\mathrm{MST})$, where $w(\mathrm{MST})$ is the weight of a minimum spanning tree of $G$. This bound is optimal in an xistential sense: there exist planar graphs $G$ for which any $(1+\epsilon)$-spanner has a weight of at least $(1+\frac{2}{\epsilon}) \cdot w(\mathrm{MST})$.<br><br>  
  
  However, as an approximation algorithm, even for a bicriteria approximation, the weight approximation factor of the greedy spanner is essentially as large as the existential bound: There exist planar graphs $G$ for which the greedy $(1+x \epsilon)$-spanner (for any $1\leq x = O(\epsilon^{-1/2})$) has a weight of $\Omega(\frac{1}{\epsilon \cdot x^2})\cdot w(G_{opt, \epsilon})$, where $G_{opt, \epsilon}$ is a $(1+\epsilon)$-spanner of $G$ of minimum weight. <br><br> 
        
  Despite the flurry of works over the past three decades on approximation algorithms for spanners as well as on light(-weight) spanners, there is still no (possibly bicriteria) approximation algorithm for light spanners in weighted planar graphs that outperforms the existential bound. As our main contribution, we present a polynomial time algorithm for constructing, in any weighted planar graph $G$, a $(1+\epsilon\cdot 2^{O(\log^* 1/\epsilon)})$-spanner for $G$ of total weight $O(1)\cdot w(G_{opt, \epsilon})$. <br><br> 
  
  To achieve this result, we develop a new technique, which we refer to as iterative planar pruning. It iteratively modifies a spanner; each iteration replaces a heavy set of edges by a light path, to substantially decrease the total weight of the spanner while only slightly increasing its stretch. We leverage planarity to prove a  laminar structural property of the edge set to be removed, which enables us to optimize the path to be inserted via dynamic programming. Our technique applies dynamic programming directly to the input planar graph, which significantly deviates from previous techniques used for network design problems in planar graphs, and might be of independent interest.
  </font>
  </details>
  
- **Light Tree Covers, Routing, and Path-Reporting Oracles via Spanning Tree Covers in Doubling Graphs**
  <br>Hsien-Chih Chang and Jonathan Conroy and **Hung Le** and Shay Solomon and Cuong Than.
  <br>[[PDF](https://arxiv.org/abs/2503.22669)]
  <br>To appear in the 57th Annual ACM Symposium on Theory of Computing. **STOC 2025**.
  <details><summary style="color:#7C4700">Abstract</summary>
  <font color = "7C4700">
  A $(1+\epsilon)$-stretch tree cover of an edge-weighted $n$-vertex graph $G$ is a collection of trees, where every pair of vertices has a $(1+\epsilon)$-stretch path in one of the trees. The celebrated Dumbbell Theorem by Arya et al. [STOC'95] states that any set of $n$ points in $d$-dimensional Euclidean space admits a $(1+\epsilon)$-stretch tree cover with a constant number of trees, where the constant depends on $\epsilon$ and the dimension $d$. This result was generalized for arbitrary doubling metrics by Bartal et al. [ICALP'19]. While the total number of edges in the tree covers of Arya et al. and Bartal et al. is $O(n)$, all known tree cover constructions incur a total lightness of $\Omega(\log n)$; whether one can get a tree cover of constant lightness has remained a longstanding open question, even for 2-dimensional point sets.<br><br> 
  
  In this work, we resolve this fundamental question in the affirmative,  as a direct corollary of a new construction of $(1+\epsilon)$-stretch spanning tree cover for doubling graphs; in a spanning tree cover,  every tree may only use edges of the input graph rather than the corresponding metric. To the best of our knowledge, this is the first constant-stretch spanning tree cover construction (let alone for  $(1+\epsilon)$-stretch) with a constant number of trees for any nontrivial family of graphs. <br><br> 
  
  We obtain several algorithmic applications from our dynamic LSO, including a dynamic fault-tolerant spanner, dynamic tree cover, dynamic nearest neighbor search with optimal search time, and dynamic (bichromatic) closest pair of points,  all in doubling metrics. Most notably, we obtain the first dynamic algorithm for maintaining an $k$-fault tolerant spanner in doubling metrics with optimal sparsity in optimal $O(\log n )$ time per update.<br><br>
  
  Concrete applications of our spanning tree cover include:
  
  <ul> <li> A $(1+\epsilon)$-stretch tree cover construction, where both the number of trees and lightness are bounded by $O(1)$, for doubling graphs. In doubling metrics, we can also bound the maximum degree of each vertex by $O(1)$ (which is impossible in doubling graphs). </li>
  <li> A compact $(1+\epsilon)$-stretch routing scheme in the labeled model for doubling graphs,  which uses the asymptotically optimal (up to the dependencies on $\epsilon$ and $d$) bound of $O(\log n)$ bits on all the involved measures (label, header, and routing tables sizes). This is a significant improvement over existing works, where the local memory usage either depends on the aspect ratio of the graph or is $\Omega(\log^3 n)$. </li>
  <li>The first path-reporting distance oracle for doubling graphs achieving optimal bounds for all important parameters: $O(n)$ space, $(1+\epsilon)$-stretch, and $O(1)$ query time for  constant $d$ and $\epsilon$.</li>
  </ul>
  </font>
  </details>


- **Dynamic Locality Sensitive Orderings in Doubling Metrics**
  <br>An La and **Hung Le**.
  <br>[[PDF](https://arxiv.org/abs/2408.14617)][[blog post](https://minorfree.github.io/LSO/)]
  <br>To appear in the 57th Annual ACM Symposium on Theory of Computing. **STOC 2025**.
  <details><summary style="color:#7C4700">Abstract</summary>
  <font color = "7C4700">
  In their pioneering work, Chan, Har-Peled, and Jones (SICOMP 2020)  introduced locality-sensitive ordering (LSO), and constructed an LSO with a constant number of orderings for point sets in the $d$-dimensional Euclidean space. Furthermore, their LSO could be made dynamic effortlessly under point insertions and deletions, taking $O(\log(n))$ time per update by exploiting Euclidean geometry. Their LSO provides a powerful primitive to solve a host of geometric problems in Euclidean spaces in both dynamic and static settings.   Filtser and Le (STOC 2022) constructed the first LSO with a constant number of orderings in the more general setting of doubling metrics.  However, their algorithm is inherently static since it relies on several sophisticated constructions in intermediate steps, none of which is known to have a dynamic version.  Making their LSO dynamic would recover the full generality of LSO and provide a general tool to dynamize a vast number of static constructions in doubling metrics.<br><br> 
  
  In this work, we give a dynamic algorithm that has $O(\log n)$ time per update for constructing an LSO in doubling metrics under point insertions and deletions. To this end, we introduce a toolkit of several new data structures: a pairwise index tree (PIT) which augments the standard net tree with the pairwise property, a pairwise tree cover which in a certain sense is a tree counterpart of LSO, a net tree cover for stabilizing the net tree, and a leaf tracker for keeping track of a DSF ordering of leaves in a dynamic tree. A key technical problem that we solves in this work is stabilizing the dynamic net tree of Cole and Gottlieb (STOC 2006), a central dynamic data structure in doubling metrics, using  a dynamic \emph{net tree cover}. Specifically,  we show that every update to the dynamic net tree can be decomposed into a few very simple updates to trees in the net tree cover. As stability is the key to any dynamic algorithm, our technique could be useful for other problems in doubling metrics. <br><br> 
  
  We obtain several algorithmic applications from our dynamic LSO, including a dynamic fault-tolerant spanner, dynamic tree cover, dynamic nearest neighbor search with optimal search time, and dynamic (bichromatic) closest pair of points,  all in doubling metrics. Most notably, we obtain the first dynamic algorithm for maintaining an $k$-fault tolerant spanner in doubling metrics with optimal sparsity in optimal $O(\log n )$ time per update.<br>
  </font>
  </details>
  
- **New Weighted Additive Spanners**
  <br>An La and **Hung Le**.
  <br>[[PDF](https://arxiv.org/abs/2408.14638)][[blog post](https://minorfree.github.io/AddtiveSpanners/)]
  <br>Manuscript. 
  <details><summary style="color:#7C4700">Abstract</summary>
  <font color = "7C4700">
  Ahmed, Bodwin, Sahneh, Kobourov, and Spence (WG 2020) introduced additive spanners for weighted graphs and constructed (i) a $+2W_{\max}$ spanner with $O(n^{3/2})$ edges and (ii)  a $+4W_{\max}$ spanner with $\tilde{O}(n^{7/5})$ edges, and (iii)  a $+8W_{\max}$ spanner with $O(n^{4/3})$ edges, for any weighted graph with $n$ vertices. Here $W_{\max} = \max_{e\in E}w(e)$ is the maximum edge weight in the graph.  Their results for $+2W_{\max}$, $+4W_{\max}$, and $+8W_{\max}$ match the state-of-the-art bounds for the unweighted counterparts where $W_{\max} = 1$. They left open the question of constructing a $+6W_{\max}$ spanner with $O(n^{4/3})$ edges.  Elkin, Gitlitz, and Neiman (DISC 2021) made significant progress on this problem by showing that there exists a $+(6+\epsilon)W_{\max}$ spanner with $O(n^{4/3}/\epsilon)$ edges for any fixed constant $\epsilon > 0$. Indeed, their result is stronger as the additive stretch is local: the stretch for any pair $u,v$ is $+(6+\epsilon)W_{uv}$ where $W_{uv}$ is the maximum weight edge on the shortest path from $u$ to $v$. <br><br>
  
  In this work, we resolve the problem posted by Ahmed et al. up to a poly-logarithmic factor in the number of edges: We construct a $+6W_{\max}$ spanner with $\tilde{O}(n^{4/3})$ edges.  We extend the construction for $+6$-spanners of Woodruff (ICALP 2010), and our main contribution is an analysis tailoring to the weighted setting.  The stretch of our spanner could also be made local, in the sense of Elkin, Gitlitz, and Neiman.  We also study the fast constructions of additive spanners with $+6W_{\max}$  and $+4W_{\max}$ stretches. We obtain, among other things, an algorithm for constructing a $+(6+\epsilon)W_{\max}$ spanner of $\tilde{O}(\frac{n^{4/3}}{\epsilon})$ edges in $\tilde{O}(n^2)$ time.<br>
  </font>
  </details>
  
- **Optimal Padded Decomposition For Bounded Treewidth Graphs**
  <br>Arnold Filtser and Tobias Friedrich and Davis Issac and Nikhil Kumar and **Hung Le** and Nadym Mallek and Ziena Zeif.
  <br>[[PDF](https://arxiv.org/abs/2407.12230)][[blog post](https://minorfree.github.io/PaddedTW/)]
  <br>Manuscript. 
  <details><summary style="color:#7C4700">Abstract</summary>
  <font color = "7C4700">
  A $(\beta,\delta,\Delta)$-padded decomposition of an edge-weighted graph $G = (V,E,w)$ is a stochastic decomposition into clusters of diameter at most $\Delta$ such that for every vertex $v\in V$, the probability that the ball $B_G(v,\gamma\Delta)$ is entirely contained in the cluster containing $v$ is at least $e^{-\beta\gamma}$ for every $\gamma \in [0,\delta]$. Padded decompositions have been studied for decades and have found numerous applications, including metric embedding, multicommodity flow-cut gap, muticut, and zero extension problems, to name a few.  In these applications, parameter $\beta$, called the padding parameter, is the most important parameter since it decides either the distortion or the approximation ratios. For general graphs with $n$ vertices, $\beta = \Theta(\log n)$.<br><br>
  
  Klein, Plotkin, and Rao (KPR) showed that $K_r$-minor-free graphs have padding parameter $\beta = O(r^3)$, which is a significant improvement over general graphs when $r$ is a constant. However, when $r= \Omega(\log n)$, the padding parameter in KPR decomposition can be much worse than $\log n$. A long-standing conjecture is to construct a padded decomposition for $K_r$-minor-free graphs with padding parameter $\beta = O(\log r)$. Despite decades of research, the best-known result is $\beta = O(r)$, even for graphs with treewidth at most $r$.<br><br>
  
  In this work, we make significant progress toward the aforementioned conjecture by showing that graphs with treewidth $\mathrm{tw}$ admit a padded decomposition with padding parameter $O(\log \mathrm{tw})$, which is tight. Our padding parameter is strictly better than $O(\log n)$ whenever $\mathrm{tw} = n^{o(1)}$, and is never worse than what is known for general graphs. As corollaries, we obtain an exponential improvement in dependency on treewidth in a host of algorithmic applications: $O(\sqrt{ \log n \cdot \log(\mathrm{tw})})$ flow-cut gap,  the maxflow-min multicut ratio of $O(\log(\mathrm{tw}))$, an $O(\log(\mathrm{tw}))$ approximation for the 0-extension problem, an $\ell^{O(\log n)}_\infty$ embedding with distortion $O(\log \mathrm{tw})$, and an $O(\log \mathrm{tw})$ bound for integrality gap for the uniform sparsest cut.<br>
  </font>
  </details>
  
- **Learning Representations for Hierarchies with Minimal Support**
  <br>Benjamin Rozonoyer and Michael Boratko and Dhruvesh Patel and Wenlong Zhao and Shib Sankar Dasgupta and **Hung Le** and Andrew McCallum.
  <br>
  Authors ordered by contribution.
  <br>[[PDF](https://openreview.net/forum?id=HFS800reZK)]
  <br>To appear in the 38th Annual Conference on Neural Information Processing Systems. **NeurIPS24**. 
  <details><summary style="color:#7C4700">Abstract</summary>
  <font color = "7C4700">
  When training node embedding models to represent large directed graphs (digraphs), it is impossible to observe all entries of the adjacency matrix during training. As a consequence most methods employ sampling. For very large digraphs, however, this means many (most) entries may be unobserved during training. In general, observing every entry would be necessary to uniquely identify a graph, however if we know the graph has a certain property some entries can be omitted - for example, only half the entries would be required for a symmetric graph. In this work, we develop a novel framework to identify a subset of entries required to uniquely distinguish a graph among all transitively-closed DAGs. We give an explicit algorithm to compute the provably minimal set of entries, and demonstrate empirically that one can train node embedding models with greater efficiency and performance, provided the energy function has an appropriate inductive bias. We achieve robust performance on synthetic hierarchies and a larger real-world taxonomy, observing improved convergence rates in a resource-constrained setting while reducing the set of training examples by as much as 99%.<br>
  </font>
  </details>
  


- **Embedding Planar Graphs into Graphs of Treewidth** $O(\log^{3}n)$
  <br>
  Hsien-Chih Chang and Vincent Cohen-Addad and Jonathan Conroy and **Hung Le** and Marcin Pilipczuk and Michał Pilipczuk.
  <br>To appear in the 36th Annual ACM-SIAM Symposium on Discrete Algorithms. **SODA 2025**.
  <br>[[PDF](https://arxiv.org/abs/2411.00216)]
  <details><summary style="color:#7C4700">Abstract</summary>
  <font color = "7C4700">
  Cohen-Addad, Le, Pilipczuk, and Pilipczuk  recently constructed a stochastic embedding with expected $1+\epsilon$ distortion of $n$-vertex planar graphs (with polynomial aspect ratio) into graphs of treewidth $O(\epsilon^{-1}\log^{13} n)$.  Their embedding is the first to achieve polylogarithmic treewidth.  However, there remains a large gap between the treewidth of their embedding and the treewidth lower bound of $\Omega(\log n)$ shown by Carroll and Goel.  In this work, we substantially narrow the gap by constructing a stochastic embedding with treewidth  $O(\epsilon^{-1}\log^{3}n)$.<br><br>
  
  We obtain our embedding by improving various steps in the CLPP construction.  First, we streamline their embedding construction by showing that one can construct a low-treewidth embedding for any graph from (i) a stochastic hierarchy of clusters and (ii) a stochastic balanced cut. We shave off some logarithmic factors in this step by using a single hierarchy of clusters.  Next, we construct a stochastic hierarchy of clusters with optimal separating probability and hop bound based on shortcut partition.  Finally, we construct a stochastic balanced cut with an improved trade-off between the cut size and the number of cuts. This is done by a new analysis of the contraction sequence; our analysis gives an optimal treewidth bound for graphs admitting a contraction sequence.<br> 
  </font>
  </details>  
  
- **Spanners in Planar Domains via Steiner Spanners and non-Steiner Tree Covers**
  <br>
  Sujoy Bhore and Balázs Keszegh and Andrey Kupavskii and **Hung Le** and Alexandre Louvet and Dömötör Pálvölgyi and Csaba D. Tóth.
  <br>[[PDF](https://arxiv.org/abs/2404.05045)][[blog post](https://minorfree.github.io/SFTreeCover/)]
  <br>To appear in the 36th Annual ACM-SIAM Symposium on Discrete Algorithms. **SODA 2025**.
  <details><summary style="color:#7C4700">Abstract</summary>
  <font color = "7C4700">
  We study spanners in planar domains, including polygonal domains, polyhedral terrain, and planar metrics. Previous work showed that for any constant $\epsilon\in (0,1)$, one could construct a $(2+\epsilon)$-spanner with $O(n\log(n))$ edges (SICOMP 2019), and there is a lower bound of $\Omega(n^2)$ edges for any $(2-\epsilon)$-spanner (SoCG 2015). The main open question is whether a linear number of edges suffices and the stretch can be reduced to $2$. We resolve this problem by showing that for stretch $2$, one needs $\Omega(n\log n)$ edges, and for stretch $2+\epsilon$ for any fixed $\epsilon \in (0,1)$, $O(n)$ edges are sufficient. Our lower bound is the first super-linear lower bound for stretch $2$. <br><br>
  
  En route to achieve our result, we introduce the problem of constructing non-Steiner tree covers for metrics, which is a natural variant of the well-known Steiner point removal problem for trees (SODA 2001). Given a tree and a set of terminals in the tree,  our goal is to construct a collection of a small number of dominating trees such that for every two points, at least one tree in the collection preserves their distance within a small stretch factor. Here, we identify an unexpected threshold phenomenon around  $2$ where a sharp transition from $n$ trees to $\Theta(\log n)$ trees and then to $O(1)$ trees happens. Specifically, (i) for stretch $ 2-\epsilon$, one needs $\Omega(n)$ trees; (ii) for stretch $2$, $\Theta(\log n)$ tree is necessary and sufficient; and (iii) for stretch $2+\epsilon$, a constant number of trees suffice. Furthermore, our lower bound technique for the non-Steiner tree covers of stretch $2$ has further applications in proving lower bounds for two related constructions in tree metrics: reliable spanners and locality-sensitive orderings. Our lower bound for locality-sensitive orderings matches the best upper bound (STOC 2022). <br><br>
  
  Finally, we study $(1+\epsilon)$-spanners in planar domains using Steiner points. In planar domains, Steiner points are necessary to obtain a stretch arbitrarily close to $1$. Here, we construct a $(1+\epsilon)$-spanner with an almost linear dependency on $\epsilon$ in the number of edges; the precise bound is $O((n/\epsilon)\cdot \log(\epsilon^{-1}\alpha(n))\cdot \log \epsilon^{-1})$ edges, where $\alpha(n)$ is the inverse Ackermann function. Our result generalizes to graphs of bounded genus. For $n$ points in a polyhedral metric, we construct a Steiner $(1+\epsilon)$-spanner with $O((n/\epsilon)\cdot \log(\epsilon^{-1}\alpha(n))\cdot \log \epsilon^{-1})$ edges.<br>
  </font>
  </details>

- **Towards Instance-Optimal Euclidean Spanners**
  <br>**Hung Le** and Shay Solomon and Cuong Than and Csaba D. Tóth and Tianyi Zhang.
  <br>[[PDF](https://arxiv.org/abs/2409.08227)]
  <br>The 65th IEEE Symposium on the Foundations of Computer Science. **FOCS 2024**
  <details><summary style="color:#7C4700">Abstract</summary>
  <font color = "7C4700">
  Euclidean spanners are important geometric objects that have been extensively studied since the 1980s. The two most basic "compactness" measures of a Euclidean spanner $E$ are the size (number of edges) $|E|$ and the weight (sum of edge weights) $\|E\|$. The state-of-the-art constructions of Euclidean $(1+\epsilon)$-spanners in $\mathbb{R}^d$ have $O_d\left(n\cdot \epsilon^{-d+1}\right)$ edges (or sparsity $O_d(\epsilon^{-d+1})$) and weight $O_d\left(\epsilon^{-d}\log\epsilon^{-1}\right) \cdot \|E_\mathrm{mst}\|$  (or lightness $O_d(\epsilon^{-d}\log\epsilon^{-1})$); here $O_d$ suppresses a factor of $d^{O(d)}$ and  $\|E_\mathrm{mst}\|$ denotes the weight of a minimum spanning tree of the input point set.<br><br>  
  
  Importantly, these two upper bounds are (near-)optimal (up to the $d^{O(d)}$ factor and disregarding the factor of $\log(\epsilon^{-1})$ in the lightness bound) for some extremal instances [Le and Solomon, 2019], and therefore they are (near-) optimal in an existential sense. Moreover, both these upper bounds are attained by the same construction---the classic greedy spanner, whose sparsity and lightness are not only existentially optimal, but they also significantly outperform those of any other Euclidean spanner construction studied in an experimental study by [Farshi-Gudmundsson, 2009] for various practical point sets in the plane. This raises the natural question of whether the greedy spanner is (near-) optimal for any point set instance?  <br><br> 
        
  Motivated by this question, we initiate the study of instance optimal Euclidean spanners. Our results are two-fold.
  
  <ul> <li> Rather surprisingly (given the aforementioned experimental study), we demonstrate that the greedy spanner is  far from being instance optimal, even when allowing its stretch to grow. More concretely, we design two hard instances of point sets in the plane, where the greedy $(1+x \epsilon)$-spanner (for basically any parameter $x \ge 1$) has $\Omega_x(\epsilon^{-1/2}) \cdot |E_{\mathrm{sparse}}|$ edges and weight $\Omega_x(\epsilon^{-1}) \cdot \|E_{\mathrm{light}}\|$, where  $E_{\mathrm{sparse}}$ and $E_{\mathrm{light}}$ denote the per-instance sparsest and lightest $(1+\epsilon)$-spanners, respectively, and the $\Omega_x$ notation suppresses a polynomial dependence on $1/x$. </li>
  <li> As our main contribution, we design a new construction of Euclidean spanners, which is inherently different from known constructions, achieving the following bounds:  a stretch of $1+\epsilon\cdot 2^{O(\log^*(d/\epsilon))}$ with $O(1) \cdot |E_{\mathrm{sparse}}|$ edges and weight $O(1) \cdot \|E_{\mathrm{light}}\|$. In other words, we show that a slight increase to the stretch suffices for obtaining instance optimality up to an absolute constant for both sparsity and lightness. Remarkably, there is only a log-star dependence on the dimension in the stretch, and there is no dependence on it whatsoever in the number of edges and weight. In general, for any integer $k \ge 1$, we can construct a Euclidean spanner in $\mathbb{R}^d$ of stretch $1+\epsilon\cdot 2^{O(k)}$ with $O\left(\log^{(k)}(\epsilon^{-1}) + \log^{(k-1)}(d)\right) \cdot |E_{\mathrm{sparse}}|$ edges and weight $O\left(\log^{(k)}(\epsilon^{-1}) + \log^{(k-1)}(d)\right) \cdot \|E_{\mathrm{light}}\|$, where $\log^{(k)}$ denotes the $k$-iterated logarithm. </li>
  </ul>
  </font>
  </details>
  
- **Optimal Euclidean Tree Covers**
  <br>
  Hsien-Chih Chang and Jonathan Conroy and **Hung Le** and Lazar Milenkovic and Shay Solomon and Cuong Than.
  <br>[[PDF](https://arxiv.org/abs/2403.17754)][[blog post](https://minorfree.github.io/EuTreeCov/)]
  <br>The 40th International Symposium on Computational Geometry. **SoCG 2024**.
  <details><summary style="color:#7C4700">Abstract</summary>
  <font color = "7C4700">
  A $(1+\epsilon)$-stretch tree cover of a metric space is a collection of trees, where every pair of points has a $(1+\epsilon)$-stretch path in one of the trees. The celebrated Dumbbell Theorem [Arya et al. STOC'95] states that any set of $n$ points in $d$-dimensional Euclidean space admits a $(1+\epsilon)$-stretch tree cover with $O_d(\epsilon^{-d} \cdot \log(1/\epsilon))$ trees, where the $O_d$ notation suppresses terms that depend solely on the dimension~$d$ The running time of their construction is $O_d(n \log n \cdot \frac{\log(1/\epsilon)}{\epsilon^{d}} + n \cdot \epsilon^{-2d})$. Since the same point may occur in multiple levels of the tree, the maximum degree of a point in the tree cover may be as large as $\Omega(\log \Phi)$, where $\Phi$ is the aspect ratio of the input point set.<br>
  
  In this work we present a  $(1+\epsilon)$-stretch tree cover with $O_d(\epsilon^{-d+1} \cdot \log(1/\epsilon))$ trees, which is optimal (up to the $\log(1/\epsilon)$ factor).  Moreover, the maximum degree of points in any tree is an absolute constant for any $d$.   As a direct corollary, we obtain an optimal routing scheme in low-dimensional Euclidean spaces.  We also present a  $(1+\epsilon)$-stretch Steiner tree cover (that may use  Steiner points) with $O_d(\epsilon^{(-d+1)/{2}} \cdot \log(1/\epsilon))$ trees, which too is optimal. The running time of our two constructions is linear in the number of edges in the respective tree covers, ignoring an additive $O_d(n \log n)$ term; this improves over the running time underlying the Dumbbell Theorem.<br>
  </font>
  </details>
  
- **Computing Diameter+2 in Truly Subquadratic Time for Unit-Disk Graphs**
  <br>
  Hsien-Chih Chang and Jie Gao and **Hung Le**
  <br>[[PDF](https://arxiv.org/abs/2401.12881)][[blog post](https://minorfree.github.io/UDG/)]
  <br>The 40th International Symposium on Computational Geometry. **SoCG 2024**.
  <details><summary style="color:#7C4700">Abstract</summary>
  <font color = "7C4700">
  Finding the diameter of a graph in general cannot be done in truly subquadratic assuming the Strong Exponential Time Hypothesis (SETH), even when the underlying graph is unweighted and sparse. When restricting to concrete classes of graphs and assuming SETH, planar graphs and minor-free graphs admit truly subquadratic algorithms, while geometric intersection graphs of unit balls, congruent equilateral triangles, and unit segments do not. Unit-disk graphs are one of the major open cases where the complexity of diameter computation remains unknown. More generally, it is conjectured that a truly subquadratic time algorithm exists for pseudo-disk graphs where each pair of objects has at most two intersections on the boundary. <br>
  
  In this paper, we show a truly subquadratic algorithm of running time $\tilde{O}(n^{2-1/18})$, for finding the diameter in a unit-disk graph, whose output differs from the optimal solution by at most 2. This is the first algorithm that provides an additive guarantee in distortion, independent of the size or the diameter of the graph. Our algorithm requires two important technical elements. First, we show that for the intersection graph of pseudo-disks, the graph VC-dimension, either of $k$-hop balls or the distance encoding vectors, is 4.  This contracts to the VC dimension of the pseudo-disks themselves as geometric ranges (which is known to be 3). Second, we introduce a clique-based $r$-clustering for geometric intersection graphs, which is an analog of the $r$-division construction for planar graphs. We also showcase the new techniques by establishing new results for distance oracles for unit-disk graphs with subquadratic storage and $O(1)$ query time. The results naturally extend to unit $L_1$ or $L_\infty$-disks and fat pseudo-disks of similar size. Last, if the pseudo-disks additionally have bounded ply, we have a truly subquadratic algorithm to find the exact diameter. <br>
  </font>
  </details>
  
- **VC Set Systems in Minor-free (Di)Graphs and Applications**
  <br>
  **Hung Le** and Christian Wulff-Nilsen
  <br>[[PDF](https://arxiv.org/abs/2304.01790)]
  <br>The 35th Annual ACM-SIAM Symposium on Discrete Algorithms. **SODA 2024**.
  <details><summary style="color:#7C4700">Abstract</summary>
  <font color = "7C4700">
  A recent line of work on VC set systems in minor-free (undirected) graphs, starting from Li and Parter~, who constructed a new VC set system for planar graphs, has given surprising algorithmic results. In this work, we initialize a more systematic study of VC set systems for minor-free graphs and their applications in both undirected graphs and directed graphs (a.k.a digraphs).  More precisely: <br>
  <ul> <li>We propose a new variant of Li-Parter set system for undirected graphs. Our set system settles two weaknesses of Li-Parter set system: the terminals can be anywhere, and the graph can be $K_h$-minor-free for any fixed $h$. We obtain several algorithmic applications, and notably: (i) the first exact distance oracle for unweighted and undirected $K_h$-minor-free graphs that has truly subquadratic space and constant query time, and (ii) the first truly subquadratic time algorithm for computing Wiener index of $K_h$-minor-free graphs, resolving an open problem posed by Ducoffe, Habib, and Viennot.</li>
  <li>We extend our set system to  $K_h$-minor-free digraphs and show that its VC dimension is $O(h^2)$.    We use this result to design the first subquadratic time algorithm for computing (unweighted) diameter and all-vertices eccentricities in   $K_h$-minor-free digraphs.</li>
  <li>We show that the system of directed balls in minor-free digraphs has VC dimension at most $h-1$. We then present a new technique to exploit the VC system of balls, giving the first exact distance oracle for unweighted minor-free  digraphs that has truly subquadratic space and logarithmic query time.</li>
  <li>On the negative side, we show that VC set system constructed from shortest path trees of planar digraphs does not have a bounded VC dimension. This leaves an intriguing open problem: determine a necessary and sufficient condition for a set system derived from a minor-free graph to have a bounded VC-dimension. </li>
  </ul>
  The highlight of our work is the results for  digraphs, as we are not aware of known algorithmic work on constructing and exploiting VC set systems for digraphs.
  </font>
  </details>
  
- **Shortcut Partitions in Minor-Free Graphs: Steiner Point Removal, Distance Oracles, Tree Covers, and More**
  <br>
  Hsien-Chih Chang and Jonathan Conroy and **Hung Le** and Lazar Milenkovic and Shay Solomon and Cuong Than.
  <br> Results in this paper subsume results for planar graphs in [our earlier paper](https://arxiv.org/abs/2306.06235).
  <br>[[PDF](https://arxiv.org/abs/2308.00555)]
  <br>The 35th Annual ACM-SIAM Symposium on Discrete Algorithms. **SODA 2024**.
  <details><summary style="color:#7C4700">Abstract</summary>
  <font color = "7C4700">
  The notion of shortcut partition, introduced recently by Chang, Conroy, Le, Milenković, Solomon, and Than, is a new type of graph partition into low-diameter clusters. Roughly speaking, the shortcut partition guarantees that for every two vertices $u$ and $v$ in the graph, there exists a path between $u$ and $v$ that intersects only a few clusters.  They proved that any planar graph admits a shortcut partition and gave several applications, including a construction of tree cover for arbitrary planar graphs with stretch $1+\epsilon$ and $O(1)$ many trees for any fixed $\epsilon \in (0,1)$.  However, the construction heavily exploits planarity in multiple steps, and is thus inherently limited to planar~graphs.<br><br>
  
  In this work, we breach the "planarity barrier" to construct a shortcut partition for $K_r$-minor-free graphs for any $r$. To this end, we take a completely different approach---our key contribution is a novel deterministic variant of the  cop decomposition in minor-free graphs.  Our shortcut partition for $K_r$-minor-free graphs yields several direct applications. Most notably, we construct the first optimal distance oracle for $K_r$-minor-free graphs, with $1+\epsilon$ stretch, linear space, and constant query time for any fixed $\epsilon \in (0,1)$.  The previous best distance oracle  uses $O(n\log n)$ space and $O(\log n)$ query time, and its construction relies on Robertson-Seymour structural theorem and other sophisticated tools.  We also obtain the first tree cover of $O(1)$ size for minor-free graphs with stretch $1+\epsilon$, while the previous best $(1+\epsilon)$-tree cover has size $O(\log^2 n)$.<br><br>  
  
  As a highlight of our work, we employ our shortcut partition to resolve a major open problem---the Steiner point removal (SPR) problem: Given any set $K$ of terminals in an arbitrary edge-weighted planar graph $G$, is it possible to construct a minor $M$ of $G$ whose vertex set is~$K$, which preserves the shortest-path distances between all pairs of terminals in $G$ up to a constant factor?  Positive answers to the SPR problem were only known for very restricted classes of planar graphs: trees, outerplanar graphs, and series-parallel graphs. We resolve the SPR problem in the affirmative for any planar graph, and more generally for any $K_r$-minor-free graph for any fixed $r$. To achieve this result, we prove the following general reduction and combine it with our new shortcut partition: For any graph family closed under taking subgraphs, the existence of a shortcut partition yields a positive solution to the SPR problem. 
  </font>
  </details>


- **Covering Planar Metrics (and Beyond): O(1) Trees Suffice**
  <br>
  Hsien-Chih Chang and Jonathan Conroy and **Hung Le** and Lazar Milenkovic and Shay Solomon and Cuong Than.
  <br>
  The 64th IEEE Symposium on the Foundations of Computer Science. **FOCS 2023**
  <br>[[PDF](https://arxiv.org/abs/2306.06215)]<br>
  <details><summary style="color:#7C4700">Abstract</summary>
  <font color = "7C4700">
  While research on the geometry of planar graphs has been active in the past decades, many properties of planar metrics remain mysterious. This paper studies a fundamental aspect of the planar graph geometry: covering planar metrics by a small collection of simpler metrics.  Specifically, a tree cover of a metric space $(X, \delta)$ is a collection of trees, so that every pair of points $u$ and $v$ in $X$ has a low-distortion path in at least one of the trees. <br><br>
  
  The celebrated Dumbbell Theorem states that any low-dimensional Euclidean space admits a tree cover with $O(1)$ trees and distortion $1+\varepsilon$, for any fixed $\varepsilon \in (0,1)$. This result has found numerous algorithmic applications, and has been generalized to the wider family of doubling metrics.  Does the same result hold for planar metrics?  A positive answer would add another evidence to the well-observed connection between Euclidean/doubling metrics and planar metrics. <br><br>
  
  In this work, we answer this fundamental question affirmatively. Specifically, we show that for any given fixed $\varepsilon \in (0,1)$, any planar metric can be covered by $O(1)$ trees with distortion $1+\varepsilon$.  Our result for planar metrics follows from a rather general framework:  First we reduce the problem to constructing tree covers with additive distortion.  Then we introduce the notion of shortcut partition, and draw connection between shortcut partition and additive tree cover.  Finally we prove the existence of shortcut partition for any planar metric, using new insights regarding the grid-like structure of planar graphs. To demonstrate the power of our framework: <br>
  
  <ul> <li>We establish additional tree cover results beyond planar metrics; in particular, we present an $O(1)$-size tree cover with distortion $1+\varepsilon$ for bounded treewidth metrics;</li>
  <li>We obtain several algorithmic applications in planar graphs from our tree cover.</li>
  </ul>
  The grid-like structure is a technical contribution that we believe is of independent interest. We showcase its applicability beyond tree cover by constructing a simpler and better embedding of planar graphs into $O(1)$-treewidth graphs with  small additive distortion, resolving an open problem in this line of research.
  </font>
  </details>
  
- **Optimal Fault-Tolerant Spanners in Euclidean and Doubling Metrics: Breaking the $\Omega(\log n)$ Lightness Barrier**
  <br>
  **Hung Le** and Shay Solomon and Cuong Than.
  <br>
 The 64th IEEE Symposium on the Foundations of Computer Science. **FOCS 2023**
  <br>[[PDF](https://arxiv.org/abs/2306.11226)]<br>
  <details><summary style="color:#7C4700">Abstract</summary>
  <font color = "7C4700">
  An essential requirement of spanners in many applications is to be em fault-tolerant: a $(1+\epsilon)$-spanner of a metric space is called  (vertex) $f$-fault-tolerant ($f$-FT) if it remains a $(1+\epsilon)$-spanner (for the non-faulty points) when up to $f$ faulty points are removed from the spanner. Fault-tolerant (FT) spanners for Euclidean and doubling metrics have been extensively studied since the 90s. <br><br>
  
  For low-dimensional Euclidean metrics, Czumaj and Zhao in SoCG'03 showed that the optimal guarantees $O(f n)$, $O(f)$ and $O(f^2)$ on the size, degree and lightness of $f$-FT spanners can be achieved via a greedy algorithm, which naively runs in $O(n^3) \cdot 2^{O(f)}$ time. An earlier construction, by Levcopoulos et al. from STOC'98, has a faster running time of  $O(n \log n) + n 2^{O(f)}$, but has   a slack of $2^{\Omega(f)}$ in all the three involved parameters. The question of whether the optimal bounds of [CZ03] can be achieved via a fast construction has remained elusive, with the  lightness  parameter being the bottleneck: <br><br>
  
  Any construction (other than [CZ03]) has lightness either $2^{\Omega(f)}$ or $\Omega(\log n)$. Moreover, in the wider family of doubling metrics, it is not even clear whether there exists an $f$-FT spanner with lightness that depends solely on $f$ (even exponentially): all existing constructions have lightness $\Omega(\log n)$ since they are built on the net-tree spanner, which is induced by a hierarchical net-tree of lightness  $\Omega(\log n)$. <br><br>
  
  In this paper we settle in the affirmative these longstanding open questions. Specifically, we design a construction of $f$-FT spanners that is optimal with respect to all the involved parameters (size, degree, lightness and running time): For any $n$-point doubling metric, any $\epsilon > 0$, and any integer   $1 \leq f \leq n-2$, our construction provides, within time $O(n  \log n + f n)$, an $f$-FT $(1+\epsilon)$-spanner with size $O(f n)$, degree $O(f)$ and lightness $O(f^2)$. <br><br>
  
  To break the $\Omega(\log n)$ lightness barrier,  we introduce a new geometric object --- the light net-forest. Like the net-tree, the light net-forest is induced by a hierarchy of nets. However, to ensure small lightness, the light net-forest is inherently less well-connected than the net-tree, which, in turn, makes the task of achieving fault-tolerance significantly more challenging. Further, to achieve the optimal degree (and size) together with optimal lightness, and to do so within the optimal running time --- we overcome several highly nontrivial technical challenges.
  </font>
  </details>
  
  
- **Planar and Minor-Free Metrics Embed into Metrics of Polylogarithmic Treewidth with Expected Multiplicative Distortion Arbitrarily Close to 1**
  <br>
  Vincent Cohen-Addad and **Hung Le** and Marcin Pilipczuk and Michał Pilipczuk.
  <br>
  The 64th IEEE Symposium on the Foundations of Computer Science. **FOCS 2023**
  <br>[[PDF](https://arxiv.org/abs/2304.07268)]<br>
  <details><summary style="color:#7C4700">Abstract</summary>
  <font color = "7C4700">
  We prove that there is a randomized polynomial-time algorithm that given an edge-weighted graph $G$ excluding a fixed-minor $Q$ on $n$ vertices and an accuracy parameter $\epsilon >0$, constructs an edge-weighted graph~$H$ and an embedding $\eta: V(G)\rightarrow V(H)$ with the following properties:<br>
  <ul> <li>For any constant size $Q$, the treewidth of $H$ is polynomial in $\epsilon^{-1}$, $\log n$, and the logarithm of the stretch of the distance metric in $G$.</li>
  <li>The expected multiplicative distortion is $(1+\epsilon)$: for every pair of vertices $u,v$ of $G$, we have $\mathrm{dist}_H(\eta(u),\eta(v))\geq \mathrm{dist}_G(u,v)$ always and $\mathbb{E}[\mathrm{dist}_H(\eta(u),\eta(v))]\leq (1+\epsilon)\mathrm{dist}_G(u,v)$.</li>
  </ul>
  Our embedding is the first to achieve polylogarithmic treewidth of the host graph and comes close to the lower bound by Carroll and Goel, who showed that any embedding of a planar graph with $O(1)$ expected distortion requires the host graph to have treewidth $\Omega(\log n)$.  It also provides a unified framework for obtaining randomized quasi-polynomial-time approximation schemes for a variety of problems including network design, clustering or routing problems, in minor-free metrics where the optimization goal is the sum of selected distances. Applications include the capacitated vehicle routing problem, and capacitated clustering problems.
  </font>
  </details>

  
- **Sparse Euclidean Spanners with Optimal Diameter: A General Robust Lower Bound Via a Concave Inverse-Ackermann Function**
  <br>
  **Hung Le** and Lazar Milenkovic and Shay Solomon
  <br>
  The 39th International Symposium on Computational Geometry. **SoCG 2023**
  <br>Manuscript<br>
  <details><summary style="color:#7C4700">Abstract</summary>
  <font color = "7C4700">
  In STOC'95, Arya et al. showed that any set of $n$ points in $\mathbb R^d$ admits a $(1+\epsilon)$-spanner with hop-diameter at most 2 (respectively, 3) and $O(n \log n)$ edges (resp., $O(n \log \log n)$ edges). They also gave a general upper bound tradeoff of hop-diameter at most $k$ and $O(n \alpha_k(n))$ edges, for any $k \geq 2$. The function $\alpha_k$ is the inverse of a certain Ackermann-style function at the $\lfloor k/2 \rfloor$th level of the primitive recursive hierarchy, where $\alpha_0(n) = \lceil n/2 \rceil, \alpha_1(n) = \left\lceil \sqrt{n} \right\rceil, \alpha_2(n) = \lceil \log{n} \rceil, \alpha_3(n) = \lceil \log\log{n} \rceil, \alpha_4(n) = \log^* n,\ldots$. Roughly speaking, for $k \geq 2$ the function $\alpha_{k}$ is close to $\lfloor \frac{k-2}{2} \rfloor$-iterated log-star function, i.e., $\log$ with $\lfloor \frac{k-2}{2} \rfloor$ stars. Also, $\alpha_{2\alpha(n)+4}(n) \leq 4$, where $\alpha(n)$ is the one-parameter inverse Ackermann function, which is an extremely slowly growing function. <br><br>
Despite a large body of work on spanners of bounded hop-diameter, the fundamental question of whether this tradeoff between size and hop-diameter of Euclidean $(1+\epsilon)$-spanners is optimal has remained open, even in one-dimensional spaces.  There are three known lower bound tradeoffs between size and hop-diameter: (i) An optimal $k$ versus $\Omega(n \alpha_k(n))$ by Alon and Schieber, but it applies to stretch 1 rather than $1+\epsilon$; (ii) a suboptimal $k$ versus $\Omega(n\alpha_{2k+6}(n))$ by Chan and Gupta, and (iii) A suboptimal $k$ versus $\Omega(\frac{n}{2^{6\lfloor k/2 \rfloor}}\alpha_k(n))$ by Le et al.. <br><br>
This paper establishes the optimal $k$ versus $\Omega(n \alpha_k(n))$ lower bound tradeoff for stretch $1+\epsilon$, for any $\epsilon> 0$, and for any $k$. The key conceptual contribution here is in achieving optimality by shaving off an extremely slowly growing term, namely $2^{6\lfloor k/2 \rfloor}$ for  $k \leq O(\alpha(n))$; such a fine-grained optimization (that achieves optimality) is very rare in the literature.<br><br>
To shave off the $2^{6\lfloor k/2 \rfloor}$ term from the previous bound of Le et al., our argument has to drill much deeper. In particular, we propose a new way of analyzing recurrences that involve inverse-Ackermann style functions, and our key technical contribution is in  presenting the first explicit construction of concave versions of these functions. An important advantage of our approach over previous ones is its robustness: While all previous lower bounds are applicable only to restricted 1-dimensional point sets, ours applies even to random point sets. 
  </font>
  </details>
  
  
- **A Unified Framework for Light Spanners**
  <br>
  **Hung Le** and Shay Solomon.
  <br>
  The 55th Annual ACM Symposium on Theory of Computing. **STOC 2023**.
  <br>[[PDF](https://arxiv.org/abs/2008.10582)]<br> This paper is a merge of [arXiv:2111.13748](https://arxiv.org/pdf/2111.13748.pdf) and [arXiv:2106.15596](https://arxiv.org/abs/2106.15596)<br>
  <details><summary style="color:#7C4700">Abstract</summary>
  <font color = "7C4700">
   Seminal works on light spanners over the years provide spanners with optimal lightness in various graph classes, such as in general graphs, Euclidean spanners and minor-free graphs. Three shortcomings of previous works on light spanners are: (1) The techniques are ad hoc per graph class, and thus can't be applied broadly.  (2) The runtimes of these constructions are almost always sub-optimal, and usually far from optimal. (3) These constructions are optimal in the standard and crude sense, but not in a refined sense that takes into account a wider range of involved parameters.<br><br>
  This work aims at addressing these shortcomings by presenting a unified framework of light spanners in a variety of graph classes. Informally, the framework boils down to a transformation from sparse spanners to light spanners; since the state-of-the-art for sparse spanners is much more advanced than that for light spanners, such a transformation is powerful. First, we apply our framework to design fast constructions with optimal lightness for several graph classes. Among various applications, we highlight the following (for simplicity assume $\epsilon >0$ is fixed):<br><br>
  
  <ul> <li>In low-dimensional Euclidean spaces, we present an $O(n\log n)$-time construction  of $(1+\epsilon)$-spanners with lightness and degree both bounded by constants in the algebraic computation tree (ACT) (or real-RAM) model, which is the basic model used in Computational Geometry. The previous state-of-the-art runtime in this model for constant lightness (even for unbounded degree) was $O(n \log^2 n / \log\log n)$, whereas $O(n \log n)$-time spanner constructions with constant degree (and  $O(n)$ edges) are known for years. Our construction is optimal with respect to all the involved quality measures --- runtime, lightness and degree --- and it resolves a major problem in the area of geometric spanners, which was open for three decades. </li>
  </ul>
  Second, we apply our framework to achieve more refined optimality bounds for several graph classes, i.e., the bounds remain optimal when taking into account a wider range of involved parameters, most notably $\epsilon$. Our new constructions are significantly better than the state-of-the-art for every examined graph class. Among various applications, we highlight the following (now $\epsilon >0$ is any parameter):<br><br>
  
  <ul> <li>For $K_r$-minor-free graphs, we provide a  $(1+\epsilon)$-spanner with lightness $\tilde{O}_{r,\epsilon}( \frac{r}{\epsilon} + \frac{1}{\epsilon^2})$, where $\tilde{O}_{r,\epsilon}$ suppresses $\mathsf{polylog}$ factors of $1/\epsilon$ and $r$, improving the lightness bound $\tilde{O}_{r,\epsilon}( \frac{r}{\epsilon^3})$ of Borradaile, Le and Wulff-Nilsen. We complement our upper bound with a highly nontrivial lower bound construction, for which any $(1+\epsilon)$-spanner must have lightness $\Omega(\frac{r}{\epsilon} + \frac{1}{\epsilon^2})$. Interestingly, our lower bound is realized by a geometric graph in $\mathbb{R}^2$. We note that the quadratic dependency on $1/\epsilon$ we proved here is surprising, as the prior work suggested that the dependency on $\epsilon$ should be around $1/\epsilon$.  </li>
  </ul>
  </font>
  </details>
  
- **Tuning the Tail Latency of Distributed Queries Using Replication**
  <br>
  Nathan Ng and **Hung Le** and Marco Serafini.
  <br>
  Authors ordered by contribution; I contributed least to this paper.
  <br>
  Manuscript.
  <br>[[PDF](https://arxiv.org/abs/2212.10387)]<br>
  <details><summary style="color:#7C4700">Abstract</summary>
  <font color = "7C4700">
  Querying graph data with low latency is an important requirement in application domains such as social networks and knowledge graphs. Graph queries perform multiple hops between vertices. When data is partitioned and stored across multiple servers, queries executing at one server often need to hop to vertices stored by another server. Such distributed traversals represent a performance bottleneck for low-latency queries. To reduce query latency, one can replicate remote data to make distributed traversals unnecessary, but replication is expensive and should be minimized. In this paper, we introduce the problem of finding data replication schemes that satisfy arbitrary user-defined query latency constraints with minimal replication cost. We propose a novel workload model to express data access causality, propose a family of heuristics, and introduce non-trivial sufficient conditions for their correctness. Our evaluation on two representative benchmarks show that our algorithms enable fine-tuning query latency with data replication and can find sweet spots in the latency/replication design space.
  </font>
  </details>
  
- **Approximate Distance Oracles for Planar Graphs with Subpolynomial Error Dependency**
  <br>
  **Hung Le**
  <br>
  The 34th Annual ACM-SIAM Symposium on Discrete Algorithms. **SODA 2023**.
  <br>[[PDF](https://arxiv.org/pdf/2207.05659.pdf)]<br>
  <details><summary style="color:#7C4700">Abstract</summary>
  <font color = "7C4700">
  Thorup [FOCS'01, JACM'04] and Klein [SODA'01] independently showed that there exists a $(1+\epsilon)$-approximate distance oracle for planar graphs with $O(n (\log n)\epsilon^{-1})$ space and $O(\epsilon^{-1})$ query time. While the dependency on $n$ is nearly linear, the space-query product of their oracles depend quadratically on $1/\epsilon$. Many follow-up results either improved the space or the query time of the oracles while having the same, sometimes worst, dependency on $1/\epsilon$. Kawarabayashi, Sommer, and Thorup [SODA'13]  were the first to improve the dependency on $1/\epsilon$ from quadratic to nearly linear (at the cost of $\log^*(n)$ factors). It is plausible to conjecture that the linear dependency on $1/\epsilon$ is optimal: for many known distance-related problems in planar graphs,  it was proved that the dependency on $1/\epsilon$ is at least linear.<br><br>
  
  In this work, we disprove this conjecture by reducing the dependency of the space-query product on $1/\epsilon$ from linear all the way down to subpolynomial $(1/\epsilon)^{o(1)}$. More precisely, we construct an oracle with $O(n\log(n)(\epsilon^{-o(1)} + \log^*n))$  space and $\log^{2+o(1)}(1/\epsilon)$ query time. Our construction is the culmination of several different ideas developed over the past two decades. 
  </font>
  </details>
  
- **Low Treewidth Embeddings of Planar and Minor-Free Metrics**
  <br>
  Arnold Filtser and **Hung Le**
  <br>
  The 63rd Annual Symposium on Foundations of Computer Science. **FOCS 2022**.
  <br>[[PDF](https://arxiv.org/pdf/2203.15627.pdf)]<br>
  <details><summary style="color:#7C4700">Abstract</summary>
  <font color = "7C4700">
  Cohen-Addad, Filtser, Klein and Le [FOCS'20] constructed a stochastic embedding of minor-free graphs of diameter $D$ into graphs of treewidth $O_{\epsilon}(\log n)$ with expected additive distortion $+\epsilon D$. Cohen-Addad  et al. then used the embedding  to design the first quasi-polynomial time approximation scheme (QPTAS) for the capacitated vehicle routing problem. Filtser and Le [STOC'21] used the embedding (in a different way) to design a QPTAS for the metric Baker's problems in minor-free graphs. In this work, we devise a new embedding technique to improve the treewidth bound of  Cohen-Addad  et al. exponentially to $O_{\epsilon}(\log\log n)^2$. As a corollary, we obtain the first efficient PTAS for the capacitated vehicle routing problem in minor-free graphs. We also significantly improve the running time of the QPTAS for the metric Baker's problems in minor-free graphs from   $n^{O_{\epsilon}(\log(n))}$ to  $n^{O_{\epsilon}(\log\log(n))^3}$.<br><br>
  
  Applying our embedding technique to planar graphs, we obtain a deterministic embedding of planar graphs of diameter $D$ into graphs of treewidth $O((\log\log n)^2)/\epsilon)$ and  additive distortion $+\epsilon D$ that can be constructed in nearly linear time.  Important corollaries of our result  include a bicriteria PTAS for metric Baker's problems and a PTAS for the vehicle routing problem with bounded capacity in planar graphs, both run in almost-linear time. The running time of our algorithms is significantly better than previous algorithms that require quadratic time.<br><br>
  
  A key idea in our embedding is the construction of an (exact) emulator  for tree metrics with treewidth $O(\log\log n)$ and hop-diameter $O(\log \log n)$. This result may be of independent interest.
  
  </font>
  </details>
  
- **Can't See The Forest for the Trees: Navigating Metric Spaces by Bounded Hop-Diameter Spanners**
  <br>
  Omri Kahalon and **Hung Le** and Lazar Milenkovic and Shay Solomon
  <br>
  The 41st ACM Symposium on Principles of Distributed Computing.  **PODC 2022**
  <br>[[PDF](https://arxiv.org/pdf/2107.14221.pdf)]<br>
  <details><summary style="color:#7C4700">Abstract</summary>
  <font color = "7C4700">
  Spanners for metric spaces have been extensively studied, perhaps most notably in low-dimensional Euclidean spaces  --- due to their numerous applications. Euclidean spanners can be viewed as means of compressing the ${\binom{n}{2}}$ pairwise distances of a $d$-dimensional Euclidean space into $O(n) = O_{\epsilon,d}(n)$ spanner edges, so that the spanner distances preserve the original distances to within a factor of $1+\epsilon$, for any $\epsilon > 0$. Moreover, one can compute such spanners efficiently in the standard centralized and distributed settings. Once the spanner has been computed, it serves as a "proxy" overlay network, on which the computation can proceed, which gives rise to huge savings in space and other important quality measures. <br><br>
  
  The original metric enables us to "navigate" optimally --- a single hop (for any two points) with the exact distance, but the price is high --- $\Theta(n^2)$ edges. Is it possible to efficiently navigate, on a sparse spanner, using $k$ hops and approximate distances, for $k$ close to 1 (say $k=2$)? Surprisingly, this fundamental question has been overlooked in Euclidean spaces, as well as in other classes of metrics, despite the long line of work on spanners in metric spaces.<br><br>
  
  We answer this question in the affirmative via a surprisingly simple observation on bounded hop-diameter spanners for tree metrics, which we apply on top of known, as well as new, tree cover theorems. Beyond its simplicity, the strength of our approach is three-fold:
  
  <ul> <li><b>Applicable</b>: We present a variety of applications of our efficient navigation scheme, including a 2-hop routing scheme in Euclidean spaces with stretch $1+\epsilon$ using $O(\log^2 n)$ bits of memory for labels and routing tables --- to the best of our knowledge, all known routing schemes prior to this work use $\Omega(\log n)$ hops.</li>
  <li><b>Unified</b>: Our navigation scheme and applications extend beyond Euclidean spaces to any class of metrics that admits an efficient tree cover theorem; currently this includes doubling, planar and general metrics, but our approach is unified.</li>
  <li><b>Fault-Tolerant</b>: In Euclidean and doubling metrics, we strengthen all our results to achieve fault-tolerance. To this end, we first design a new construction of fault-tolerant spanners of bounded hop-diameter, which, in turn, relies on a new tree cover theorem for doubling metrics --- hereafter the "Robust Tree Cover" Theorem, which generalizes the classic "Dumbbell Tree" Theorem [Arya et al., STOC'95] in Euclidean spaces. </li>
  </ul>
  </font>
  </details>

  
- **Locality-Sensitive Orderings and Applications to Reliable Spanners**
  <br>
  Arnold Filtser and **Hung Le**
  <br>
  The 54th Annual ACM Symposium on Theory of Computing. **STOC 2022**.
  <br>[[Official version](https://dl.acm.org/doi/pdf/10.1145/3519935.3520042)][[PDF](https://arxiv.org/pdf/2101.07428.pdf)][[Slides](http://hunglvosu.github.io/files/Reliable-Spanners.pdf)]<br>
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
  The 38th International Symposium on Computational Geometry. **SoCG 2022**
  <br>[[Official version](https://drops.dagstuhl.de/opus/volltexte/2022/16062/pdf/LIPIcs-SoCG-2022-54.pdf)][[PDF](https://arxiv.org/pdf/2112.09124.pdf)]<br>
  <details><summary style="color:#7C4700">Abstract</summary>
  <font color = "7C4700">
  In STOC'95 Arya et al. showed that any set of $n$ points in $\mathbb R^d$ admits a $(1+\epsilon)$-spanner with hop-diameter at most 2 (respectively, 3) and $O(n \log n)$ edges (resp., $O(n \log \log n)$ edges). They also gave a general upper bound tradeoff of hop-diameter at most $k$ and $O(n \alpha_k(n))$ edges, for any $k \geq 2$.
  
  The function $\alpha_k$ is the inverse of a certain Ackermann-style function at the $\lfloor k/2 \rfloor$th level of the primitive recursive hierarchy, where $\alpha_0(n) = \lceil n/2 \rceil$, $\alpha_1(n) = \left\lceil \sqrt{n} \right\rceil$, $\alpha_2(n) = \lceil \log{n} \rceil$, $\alpha_3(n) = \lceil \log\log{n} \rceil$, $\alpha_4(n) = \log^* n$, $\alpha_5(n) = \lfloor \frac{1}{2} \log^*n \rfloor, \ldots$. Roughly speaking, for $k \geq 2$ the function $\alpha_{k}$ is close to $\lfloor \frac{k-2}{2} \rfloor$-iterated log-star function, i.e., $\log$ with $\lfloor \frac{k-2}{2} \rfloor$ stars.<br><br>
  
  Whether or not this tradeoff is tight has remained open, even for the cases $k = 2$ and $k = 3$. Two lower bounds are known: The first applies only to spanners with stretch 1 and the second is sub-optimal and applies only to sufficiently large (constant) values of $k$. In this paper we prove a tight lower bound for any constant $k$: For any fixed  $\epsilon > 0$, any $(1+\epsilon)$-spanner for the uniform line metric with hop-diameter at most $k$ must have at least $\Omega(n \alpha_k(n))$ edges.
  
  </font>
  </details>
  
- **Dynamic Matching Algorithms Under Vertex Updates**
  <br>
  **Hung Le** and Lazar Milenkovic and Shay Solomon and Virginia Vassilevska Williams
  <br>
  The 13th Innovations in Theoretical Computer Science. **ITCS 2022**
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

