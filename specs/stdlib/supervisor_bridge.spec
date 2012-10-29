name:start_link/2
def:start_link(Module, Args) -> Result
types:
      Module = module(),
      Args = term(),
      Result = {ok, Pid} | ignore | {error, Error},
      Error = {already_started, Pid} | term(),
      Pid = pid()

name:start_link/3
def:start_link(SupBridgeName, Module, Args) -> Result
types:
      SupBridgeName = {local, Name} | {global, Name},
      Name = atom(),
      Module = module(),
      Args = term(),
      Result = {ok, Pid} | ignore | {error, Error},
      Error = {already_started, Pid} | term(),
      Pid = pid()

