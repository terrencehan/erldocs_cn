name:abstract/1
def:abstract(Data) -> AbsTerm
types:
      Data = term(),
      AbsTerm = abstract_expr()

name:error_bad_decl/2
def:error_bad_decl(integer(), attributes()) -> no_return()

name:format_error/1
def:format_error(any()) -> [char() | list()]

name:func_prec/0
def:func_prec() -> {800,700}

name:max_prec/0
def:max_prec() -> 1000

name:normalise/1
def:normalise(AbsTerm) -> Data
types:
      AbsTerm = abstract_expr(),
      Data = term()

name:parse/1
def:parse(Tokens :: list()) -> yecc_ret()

name:parse_and_scan/5
def:parse_and_scan({function() | {atom(), atom()}, [_]}
                     | {atom(), atom(), [_]}) -> yecc_ret()

name:parse_exprs/1
def:parse_exprs(Tokens) -> {ok, ExprList} | {error, ErrorInfo}
types:
      Tokens = [token()],
      ExprList = [abstract_expr()],
      ErrorInfo = error_info()

name:parse_form/1
def:parse_form(Tokens) -> {ok, AbsForm} | {error, ErrorInfo}
types:
      Tokens = [token()],
      AbsForm = abstract_form(),
      ErrorInfo = error_info()

name:parse_term/1
def:parse_term(Tokens) -> {ok, Term} | {error, ErrorInfo}
types:
      Tokens = [token()],
      Term = term(),
      ErrorInfo = error_info()

name:preop_prec/1
def:preop_prec(pre_op()) -> {0 | 600 | 700, 100 | 700 | 800}

name:ret_err/2
def:ret_err(_, _) -> no_return()

name:return_error/2
def:return_error(integer(), any()) -> no_return()

name:tokens/1
def:tokens(AbsTerm) -> Tokens
types:
      AbsTerm = abstract_expr(),
      Tokens = [token()]

name:tokens/2
def:tokens(AbsTerm, MoreTokens) -> Tokens
types:
      AbsTerm = abstract_expr(),
      MoreTokens = [token()],
      Tokens = [token()]

