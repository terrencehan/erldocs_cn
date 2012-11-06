name:abcast/2
def:abcast(Name, Msg) -> abcast
types:
      Name = atom(),
      Msg = term()

name:abcast/3
def:abcast(Nodes, Name, Msg) -> abcast
types:
      Nodes = [node()],
      Name = atom(),
      Msg = term()

name:async_call/4
def:async_call(Node, Module, Function, Args) -> Key
types:
      Node = node(),
      Module = module(),
      Function = atom(),
      Args = [term()],
      Key = key()

name:block_call/4
def:block_call(Node, Module, Function, Args) -> Res | {badrpc, Reason}
types:
      Node = node(),
      Module = module(),
      Function = atom(),
      Args = [term()],
      Res = term(),
      Reason = term()

name:block_call/5
def:block_call(Node, Module, Function, Args, Timeout) ->
                  Res | {badrpc, Reason}
types:
      Node = node(),
      Module = module(),
      Function = atom(),
      Args = [term()],
      Res = term(),
      Reason = term(),
      Timeout = timeout()

name:call/4
def:call(Node, Module, Function, Args) -> Res | {badrpc, Reason}
types:
      Node = node(),
      Module = module(),
      Function = atom(),
      Args = [term()],
      Res = term(),
      Reason = term()

name:call/5
def:call(Node, Module, Function, Args, Timeout) ->
                  Res | {badrpc, Reason}
types:
      Node = node(),
      Module = module(),
      Function = atom(),
      Args = [term()],
      Res = term(),
      Reason = term(),
      Timeout = timeout()

name:cast/4
def:cast(Node, Module, Function, Args) -> true
types:
      Node = node(),
      Module = module(),
      Function = atom(),
      Args = [term()]

name:code_change/3
def:code_change(term(), state(), term()) -> {'ok', state()}

name:do_yield/2
def:do_yield(pid(), timeout()) -> {'value', _} | 'timeout'

name:eval_everywhere/3
def:eval_everywhere(Module, Function, Args) -> abcast
types:
      Module = module(),
      Function = atom(),
      Args = [term()]

name:eval_everywhere/4
def:eval_everywhere(Nodes, Module, Function, Args) -> abcast
types:
      Nodes = [node()],
      Module = module(),
      Function = atom(),
      Args = [term()]

name:handle_call/3
def:handle_call(term(), term(), state()) ->
        {'noreply', state()} |
	{'reply', term(), state()} |
	{'stop', 'normal', 'stopped', state()}

name:handle_cast/2
def:handle_cast(term(), state()) -> {'noreply', state()}

name:handle_info/2
def:handle_info(term(), state()) -> {'noreply', state()}

name:init/1
def:init([]) -> {'ok', state()}

name:multi_server_call/2
def:multi_server_call(Name, Msg) -> {Replies, BadNodes}
types:
      Name = atom(),
      Msg = term(),
      Replies = [Reply = term()],
      BadNodes = [node()]

name:multi_server_call/3
def:multi_server_call(Nodes, Name, Msg) -> {Replies, BadNodes}
types:
      Nodes = [node()],
      Name = atom(),
      Msg = term(),
      Replies = [Reply = term()],
      BadNodes = [node()]

name:multicall/3
def:multicall(Module, Function, Args) -> {ResL, BadNodes}
types:
      Module = module(),
      Function = atom(),
      Args = [term()],
      ResL = [term()],
      BadNodes = [node()]

name:multicall/4
def:multicall(Nodes, Module, Function, Args) -> {ResL, BadNodes}
types:
                  Nodes = [node()],
                  Module = module(),
                  Function = atom(),
                  Args = [term()],
                  ResL = [term()],
                  BadNodes = [node()];
               (Module, Function, Args, Timeout) -> {ResL, BadNodes} when
                  Module = module(),
                  Function = atom(),
                  Args = [term()],
                  Timeout = timeout(),
                  ResL = [term()],
                  BadNodes = [node()]

name:multicall/5
def:multicall(Nodes, Module, Function, Args, Timeout) ->
                       {ResL, BadNodes}
types:
      Nodes = [node()],
      Module = module(),
      Function = atom(),
      Args = [term()],
      Timeout = timeout(),
      ResL = [term()],
      BadNodes = [node()]

name:nb_yield/2
def:nb_yield(Key, Timeout) -> {value, Val} | timeout
types:
      Key = key(),
      Timeout = timeout(),
      Val = (Res = term()) | {badrpc, Reason = term()}

name:nb_yield/1
def:nb_yield(Key) -> {value, Val} | timeout
types:
      Key = key(),
      Val = (Res = term()) | {badrpc, Reason = term()}

name:parallel_eval/1
def:parallel_eval(FuncCalls) -> ResL
types:
      FuncCalls = [{Module, Function, Args}],
      Module = module(),
      Function = atom(),
      Args = [term()],
      ResL = [term()]

name:pinfo/1
def:pinfo(Pid) -> [{Item, Info}] | undefined
types:
      Pid = pid(),
      Item = atom(),
      Info = term()

name:pinfo/2
def:pinfo(Pid, Item) -> {Item, Info} | undefined | []
types:
      Pid = pid(),
      Item = atom(),
      Info = term()

name:pmap/3
def:pmap(FuncSpec, ExtraArgs, List1) -> List2
types:
      FuncSpec = {Module,Function},
      Module = module(),
      Function = atom(),
      ExtraArgs = [term()],
      List1 = [Elem = term()],
      List2 = [term()]

name:proxy_user_flush/0
def:proxy_user_flush() -> no_return()

name:safe_multi_server_call/2
def:safe_multi_server_call(Name, Msg) -> {Replies, BadNodes}
types:
      Name = atom(),
      Msg = term(),
      Replies = [Reply = term()],
      BadNodes = [node()]

name:safe_multi_server_call/3
def:safe_multi_server_call(Nodes, Name, Msg) -> {Replies, BadNodes}
types:
      Nodes = [node()],
      Name = atom(),
      Msg = term(),
      Replies = [Reply = term()],
      BadNodes = [node()]

name:sbcast/2
def:sbcast(Name, Msg) -> {GoodNodes, BadNodes}
types:
      Name = atom(),
      Msg = term(),
      GoodNodes = [node()],
      BadNodes = [node()]

name:sbcast/3
def:sbcast(Nodes, Name, Msg) -> {GoodNodes, BadNodes}
types:
      Name = atom(),
      Msg = term(),
      Nodes = [node()],
      GoodNodes = [node()],
      BadNodes = [node()]

name:server_call/4
def:server_call(Node, Name, ReplyWrapper, Msg) -> Reply | {error, Reason}
types:
      Node = node(),
      Name = atom(),
      ReplyWrapper = term(),
      Msg = term(),
      Reply = term(),
      Reason = nodedown

name:start/0
def:start() -> {'ok', pid()} | 'ignore' | {'error', term()}

name:start_link/0
def:start_link() -> {'ok', pid()} | 'ignore' | {'error', term()}

name:stop/0
def:stop() -> term()

name:terminate/2
def:terminate(term(), state()) -> 'ok'

name:yield/1
def:yield(Key) -> Res | {badrpc, Reason}
types:
      Key = key(),
      Res = term(),
      Reason = term()

