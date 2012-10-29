name:append/3
def:append(Key, Value, Orddict1) -> Orddict2
types:
      Key = term(),
      Value = term(),
      Orddict1 = orddict(),
      Orddict2 = orddict()

name:append_list/3
def:append_list(Key, ValList, Orddict1) -> Orddict2
types:
      Key = term(),
      ValList = [Value = term()],
      Orddict1 = orddict(),
      Orddict2 = orddict()

name:erase/2
def:erase(Key, Orddict1) -> Orddict2
types:
      Key = term(),
      Orddict1 = orddict(),
      Orddict2 = orddict()

name:fetch/2
def:fetch(Key, Orddict) -> Value
types:
      Key = term(),
      Value = term(),
      Orddict = orddict()

name:fetch_keys/1
def:fetch_keys(Orddict) -> Keys
types:
      Orddict = orddict(),
      Keys = [term()]

name:filter/2
def:filter(Pred, Orddict1) -> Orddict2
types:
      Pred = fun((Key = term(), Value = term()) -> boolean()),
      Orddict1 = orddict(),
      Orddict2 = orddict()

name:find/2
def:find(Key, Orddict) -> {'ok', Value} | 'error'
types:
      Key = term(),
      Orddict = orddict(),
      Value = term()

name:fold/3
def:fold(Fun, Acc0, Orddict) -> Acc1
types:
      Fun = fun((Key = term(), Value = term(), AccIn = term()) -> AccOut = term()),
      Acc0 = term(),
      Acc1 = term(),
      Orddict = orddict()

name:from_list/1
def:from_list(List) -> Orddict
types:
      List = [{Key = term(), Value = term()}],
      Orddict = orddict()

name:is_key/2
def:is_key(Key, Orddict) -> boolean()
types:
      Key = term(),
      Orddict = orddict()

name:map/2
def:map(Fun, Orddict1) -> Orddict2
types:
      Fun = fun((Key = term(), Value1 = term()) -> Value2 = term()),
      Orddict1 = orddict(),
      Orddict2 = orddict()

name:merge/3
def:merge(Fun, Orddict1, Orddict2) -> Orddict3
types:
      Fun = fun((Key = term(), Value1 = term(), Value2 = term()) -> Value = term()),
      Orddict1 = orddict(),
      Orddict2 = orddict(),
      Orddict3 = orddict()

name:new/0
def:new() -> orddict()

name:size/1
def:size(Orddict) -> non_neg_integer()
types:
      Orddict = orddict()

name:store/3
def:store(Key, Value, Orddict1) -> Orddict2
types:
      Key = term(),
      Value = term(),
      Orddict1 = orddict(),
      Orddict2 = orddict()

name:to_list/1
def:to_list(Orddict) -> List
types:
      Orddict = orddict(),
      List = [{Key = term(), Value = term()}]

name:update/3
def:update(Key, Fun, Orddict1) -> Orddict2
types:
      Key = term(),
      Fun = fun((Value1 = term()) -> Value2 = term()),
      Orddict1 = orddict(),
      Orddict2 = orddict()

name:update/4
def:update(Key, Fun, Initial, Orddict1) -> Orddict2
types:
      Key = term(),
      Initial = term(),
      Fun = fun((Value1 = term()) -> Value2 = term()),
      Orddict1 = orddict(),
      Orddict2 = orddict()

name:update_counter/3
def:update_counter(Key, Increment, Orddict1) -> Orddict2
types:
      Key = term(),
      Increment = number(),
      Orddict1 = orddict(),
      Orddict2 = orddict()

