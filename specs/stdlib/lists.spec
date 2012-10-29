name:all/2
def:all(Pred, List) -> boolean()
types:
      Pred = fun((Elem = T) -> boolean()),
      List = [T],
      T = term()

name:any/2
def:any(Pred, List) -> boolean()
types:
      Pred = fun((Elem = T) -> boolean()),
      List = [T],
      T = term()

name:append/2
def:append(List1, List2) -> List3
types:
      List1 = [T],
      List2 = [T],
      List3 = [T],
      T = term()

name:append/1
def:append(ListOfLists) -> List1
types:
      ListOfLists = [List],
      List = [T],
      List1 = [T],
      T = term()

name:concat/1
def:concat(Things) -> string()
types:
      Things = [Thing],
      Thing = atom() | integer() | float() | string()

name:delete/2
def:delete(Elem, List1) -> List2
types:
      Elem = T,
      List1 = [T],
      List2 = [T],
      T = term()

name:dropwhile/2
def:dropwhile(Pred, List1) -> List2
types:
      Pred = fun((Elem = T) -> boolean()),
      List1 = [T],
      List2 = [T],
      T = term()

name:duplicate/2
def:duplicate(N, Elem) -> List
types:
      N = non_neg_integer(),
      Elem = T,
      List = [T],
      T = term()

name:filter/2
def:filter(Pred, List1) -> List2
types:
      Pred = fun((Elem = T) -> boolean()),
      List1 = [T],
      List2 = [T],
      T = term()

name:flatlength/1
def:flatlength(DeepList) -> non_neg_integer()
types:
      DeepList = [term() | DeepList]

name:flatmap/2
def:flatmap(Fun, List1) -> List2
types:
      Fun = fun((A) -> [B]),
      List1 = [A],
      List2 = [B],
      A = term(),
      B = term()

name:flatten/1
def:flatten(DeepList) -> List
types:
      DeepList = [term() | DeepList],
      List = [term()]

name:flatten/2
def:flatten(DeepList, Tail) -> List
types:
      DeepList = [term() | DeepList],
      Tail = [term()],
      List = [term()]

name:foldl/3
def:foldl(Fun, Acc0, List) -> Acc1
types:
      Fun = fun((Elem = T, AccIn) -> AccOut),
      Acc0 = term(),
      Acc1 = term(),
      AccIn = term(),
      AccOut = term(),
      List = [T],
      T = term()

name:foldr/3
def:foldr(Fun, Acc0, List) -> Acc1
types:
      Fun = fun((Elem = T, AccIn) -> AccOut),
      Acc0 = term(),
      Acc1 = term(),
      AccIn = term(),
      AccOut = term(),
      List = [T],
      T = term()

name:foreach/2
def:foreach(Fun, List) -> ok
types:
      Fun = fun((Elem = T) -> term()),
      List = [T],
      T = term()

name:keydelete/3
def:keydelete(Key, N, TupleList1) -> TupleList2
types:
      Key = term(),
      N = pos_integer(),
      TupleList1 = [Tuple],
      TupleList2 = [Tuple],
      Tuple = tuple()

name:keymap/3
def:keymap(Fun, N, TupleList1) -> TupleList2
types:
      Fun = fun((Term1 = term()) -> Term2 = term()),
      N = pos_integer(),
      TupleList1 = [Tuple],
      TupleList2 = [Tuple],
      Tuple = tuple()

name:keymerge/3
def:keymerge(N, TupleList1, TupleList2) -> TupleList3
types:
      N = pos_integer(),
      TupleList1 = [T1],
      TupleList2 = [T2],
      TupleList3 = [(T1 | T2)],
      T1 = Tuple,
      T2 = Tuple,
      Tuple = tuple()

name:keyreplace/4
def:keyreplace(Key, N, TupleList1, NewTuple) -> TupleList2
types:
      Key = term(),
      N = pos_integer(),
      TupleList1 = [Tuple],
      TupleList2 = [Tuple],
      NewTuple = Tuple,
      Tuple = tuple()

name:keysort/2
def:keysort(N, TupleList1) -> TupleList2
types:
      N = pos_integer(),
      TupleList1 = [Tuple],
      TupleList2 = [Tuple],
      Tuple = tuple()

name:keystore/4
def:keystore(Key, N, TupleList1, NewTuple) -> TupleList2
types:
      Key = term(),
      N = pos_integer(),
      TupleList1 = [Tuple],
      TupleList2 = [Tuple, ...],
      NewTuple = Tuple,
      Tuple = tuple()

name:keytake/3
def:keytake(Key, N, TupleList1) -> {value, Tuple, TupleList2} | false
types:
      Key = term(),
      N = pos_integer(),
      TupleList1 = [tuple()],
      TupleList2 = [tuple()],
      Tuple = tuple()

name:last/1
def:last(List) -> Last
types:
      List = [T,...],
      Last = T,
      T = term()

name:map/2
def:map(Fun, List1) -> List2
types:
      Fun = fun((A) -> B),
      List1 = [A],
      List2 = [B],
      A = term(),
      B = term()

name:mapfoldl/3
def:mapfoldl(Fun, Acc0, List1) -> {List2, Acc1}
types:
      Fun = fun((A, AccIn) -> {B, AccOut}),
      Acc0 = term(),
      Acc1 = term(),
      AccIn = term(),
      AccOut = term(),
      List1 = [A],
      List2 = [B],
      A = term(),
      B = term()

name:mapfoldr/3
def:mapfoldr(Fun, Acc0, List1) -> {List2, Acc1}
types:
      Fun = fun((A, AccIn) -> {B, AccOut}),
      Acc0 = term(),
      Acc1 = term(),
      AccIn = term(),
      AccOut = term(),
      List1 = [A],
      List2 = [B],
      A = term(),
      B = term()

name:max/1
def:max(List) -> Max
types:
      List = [T,...],
      Max = T,
      T = term()

name:merge/1
def:merge(ListOfLists) -> List1
types:
      ListOfLists = [List],
      List = [T],
      List1 = [T],
      T = term()

name:merge/2
def:merge(List1, List2) -> List3
types:
      List1 = [X],
      List2 = [Y],
      List3 = [(X | Y)],
      X = term(),
      Y = term()

name:merge/3
def:merge(Fun, List1, List2) -> List3
types:
      Fun = fun((A, B) -> boolean()),
      List1 = [A],
      List2 = [B],
      List3 = [(A | B)],
      A = term(),
      B = term()

name:merge3/3
def:merge3(List1, List2, List3) -> List4
types:
      List1 = [X],
      List2 = [Y],
      List3 = [Z],
      List4 = [(X | Y | Z)],
      X = term(),
      Y = term(),
      Z = term()

name:min/1
def:min(List) -> Min
types:
      List = [T,...],
      Min = T,
      T = term()

name:nth/2
def:nth(N, List) -> Elem
types:
      N = pos_integer(),
      List = [T,...],
      Elem = T,
      T = term()

name:nthtail/2
def:nthtail(N, List) -> Tail
types:
      N = non_neg_integer(),
      List = [T,...],
      Tail = [T],
      T = term()

name:partition/2
def:partition(Pred, List) -> {Satisfying, NotSatisfying}
types:
      Pred = fun((Elem = T) -> boolean()),
      List = [T],
      Satisfying = [T],
      NotSatisfying = [T],
      T = term()

name:prefix/2
def:prefix(List1, List2) -> boolean()
types:
      List1 = [T],
      List2 = [T],
      T = term()

name:reverse/1
def:reverse(List1) -> List2
types:
      List1 = [T],
      List2 = [T],
      T = term()

name:rkeymerge/3
def:rkeymerge(pos_integer(), [X], [Y]) ->
	[R]
types: X = tuple(), Y = tuple(), R = tuple()

name:rmerge/2
def:rmerge([X], [Y]) -> [(X | Y)]

name:rmerge/2
def:rmerge(fun((X, Y) -> boolean()), [X], [Y]) -> [(X | Y)]

name:rmerge3/3
def:rmerge3([X], [Y], [Z]) -> [(X | Y | Z)]

name:rukeymerge/3
def:rukeymerge(pos_integer(), [X], [Y]) ->
	[(X | Y)]
types: X = tuple(), Y = tuple()

name:rumerge/2
def:rumerge(fun((X, Y) -> boolean()), [X], [Y]) -> [(X | Y)]

name:rumerge/2
def:rumerge([X], [Y]) -> [(X | Y)]

name:rumerge3/3
def:rumerge3([X], [Y], [Z]) -> [(X | Y | Z)]

name:seq/2
def:seq(From, To) -> Seq
types:
      From = integer(),
      To = integer(),
      Seq = [integer()]

name:seq/3
def:seq(From, To, Incr) -> Seq
types:
      From = integer(),
      To = integer(),
      Incr = integer(),
      Seq = [integer()]

name:sort/1
def:sort(List1) -> List2
types:
      List1 = [T],
      List2 = [T],
      T = term()

name:sort/2
def:sort(Fun, List1) -> List2
types:
      Fun = fun((A = T, B = T) -> boolean()),
      List1 = [T],
      List2 = [T],
      T = term()

name:split/2
def:split(N, List1) -> {List2, List3}
types:
      N = non_neg_integer(),
      List1 = [T],
      List2 = [T],
      List3 = [T],
      T = term()

name:splitwith/2
def:splitwith(Pred, List) -> {List1, List2}
types:
      Pred = fun((T) -> boolean()),
      List = [T],
      List1 = [T],
      List2 = [T],
      T = term()

name:sublist/3
def:sublist(List1, Start, Len) -> List2
types:
      List1 = [T],
      List2 = [T],
      Start = pos_integer(),
      Len = non_neg_integer(),
      T = term()

name:sublist/2
def:sublist(List1, Len) -> List2
types:
      List1 = [T],
      List2 = [T],
      Len = non_neg_integer(),
      T = term()

name:subtract/2
def:subtract(List1, List2) -> List3
types:
      List1 = [T],
      List2 = [T],
      List3 = [T],
      T = term()

name:suffix/2
def:suffix(List1, List2) -> boolean()
types:
      List1 = [T],
      List2 = [T],
      T = term()

name:sum/1
def:sum(List) -> number()
types:
      List = [number()]

name:takewhile/2
def:takewhile(Pred, List1) -> List2
types:
      Pred = fun((Elem = T) -> boolean()),
      List1 = [T],
      List2 = [T],
      T = term()

name:ukeymerge/3
def:ukeymerge(N, TupleList1, TupleList2) -> TupleList3
types:
      N = pos_integer(),
      TupleList1 = [T1],
      TupleList2 = [T2],
      TupleList3 = [(T1 | T2)],
      T1 = Tuple,
      T2 = Tuple,
      Tuple = tuple()

name:ukeysort/2
def:ukeysort(N, TupleList1) -> TupleList2
types:
      N = pos_integer(),
      TupleList1 = [Tuple],
      TupleList2 = [Tuple],
      Tuple = tuple()

name:umerge/3
def:umerge(Fun, List1, List2) -> List3
types:
      Fun = fun((A, B) -> boolean()),
      List1 = [A],
      List2 = [B],
      List3 = [(A | B)],
      A = term(),
      B = term()

name:umerge/1
def:umerge(ListOfLists) -> List1
types:
      ListOfLists = [List],
      List = [T],
      List1 = [T],
      T = term()

name:umerge/2
def:umerge(List1, List2) -> List3
types:
      List1 = [X],
      List2 = [Y],
      List3 = [(X | Y)],
      X = term(),
      Y = term()

name:umerge3/3
def:umerge3(List1, List2, List3) -> List4
types:
      List1 = [X],
      List2 = [Y],
      List3 = [Z],
      List4 = [(X | Y | Z)],
      X = term(),
      Y = term(),
      Z = term()

name:unzip/1
def:unzip(List1) -> {List2, List3}
types:
      List1 = [{A, B}],
      List2 = [A],
      List3 = [B],
      A = term(),
      B = term()

name:unzip3/1
def:unzip3(List1) -> {List2, List3, List4}
types:
      List1 = [{A, B, C}],
      List2 = [A],
      List3 = [B],
      List4 = [C],
      A = term(),
      B = term(),
      C = term()

name:usort/2
def:usort(Fun, List1) -> List2
types:
      Fun = fun((T, T) -> boolean()),
      List1 = [T],
      List2 = [T],
      T = term()

name:usort/1
def:usort(List1) -> List2
types:
      List1 = [T],
      List2 = [T],
      T = term()

name:zf/1
def:zf(fun((T) -> boolean() | {'true', X}), [T]) -> [(T | X)]

name:zip/2
def:zip(List1, List2) -> List3
types:
      List1 = [A],
      List2 = [B],
      List3 = [{A, B}],
      A = term(),
      B = term()

name:zip3/3
def:zip3(List1, List2, List3) -> List4
types:
      List1 = [A],
      List2 = [B],
      List3 = [C],
      List4 = [{A, B, C}],
      A = term(),
      B = term(),
      C = term()

name:zipwith/3
def:zipwith(Combine, List1, List2) -> List3
types:
      Combine = fun((X, Y) -> T),
      List1 = [X],
      List2 = [Y],
      List3 = [T],
      X = term(),
      Y = term(),
      T = term()

name:zipwith3/4
def:zipwith3(Combine, List1, List2, List3) -> List4
types:
      Combine = fun((X, Y, Z) -> T),
      List1 = [X],
      List2 = [Y],
      List3 = [Z],
      List4 = [T],
      X = term(),
      Y = term(),
      Z = term(),
      T = term()

