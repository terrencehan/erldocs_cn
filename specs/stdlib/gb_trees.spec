name:balance/1
def:balance(Tree1) -> Tree2
types:
      Tree1 = gb_tree(),
      Tree2 = gb_tree()

name:delete/2
def:delete(Key, Tree1) -> Tree2
types:
      Key = term(),
      Tree1 = gb_tree(),
      Tree2 = gb_tree()

name:delete_any/2
def:delete_any(Key, Tree1) -> Tree2
types:
      Key = term(),
      Tree1 = gb_tree(),
      Tree2 = gb_tree()

name:empty/0
def:empty() -> gb_tree()

name:enter/3
def:enter(Key, Val, Tree1) -> Tree2
types:
      Key = term(),
      Val = term(),
      Tree1 = gb_tree(),
      Tree2 = gb_tree()

name:from_orddict/1
def:from_orddict(List) -> Tree
types:
      List = [{Key = term(), Val = term()}],
      Tree = gb_tree()

name:get/2
def:get(Key, Tree) -> Val
types:
      Key = term(),
      Tree = gb_tree(),
      Val = term()

name:insert/3
def:insert(Key, Val, Tree1) -> Tree2
types:
      Key = term(),
      Val = term(),
      Tree1 = gb_tree(),
      Tree2 = gb_tree()

name:is_defined/2
def:is_defined(Key, Tree) -> boolean()
types:
      Key = term(),
      Tree = gb_tree()

name:is_empty/1
def:is_empty(Tree) -> boolean()
types:
      Tree = gb_tree()

name:iterator/1
def:iterator(Tree) -> Iter
types:
      Tree = gb_tree(),
      Iter = iter()

name:keys/1
def:keys(Tree) -> [Key]
types:
      Tree = gb_tree(),
      Key = term()

name:largest/1
def:largest(Tree) -> {Key, Val}
types:
      Tree = gb_tree(),
      Key = term(),
      Val = term()

name:lookup/2
def:lookup(Key, Tree) -> 'none' | {'value', Val}
types:
      Key = term(),
      Val = term(),
      Tree = gb_tree()

name:map/2
def:map(Function, Tree1) -> Tree2
types:
      Function = fun((K = term(), V1 = term()) -> V2 = term()),
      Tree1 = gb_tree(),
      Tree2 = gb_tree()

name:next/1
def:next(Iter1) -> 'none' | {Key, Val, Iter2}
types:
      Iter1 = iter(),
      Iter2 = iter(),
      Key = term(),
      Val = term()

name:size/1
def:size(Tree) -> non_neg_integer()
types:
      Tree = gb_tree()

name:smallest/1
def:smallest(Tree) -> {Key, Val}
types:
      Tree = gb_tree(),
      Key = term(),
      Val = term()

name:take_largest/1
def:take_largest(Tree1) -> {Key, Val, Tree2}
types:
      Tree1 = gb_tree(),
      Tree2 = gb_tree(),
      Key = term(),
      Val = term()

name:take_smallest/1
def:take_smallest(Tree1) -> {Key, Val, Tree2}
types:
      Tree1 = gb_tree(),
      Tree2 = gb_tree(),
      Key = term(),
      Val = term()

name:to_list/1
def:to_list(Tree) -> [{Key, Val}]
types:
      Tree = gb_tree(),
      Key = term(),
      Val = term()

name:update/3
def:update(Key, Val, Tree1) -> Tree2
types:
      Key = term(),
      Val = term(),
      Tree1 = gb_tree(),
      Tree2 = gb_tree()

name:values/1
def:values(Tree) -> [Val]
types:
      Tree = gb_tree(),
      Val = term()

