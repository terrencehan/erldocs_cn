name:add/2
def:add(Element, Set1) -> Set2
types:
      Element = term(),
      Set1 = gb_set(),
      Set2 = gb_set()

name:add_element/2
def:add_element(Element, Set1) -> Set2
types:
      Element = term(),
      Set1 = gb_set(),
      Set2 = gb_set()

name:balance/1
def:balance(Set1) -> Set2
types:
      Set1 = gb_set(),
      Set2 = gb_set()

name:del_element/2
def:del_element(Element, Set1) -> Set2
types:
      Element = term(),
      Set1 = gb_set(),
      Set2 = gb_set()

name:delete/2
def:delete(Element, Set1) -> Set2
types:
      Element = term(),
      Set1 = gb_set(),
      Set2 = gb_set()

name:delete_any/2
def:delete_any(Element, Set1) -> Set2
types:
      Element = term(),
      Set1 = gb_set(),
      Set2 = gb_set()

name:difference/2
def:difference(Set1, Set2) -> Set3
types:
      Set1 = gb_set(),
      Set2 = gb_set(),
      Set3 = gb_set()

name:empty/0
def:empty() -> Set
types:
      Set = gb_set()

name:filter/2
def:filter(Pred, Set1) -> Set2
types:
      Pred = fun((E = term()) -> boolean()),
      Set1 = gb_set(),
      Set2 = gb_set()

name:fold/3
def:fold(Function, Acc0, Set) -> Acc1
types:
      Function = fun((E = term(), AccIn) -> AccOut),
      Acc0 = term(),
      Acc1 = term(),
      AccIn = term(),
      AccOut = term(),
      Set = gb_set()

name:from_list/1
def:from_list(List) -> Set
types:
      List = [term()],
      Set = gb_set()

name:from_ordset/1
def:from_ordset(List) -> Set
types:
      List = [term()],
      Set = gb_set()

name:insert/2
def:insert(Element, Set1) -> Set2
types:
      Element = term(),
      Set1 = gb_set(),
      Set2 = gb_set()

name:intersection/2
def:intersection(Set1, Set2) -> Set3
types:
      Set1 = gb_set(),
      Set2 = gb_set(),
      Set3 = gb_set()

name:intersection/1
def:intersection(SetList) -> Set
types:
      SetList = [gb_set(),...],
      Set = gb_set()

name:is_disjoint/2
def:is_disjoint(Set1, Set2) -> boolean()
types:
      Set1 = gb_set(),
      Set2 = gb_set()

name:is_element/2
def:is_element(Element, Set) -> boolean()
types:
      Element = term(),
      Set = gb_set()

name:is_empty/1
def:is_empty(Set) -> boolean()
types:
      Set = gb_set()

name:is_member/2
def:is_member(Element, Set) -> boolean()
types:
      Element = term(),
      Set = gb_set()

name:is_set/1
def:is_set(Term) -> boolean()
types:
      Term = term()

name:is_subset/2
def:is_subset(Set1, Set2) -> boolean()
types:
      Set1 = gb_set(),
      Set2 = gb_set()

name:iterator/1
def:iterator(Set) -> Iter
types:
      Set = gb_set(),
      Iter = iter()

name:largest/1
def:largest(Set) -> term()
types:
      Set = gb_set()

name:mk_set/2
def:mk_set(non_neg_integer(), gb_set_node()) -> gb_set()

name:new/0
def:new() -> Set
types:
      Set = gb_set()

name:next/1
def:next(Iter1) -> {Element, Iter2} | 'none'
types:
      Iter1 = iter(),
      Iter2 = iter(),
      Element = term()

name:singleton/1
def:singleton(Element) -> gb_set()
types:
      Element = term()

name:size/1
def:size(Set) -> non_neg_integer()
types:
      Set = gb_set()

name:smallest/1
def:smallest(Set) -> term()
types:
      Set = gb_set()

name:subtract/2
def:subtract(Set1, Set2) -> Set3
types:
      Set1 = gb_set(),
      Set2 = gb_set(),
      Set3 = gb_set()

name:take_largest/1
def:take_largest(Set1) -> {Element, Set2}
types:
      Set1 = gb_set(),
      Set2 = gb_set(),
      Element = term()

name:take_smallest/1
def:take_smallest(Set1) -> {Element, Set2}
types:
      Set1 = gb_set(),
      Set2 = gb_set(),
      Element = term()

name:to_list/1
def:to_list(Set) -> List
types:
      Set = gb_set(),
      List = [term()]

name:union/2
def:union(Set1, Set2) -> Set3
types:
      Set1 = gb_set(),
      Set2 = gb_set(),
      Set3 = gb_set()

name:union/1
def:union(SetList) -> Set
types:
      SetList = [gb_set(),...],
      Set = gb_set()

