name:init/1
def:init([]) -> {'error','no_stderror'} | {'ok',pid(),pid()}

name:start_link/0
def:start_link() -> 'ignore' | {'error',term()} | {'ok',pid()}

name:terminate/2
def:terminate(term(), pid()) -> 'ok'

