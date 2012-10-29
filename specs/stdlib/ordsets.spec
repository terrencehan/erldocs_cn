name:add_element/2
def:add_element(Element, Ordset1) -> Ordset2
types:
      Element = E,
      Ordset1 = ordset(T),
      Ordset2 = ordset(T | E)

name:add_element/2
def:add_element(E, ordset(T)) -> [T | E,...]

name:del_element/2
def:del_element(Element, Ordset1) -> Ordset2
types:
      Element = term(),
      Ordset1 = ordset(T),
      Ordset2 = ordset(T)

name:filter/2
def:filter(Pred, Ordset1) -> Ordset2
types:
      Pred = fun((Element = T) -> boolean()),
      Ordset1 = ordset(T),
      Ordset2 = ordset(T)

name:fold/3
def:fold(Function, Acc0, Ordset) -> Acc1
types:
      Function = fun((Element = T, AccIn = term()) -> AccOut = term()),
      Ordset = ordset(T),
      Acc0 = term(),
      Acc1 = term()

name:from_list/1
def:from_list(List) -> Ordset
types:
      List = [T],
      Ordset = ordset(T)

name:intersection/2
def:intersection(Ordset1, Ordset2) -> Ordset3
types:
      Ordset1 = ordset(_),
      Ordset2 = ordset(_),
      Ordset3 = ordset(_)

name:intersection/1
def:intersection(OrdsetList) -> Ordset
types:
      OrdsetList = [ordset(_),...],
      Ordset = ordset(_)

name:is_disjoint/2
def:is_disjoint(Ordset1, Ordset2) -> boolean()
types:
      Ordset1 = ordset(_),
      Ordset2 = ordset(_)

name:is_element/2
def:is_element(Element, Ordset) -> boolean()
types:
      Element = term(),
      Ordset = ordset(_)

name:is_set/1
def:is_set(Ordset) -> boolean()
types:
      Ordset = term()

name:is_subset/2
def:is_subset(Ordset1, Ordset2) -> boolean()
types:
      Ordset1 = ordset(_),
      Ordset2 = ordset(_)

name:new/0
def:new() -> []

name:size/1
def:size(Ordset) -> non_neg_integer()
types:
      Ordset = ordset(_)

name:subtract/2
def:subtract(Ordset1, Ordset2) -> Ordset3
types:
      Ordset1 = ordset(_),
      Ordset2 = ordset(_),
      Ordset3 = ordset(_)

name:to_list/1
def:to_list(Ordset) -> List
types:
      Ordset = ordset(T),
      List = [T]

name:union/2
def:union(Ordset1, Ordset2) -> Ordset3
types:
      Ordset1 = ordset(T1),
      Ordset2 = ordset(T2),
      Ordset3 = ordset(T1 | T2)

name:union/1
def:union(OrdsetList) -> Ordset
types:
      OrdsetList = [ordset(T)],
      Ordset = ordset(T)

