name:append/1
def:append(QHL) -> QH
types:
      QHL = [query_handle_or_list()],
      QH = query_handle()

name:append/2
def:append(QH1, QH2) -> QH3
types:
      QH1 = query_handle_or_list(),
      QH2 = query_handle_or_list(),
      QH3 = query_handle()

name:cursor/1
def:cursor(QH) -> Cursor
types:
      QH = query_handle_or_list(),
      Cursor = query_cursor()

name:cursor/2
def:cursor(QH, Options) -> Cursor
types:
      QH = query_handle_or_list(),
      Options = [Option] | Option,
      Option = {cache_all, cache()} | cache_all
              | {max_list_size, max_list_size()}
              | {spawn_options, spawn_options()}
              | {tmpdir_usage, tmp_file_usage()}
              | {tmpdir, tmp_directory()}
              | {unique_all, boolean()} | unique_all,
      Cursor = query_cursor()

name:delete_cursor/1
def:delete_cursor(QueryCursor) -> ok
types:
      QueryCursor = query_cursor()

name:e/1
def:e(QH) -> Answers | Error
types:
      QH = query_handle_or_list(),
      Answers = answers(),
      Error = {error, module(), Reason},
      Reason = file_sorter:reason()

name:e/2
def:e(QH, Options) -> Answers | Error
types:
      QH = query_handle_or_list(),
      Options = [Option] | Option,
      Option = {cache_all, cache()} | cache_all
              | {max_list_size, max_list_size()}
              | {tmpdir_usage, tmp_file_usage()}
              | {tmpdir, tmp_directory()}
              | {unique_all, boolean()} | unique_all,
      Answers = answers(),
      Error = {error, module(), Reason},
      Reason = file_sorter:reason()

name:eval/1
def:eval(QH) -> Answers | Error
types:
      QH = query_handle_or_list(),
      Answers = answers(),
      Error = {error, module(), Reason},
      Reason = file_sorter:reason()

name:eval/2
def:eval(QH, Options) -> Answers | Error
types:
      QH = query_handle_or_list(),
      Answers = answers(),
      Options = [Option] | Option,
      Option = {cache_all, cache()} | cache_all
              | {max_list_size, max_list_size()}
              | {tmpdir_usage, tmp_file_usage()}
              | {tmpdir, tmp_directory()}
              | {unique_all, boolean()} | unique_all,
      Error = {error, module(), Reason},
      Reason = file_sorter:reason()

name:fold/3
def:fold(Function, Acc0, QH) ->
               Acc1 | Error
types:
      QH = query_handle_or_list(),
      Function = fun((answer(), AccIn) -> AccOut),
      Acc0 = term(),
      Acc1 = term(),
      AccIn = term(),
      AccOut = term(),
      Error = {error, module(), Reason},
      Reason = file_sorter:reason()

name:fold/4
def:fold(Function, Acc0, QH, Options) ->
               Acc1 | Error
types:
      QH = query_handle_or_list(),
      Function = fun((answer(), AccIn) -> AccOut),
      Acc0 = term(),
      Acc1 = term(),
      AccIn = term(),
      AccOut = term(),
      Options = [Option] | Option,
      Option = {cache_all, cache()} | cache_all
              | {max_list_size, max_list_size()}
              | {tmpdir_usage, tmp_file_usage()}
              | {tmpdir, tmp_directory()}
              | {unique_all, boolean()} | unique_all,
      Error = {error, module(), Reason},
      Reason = file_sorter:reason()

name:format_error/1
def:format_error(Error) -> Chars
types:
      Error = {error, module(), term()},
      Chars = io_lib:chars()

name:info/1
def:info(QH) -> Info
types:
      QH = query_handle_or_list(),
      Info = abstract_expr() | string()

name:info/2
def:info(QH, Options) -> Info
types:
      QH = query_handle_or_list(),
      Options = [Option] | Option,
      Option = EvalOption | ReturnOption,
      EvalOption = {cache_all, cache()} | cache_all
                  | {max_list_size, max_list_size()}
                  | {tmpdir_usage, tmp_file_usage()}
                  | {tmpdir, tmp_directory()}
                  | {unique_all, boolean()} | unique_all,
      ReturnOption = {depth, Depth}
                    | {flat, boolean()}
                    | {format, Format}
                    | {n_elements, NElements},
      Depth = infinity | non_neg_integer(),
      Format = abstract_code | string,
      NElements = infinity | pos_integer(),
      Info = abstract_expr() | string()

name:keysort/2
def:keysort(KeyPos, QH1) -> QH2
types:
      KeyPos = key_pos(),
      QH1 = query_handle_or_list(),
      QH2 = query_handle()

name:keysort/3
def:keysort(KeyPos, QH1, SortOptions) -> QH2
types:
      KeyPos = key_pos(),
      SortOptions = sort_options(),
      QH1 = query_handle_or_list(),
      QH2 = query_handle()

name:next_answers/1
def:next_answers(QueryCursor) ->
            Answers | Error
types:
      QueryCursor = query_cursor(),
      Answers = answers(),
      Error = {error, module(), Reason},
      Reason = file_sorter:reason()

name:next_answers/2
def:next_answers(QueryCursor, NumberOfAnswers) ->
            Answers | Error
types:
      QueryCursor = query_cursor(),
      Answers = answers(),
      NumberOfAnswers = all_remaining | pos_integer(),
      Error = {error, module(), Reason},
      Reason = file_sorter:reason()

name:parse_transform/2
def:parse_transform(Forms, Options) -> Forms2
types:
      Forms = [erl_parse:abstract_form()],
      Forms2 = [erl_parse:abstract_form()],
      Options = [Option],
      Option = type_checker | compile:option()

name:q/1
def:q(QLC) -> QH
types:
      QLC = query_list_comprehension(),
      QH = query_handle()

name:q/2
def:q(QLC, Options) -> QH
types:
      QH = query_handle(),
      Options = [Option] | Option,
      Option = {max_lookup, MaxLookup}
              | {cache, cache()} | cache
              | {join, Join}
              | {lookup, Lookup}
              | {unique, boolean()} | unique,
      MaxLookup = non_neg_integer() | infinity,
      Join = any | lookup | merge | nested_loop,
      Lookup = boolean() | any,
      QLC = query_list_comprehension()

name:sort/1
def:sort(QH1) -> QH2
types:
      QH1 = query_handle_or_list(),
      QH2 = query_handle()

name:sort/2
def:sort(QH1, SortOptions) -> QH2
types:
      SortOptions = sort_options(),
      QH1 = query_handle_or_list(),
      QH2 = query_handle()

name:string_to_handle/1
def:string_to_handle(QueryString) -> QH | Error
types:
      QueryString = string(),
      QH = query_handle(),
      Error = {error, module(), Reason},
      Reason = erl_parse:error_info() | erl_scan:error_info()

name:string_to_handle/2
def:string_to_handle(QueryString, Options) -> QH | Error
types:
      QueryString = string(),
      Options = [Option] | Option,
      Option = {max_lookup, MaxLookup}
              | {cache, cache()} | cache
              | {join, Join}
              | {lookup, Lookup}
              | {unique, boolean()} | unique,
      MaxLookup = non_neg_integer() | infinity,
      Join = any | lookup | merge | nested_loop,
      Lookup = boolean() | any,
      QH = query_handle(),
      Error = {error, module(), Reason},
      Reason = erl_parse:error_info() | erl_scan:error_info()

name:string_to_handle/3
def:string_to_handle(QueryString, Options, Bindings) -> QH | Error
types:
      QueryString = string(),
      Options = [Option] | Option,
      Option = {max_lookup, MaxLookup}
              | {cache, cache()} | cache
              | {join, Join}
              | {lookup, Lookup}
              | {unique, boolean()} | unique,
      MaxLookup = non_neg_integer() | infinity,
      Join = any | lookup | merge | nested_loop,
      Lookup = boolean() | any,
      Bindings = erl_eval:binding_struct(),
      QH = query_handle(),
      Error = {error, module(), Reason},
      Reason = erl_parse:error_info() | erl_scan:error_info()

name:table/2
def:table(TraverseFun, Options) -> QH
types:
      TraverseFun = TraverseFun0 | TraverseFun1,
      TraverseFun0 = fun(() -> TraverseResult),
      TraverseFun1 = fun((match_expression()) -> TraverseResult),
      TraverseResult = Objects | term(),
      Objects = [] | [term() | ObjectList],
      ObjectList = TraverseFun0 | Objects,
      Options = [Option] | Option,
      Option = {format_fun, FormatFun}
              | {info_fun, InfoFun}
              | {lookup_fun, LookupFun}
              | {parent_fun, ParentFun}
              | {post_fun, PostFun}
              | {pre_fun, PreFun}
              | {key_equality, KeyComparison},
      FormatFun = undefined  | fun((SelectedObjects) -> FormatedTable),
      SelectedObjects = all
                       | {all, NElements, DepthFun}
                       | {match_spec, match_expression()}
                       | {lookup, Position, Keys}
                       | {lookup, Position, Keys, NElements, DepthFun},
      NElements = infinity | pos_integer(),
      DepthFun = fun((term()) -> term()),
      FormatedTable = {Mod, Fun, Args}
                     | abstract_expr()
                     | string(),
      InfoFun = undefined  | fun((InfoTag) -> InfoValue),
      InfoTag = indices | is_unique_objects | keypos | num_of_objects,
      InfoValue = undefined  | term(),
      LookupFun = undefined  | fun((Position, Keys) -> LookupResult),
      LookupResult = [term()] | term(),
      ParentFun = undefined  | fun(() -> ParentFunValue),
      PostFun = undefined  | fun(() -> term()),
      PreFun = undefined  | fun((PreArgs) -> term()),
      PreArgs = [PreArg],
      PreArg = {parent_value, ParentFunValue}  | {stop_fun, StopFun},
      ParentFunValue = undefined  | term(),
      StopFun = undefined  | fun(() -> term()),
      KeyComparison = '=:=' | '==',
      Position = pos_integer(),
      Keys = [term()],
      Mod = atom(),
      Fun = atom(),
      Args = [term()],
      QH = query_handle()

name:throw_error/1
def:throw_error(term()) -> no_return()

name:throw_file_error/3
def:throw_file_error(string(), {'error',atom()}) -> no_return()

name:throw_reason/1
def:throw_reason(term()) -> no_return()

name:transform_from_evaluator/2
def:transform_from_evaluator(LC, Bs) -> Expr
types:
      LC = abstract_expr(),
      Expr = abstract_expr(),
      Bs = erl_eval:binding_struct()

