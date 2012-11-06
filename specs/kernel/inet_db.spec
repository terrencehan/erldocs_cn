name:handle_call/4
def:handle_call(term(), {pid(), term()}, state()) ->
        {'reply', term(), state()} | {'stop', 'normal', 'ok', state()}

name:handle_cast/2
def:handle_cast(term(), state()) -> {'noreply', state()}

name:handle_info/2
def:handle_info(term(), state()) -> {'noreply', state()}

name:init/1
def:init([]) -> {'ok', state()}

name:terminate/2
def:terminate(term(), state()) -> 'ok'

