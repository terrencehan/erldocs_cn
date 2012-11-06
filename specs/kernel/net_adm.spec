name:dns_hostname/1
def:dns_hostname(Host) -> {ok, Name} | {error, Host}
types:
      Host = atom() | string(),
      Name = string()

name:host_file/0
def:host_file() -> Hosts | {error, Reason}
types:
      Hosts = [Host = atom()],
      %% Copied from file:path_consult/2:
      Reason = file:posix() | badarg | terminated | system_limit
              | {Line = integer(), Mod = module(), Term = term()}

name:localhost/0
def:localhost() -> Name
types:
      Name = string()

name:names/0
def:names() -> {ok, [{Name, Port}]} | {error, Reason}
types:
      Name = string(),
      Port = non_neg_integer(),
      Reason = address | file:posix()

name:names/1
def:names(Host) -> {ok, [{Name, Port}]} | {error, Reason}
types:
      Host = atom() | string(),
      Name = string(),
      Port = non_neg_integer(),
      Reason = address | file:posix()

name:ping/1
def:ping(Node) -> pong | pang
types:
      Node = atom()

name:ping_list/1
def:ping_list([atom()]) -> [atom()]

name:world/0
def:world() -> [node()]

name:world/1
def:world(Arg) -> [node()]
types:
      Arg = verbosity()

name:world_list/1
def:world_list(Hosts) -> [node()]
types:
      Hosts = [atom()]

name:world_list/2
def:world_list(Hosts, Arg) -> [node()]
types:
      Hosts = [atom()],
      Arg = verbosity()

