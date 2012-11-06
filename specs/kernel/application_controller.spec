name:code_change/3
def:code_change(term(), state(), term()) -> {'ok', state()}

name:handle_call/4
def:handle_call(calls(), {pid(), term()}, state()) ->
        {'noreply', state()} | {'reply', term(), state()}

name:handle_cast/4
def:handle_cast({'application_started', appname(), _}, state()) ->
        {'noreply', state()} | {'stop', string(), state()}

name:handle_info/2
def:handle_info(term(), state()) ->
        {'noreply', state()} | {'stop', string(), state()}

name:terminate/2
def:terminate(term(), state()) -> 'ok'

name:to_string/1
def:to_string(term()) -> string()

