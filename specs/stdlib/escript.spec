name:create/2
def:create(file:filename() | binary, [section()]) ->
		    ok | {ok, binary()} | {error, term()}

name:extract/2
def:extract(file:filename(), [extract_option()]) ->
        {ok, [section()]} | {error, term()}

name:script_name/0
def:script_name() -> string()

name:start/0
def:start() -> no_return()

name:start/1
def:start([string()]) -> no_return()

