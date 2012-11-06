name:clear_cmd/0
def:clear_cmd() -> ok

name:cycle/0
def:cycle() -> 'ok' | {'error', term()}

name:get_cmd/0
def:get_cmd() -> {ok, Cmd}
types:
      Cmd = string()

name:init/2
def:init(pid(), pid()) -> {'no_heart', pid()} | {'start_error', pid()}

name:no_reboot_shutdown/1
def:no_reboot_shutdown(port()) -> no_return()

name:set_cmd/1
def:set_cmd(Cmd) -> 'ok' | {'error', {'bad_cmd', Cmd}}
types:
      Cmd = string()

name:start/0
def:start() -> 'ignore' | {'error', term()} | {'ok', pid()}

