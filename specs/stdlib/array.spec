name:default/1
def:default(Array :: array()) -> term()

name:find_max/2
def:find_max(integer(), integer()) -> integer()

name:fix/1
def:fix(Array :: array()) -> array()

name:foldl/3
def:foldl(Function, InitialAcc :: A, Array :: array()) -> B
types:
      Function = fun((Index = array_indx(), Value = _, Acc = A) -> B)

name:foldl_3/7
def:foldl_3(pos_integer(), _, A, array_indx(),
	      fun((array_indx, _, A) -> B), integer()) -> B

name:foldr/3
def:foldr(Function, InitialAcc :: A, Array :: array()) -> B
types:
      Function = fun((Index = array_indx(), Value = _, Acc = A) -> B)

name:foldr_3/7
def:foldr_3(array_indx(), term(), integer(), A,
	      fun((array_indx(), _, A) -> B)) -> B

name:from_list/1
def:from_list(List :: list()) -> array()

name:from_list/2
def:from_list(List :: list(), Default :: term()) -> array()

name:from_orddict/1
def:from_orddict(Orddict :: indx_pairs()) -> array()

name:from_orddict/2
def:from_orddict(Orddict :: indx_pairs(), Default :: term()) -> array()

name:get/2
def:get(I :: array_indx(), Array :: array()) -> term()

name:is_array/1
def:is_array(X :: term()) -> boolean()

name:is_fix/1
def:is_fix(Array :: array()) -> boolean()

name:map/2
def:map(Function, Array :: array()) -> array()
types:
      Function = fun((Index = array_indx(), Value = _) -> _)

name:map_3/5
def:map_3(pos_integer(), _, array_indx(),
	    fun((array_indx(),_) -> _), _, non_neg_integer(), [X]) -> [X]

name:new/0
def:new() -> array()

name:new/1
def:new(Options :: array_opts()) -> array()

name:new/2
def:new(Size :: non_neg_integer(), Options :: array_opts()) -> array()

name:push_pairs/4
def:push_pairs(non_neg_integer(), array_indx(), term(), indx_pairs()) ->
	  indx_pairs()

name:push_tuple_pairs/4
def:push_tuple_pairs(non_neg_integer(), array_indx(), term(), indx_pairs()) ->
	  indx_pairs()

name:relax/1
def:relax(Array :: array()) -> array()

name:reset/2
def:reset(I :: array_indx(), Array :: array()) -> array()

name:resize/2
def:resize(Size :: non_neg_integer(), Array :: array()) -> array()

name:resize/1
def:resize(Array :: array()) -> array()

name:set/3
def:set(I :: array_indx(), Value :: term(), Array :: array()) -> array()

name:size/1
def:size(Array :: array()) -> non_neg_integer()

name:sparse_foldl/3
def:sparse_foldl(Function, InitialAcc :: A, Array :: array()) -> B
types:
      Function = fun((Index = array_indx(), Value = _, Acc = A) -> B)

name:sparse_foldr/3
def:sparse_foldr(Function, InitialAcc :: A, Array :: array()) -> B
types:
      Function = fun((Index = array_indx(), Value = _, Acc = A) -> B)

name:sparse_foldr_3/7
def:sparse_foldr_3(array_indx(), _, array_indx(), A,
		     fun((array_indx(), _, A) -> B), _) -> B

name:sparse_map/2
def:sparse_map(Function, Array :: array()) -> array()
types:
      Function = fun((Index = array_indx(), Value = _) -> _)

name:sparse_map_3/5
def:sparse_map_3(pos_integer(), _, array_indx(),
		   fun((array_indx(),_) -> _), _, [X]) -> [X]

name:sparse_push_tuple_pairs/5
def:sparse_push_tuple_pairs(non_neg_integer(), array_indx(),
			      _, _, indx_pairs()) -> indx_pairs()

name:sparse_size/1
def:sparse_size(Array :: array()) -> non_neg_integer()

name:sparse_to_list/1
def:sparse_to_list(Array :: array()) -> list()

name:sparse_to_orddict/1
def:sparse_to_orddict(Array :: array()) -> indx_pairs()

name:to_list/1
def:to_list(Array :: array()) -> list()

name:to_orddict/1
def:to_orddict(Array :: array()) -> indx_pairs()

