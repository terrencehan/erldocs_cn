name:pseudo/2
def:pseudo(Master, ServerList) -> ok
types:
      Master = node(),
      ServerList = [atom()]

name:relay/1
def:relay(Pid) -> no_return()
types:
      Pid = pid()

name:start/1
def:start(Host) -> {ok, Node} | {error, Reason}
types:
      Host = atom(),
      Node = node(),
      Reason = timeout | no_rsh | {already_running, Node}

name:start/2
def:start(Host, Name) -> {ok, Node} | {error, Reason}
types:
      Host = atom(),
      Name = atom(),
      Node = node(),
      Reason = timeout | no_rsh | {already_running, Node}

name:start/3
def:start(Host, Name, Args) -> {ok, Node} | {error, Reason}
types:
      Host = atom(),
      Name = atom(),
      Args = string(),
      Node = node(),
      Reason = timeout | no_rsh | {already_running, Node}

name:start_link/1
def:start_link(Host) -> {ok, Node} | {error, Reason}
types:
      Host = atom(),
      Node = node(),
      Reason = timeout | no_rsh | {already_running, Node}

name:start_link/2
def:start_link(Host, Name) -> {ok, Node} | {error, Reason}
types:
      Host = atom(),
      Name = atom(),
      Node = node(),
      Reason = timeout | no_rsh | {already_running, Node}

name:start_link/3
def:start_link(Host, Name, Args) -> {ok, Node} | {error, Reason}
types:
      Host = atom(),
      Name = atom(),
      Args = string(),
      Node = node(),
      Reason = timeout | no_rsh | {already_running, Node}

name:stop/1
def:stop(Node) -> ok
types:
      Node = node()

