name:arborescence_root/1
def:arborescence_root(Digraph) -> 'no' | {'yes', Root}
types:
      Digraph = digraph(),
      Root = digraph:vertex()

name:components/1
def:components(Digraph) -> [Component]
types:
      Digraph = digraph(),
      Component = [digraph:vertex()]

name:condensation/1
def:condensation(Digraph) -> CondensedDigraph
types:
      Digraph = digraph(),
      CondensedDigraph = digraph()

name:cyclic_strong_components/1
def:cyclic_strong_components(Digraph) -> [StrongComponent]
types:
      Digraph = digraph(),
      StrongComponent = [digraph:vertex()]

name:is_acyclic/1
def:is_acyclic(Digraph) -> boolean()
types:
      Digraph = digraph()

name:is_arborescence/1
def:is_arborescence(Digraph) -> boolean()
types:
      Digraph = digraph()

name:is_tree/1
def:is_tree(Digraph) -> boolean()
types:
      Digraph = digraph()

name:loop_vertices/1
def:loop_vertices(Digraph) -> Vertices
types:
      Digraph = digraph(),
      Vertices = [digraph:vertex()]

name:postorder/1
def:postorder(Digraph) -> Vertices
types:
      Digraph = digraph(),
      Vertices = [digraph:vertex()]

name:preorder/1
def:preorder(Digraph) -> Vertices
types:
      Digraph = digraph(),
      Vertices = [digraph:vertex()]

name:reachable/2
def:reachable(Vertices, Digraph) -> Reachable
types:
      Digraph = digraph(),
      Vertices = [digraph:vertex()],
      Reachable = [digraph:vertex()]

name:reachable_neighbours/2
def:reachable_neighbours(Vertices, Digraph) -> Reachable
types:
      Digraph = digraph(),
      Vertices = [digraph:vertex()],
      Reachable = [digraph:vertex()]

name:reaching/2
def:reaching(Vertices, Digraph) -> Reaching
types:
      Digraph = digraph(),
      Vertices = [digraph:vertex()],
      Reaching = [digraph:vertex()]

name:reaching_neighbours/2
def:reaching_neighbours(Vertices, Digraph) -> Reaching
types:
      Digraph = digraph(),
      Vertices = [digraph:vertex()],
      Reaching = [digraph:vertex()]

name:strong_components/1
def:strong_components(Digraph) -> [StrongComponent]
types:
      Digraph = digraph(),
      StrongComponent = [digraph:vertex()]

name:subgraph/2
def:subgraph(Digraph, Vertices) -> SubGraph
types:
      Digraph = digraph(),
      Vertices = [digraph:vertex()],
      SubGraph = digraph()

name:subgraph/3
def:subgraph(Digraph, Vertices, Options) -> SubGraph
types:
      Digraph = digraph(),
      SubGraph = digraph(),
      Vertices = [digraph:vertex()],
      Options = [{'type', SubgraphType} | {'keep_labels', boolean()}],
      SubgraphType = 'inherit' | [digraph:d_type()]

name:topsort/1
def:topsort(Digraph) -> Vertices | 'false'
types:
      Digraph = digraph(),
      Vertices = [digraph:vertex()]

