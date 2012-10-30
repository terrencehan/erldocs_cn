name:format_error/1
def:format_error(Error) -> Chars
types:
      Error = {error, module(), term()},
      Chars = io_lib:chars()

name:parse_transform/2
def:parse_transform(Forms, Options) -> Forms
types:
      Forms = [erl_parse:abstract_form()],
      Options = term()

name:transform_from_shell/3
def:transform_from_shell(Dialect, Clauses, BoundEnvironment) -> term()
types:
      Dialect = ets | dbg,
      Clauses = [erl_parse:abstract_clause()],
      BoundEnvironment = erl_eval:binding_struct()

