name:bool_option/4
def:bool_option(atom(), atom(), boolean(), [compile:option()]) -> boolean()

name:call_function/4
def:call_function(line(), atom(), arity(), lint_state()) -> lint_state()

name:define_function/4
def:define_function(line(), atom(), arity(), lint_state()) -> lint_state()

name:export/3
def:export(line(), [fa()], lint_state()) -> lint_state()

name:export_type/3
def:export_type(line(), [ta()], lint_state()) -> lint_state()

name:format_error/1
def:format_error(ErrorDescriptor) -> io_lib:chars()
types:
      ErrorDescriptor = error_description()

name:import/3
def:import(line(), import(), lint_state()) -> lint_state()

name:imported/3
def:imported(atom(), arity(), lint_state()) -> {'yes',module()} | 'no'

name:is_guard_test/1
def:is_guard_test(Expr) -> boolean()
types:
      Expr = erl_parse:abstract_expr()

name:module/1
def:module(AbsForms) -> {ok, Warnings} | {error, Errors, Warnings}
types:
      AbsForms = [erl_parse:abstract_form()],
      Warnings = [{file:filename(),[ErrorInfo]}],
      Errors = [{FileName2 = file:filename(),[ErrorInfo]}],
      ErrorInfo = error_info()

name:module/2
def:module(AbsForms, FileName) ->
             {ok, Warnings} | {error, Errors, Warnings}
types:
      AbsForms = [erl_parse:abstract_form()],
      FileName = atom() | string(),
      Warnings = [{file:filename(),[ErrorInfo]}],
      Errors = [{FileName2 = file:filename(),[ErrorInfo]}],
      ErrorInfo = error_info()

name:module/3
def:module(AbsForms, FileName, CompileOptions) ->
             {ok, Warnings} | {error, Errors, Warnings}
types:
      AbsForms = [erl_parse:abstract_form()],
      FileName = atom() | string(),
      CompileOptions = [compile:option()],
      Warnings = [{file:filename(),[ErrorInfo]}],
      Errors = [{FileName2 = file:filename(),[ErrorInfo]}],
      ErrorInfo = error_info()

name:on_load/3
def:on_load(line(), fa(), lint_state()) -> lint_state()

