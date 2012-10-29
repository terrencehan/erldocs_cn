name:catch_exception/1
def:catch_exception(Bool) -> Bool
types:
      Bool = boolean()

name:history/1
def:history(N) -> non_neg_integer()
types:
      N = non_neg_integer()

name:prompt_func/1
def:prompt_func(PromptFunc) -> PromptFunc
types:
      PromptFunc = 'default' | {module(),atom()}

name:results/1
def:results(N) -> non_neg_integer()
types:
      N = non_neg_integer()

name:server/2
def:server(boolean(), boolean()) -> 'terminated'

name:server/1
def:server(boolean()) -> 'terminated'

name:start/0
def:start() -> pid()

name:start_restricted/1
def:start_restricted(Module) -> {'error', Reason}
types:
      Module = module(),
      Reason = code:load_error_rsn()

name:stop_restricted/0
def:stop_restricted() -> no_return()

name:strip_bindings/1
def:strip_bindings(erl_eval:binding_struct()) -> erl_eval:binding_struct()

name:whereis_evaluator/0
def:whereis_evaluator() -> 'undefined' | pid()

name:whereis_evaluator/1
def:whereis_evaluator(pid()) -> 'undefined' | pid()

