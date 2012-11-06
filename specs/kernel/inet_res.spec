name:getbyname/2
def:getbyname(Name, Type) -> {ok, Hostent} | {error, Reason}
types:
      Name = dns_name(),
      Type = rr_type(),
      Hostent = inet:hostent(),
      Reason = inet:posix() | res_error()

name:getbyname/3
def:getbyname(Name, Type, Timeout) -> {ok, Hostent} | {error, Reason}
types:
      Name = dns_name(),
      Type = rr_type(),
      Timeout = timeout(),
      Hostent = inet:hostent(),
      Reason = inet:posix() | res_error()

name:gethostbyaddr/1
def:gethostbyaddr(Address) -> {ok, Hostent} | {error, Reason}
types:
      Address = inet:ip_address(),
      Hostent = inet:hostent(),
      Reason = inet:posix() | res_error()

name:gethostbyaddr/2
def:gethostbyaddr(Address, Timeout) -> {ok, Hostent} | {error, Reason}
types:
      Address = inet:ip_address(),
      Timeout = timeout(),
      Hostent = inet:hostent(),
      Reason = inet:posix() | res_error()

name:gethostbyname/1
def:gethostbyname(Name) -> {ok, Hostent} | {error, Reason}
types:
      Name = dns_name(),
      Hostent = inet:hostent(),
      Reason = inet:posix() | res_error()

name:gethostbyname/2
def:gethostbyname(Name, Family) -> {ok, Hostent} | {error, Reason}
types:
      Name = dns_name(),
      Hostent = inet:hostent(),
      Family = inet:address_family(),
      Reason = inet:posix() | res_error()

name:gethostbyname/3
def:gethostbyname(Name, Family, Timeout) ->
                           {ok, Hostent} | {error, Reason}
types:
      Name = dns_name(),
      Hostent = inet:hostent(),
      Timeout = timeout(),
      Family = inet:address_family(),
      Reason = inet:posix() | res_error()

name:lookup/3
def:lookup(Name, Class, Type) -> [dns_data()]
types:
      Name = dns_name() | inet:ip_address(),
      Class = dns_class(),
      Type = rr_type()

name:lookup/4
def:lookup(Name, Class, Type, Opts) -> [dns_data()]
types:
      Name = dns_name() | inet:ip_address(),
      Class = dns_class(),
      Type = rr_type(),
      Opts = [res_option() | verbose]

name:lookup/5
def:lookup(Name, Class, Type, Opts, Timeout) -> [dns_data()]
types:
      Name = dns_name() | inet:ip_address(),
      Class = dns_class(),
      Type = rr_type(),
      Opts = [res_option() | verbose],
      Timeout = timeout()

name:nnslookup/4
def:nnslookup(Name, Class, Type, Nameservers) ->
                      {ok, dns_msg()} | {error, Reason}
types:
      Name = dns_name() | inet:ip_address(),
      Class = dns_class(),
      Type = rr_type(),
      Nameservers = [nameserver()],
      Reason = inet:posix()

name:nnslookup/5
def:nnslookup(Name, Class, Type, Nameservers, Timeout) ->
                      {ok, dns_msg()} | {error, Reason}
types:
      Name = dns_name() | inet:ip_address(),
      Class = dns_class(),
      Type = rr_type(),
      Timeout = timeout(),
      Nameservers = [nameserver()],
      Reason = inet:posix()

name:nslookup/3
def:nslookup(Name, Class, Type) -> {ok, dns_msg()} | {error, Reason}
types:
      Name = dns_name() | inet:ip_address(),
      Class = dns_class(),
      Type = rr_type(),
      Reason = inet:posix() | res_error()

name:nslookup/4
def:nslookup(Name, Class, Type, Timeout) ->
                      {ok, dns_msg()} | {error, Reason}
types:
                  Name = dns_name() | inet:ip_address(),
                  Class = dns_class(),
                  Type = rr_type(),
                  Timeout = timeout(),
                  Reason = inet:posix() | res_error();
              (Name, Class, Type, Nameservers) ->
                      {ok, dns_msg()} | {error, Reason} when
                  Name = dns_name() | inet:ip_address(),
                  Class = dns_class(),
                  Type = rr_type(),
                  Nameservers = [nameserver()],
                  Reason = inet:posix() | res_error()

name:resolve/3
def:resolve(Name, Class, Type) -> {ok, dns_msg()} | Error
types:
      Name = dns_name() | inet:ip_address(),
      Class = dns_class(),
      Type = rr_type(),
      Error = {error, Reason} | {error,{Reason,dns_msg()}},
      Reason = inet:posix() | res_error()

name:resolve/4
def:resolve(Name, Class, Type, Opts) ->
                     {ok, dns_msg()} | Error
types:
      Name = dns_name() | inet:ip_address(),
      Class = dns_class(),
      Type = rr_type(),
      Opts = [Opt],
      Opt = res_option() | verbose | atom(),
      Error = {error, Reason} | {error,{Reason,dns_msg()}},
      Reason = inet:posix() | res_error()

name:resolve/5
def:resolve(Name, Class, Type, Opts, Timeout) ->
                     {ok, dns_msg()} | Error
types:
      Name = dns_name() | inet:ip_address(),
      Class = dns_class(),
      Type = rr_type(),
      Opts = [Opt],
      Opt = res_option() | verbose | atom(),
      Timeout = timeout(),
      Error = {error, Reason} | {error,{Reason,dns_msg()}},
      Reason = inet:posix() | res_error()

