name:add_slave/1
def:add_slave(Slave) -> 'ok' | {'error', What}
types:
      Slave = Host,
      Host = atom(),
      What = any()

name:add_subnet/2
def:add_subnet(Mask :: ip4_address(), Addr :: ip4_address()) ->
	'ok' | {'error', any()}

name:boot_init/1
def:boot_init(reference()) -> no_return()

name:code_change/3
def:code_change(term(), state(), term()) -> {'ok', state()}

name:delete_slave/1
def:delete_slave(Slave) -> 'ok' | {'error', What}
types:
      Slave = Host,
      Host = atom(),
      What = any()

name:delete_subnet/2
def:delete_subnet(Mask :: ip4_address(), Addr :: ip4_address()) -> 'ok'

name:handle_call/5
def:handle_call('which' | {'add',atom()} | {'delete',atom()}, _, state()) ->
        {'reply', 'ok' | [atom()], state()}

name:handle_cast/2
def:handle_cast(term(), [atom()]) -> {'noreply', [atom()]}

name:handle_info/2
def:handle_info(term(), state()) -> {'noreply', state()}

name:init/1
def:init([atom()]) -> {'ok', state()}

name:start/1
def:start(Slaves) -> {'ok', Pid} | {'error', What}
types:
      Slaves = [Host],
      Host = atom(),
      Pid = pid(),
      What = any()

name:start_link/1
def:start_link(Slaves) -> {'ok', Pid} | {'error', What}
types:
      Slaves = [Host],
      Host = atom(),
      Pid = pid(),
      What = any()

name:terminate/2
def:terminate(term(), state()) -> 'ok'

name:which_slaves/0
def:which_slaves() -> Slaves
types:
      Slaves = [Host],
      Host = atom()

