name:create/1
def:create(PgName) -> 'ok' | {'error', Reason}
types:
      PgName = term(),
      Reason = 'already_created' | term()

name:create/2
def:create(PgName, Node) -> 'ok' | {'error', Reason}
types:
      PgName = term(),
      Node = node(),
      Reason = 'already_created' | term()

name:esend/2
def:esend(PgName, Msg) -> 'ok'
types:
      PgName = term(),
      Msg = term()

name:join/2
def:join(PgName, Pid) -> Members
types:
      PgName = term(),
      Pid = pid(),
      Members = [pid()]

name:master/1
def:master(term()) -> no_return()

name:members/1
def:members(PgName) -> Members
types:
      PgName = term(),
      Members = [pid()]

name:name_to_pid/1
def:name_to_pid(atom()) -> pid() | 'undefined'

name:send/2
def:send(PgName, Msg) -> 'ok'
types:
      PgName = term(),
      Msg = term()

name:standby/2
def:standby(term(), node()) -> 'ok'

