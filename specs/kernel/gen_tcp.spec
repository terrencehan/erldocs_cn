name:accept/1
def:accept(ListenSocket) -> {ok, Socket} | {error, Reason}
types:
      ListenSocket = socket(),
      Socket = socket(),
      Reason = closed | timeout | system_limit | inet:posix()

name:accept/2
def:accept(ListenSocket, Timeout) -> {ok, Socket} | {error, Reason}
types:
      ListenSocket = socket(),
      Timeout = timeout(),
      Socket = socket(),
      Reason = closed | timeout | system_limit | inet:posix()

name:close/1
def:close(Socket) -> ok
types:
      Socket = socket()

name:connect/3
def:connect(Address, Port, Options) -> {ok, Socket} | {error, Reason}
types:
      Address = inet:ip_address() | inet:hostname(),
      Port = inet:port_number(),
      Options = [connect_option()],
      Socket = socket(),
      Reason = inet:posix()

name:connect/4
def:connect(Address, Port, Options, Timeout) ->
                     {ok, Socket} | {error, Reason}
types:
      Address = inet:ip_address() | inet:hostname(),
      Port = inet:port_number(),
      Options = [connect_option()],
      Timeout = timeout(),
      Socket = socket(),
      Reason = inet:posix()

name:controlling_process/2
def:controlling_process(Socket, Pid) -> ok | {error, Reason}
types:
      Socket = socket(),
      Pid = pid(),
      Reason = closed | not_owner | inet:posix()

name:listen/2
def:listen(Port, Options) -> {ok, ListenSocket} | {error, Reason}
types:
      Port = inet:port_number(),
      Options = [listen_option()],
      ListenSocket = socket(),
      Reason = system_limit | inet:posix()

name:recv/2
def:recv(Socket, Length) -> {ok, Packet} | {error, Reason}
types:
      Socket = socket(),
      Length = non_neg_integer(),
      Packet = string() | binary() | HttpPacket,
      Reason = closed | inet:posix(),
      HttpPacket = term()

name:recv/3
def:recv(Socket, Length, Timeout) -> {ok, Packet} | {error, Reason}
types:
      Socket = socket(),
      Length = non_neg_integer(),
      Timeout = timeout(),
      Packet = string() | binary() | HttpPacket,
      Reason = closed | inet:posix(),
      HttpPacket = term()

name:send/2
def:send(Socket, Packet) -> ok | {error, Reason}
types:
      Socket = socket(),
      Packet = iodata(),
      Reason = inet:posix()

name:shutdown/2
def:shutdown(Socket, How) -> ok | {error, Reason}
types:
      Socket = socket(),
      How = read | write | read_write,
      Reason = inet:posix()

