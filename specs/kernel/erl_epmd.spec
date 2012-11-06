name:code_change/3
def:code_change(term(), state(), term()) -> {'ok', state()}

name:handle_call/3
def:handle_call(calls(), term(), state()) ->
        {'reply', term(), state()} | {'stop', 'shutdown', 'ok', state()}

name:handle_cast/2
def:handle_cast(term(), state()) -> {'noreply', state()}

name:handle_info/2
def:handle_info(term(), state()) -> {'noreply', state()}

name:init/1
def:init(_) -> {'ok', state()}

name:terminate/2
def:terminate(term(), state()) -> 'ok'

