name:breakpoint/3
def:breakpoint(Module :: atom(), Function :: atom(), Args :: [_]) ->
	any()

name:crash/2
def:crash(atom(), [term()]) -> no_return()

name:crash/3
def:crash(atom(), atom(), arity()) -> no_return()

name:crash/1
def:crash(tuple()) -> no_return()

name:stub_function/3
def:stub_function(atom(), atom(), [_]) -> no_return()

name:undefined_function/3
def:undefined_function(Module, Function, Args) ->
	any()
types:
      Module = atom(),
      Function = atom(),
      Args = list()

name:undefined_lambda/3
def:undefined_lambda(Module, Fun, Args) -> term()
types:
      Module = atom(),
      Fun = fun(),
      Args = list()

