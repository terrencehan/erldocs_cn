name:close/1
def:close(Socket) -> ok
types:
      Socket = socket()

name:controlling_process/2
def:controlling_process(Socket, Pid) -> ok | {error, Reason}
types:
      Socket = socket(),
      Pid = pid(),
      Reason = closed | not_owner | inet:posix()

name:open/1
def:open(Port) -> {ok, Socket} | {error, Reason}
types:
      Port = inet:port_number(),
      Socket = socket(),
      Reason = inet:posix()

name:open/2
def:open(Port, Opts) -> {ok, Socket} | {error, Reason}
types:
      Port = inet:port_number(),
      Opts = [Option],
      Option = {ip, inet:ip_address()}
              | {fd, non_neg_integer()}
              | {ifaddr, inet:ip_address()}
              | inet:address_family()
              | {port, inet:port_number()}
              | option(),
      Socket = socket(),
      Reason = inet:posix()

name:recv/2
def:recv(Socket, Length) ->
                  {ok, {Address, Port, Packet}} | {error, Reason}
types:
      Socket = socket(),
      Length = non_neg_integer(),
      Address = inet:ip_address(),
      Port = inet:port_number(),
      Packet = string() | binary(),
      Reason = not_owner | inet:posix()

name:recv/3
def:recv(Socket, Length, Timeout) ->
                  {ok, {Address, Port, Packet}} | {error, Reason}
types:
      Socket = socket(),
      Length = non_neg_integer(),
      Timeout = timeout(),
      Address = inet:ip_address(),
      Port = inet:port_number(),
      Packet = string() | binary(),
      Reason = not_owner | inet:posix()

name:send/4
def:send(Socket, Address, Port, Packet) -> ok | {error, Reason}
types:
      Socket = socket(),
      Address = inet:ip_address() | inet:hostname(),
      Port = inet:port_number(),
      Packet = iodata(),
      Reason = not_owner | inet:posix()

