name:attribute/1
def:attribute(Attribute) -> io_lib:chars()
types:
      Attribute = erl_parse:abstract_form()

name:attribute/2
def:attribute(Attribute, HookFunction) -> io_lib:chars()
types:
      Attribute = erl_parse:abstract_form(),
      HookFunction = hook_function()

name:expr/1
def:expr(Expression) -> io_lib:chars()
types:
      Expression = erl_parse:abstract_expr()

name:expr/2
def:expr(Expression, HookFunction) -> io_lib:chars()
types:
      Expression = erl_parse:abstract_expr(),
      HookFunction = hook_function()

name:expr/3
def:expr(Expression, Indent, HookFunction) -> io_lib:chars()
types:
      Expression = erl_parse:abstract_expr(),
      Indent = integer(),
      HookFunction = hook_function()

name:expr/4
def:expr(Expression, Indent, Precedence, HookFunction) -> io_lib:chars()
types:
      Expression = erl_parse:abstract_expr(),
      Indent = integer(),
      Precedence = non_neg_integer(),
      HookFunction = hook_function()

name:exprs/1
def:exprs(Expressions) -> io_lib:chars()
types:
      Expressions = [erl_parse:abstract_expr()])

name:exprs/2
def:exprs(Expressions, HookFunction) -> io_lib:chars()
types:
      Expressions = [erl_parse:abstract_expr()],
      HookFunction = hook_function()

name:exprs/3
def:exprs(Expressions, Indent, HookFunction) -> io_lib:chars()
types:
      Expressions = [erl_parse:abstract_expr()],
      Indent = integer(),
      HookFunction = hook_function()

name:form/1
def:form(Form) -> io_lib:chars()
types:
      Form = erl_parse:abstract_form()

name:form/2
def:form(Form, HookFunction) -> io_lib:chars()
types:
      Form = erl_parse:abstract_form(),
      HookFunction = hook_function()

name:function/1
def:function(Function) -> io_lib:chars()
types:
      Function = erl_parse:abstract_form()

name:function/2
def:function(Function, HookFunction) -> io_lib:chars()
types:
      Function = erl_parse:abstract_form(),
      HookFunction = hook_function()

name:guard/1
def:guard(Guard) -> io_lib:chars()
types:
      Guard = [erl_parse:abstract_expr()])

name:guard/2
def:guard(Guard, HookFunction) -> io_lib:chars()
types:
      Guard = [erl_parse:abstract_expr()],
      HookFunction = hook_function()

