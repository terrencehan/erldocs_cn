name:arith_op/2
def:arith_op(OpName, Arity) -> boolean()
types:
      OpName = atom(),
      Arity = arity()

name:bif/3
def:bif(Mod::atom(), Name::atom(), Arity::arity()) -> boolean()

name:bif/2
def:bif(Name, Arity) -> boolean()
types:
      Name = atom(),
      Arity=arity()

name:bool_op/2
def:bool_op(OpName, Arity) -> boolean()
types:
      OpName = atom(),
      Arity = arity()

name:comp_op/2
def:comp_op(OpName, Arity) -> boolean()
types:
      OpName = atom(),
      Arity = arity()

name:guard_bif/2
def:guard_bif(Name, Arity) -> boolean()
types:
      Name = atom(),
      Arity = arity()

name:list_op/2
def:list_op(OpName, Arity) -> boolean()
types:
      OpName = atom(),
      Arity = arity()

name:new_type_test/2
def:new_type_test(Name::atom(), Arity::arity()) -> boolean()

name:old_bif/2
def:old_bif(Name::atom(), Arity::arity()) -> boolean()

name:old_type_test/2
def:old_type_test(Name::atom(), Arity::arity()) -> boolean()

name:op_type/2
def:op_type(OpName, Arity) -> Type
types:
      OpName = atom(),
      Arity = arity(),
      Type = 'arith' | 'bool' | 'comp' | 'list' | 'send'

name:send_op/2
def:send_op(OpName, Arity) -> boolean()
types:
      OpName = atom(),
      Arity = arity()

name:type_test/2
def:type_test(Name, Arity) -> boolean()
types:
      Name = atom(),
      Arity = arity()

