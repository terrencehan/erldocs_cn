name:parse_transform/2
def:parse_transform(Forms, Options) -> Forms2
types:
      Forms = [erl_parse:abstract_form()],
      Forms2 = [erl_parse:abstract_form()],
      Options = [Option],
      Option = type_checker | compile:option()

name:transform_expression/2
def:transform_expression(LC, Bs) -> Expr
types:
      LC = erl_parse:abstract_expr(),
      Expr = erl_parse:abstract_expr(),
      Bs = erl_eval:binding_struct()

name:transform_from_evaluator/2
def:transform_from_evaluator(LC, Bs) -> Expr
types:
      LC = erl_parse:abstract_expr(),
      Expr = erl_parse:abstract_expr(),
      Bs = erl_eval:binding_struct()

