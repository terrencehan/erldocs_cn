name:init/1
def:init([]) -> {'ok', pid(), pid()} | {'error', term()}

name:system_code_change/4
def:system_code_change(state(), module(), term(), term()) -> {'ok', state()}

name:terminate/2
def:terminate(term(), pid()) -> 'ok'

