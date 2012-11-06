name:code_change/3
def:code_change(term(), state(), term()) -> {'ok', state()}

name:del_lock/1
def:del_lock(Id) -> 'true'
types:
      Id = id()

name:del_lock/2
def:del_lock(Id, Nodes) -> 'true'
types:
      Id = id(),
      Nodes = [node()]

name:handle_call/4
def:handle_call(term(), {pid(), term()}, state()) ->
        {'noreply', state()} |
	{'reply', term(), state()} |
	{'stop', 'normal', 'stopped', state()}

name:handle_cast/2
def:handle_cast(term(), state()) -> {'noreply', state()}

name:handle_info/2
def:handle_info(term(), state()) ->
        {'noreply', state()} | {'stop', term(), state()}

name:init/1
def:init([]) -> {'ok', state()}

name:notify_all_name/3
def:notify_all_name(Name, Pid1, Pid2) -> 'none'
types:
      Name = term(),
      Pid1 = pid(),
      Pid2 = pid()

name:random_exit_name/3
def:random_exit_name(Name, Pid1, Pid2) -> pid()
types:
      Name = term(),
      Pid1 = pid(),
      Pid2 = pid()

name:random_notify_name/3
def:random_notify_name(Name, Pid1, Pid2) -> pid()
types:
      Name = term(),
      Pid1 = pid(),
      Pid2 = pid()

name:re_register_name/2
def:re_register_name(Name, Pid) -> 'yes'
types:
      Name = term(),
      Pid = pid()

name:re_register_name/3
def:re_register_name(Name, Pid, Resolve) -> 'yes'
types:
      Name = term(),
      Pid = pid(),
      Resolve = method()

name:register_name/2
def:register_name(Name, Pid) -> 'yes' | 'no'
types:
      Name = term(),
      Pid = pid()

name:register_name/3
def:register_name(Name, Pid, Resolve) -> 'yes' | 'no'
types:
      Name = term(),
      Pid = pid(),
      Resolve = method()

name:registered_names/0
def:registered_names() -> [Name]
types:
      Name = term()

name:send/2
def:send(Name, Msg) -> Pid
types:
      Name = term(),
      Msg = term(),
      Pid = pid()

name:set_lock/1
def:set_lock(Id) -> boolean()
types:
      Id = id()

name:set_lock/2
def:set_lock(Id, Nodes) -> boolean()
types:
      Id = id(),
      Nodes = [node()]

name:set_lock/3
def:set_lock(Id, Nodes, Retries) -> boolean()
types:
      Id = id(),
      Nodes = [node()],
      Retries = retries()

name:sync/0
def:sync() -> 'ok' | {'error', Reason :: term()}

name:sync/1
def:sync([node()]) -> 'ok' | {'error', Reason :: term()}

name:terminate/2
def:terminate(term(), state()) -> 'ok'

name:trans/2
def:trans(Id, Fun) -> Res | aborted
types:
      Id = id(),
      Fun = trans_fun(),
      Res = term()

name:trans/3
def:trans(Id, Fun, Nodes) -> Res | aborted
types:
      Id = id(),
      Fun = trans_fun(),
      Nodes = [node()],
      Res = term()

name:trans/4
def:trans(Id, Fun, Nodes, Retries) -> Res | aborted
types:
      Id = id(),
      Fun = trans_fun(),
      Nodes = [node()],
      Retries = retries(),
      Res = term()

name:unregister_name/1
def:unregister_name(Name) -> _
types:
      Name = term()

name:whereis_name/1
def:whereis_name(Name) -> pid() | 'undefined'
types:
      Name = term()

