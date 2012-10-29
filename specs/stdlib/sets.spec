name:add_bkt_el/3
def:add_bkt_el(T, [T], [T]) -> {[T], 0 | 1}

name:add_element/2
def:add_element(Element, Set1) -> Set2
types:
      Element = term(),
      Set1 = set(),
      Set2 = set()

name:contract_segs/1
def:contract_segs(segs()) -> segs()

name:del_bkt_el/2
def:del_bkt_el(T, [T]) -> {[T], 0 | 1}

name:del_element/2
def:del_element(Element, Set1) -> Set2
types:
      Element = term(),
      Set1 = set(),
      Set2 = set()

name:expand_segs/2
def:expand_segs(segs(), seg()) -> segs()

name:filter/2
def:filter(Pred, Set1) -> Set2
types:
      Pred = fun((E = term()) -> boolean()),
      Set1 = set(),
      Set2 = set()

name:fold/3
def:fold(Function, Acc0, Set) -> Acc1
types:
      Function = fun((E = term(),AccIn) -> AccOut),
      Set = set(),
      Acc0 = T,
      Acc1 = T,
      AccIn = T,
      AccOut = T

name:from_list/1
def:from_list(List) -> Set
types:
      List = [term()],
      Set = set()

name:get_bucket/2
def:get_bucket(set(), non_neg_integer()) -> term()

name:get_slot/2
def:get_slot(set(), term()) -> non_neg_integer()

name:intersection/2
def:intersection(Set1, Set2) -> Set3
types:
      Set1 = set(),
      Set2 = set(),
      Set3 = set()

name:intersection/1
def:intersection(SetList) -> Set
types:
      SetList = [set(),...],
      Set = set()

name:intersection1/2
def:intersection1(set(), [set()]) -> set()

name:is_disjoint/2
def:is_disjoint(Set1, Set2) -> boolean()
types:
      Set1 = set(),
      Set2 = set()

name:is_element/2
def:is_element(Element, Set) -> boolean()
types:
      Element = term(),
      Set = set()

name:is_set/1
def:is_set(Set) -> boolean()
types:
      Set = term()

name:is_subset/2
def:is_subset(Set1, Set2) -> boolean()
types:
      Set1 = set(),
      Set2 = set()

name:maybe_contract/2
def:maybe_contract(set(), non_neg_integer()) -> set()

name:maybe_contract_segs/1
def:maybe_contract_segs(set()) -> set()

name:maybe_expand/2
def:maybe_expand(set(), 0 | 1) -> set()

name:maybe_expand_segs/1
def:maybe_expand_segs(set()) -> set()

name:mk_seg/1
def:mk_seg(16) -> seg()

name:new/0
def:new() -> set()

name:on_bucket/1
def:on_bucket(fun((_) -> {[_], 0 | 1}), set(), non_neg_integer()) ->
	  {set(), 0 | 1}

name:rehash/4
def:rehash([T], integer(), pos_integer(), pos_integer()) -> {[T],[T]}

name:size/1
def:size(Set) -> non_neg_integer()
types:
      Set = set()

name:subtract/2
def:subtract(Set1, Set2) -> Set3
types:
      Set1 = set(),
      Set2 = set(),
      Set3 = set()

name:to_list/1
def:to_list(Set) -> List
types:
      Set = set(),
      List = [term()]

name:union/2
def:union(Set1, Set2) -> Set3
types:
      Set1 = set(),
      Set2 = set(),
      Set3 = set()

name:union/1
def:union(SetList) -> Set
types:
      SetList = [set()],
      Set = set()

name:union1/2
def:union1(set(), [set()]) -> set()

