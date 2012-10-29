name:acyclic_add_edge/5
def:acyclic_add_edge(edge(), vertex(), vertex(), label(), digraph()) ->
	edge() | {'error', {'bad_edge', [vertex()]}}

name:add_edge/3
def:add_edge(G, V1, V2) -> edge() | {'error', add_edge_err_rsn()}
types:
      G = digraph(),
      V1 = vertex(),
      V2 = vertex()

name:add_edge/4
def:add_edge(G, V1, V2, Label) -> edge() | {'error', add_edge_err_rsn()}
types:
      G = digraph(),
      V1 = vertex(),
      V2 = vertex(),
      Label = label()

name:add_edge/5
def:add_edge(G, E, V1, V2, Label) -> edge() | {'error', add_edge_err_rsn()}
types:
      G = digraph(),
      E = edge(),
      V1 = vertex(),
      V2 = vertex(),
      Label = label()

name:add_vertex/1
def:add_vertex(G) -> vertex()
types:
      G = digraph()

name:add_vertex/2
def:add_vertex(G, V) -> vertex()
types:
      G = digraph(),
      V = vertex()

name:add_vertex/3
def:add_vertex(G, V, Label) -> vertex()
types:
      G = digraph(),
      V = vertex(),
      Label = label()

name:check_type/4
def:check_type([d_type()], d_protection(), [{'cyclic', boolean()}]) ->
%       	{d_protection(), [{'cyclic', boolean()}]}

name:del_edge/2
def:del_edge(G, E) -> 'true'
types:
      G = digraph(),
      E = edge()

name:del_edges/2
def:del_edges(G, Edges) -> 'true'
types:
      G = digraph(),
      Edges = [edge()]

name:del_path/3
def:del_path(G, V1, V2) -> 'true'
types:
      G = digraph(),
      V1 = vertex(),
      V2 = vertex()

name:del_vertex/2
def:del_vertex(G, V) -> 'true'
types:
      G = digraph(),
      V = vertex()

name:del_vertices/2
def:del_vertices(G, Vertices) -> 'true'
types:
      G = digraph(),
      Vertices = [vertex()]

name:delete/1
def:delete(G) -> 'true'
types:
      G = digraph()

name:do_add_edge/5
def:do_add_edge({edge(), vertex(), vertex(), label()}, digraph()) ->
	edge() | {'error', add_edge_err_rsn()}

name:do_add_vertex/3
def:do_add_vertex({vertex(), label()}, digraph()) -> vertex()

name:do_insert_edge/5
def:do_insert_edge(edge(), vertex(), vertex(), label(), digraph()) -> edge()

name:edge/2
def:edge(G, E) -> {E, V1, V2, Label} | 'false'
types:
      G = digraph(),
      E = edge(),
      V1 = vertex(),
      V2 = vertex(),
      Label = label()

name:edges/1
def:edges(G) -> Edges
types:
      G = digraph(),
      Edges = [edge()]

name:edges/2
def:edges(G, V) -> Edges
types:
      G = digraph(),
      V = vertex(),
      Edges = [edge()]

name:get_cycle/2
def:get_cycle(G, V) -> Vertices | 'false'
types:
      G = digraph(),
      V = vertex(),
      Vertices = [vertex(),...]

name:get_path/3
def:get_path(G, V1, V2) -> Vertices | 'false'
types:
      G = digraph(),
      V1 = vertex(),
      V2 = vertex(),
      Vertices = [vertex(),...]

name:get_short_cycle/2
def:get_short_cycle(G, V) -> Vertices | 'false'
types:
      G = digraph(),
      V = vertex(),
      Vertices = [vertex(),...]

name:get_short_path/3
def:get_short_path(G, V1, V2) -> Vertices | 'false'
types:
      G = digraph(),
      V1 = vertex(),
      V2 = vertex(),
      Vertices = [vertex(),...]

name:in_degree/2
def:in_degree(G, V) -> non_neg_integer()
types:
      G = digraph(),
      V = vertex()

name:in_edges/2
def:in_edges(G, V) -> Edges
types:
      G = digraph(),
      V = vertex(),
      Edges = [edge()]

name:in_neighbours/2
def:in_neighbours(G, V) -> Vertex
types:
      G = digraph(),
      V = vertex(),
      Vertex = [vertex()]

name:info/1
def:info(G) -> InfoList
types:
      G = digraph(),
      InfoList = [{'cyclicity', Cyclicity = d_cyclicity()} |
                   {'memory', NoWords = non_neg_integer()} |
                   {'protection', Protection = d_protection()}]

name:new/0
def:new() -> digraph()

name:new/1
def:new(Type) -> digraph()
types:
      Type = [d_type()]

name:new_edge_id/1
def:new_edge_id(digraph()) -> edge()

name:new_vertex_id/1
def:new_vertex_id(digraph()) -> vertex()

name:no_edges/1
def:no_edges(G) -> non_neg_integer()
types:
      G = digraph()

name:no_vertices/1
def:no_vertices(G) -> non_neg_integer()
types:
      G = digraph()

name:out_degree/2
def:out_degree(G, V) -> non_neg_integer()
types:
      G = digraph(),
      V = vertex()

name:out_edges/2
def:out_edges(G, V) -> Edges
types:
      G = digraph(),
      V = vertex(),
      Edges = [edge()]

name:out_neighbours/2
def:out_neighbours(G, V) -> Vertices
types:
      G = digraph(),
      V = vertex(),
      Vertices = [vertex()]

name:rm_edge/3
def:rm_edge(vertex(), vertex(), digraph()) -> 'ok'

name:rm_edges/3
def:rm_edges([vertex(),...], digraph()) -> 'true'

name:set_type/3
def:set_type([{'cyclic', boolean()}], digraph()) -> digraph()

name:sink_vertices/1
def:sink_vertices(digraph()) -> [vertex()]

name:source_vertices/1
def:source_vertices(digraph()) -> [vertex()]

name:vertex/2
def:vertex(G, V) -> {V, Label} | 'false'
types:
      G = digraph(),
      V = vertex(),
      Label = label()

name:vertices/1
def:vertices(G) -> Vertices
types:
      G = digraph(),
      Vertices = [vertex()]

