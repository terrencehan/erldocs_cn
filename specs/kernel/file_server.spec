name:code_change/3
def:code_change(term(), state(), term()) -> {'ok', state()}

name:handle_call/3
def:handle_call(term(), term(), state()) ->
        {'noreply', state()} |
	{'reply', 'eof' | 'ok' | {'error', term()} | {'ok', term()}, state()} |
	{'stop', 'normal', 'stopped', state()}

name:handle_cast/2
def:handle_cast(term(), state()) -> {'noreply', state()}

name:handle_info/2
def:handle_info(term(), state()) ->
        {'noreply', state()} | {'stop', 'normal', state()}

name:init/1
def:init([]) -> {'ok', state()} | {'stop', term()}

name:terminate/2
def:terminate(term(), state()) -> 'ok'

