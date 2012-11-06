name:cmd/1
def:cmd(Command) -> string()
types:
      Command = atom() | io_lib:chars()

name:extensions/0
def:extensions() -> [string(),...]

name:find_executable/1
def:find_executable(Name) -> Filename | 'false'
types:
      Name = string(),
      Filename = string()

name:find_executable/2
def:find_executable(Name, Path) -> Filename | 'false'
types:
      Name = string(),
      Path = string(),
      Filename = string()

name:start_port/0
def:start_port() -> port()

name:type/0
def:type() -> vxworks | {Osfamily, Osname}
types:
      Osfamily = unix | win32,
      Osname = atom()

name:version/0
def:version() -> VersionString | {Major, Minor, Release}
types:
      VersionString = string(),
      Major = non_neg_integer(),
      Minor = non_neg_integer(),
      Release = non_neg_integer()

