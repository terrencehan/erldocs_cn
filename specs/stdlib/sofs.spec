name:a_function/1
def:a_function(Tuples) -> Function
types:
      Function = a_function(),
      Tuples = [tuple()])

name:a_function/2
def:a_function(Tuples, Type) -> Function
types:
      Function = a_function(),
      Tuples = [tuple()],
      Type = type()

name:canonical_relation/1
def:canonical_relation(SetOfSets) -> BinRel
types:
      BinRel = binary_relation(),
      SetOfSets = set_of_sets()

name:composite/2
def:composite(Function1, Function2) -> Function3
types:
      Function1 = a_function(),
      Function2 = a_function(),
      Function3 = a_function()

name:constant_function/2
def:constant_function(Set, AnySet) -> Function
types:
      AnySet = anyset(),
      Function = a_function(),
      Set = a_set()

name:converse/1
def:converse(BinRel1) -> BinRel2
types:
      BinRel1 = binary_relation(),
      BinRel2 = binary_relation()

name:difference/2
def:difference(Set1, Set2) -> Set3
types:
      Set1 = a_set(),
      Set2 = a_set(),
      Set3 = a_set()

name:digraph_to_family/1
def:digraph_to_family(Graph) -> Family
types:
      Graph = digraph(),
      Family = family()

name:digraph_to_family/2
def:digraph_to_family(Graph, Type) -> Family
types:
      Graph = digraph(),
      Family = family(),
      Type = type()

name:domain/1
def:domain(BinRel) -> Set
types:
      BinRel = binary_relation(),
      Set = a_set()

name:drestriction/2
def:drestriction(BinRel1, Set) -> BinRel2
types:
      BinRel1 = binary_relation(),
      BinRel2 = binary_relation(),
      Set = a_set()

name:drestriction/3
def:drestriction(SetFun, Set1, Set2) -> Set3
types:
      SetFun = set_fun(),
      Set1 = a_set(),
      Set2 = a_set(),
      Set3 = a_set()

name:empty_set/0
def:empty_set() -> Set
types:
      Set = a_set()

name:extension/3
def:extension(BinRel1, Set, AnySet) -> BinRel2
types:
      AnySet = anyset(),
      BinRel1 = binary_relation(),
      BinRel2 = binary_relation(),
      Set = a_set()

name:fam2rel/1
def:fam2rel(Family) -> BinRel
types:
      Family = family(),
      BinRel = binary_relation()

name:family/1
def:family(Tuples) -> Family
types:
      Family = family(),
      Tuples = [tuple()])

name:family/2
def:family(Tuples, Type) -> Family
types:
      Family = family(),
      Tuples = [tuple()],
      Type = type()

name:family_difference/2
def:family_difference(Family1, Family2) -> Family3
types:
      Family1 = family(),
      Family2 = family(),
      Family3 = family()

name:family_domain/1
def:family_domain(Family1) -> Family2
types:
      Family1 = family(),
      Family2 = family()

name:family_field/1
def:family_field(Family1) -> Family2
types:
      Family1 = family(),
      Family2 = family()

name:family_intersection/1
def:family_intersection(Family1) -> Family2
types:
      Family1 = family(),
      Family2 = family()

name:family_intersection/2
def:family_intersection(Family1, Family2) -> Family3
types:
      Family1 = family(),
      Family2 = family(),
      Family3 = family()

name:family_projection/2
def:family_projection(SetFun, Family1) -> Family2
types:
      SetFun = set_fun(),
      Family1 = family(),
      Family2 = family()

name:family_range/1
def:family_range(Family1) -> Family2
types:
      Family1 = family(),
      Family2 = family()

name:family_specification/2
def:family_specification(Fun, Family1) -> Family2
types:
      Fun = spec_fun(),
      Family1 = family(),
      Family2 = family()

name:family_to_digraph/1
def:family_to_digraph(Family) -> Graph
types:
      Graph = digraph(),
      Family = family()

name:family_to_digraph/2
def:family_to_digraph(Family, GraphType) -> Graph
types:
      Graph = digraph(),
      Family = family(),
      GraphType = [digraph:d_type()])

name:family_to_relation/1
def:family_to_relation(Family) -> BinRel
types:
      Family = family(),
      BinRel = binary_relation()

name:family_union/1
def:family_union(Family1) -> Family2
types:
      Family1 = family(),
      Family2 = family()

name:family_union/2
def:family_union(Family1, Family2) -> Family3
types:
      Family1 = family(),
      Family2 = family(),
      Family3 = family()

name:field/1
def:field(BinRel) -> Set
types:
      BinRel = binary_relation(),
      Set = a_set()

name:from_external/2
def:from_external(ExternalSet, Type) -> AnySet
types:
      ExternalSet = external_set(),
      AnySet = anyset(),
      Type = type()

name:from_sets/1
def:from_sets(ListOfSets) -> Set
types:
      Set = a_set(),
      ListOfSets = [anyset()];
               (TupleOfSets) -> Ordset when
      Ordset = ordset(),
      TupleOfSets = tuple_of(anyset())

name:from_term/1
def:from_term(Term) -> AnySet
types:
      AnySet = anyset(),
      Term = term()

name:from_term/2
def:from_term(Term, Type) -> AnySet
types:
      AnySet = anyset(),
      Term = term(),
      Type = type()

name:image/2
def:image(BinRel, Set1) -> Set2
types:
      BinRel = binary_relation(),
      Set1 = a_set(),
      Set2 = a_set()

name:intersection/2
def:intersection(Set1, Set2) -> Set3
types:
      Set1 = a_set(),
      Set2 = a_set(),
      Set3 = a_set()

name:intersection/1
def:intersection(SetOfSets) -> Set
types:
      Set = a_set(),
      SetOfSets = set_of_sets()

name:intersection_of_family/1
def:intersection_of_family(Family) -> Set
types:
      Family = family(),
      Set = a_set()

name:inverse/1
def:inverse(Function1) -> Function2
types:
      Function1 = a_function(),
      Function2 = a_function()

name:inverse_image/2
def:inverse_image(BinRel, Set1) -> Set2
types:
      BinRel = binary_relation(),
      Set1 = a_set(),
      Set2 = a_set()

name:is_a_function/1
def:is_a_function(BinRel) -> Bool
types:
      Bool = boolean(),
      BinRel = binary_relation()

name:is_disjoint/2
def:is_disjoint(Set1, Set2) -> Bool
types:
      Bool = boolean(),
      Set1 = a_set(),
      Set2 = a_set()

name:is_empty_set/1
def:is_empty_set(AnySet) -> Bool
types:
      AnySet = anyset(),
      Bool = boolean()

name:is_equal/2
def:is_equal(AnySet1, AnySet2) -> Bool
types:
      AnySet1 = anyset(),
      AnySet2 = anyset(),
      Bool = boolean()

name:is_set/1
def:is_set(AnySet) -> Bool
types:
      AnySet = anyset(),
      Bool = boolean()

name:is_sofs_set/1
def:is_sofs_set(Term) -> Bool
types:
      Bool = boolean(),
      Term = term()

name:is_subset/2
def:is_subset(Set1, Set2) -> Bool
types:
      Bool = boolean(),
      Set1 = a_set(),
      Set2 = a_set()

name:is_type/1
def:is_type(Term) -> Bool
types:
      Bool = boolean(),
      Term = term()

name:join/4
def:join(Relation1, I, Relation2, J) -> Relation3
types:
      Relation1 = relation(),
      Relation2 = relation(),
      Relation3 = relation(),
      I = pos_integer(),
      J = pos_integer()

name:multiple_relative_product/2
def:multiple_relative_product(TupleOfBinRels, BinRel1) -> BinRel2
types:
      TupleOfBinRels = tuple_of(BinRel),
      BinRel = binary_relation(),
      BinRel1 = binary_relation(),
      BinRel2 = binary_relation()

name:no_elements/1
def:no_elements(ASet) -> NoElements
types:
      ASet = a_set() | ordset(),
      NoElements = non_neg_integer()

name:partition/1
def:partition(SetOfSets) -> Partition
types:
      SetOfSets = set_of_sets(),
      Partition = a_set()

name:partition/2
def:partition(SetFun, Set) -> Partition
types:
      SetFun = set_fun(),
      Partition = a_set(),
      Set = a_set()

name:partition/3
def:partition(SetFun, Set1, Set2) -> {Set3, Set4}
types:
      SetFun = set_fun(),
      Set1 = a_set(),
      Set2 = a_set(),
      Set3 = a_set(),
      Set4 = a_set()

name:partition_family/2
def:partition_family(SetFun, Set) -> Family
types:
      Family = family(),
      SetFun = set_fun(),
      Set = a_set()

name:product/2
def:product(Set1, Set2) -> BinRel
types:
      BinRel = binary_relation(),
      Set1 = a_set(),
      Set2 = a_set()

name:product/1
def:product(TupleOfSets) -> Relation
types:
      Relation = relation(),
      TupleOfSets = tuple_of(a_set())

name:projection/2
def:projection(SetFun, Set1) -> Set2
types:
      SetFun = set_fun(),
      Set1 = a_set(),
      Set2 = a_set()

name:range/1
def:range(BinRel) -> Set
types:
      BinRel = binary_relation(),
      Set = a_set()

name:relation/1
def:relation(Tuples) -> Relation
types:
      Relation = relation(),
      Tuples = [tuple()])

name:relation/2
def:relation(Tuples, Type) -> Relation
types:
      N = integer(),
      Type = N | type(),
      Relation = relation(),
      Tuples = [tuple()])

name:relation_to_family/1
def:relation_to_family(BinRel) -> Family
types:
      Family = family(),
      BinRel = binary_relation()

name:relative_product/1
def:relative_product(ListOfBinRels) -> BinRel2
types:
      ListOfBinRels = [BinRel, ...],
      BinRel = binary_relation(),
      BinRel2 = binary_relation()

name:relative_product/2
def:relative_product(ListOfBinRels, BinRel1) -> BinRel2
types:
      ListOfBinRels = [BinRel, ...],
      BinRel = binary_relation(),
      BinRel1 = binary_relation(),
      BinRel2 = binary_relation();
                      (BinRel1, BinRel2) -> BinRel3 when
      BinRel1 = binary_relation(),
      BinRel2 = binary_relation(),
      BinRel3 = binary_relation()

name:relative_product1/2
def:relative_product1(BinRel1, BinRel2) -> BinRel3
types:
      BinRel1 = binary_relation(),
      BinRel2 = binary_relation(),
      BinRel3 = binary_relation()

name:restriction/2
def:restriction(BinRel1, Set) -> BinRel2
types:
      BinRel1 = binary_relation(),
      BinRel2 = binary_relation(),
      Set = a_set()

name:restriction/3
def:restriction(SetFun, Set1, Set2) -> Set3
types:
      SetFun = set_fun(),
      Set1 = a_set(),
      Set2 = a_set(),
      Set3 = a_set()

name:set/1
def:set(Terms) -> Set
types:
      Set = a_set(),
      Terms = [term()])

name:set/2
def:set(Terms, Type) -> Set
types:
      Set = a_set(),
      Terms = [term()],
      Type = type()

name:specification/2
def:specification(Fun, Set1) -> Set2
types:
      Fun = spec_fun(),
      Set1 = a_set(),
      Set2 = a_set()

name:strict_relation/1
def:strict_relation(BinRel1) -> BinRel2
types:
      BinRel1 = binary_relation(),
      BinRel2 = binary_relation()

name:substitution/2
def:substitution(SetFun, Set1) -> Set2
types:
      SetFun = set_fun(),
      Set1 = a_set(),
      Set2 = a_set()

name:symdiff/2
def:symdiff(Set1, Set2) -> Set3
types:
      Set1 = a_set(),
      Set2 = a_set(),
      Set3 = a_set()

name:symmetric_partition/2
def:symmetric_partition(Set1, Set2) -> {Set3, Set4, Set5}
types:
      Set1 = a_set(),
      Set2 = a_set(),
      Set3 = a_set(),
      Set4 = a_set(),
      Set5 = a_set()

name:to_external/1
def:to_external(AnySet) -> ExternalSet
types:
      ExternalSet = external_set(),
      AnySet = anyset()

name:to_sets/1
def:to_sets(ASet) -> Sets
types:
      ASet = a_set() | ordset(),
      Sets = tuple_of(AnySet) | [AnySet],
      AnySet = anyset()

name:type/1
def:type(AnySet) -> Type
types:
      AnySet = anyset(),
      Type = type()

name:union/2
def:union(Set1, Set2) -> Set3
types:
      Set1 = a_set(),
      Set2 = a_set(),
      Set3 = a_set()

name:union/1
def:union(SetOfSets) -> Set
types:
      Set = a_set(),
      SetOfSets = set_of_sets()

name:union_of_family/1
def:union_of_family(Family) -> Set
types:
      Family = family(),
      Set = a_set()

name:weak_relation/1
def:weak_relation(BinRel1) -> BinRel2
types:
      BinRel1 = binary_relation(),
      BinRel2 = binary_relation()

