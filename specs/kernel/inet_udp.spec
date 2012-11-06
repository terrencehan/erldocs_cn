name:close/1
def:close(inet:socket()) -> ok

name:open/1
def:open(_) -> {ok, inet:socket()} | {error, atom()}

name:open/2
def:open(_, _) -> {ok, inet:socket()} | {error, atom()}

