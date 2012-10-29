name:adjacents/1
def:adjacents(pid()) -> [pid()]

name:flush/1
def:flush(pid()) -> 'true'

name:format/1
def:format(CrashReport) -> string()
types:
      CrashReport = [term()]

name:get_ancestors/1
def:get_ancestors(pid()) -> {'ancestors', [pid()]}

name:get_ancestors/0
def:get_ancestors() -> [pid()]

name:hibernate/3
def:hibernate(Module, Function, Args) -> no_return()
types:
      Module = module(),
      Function = atom(),
      Args = [term()]

name:init_ack/2
def:init_ack(Parent, Ret) -> 'ok'
types:
      Parent = pid(),
      Ret = term()

name:init_ack/1
def:init_ack(Ret) -> 'ok'
types:
      Ret = term()

name:init_p/3
def:init_p(pid(), [pid()], function()) -> term()

name:init_p/5
def:init_p(pid(), [pid()], atom(), atom(), [term()]) -> term()

name:initial_call/1
def:initial_call(Process) -> {Module, Function, Args} | 'false'
types:
      Process = dict_or_pid(),
      Module = module(),
      Function = atom(),
      Args = [atom()]

name:neighbours/1
def:neighbours(pid()) -> [pid()]

name:spawn/1
def:spawn(Fun) -> pid()
types:
      Fun = function()

name:spawn/3
def:spawn(Module, Function, Args) -> pid()
types:
      Module = module(),
      Function = atom(),
      Args = [term()]

name:spawn/2
def:spawn(Node, Fun) -> pid()
types:
      Node = node(),
      Fun = function()

name:spawn/4
def:spawn(Node, Module, Function, Args) -> pid()
types:
      Node = node(),
      Module = module(),
      Function = atom(),
      Args = [term()]

name:spawn_link/1
def:spawn_link(Fun) -> pid()
types:
      Fun = function()

name:spawn_link/3
def:spawn_link(Module, Function, Args) -> pid()
types:
      Module = module(),
      Function = atom(),
      Args = [term()]

name:spawn_link/2
def:spawn_link(Node, Fun) -> pid()
types:
      Node = node(),
      Fun = function()

name:spawn_link/4
def:spawn_link(Node, Module, Function, Args) -> pid()
types:
      Node = node(),
      Module = module(),
      Function = atom(),
      Args = [term()]

name:spawn_opt/2
def:spawn_opt(Fun, SpawnOpts) -> pid()
types:
      Fun = function(),
      SpawnOpts = [spawn_option()]

name:spawn_opt/3
def:spawn_opt(Node, Function, SpawnOpts) -> pid()
types:
      Node = node(),
      Function = function(),
      SpawnOpts = [spawn_option()]

name:spawn_opt/4
def:spawn_opt(Module, Function, Args, SpawnOpts) -> pid()
types:
      Module = module(),
      Function = atom(),
      Args = [term()],
      SpawnOpts = [spawn_option()]

name:spawn_opt/5
def:spawn_opt(Node, Module, Function, Args, SpawnOpts) -> pid()
types:
      Node = node(),
      Module = module(),
      Function = atom(),
      Args = [term()],
      SpawnOpts = [spawn_option()]

name:start/3
def:start(Module, Function, Args) -> Ret
types:
      Module = module(),
      Function = atom(),
      Args = [term()],
      Ret = term() | {error, Reason = term()}

name:start/4
def:start(Module, Function, Args, Time) -> Ret
types:
      Module = module(),
      Function = atom(),
      Args = [term()],
      Time = timeout(),
      Ret = term() | {error, Reason = term()}

name:start/5
def:start(Module, Function, Args, Time, SpawnOpts) -> Ret
types:
      Module = module(),
      Function = atom(),
      Args = [term()],
      Time = timeout(),
      SpawnOpts = [spawn_option()],
      Ret = term() | {error, Reason = term()}

name:start_link/3
def:start_link(Module, Function, Args) -> Ret
types:
      Module = module(),
      Function = atom(),
      Args = [term()],
      Ret = term() | {error, Reason = term()}

name:start_link/4
def:start_link(Module, Function, Args, Time) -> Ret
types:
      Module = module(),
      Function = atom(),
      Args = [term()],
      Time = timeout(),
      Ret = term() | {error, Reason = term()}

name:start_link/5
def:start_link(Module, Function, Args, Time, SpawnOpts) -> Ret
types:
      Module = module(),
      Function = atom(),
      Args = [term()],
      Time = timeout(),
      SpawnOpts = [spawn_option()],
      Ret = term() | {error, Reason = term()}

name:translate_initial_call/1
def:translate_initial_call(Process) -> {Module, Function, Arity}
types:
      Process = dict_or_pid(),
      Module = module(),
      Function = atom(),
      Arity = byte()

name:wake_up/3
def:wake_up(atom(), atom(), [term()]) -> term()

