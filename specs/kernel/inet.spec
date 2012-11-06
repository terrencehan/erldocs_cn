name:close/1
def:close(Socket) -> 'ok'
types:
      Socket = socket()

name:fdopen/6
def:fdopen(Fd :: non_neg_integer(),
	     Opts :: [socket_setopt()],
	     Protocol :: socket_protocol(),
	     Family :: address_family(),
	     Type :: socket_type(),
	     Module :: atom()) ->
	{'ok', socket()} | {'error', posix()}

name:format_error/1
def:format_error(Reason) -> string()
types:
      Reason = posix() | system_limit

name:get_rc/0
def:get_rc() -> [{Par :: any(), Val :: any()}]

name:getaddr/2
def:getaddr(Host, Family) -> {ok, Address} | {error, posix()}
types:
      Host = ip_address() | hostname(),
      Family = address_family(),
      Address = ip_address()

name:getaddr/3
def:getaddr(Host :: ip_address() | hostname(),
	      Family :: address_family(),
	      Timeout :: non_neg_integer() | 'infinity') ->
	{'ok', ip_address()} | {'error', posix()}

name:getaddrs/2
def:getaddrs(Host, Family) ->
	{ok, Addresses} | {error, posix()}
types:
      Host = ip_address() | hostname(),
      Family = address_family(),
      Addresses = [ip_address()]

name:getaddrs/3
def:getaddrs(Host :: ip_address() | string() | atom(),
	       Family :: address_family(),
	       Timeout :: non_neg_integer() | 'infinity') ->
	{'ok', [ip_address()]} | {'error', posix()}

name:getfd/1
def:getfd(Socket :: socket()) ->
	{'ok', non_neg_integer()} | {'error', posix()}

name:gethostbyaddr/1
def:gethostbyaddr(Address) -> {ok, Hostent} | {error, posix()}
types:
      Address = string() | ip_address(),
      Hostent = hostent()

name:gethostbyaddr/2
def:gethostbyaddr(Address :: string() | ip_address(), 
	            Timeout :: non_neg_integer() | 'infinity') ->
	{'ok', #hostent{}} | {'error', posix()}

name:gethostbyname/1
def:gethostbyname(Hostname) -> {ok, Hostent} | {error, posix()}
types:
      Hostname = hostname(),
      Hostent = hostent()

name:gethostbyname/2
def:gethostbyname(Hostname, Family) ->
                           {ok, Hostent} | {error, posix()}
types:
      Hostname = hostname(),
      Family = address_family(),
      Hostent = hostent()

name:gethostbyname/3
def:gethostbyname(Name :: hostname(),
	            Family :: address_family(),
	            Timeout :: non_neg_integer() | 'infinity') ->
	{'ok', #hostent{}} | {'error', posix()}

name:gethostname/0
def:gethostname() -> {'ok', Hostname}
types:
      Hostname = string()

name:gethostname/1
def:gethostname(Socket :: socket()) ->
	{'ok', string()} | {'error', posix()}

name:getif/0
def:getif() ->
	{'ok', [{ip_address(), ip_address() | 'undefined', ip_address()}]} | 
	{'error', posix()}

name:getif/1
def:getif(Socket :: socket()) ->
	{'ok', [{ip_address(), ip_address() | 'undefined', ip_address()}]} | 
	{'error', posix()}

name:getifaddrs/1
def:getifaddrs(Socket :: socket()) ->
	{'ok', [string()]} | {'error', posix()}

name:getifaddrs/0
def:getifaddrs() -> {ok, Iflist} | {error, posix()}
types:
      Iflist = [{Ifname,[Ifopt]}],
      Ifname = string(),
      Ifopt = {flag,[Flag]} | {addr,Addr} | {netmask,Netmask}
             | {broadaddr,Broadaddr} | {dstaddr,Dstaddr}
             | {hwaddr,Hwaddr},
      Flag = up | broadcast | loopback | pointtopoint
            | running | multicast,
      Addr = ip_address(),
      Netmask = ip_address(),
      Broadaddr = ip_address(),
      Dstaddr = ip_address(),
      Hwaddr = [byte()]

name:getiflist/1
def:getiflist(Socket :: socket()) ->
	{'ok', [string()]} | {'error', posix()}

name:getiflist/0
def:getiflist() -> {'ok', [string()]} | {'error', posix()}

name:getll/1
def:getll(Socket :: socket()) -> {'ok', socket()}

name:getopts/2
def:getopts(Socket, Options) ->
	{'ok', OptionValues} | {'error', posix()}
types:
      Socket = socket(),
      Options = [socket_getopt()],
      OptionValues = [socket_setopt()]

name:getservbyname/2
def:getservbyname(Name :: atom() | string(),
	            Protocol :: atom() | string()) ->
	{'ok', port_number()} | {'error', posix()}

name:getservbyport/2
def:getservbyport(Port :: port_number(), Protocol :: atom() | string()) ->
	{'ok', string()} | {'error', posix()}

name:getstat/1
def:getstat(Socket) ->
	{ok, OptionValues} | {error, posix()}
types:
      Socket = socket(),
      OptionValues = [{stat_option(), integer()}]

name:getstat/2
def:getstat(Socket, Options) ->
	{ok, OptionValues} | {error, posix()}
types:
      Socket = socket(),
      Options = [stat_option()],
      OptionValues = [{stat_option(), integer()}]

name:ifget/3
def:ifget(Socket :: socket(),
            Name :: string() | atom(),
	    Opts :: [if_getopt()]) ->
	{'ok', [if_setopt()]} | {'error', posix()}

name:ifget/2
def:ifget(Name :: string() | atom(), Opts :: [if_getopt()]) ->
	{'ok', [if_setopt()]} | {'error', posix()}

name:ific/18
def:ific (though they may be similar to their
    % TCP and UDP counter-parts):
    sctp_rtoinfo,   		 sctp_associnfo,	sctp_initmsg,
    sctp_autoclose,		 sctp_nodelay,		sctp_disable_fragments,
    sctp_i_want_mapped_v4_addr,  sctp_maxseg,		sctp_primary_addr,
    sctp_set_peer_primary_addr,  sctp_adaptation_layer,	sctp_peer_addr_params,
    sctp_default_send_param,	 sctp_events,		sctp_delayed_ack_time,
    sctp_status,	   	 sctp_get_peer_addr_info
].

sctp_options(Opts, Mod)  ->
    case sctp_opt(Opts, Mod, #sctp_opts{}, sctp_options()) of
	{ok,#sctp_opts{ifaddr=undefined}=SO} -> 
	    {ok,SO#sctp_opts{ifaddr=Mod:translate_ip(?SCTP_DEF_IFADDR)}};
	{ok,_}=OK ->
	    OK;
	Error -> Error
    end

name:ifset/3
def:ifset(Socket :: socket(),
            Name :: string() | atom(),
	    Opts :: [if_setopt()]) ->
	'ok' | {'error', posix()}

name:ifset/2
def:ifset(Name :: string() | atom(), Opts :: [if_setopt()]) ->
	'ok' | {'error', posix()}

name:ip/1
def:ip(Ip :: ip_address() | string() | atom()) ->
	{'ok', ip_address()} | {'error', posix()}

name:open/8
def:open(Fd :: integer(),
	   Addr :: ip_address(),
	   Port :: port_number(),
	   Opts :: [socket_setopt()],
	   Protocol :: socket_protocol(),
	   Family :: address_family(),
	   Type :: socket_type(),
	   Module :: atom()) ->
	{'ok', socket()} | {'error', posix()}

name:peername/1
def:peername(Socket) ->  {ok, {Address, Port}} | {error, posix()}
types:
      Socket = socket(),
      Address = ip_address(),
      Port = non_neg_integer()

name:port/1
def:port(Socket) -> {'ok', Port} | {'error', any()}
types:
      Socket = socket(),
      Port = port_number()

name:send/2
def:send(Socket :: socket(), Packet :: iolist()) -> % iolist()?
	'ok' | {'error', posix()}

name:setopts/2
def:setopts(Socket, Options) -> ok | {error, posix()}
types:
      Socket = socket(),
      Options = [socket_setopt()]

name:setpeername/3
def:setpeername(Socket :: socket(), Address :: {ip_address(), port_number()}) ->
	'ok' | {'error', any()}

name:setsockname/3
def:setsockname(Socket :: socket(), Address :: {ip_address(), port_number()}) ->
	'ok' | {'error', any()}

name:sockname/1
def:sockname(Socket) -> {ok, {Address, Port}} | {error, posix()}
types:
      Socket = socket(),
      Address = ip_address(),
      Port = non_neg_integer()

name:stats/0
def:stats() -> [stat_option(),...]

