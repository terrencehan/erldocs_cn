name:add_binding/3
def:add_binding(Name, Value, BindingStruct) -> binding_struct()
types:
      Name = name(),
      Value = value(),
      BindingStruct = binding_struct()

name:binding/2
def:binding(Name, BindingStruct) -> {value, value()} | unbound
types:
      Name = name(),
      BindingStruct = binding_struct()

name:bindings/1
def:bindings(BindingStruct :: binding_struct()) -> bindings()

name:del_binding/2
def:del_binding(Name, BindingStruct) -> binding_struct()
types:
      Name = name(),
      BindingStruct = binding_struct()

name:expr/2
def:expr(Expression, Bindings) -> {value, Value, NewBindings}
types:
      Expression = expression(),
      Bindings = binding_struct(),
      Value = value(),
      NewBindings = binding_struct()

name:expr/3
def:expr(Expression, Bindings, LocalFunctionHandler) ->
             {value, Value, NewBindings}
types:
      Expression = expression(),
      Bindings = binding_struct(),
      LocalFunctionHandler = local_function_handler(),
      Value = value(),
      NewBindings = binding_struct()

name:expr/4
def:expr(Expression, Bindings, LocalFunctionHandler,
           NonLocalFunctionHandler) ->
             {value, Value, NewBindings}
types:
      Expression = expression(),
      Bindings = binding_struct(),
      LocalFunctionHandler = local_function_handler(),
      NonLocalFunctionHandler = non_local_function_handler(),
      Value = value(),
      NewBindings = binding_struct()

name:expr/5
def:expr(Expression, Bindings, LocalFunctionHandler,
           NonLocalFunctionHandler, ReturnFormat) ->
             {value, Value, NewBindings} | Value
types:
      Expression = expression(),
      Bindings = binding_struct(),
      LocalFunctionHandler = local_function_handler(),
      NonLocalFunctionHandler = non_local_function_handler(),
      ReturnFormat = none | value,
      Value = value(),
      NewBindings = binding_struct()

name:expr_list/2
def:expr_list(ExpressionList, Bindings) -> {ValueList, NewBindings}
types:
      ExpressionList = expression_list(),
      Bindings = binding_struct(),
      ValueList = [value()],
      NewBindings = binding_struct()

name:expr_list/3
def:expr_list(ExpressionList, Bindings, LocalFunctionHandler) ->
             {ValueList, NewBindings}
types:
      ExpressionList = expression_list(),
      Bindings = binding_struct(),
      LocalFunctionHandler = local_function_handler(),
      ValueList = [value()],
      NewBindings = binding_struct()

name:expr_list/4
def:expr_list(ExpressionList, Bindings, LocalFunctionHandler,
                NonLocalFunctionHandler) ->
             {ValueList, NewBindings}
types:
      ExpressionList = expression_list(),
      Bindings = binding_struct(),
      LocalFunctionHandler = local_function_handler(),
      NonLocalFunctionHandler = non_local_function_handler(),
      ValueList = [value()],
      NewBindings = binding_struct()

name:exprs/2
def:exprs(Expressions, Bindings) -> {value, Value, NewBindings}
types:
      Expressions = expressions(),
      Bindings = binding_struct(),
      Value = value(),
      NewBindings = binding_struct()

name:exprs/3
def:exprs(Expressions, Bindings, LocalFunctionHandler) ->
             {value, Value, NewBindings}
types:
      Expressions = expressions(),
      Bindings = binding_struct(),
      LocalFunctionHandler = local_function_handler(),
      Value = value(),
      NewBindings = binding_struct()

name:exprs/4
def:exprs(Expressions, Bindings, LocalFunctionHandler,
            NonLocalFunctionHandler) ->
             {value, Value, NewBindings}
types:
      Expressions = expressions(),
      Bindings = binding_struct(),
      LocalFunctionHandler = local_function_handler(),
      NonLocalFunctionHandler = non_local_function_handler(),
      Value = value(),
      NewBindings = binding_struct()

name:match_clause/4
def:match_clause(Clauses, ValueList, Bindings, LocalFunctionHandler) ->
             {Body, NewBindings} | nomatch
types:
      Clauses = clauses(),
      ValueList = [value()],
      Bindings = binding_struct(),
      LocalFunctionHandler = local_function_handler(),
      Body = expression_list(),
      NewBindings = binding_struct()

name:new_bindings/0
def:new_bindings() -> binding_struct()

