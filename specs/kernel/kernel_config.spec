name:code_change/3
def:code_change(term(), State, term()) -> {'ok', State}

name:handle_call/3
def:handle_call(term(), term(), State) -> {'reply', 'ok', State}

name:handle_cast/2
def:handle_cast(term(), State) -> {'noreply', State}

name:handle_info/2
def:handle_info(term(), State) -> {'noreply', State}

name:init/1
def:init([]) -> {'ok', []} | {'stop', term()}

name:terminate/2
def:terminate(term(), term()) -> 'ok'

