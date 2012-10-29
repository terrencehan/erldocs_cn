name:append/3
def:append(Key, Value, Dict1) -> Dict2
types:
      Key = term(),
      Value = term(),
      Dict1 = dict(),
      Dict2 = dict()

name:append_list/3
def:append_list(Key, ValList, Dict1) -> Dict2
types:
      Key = term(),
      ValList = [Value = term()],
      Dict1 = dict(),
      Dict2 = dict()

name:erase/2
def:erase(Key, Dict1) -> Dict2
types:
      Key = term(),
      Dict1 = dict(),
      Dict2 = dict()

name:fetch/2
def:fetch(Key, Dict) -> Value
types:
      Key = term(),
      Dict = dict(),
      Value = term()

name:fetch_keys/1
def:fetch_keys(Dict) -> Keys
types:
      Dict = dict(),
      Keys = [term()]

name:filter/2
def:filter(Pred, Dict1) -> Dict2
types:
      Pred = fun((Key = term(), Value = term()) -> boolean()),
      Dict1 = dict(),
      Dict2 = dict()

name:find/2
def:find(Key, Dict) -> {'ok', Value} | 'error'
types:
      Key = term(),
      Dict = dict(),
      Value = term()

name:fold/3
def:fold(Fun, Acc0, Dict) -> Acc1
types:
      Fun = fun((Key, Value, AccIn) -> AccOut),
      Key = term(),
      Value = term(),
      Acc0 = term(),
      Acc1 = term(),
      AccIn = term(),
      AccOut = term(),
      Dict = dict()

name:from_list/1
def:from_list(List) -> Dict
types:
      List = [{Key = term(), Value = term()}],
      Dict = dict()

name:is_key/2
def:is_key(Key, Dict) -> boolean()
types:
      Key = term(),
      Dict = dict()

name:map/2
def:map(Fun, Dict1) -> Dict2
types:
      Fun = fun((Key = term(), Value1 = term()) -> Value2 = term()),
      Dict1 = dict(),
      Dict2 = dict()

name:merge/3
def:merge(Fun, Dict1, Dict2) -> Dict3
types:
      Fun = fun((Key = term(), Value1 = term(), Value2 = term()) -> Value = term()),
      Dict1 = dict(),
      Dict2 = dict(),
      Dict3 = dict()

name:new/0
def:new() -> dict()

name:size/1
def:size(Dict) -> non_neg_integer()
types:
      Dict = dict()

name:store/3
def:store(Key, Value, Dict1) -> Dict2
types:
      Key = term(),
      Value = term(),
      Dict1 = dict(),
      Dict2 = dict()

name:to_list/1
def:to_list(Dict) -> List
types:
      Dict = dict(),
      List = [{Key = term(), Value = term()}]

name:update/3
def:update(Key, Fun, Dict1) -> Dict2
types:
      Key = term(),
      Fun = fun((Value1 = term()) -> Value2 = term()),
      Dict1 = dict(),
      Dict2 = dict()

name:update/4
def:update(Key, Fun, Initial, Dict1) -> Dict2
types:
      Key = term(),
      Initial = term(),
      Fun = fun((Value1 = term()) -> Value2 = term()),
      Dict1 = dict(),
      Dict2 = dict()

name:update_counter/3
def:update_counter(Key, Increment, Dict1) -> Dict2
types:
      Key = term(),
      Increment = number(),
      Dict1 = dict(),
      Dict2 = dict()

