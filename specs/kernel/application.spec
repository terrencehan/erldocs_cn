name:get_all_env/0
def:get_all_env() -> Env
types:
      Env = [{Par = atom(), Val = term()}]

name:get_all_env/1
def:get_all_env(Application) -> Env
types:
      Application = atom(),
      Env = [{Par = atom(), Val = term()}]

name:get_all_key/0
def:get_all_key() -> [] | {'ok', Keys}
types:
      Keys = [{Key = atom(),Val = term()},...]

name:get_all_key/1
def:get_all_key(Application) -> 'undefined' | Keys
types:
      Application = atom(),
      Keys = {'ok', [{Key = atom(),Val = term()},...]}

name:get_application/0
def:get_application() -> 'undefined' | {'ok', Application}
types:
      Application = atom()

name:get_application/1
def:get_application(PidOrModule) -> 'undefined' | {'ok', Application}
types:
      PidOrModule = (Pid = pid()) | (Module = module()),
      Application = atom()

name:get_env/1
def:get_env(Par) -> 'undefined' | {'ok', Val}
types:
      Par = atom(),
      Val = term()

name:get_env/2
def:get_env(Application, Par) -> 'undefined' | {'ok', Val}
types:
      Application = atom(),
      Par = atom(),
      Val = term()

name:get_key/1
def:get_key(Key) -> 'undefined' | {'ok', Val}
types:
      Key = atom(),
      Val = term()

name:get_key/2
def:get_key(Application, Key) -> 'undefined' | {'ok', Val}
types:
      Application = atom(),
      Key = atom(),
      Val = term()

name:info/0
def:info() -> term()

name:load/1
def:load(AppDescr) -> 'ok' | {'error', Reason}
types:
      AppDescr = Application | (AppSpec = application_spec()),
      Application = atom(),
      Reason = term()

name:load/2
def:load(AppDescr, Distributed) -> 'ok' | {'error', Reason}
types:
      AppDescr = Application | (AppSpec = application_spec()),
      Application = atom(),
      Distributed = {Application,Nodes}
                   | {Application,Time,Nodes}
                   | 'default',
      Nodes = [node() | tuple_of(node())],
      Time = pos_integer(),
      Reason = term()

name:loaded_applications/0
def:loaded_applications() -> [{Application, Description, Vsn}]
types:
      Application = atom(),
      Description = string(),
      Vsn = string()

name:permit/2
def:permit(Application, Permission) -> 'ok' | {'error', Reason}
types:
      Application = atom(),
      Permission = boolean(),
      Reason = term()

name:set_env/3
def:set_env(Application, Par, Val) -> 'ok'
types:
      Application = atom(),
      Par = atom(),
      Val = term()

name:set_env/4
def:set_env(Application, Par, Val, Timeout) -> 'ok'
types:
      Application = atom(),
      Par = atom(),
      Val = term(),
      Timeout = timeout()

name:start/1
def:start(Application) -> 'ok' | {'error', Reason}
types:
      Application = atom(),
      Reason = term()

name:start/2
def:start(Application, Type) -> 'ok' | {'error', Reason}
types:
      Application = atom(),
      Type = restart_type(),
      Reason = term()

name:start_boot/1
def:start_boot(Application :: atom()) -> 'ok' | {'error', term()}

name:start_boot/2
def:start_boot(Application :: atom(), RestartType :: restart_type()) ->
	     'ok' | {'error', term()}

name:start_type/0
def:start_type() -> StartType | 'undefined' | 'local'
types:
      StartType = start_type()

name:stop/1
def:stop(Application) -> 'ok' | {'error', Reason}
types:
      Application = atom(),
      Reason = term()

name:takeover/2
def:takeover(Application, Type) -> 'ok' | {'error', Reason}
types:
      Application = atom(),
      Type = restart_type(),
      Reason = term()

name:unload/1
def:unload(Application) -> 'ok' | {'error', Reason}
types:
      Application = atom(),
      Reason = term()

name:unset_env/2
def:unset_env(Application, Par) -> 'ok'
types:
      Application = atom(),
      Par = atom()

name:unset_env/3
def:unset_env(Application, Par, Timeout) -> 'ok'
types:
      Application = atom(),
      Par = atom(),
      Timeout = timeout()

name:which_applications/0
def:which_applications() -> [{Application, Description, Vsn}]
types:
      Application = atom(),
      Description = string(),
      Vsn = string()

name:which_applications/1
def:which_applications(Timeout) -> [{Application, Description, Vsn}]
types:
      Timeout = timeout(),
      Application = atom(),
      Description = string(),
      Vsn = string()

