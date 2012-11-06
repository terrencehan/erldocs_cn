name:abort/2
def:abort(Socket, Assoc) -> ok | {error, inet:posix()}
types:
      Socket = sctp_socket(),
      Assoc = #sctp_assoc_change{}

name:close/1
def:close(Socket) -> ok | {error, inet:posix()}
types:
      Socket = sctp_socket()

name:connect/4
def:connect(Socket, Addr, Port, Opts) -> {ok, Assoc} | {error, inet:posix()}
types:
      Socket = sctp_socket(),
      Addr = inet:ip_address() | inet:hostname(),
      Port = inet:port_number(),
      Opts = [Opt = option()],
      Assoc = #sctp_assoc_change{}

name:connect/5
def:connect(Socket, Addr, Port, Opts, Timeout) ->
                     {ok, Assoc} | {error, inet:posix()}
types:
      Socket = sctp_socket(),
      Addr = inet:ip_address() | inet:hostname(),
      Port = inet:port_number(),
      Opts = [Opt = option()],
      Timeout = timeout(),
      Assoc = #sctp_assoc_change{}

name:connect_init/4
def:connect_init(Socket, Addr, Port, Opts) ->
                          ok | {error, inet:posix()}
types:
      Socket = sctp_socket(),
      Addr = inet:ip_address() | inet:hostname(),
      Port = inet:port_number(),
      Opts = [option()]

name:connect_init/5
def:connect_init(Socket, Addr, Port, Opts, Timeout) ->
                          ok | {error, inet:posix()}
types:
      Socket = sctp_socket(),
      Addr = inet:ip_address() | inet:hostname(),
      Port = inet:port_number(),
      Opts = [option()],
      Timeout = timeout()

name:controlling_process/2
def:controlling_process(Socket, Pid) -> ok | {error, Reason}
types:
      Socket = sctp_socket(),
      Pid = pid(),
      Reason = closed | not_owner | inet:posix()

name:eof/2
def:eof(Socket, Assoc) -> ok | {error, Reason}
types:
      Socket = sctp_socket(),
      Assoc = #sctp_assoc_change{},
      Reason = term()

name:error_string/1
def:error_string(ErrorNumber) -> ok | string() | unknown_error
types:
      ErrorNumber = integer()

name:listen/2
def:listen(Socket, IsServer) -> ok | {error, Reason}
types:
      Socket = sctp_socket(),
      IsServer = boolean(),
      Reason = term();
	    (Socket, Backlog) -> ok | {error, Reason} when
      Socket = sctp_socket(),
      Backlog = integer(),
      Reason = term()

name:open/0
def:open() -> {ok, Socket} | {error, inet:posix()}
types:
      Socket = sctp_socket()

name:open/1
def:open(Port) -> {ok, Socket} | {error, inet:posix()}
types:
              Port = inet:port_number(),
              Socket = sctp_socket();
          (Opts) -> {ok, Socket} | {error, inet:posix()} when
              Opts = [Opt],
              Opt = {ip,IP}
                   | {ifaddr,IP}
                   | inet:address_family()
                   | {port,Port}
		   | {type,SockType}
                   | option(),
              IP = inet:ip_address() | any | loopback,
              Port = inet:port_number(),
	      SockType = seqpacket | stream,
              Socket = sctp_socket()

name:open/2
def:open(Port, Opts) -> {ok, Socket} | {error, inet:posix()}
types:
      Opts = [Opt],
              Opt = {ip,IP}
                   | {ifaddr,IP}
                   | inet:address_family()
                   | {port,Port}
		   | {type,SockType}
                   | option(),
      IP = inet:ip_address() | any | loopback,
      Port = inet:port_number(),
      SockType = seqpacket | stream,
      Socket = sctp_socket()

name:peeloff/2
def:peeloff(Socket, Assoc) -> {ok, NewSocket} | {error, Reason}
types:
      Socket = sctp_socket(),
      Assoc = #sctp_assoc_change{} | assoc_id(),
      NewSocket = sctp_socket(),
      Reason = term()

name:recv/1
def:recv(Socket) -> {ok, {FromIP, FromPort, AncData, Data}}
                          | {error, Reason}
types:
      Socket = sctp_socket(),
      FromIP   = inet:ip_address(),
      FromPort = inet:port_number(),
      AncData  = [#sctp_sndrcvinfo{}],
      Data     = binary() | string() | #sctp_sndrcvinfo{}
                | #sctp_assoc_change{} | #sctp_paddr_change{}
                | #sctp_adaptation_event{},
      Reason   = inet:posix() | #sctp_send_failed{} | #sctp_paddr_change{}
                | #sctp_pdapi_event{} | #sctp_remote_error{}
                | #sctp_shutdown_event{}

name:recv/2
def:recv(Socket, Timeout) -> {ok, {FromIP, FromPort, AncData, Data}}
                                   | {error, Reason}
types:
      Socket = sctp_socket(),
      Timeout = timeout(),
      FromIP   = inet:ip_address(),
      FromPort = inet:port_number(),
      AncData  = [#sctp_sndrcvinfo{}],
      Data     = binary() | string() | #sctp_sndrcvinfo{}
                | #sctp_assoc_change{} | #sctp_paddr_change{}
                | #sctp_adaptation_event{},
      Reason   = inet:posix() | #sctp_send_failed{} | #sctp_paddr_change{}
                | #sctp_pdapi_event{} | #sctp_remote_error{}
                | #sctp_shutdown_event{}

name:send/3
def:send(Socket, SndRcvInfo, Data) -> ok | {error, Reason}
types:
      Socket = sctp_socket(),
      SndRcvInfo = #sctp_sndrcvinfo{},
      Data = binary() | iolist(),
      Reason = term()

name:send/4
def:send(Socket, Assoc, Stream, Data) -> ok | {error, Reason}
types:
      Socket = sctp_socket(),
      Assoc = #sctp_assoc_change{} | assoc_id(),
      Stream = integer(),
      Data = binary() | iolist(),
      Reason = term()

