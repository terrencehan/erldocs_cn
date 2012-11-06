name:init/1
def:init([]) -> 'ignore' | {'error', 'nouser'} | {'ok', pid(), pid()}

name:relay/1
def:relay(pid()) -> no_return()

name:start/0
def:start() -> {'error', {'already_started', pid()}} | {'ok', pid()}

name:terminate/2
def:terminate(term(), pid()) -> 'ok'

