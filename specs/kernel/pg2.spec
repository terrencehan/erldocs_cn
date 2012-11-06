name:create/1
def:create(Name :: name()) -> 'ok'

name:delete/1
def:delete(Name :: name()) -> 'ok'

name:get_closest_pid/1
def:get_closest_pid(Name) ->  pid() | {'error', Reason}
types:
      Name = name(),
      Reason =  {'no_process', Name} | {'no_such_group', Name}

name:get_local_members/1
def:get_local_members(Name) -> [pid()] | {'error', {'no_such_group', Name}}
types: Name = name()

name:get_members/1
def:get_members(Name) -> [pid()] | {'error', {'no_such_group', Name}}
types: Name = name()

name:handle_call/10
def:handle_call(Call :: {'create', Name}
                        | {'delete', Name}
                        | {'join', Name, Pid :: pid()}
                        | {'leave', Name, Pid :: pid()},
                  From :: {pid(),Tag :: any()},
                  State :: state()) -> {'reply', 'ok', state()}
types: Name = name()

name:handle_cast/7
def:handle_cast(Cast :: {'exchange', node(), Names :: [[Name,...]]}
                        | {'del_member', Name, Pid :: pid()},
                  State :: state()) -> {'noreply', state()}
types: Name = name()

name:handle_info/2
def:handle_info(Tuple :: tuple(), State :: state()) ->
    {'noreply', state()}

name:init/1
def:init(Arg :: []) -> {'ok', state()}

name:join/2
def:join(Name, Pid :: pid()) -> 'ok' | {'error', {'no_such_group', Name}}
types: Name = name()

name:leave/2
def:leave(Name, Pid :: pid()) -> 'ok' | {'error', {'no_such_group', Name}}
types: Name = name()

name:start/0
def:start() -> {'ok', pid()} | {'error', any()}

name:start_link/0
def:start_link() -> {'ok', pid()} | {'error', any()}

name:terminate/2
def:terminate(Reason :: any(), State :: state()) -> 'ok'

name:which_groups/0
def:which_groups() -> [Name :: name()]

