name:apply_after/4
def:apply_after(Time, Module, Function, Arguments) ->
                         {'ok', TRef} | {'error', Reason}
types:
      Time = time(),
      Module = module(),
      Function = atom(),
      Arguments = [term()],
      TRef = tref(),
      Reason = term()

name:apply_interval/4
def:apply_interval(Time, Module, Function, Arguments) ->
                            {'ok', TRef} | {'error', Reason}
types:
      Time = time(),
      Module = module(),
      Function = atom(),
      Arguments = [term()],
      TRef = tref(),
      Reason = term()

name:cancel/1
def:cancel(TRef) -> {'ok', 'cancel'} | {'error', Reason}
types:
      TRef = tref(),
      Reason = term()

name:code_change/3
def:code_change(term(), State, term()) -> {'ok', State}

name:ensure_started/0
def:ensure_started() -> 'ok'

name:exit_after/3
def:exit_after(Time, Pid, Reason1) -> {'ok', TRef} | {'error', Reason2}
types:
      Time = time(),
      Pid = pid() | (RegName = atom()),
      TRef = tref(),
      Reason1 = term(),
      Reason2 = term()

name:exit_after/2
def:exit_after(Time, Reason1) -> {'ok', TRef} | {'error', Reason2}
types:
      Time = time(),
      TRef = tref(),
      Reason1 = term(),
      Reason2 = term()

name:get_status/0
def:get_status() ->
	{{?TIMER_TAB,non_neg_integer()},{?INTERVAL_TAB,non_neg_integer()}}

name:handle_call/3
def:handle_call(term(), term(), timers()) ->
        {'reply', term(), timers(), timeout()} | {'noreply', timers(), timeout()}

name:handle_cast/2
def:handle_cast(term(), timers()) -> {'noreply', timers(), timeout()}

name:handle_info/2
def:handle_info(term(), timers()) -> {'noreply', timers(), timeout()}

name:hms/3
def:hms(Hours, Minutes, Seconds) -> MilliSeconds
types:
      Hours = non_neg_integer(),
      Minutes = non_neg_integer(),
      Seconds = non_neg_integer(),
      MilliSeconds = non_neg_integer()

name:hours/1
def:hours(Hours) -> MilliSeconds
types:
      Hours = non_neg_integer(),
      MilliSeconds = non_neg_integer()

name:init/1
def:init([]) -> {'ok', [], 'infinity'}

name:kill_after/2
def:kill_after(Time, Pid) -> {'ok', TRef} | {'error', Reason2}
types:
      Time = time(),
      Pid = pid() | (RegName = atom()),
      TRef = tref(),
      Reason2 = term()

name:kill_after/1
def:kill_after(Time) -> {'ok', TRef} | {'error', Reason2}
types:
      Time = time(),
      TRef = tref(),
      Reason2 = term()

name:minutes/1
def:minutes(Minutes) -> MilliSeconds
types:
      Minutes = non_neg_integer(),
      MilliSeconds = non_neg_integer()

name:next_timeout/0
def:next_timeout() -> timeout()

name:now_diff/2
def:now_diff(T2, T1) -> Tdiff
types:
      T1 = erlang:timestamp(),
      T2 = erlang:timestamp(),
      Tdiff = integer()

name:pid_delete/1
def:pid_delete(pid()) -> 'ok'

name:seconds/1
def:seconds(Seconds) -> MilliSeconds
types:
      Seconds = non_neg_integer(),
      MilliSeconds = non_neg_integer()

name:send_after/3
def:send_after(Time, Pid, Message) -> {'ok', TRef} | {'error', Reason}
types:
      Time = time(),
      Pid = pid() | (RegName = atom()),
      Message = term(),
      TRef = tref(),
      Reason = term()

name:send_after/2
def:send_after(Time, Message) -> {'ok', TRef} | {'error', Reason}
types:
      Time = time(),
      Message = term(),
      TRef = tref(),
      Reason = term()

name:send_interval/3
def:send_interval(Time, Pid, Message) ->
                           {'ok', TRef} | {'error', Reason}
types:
      Time = time(),
      Pid = pid() | (RegName = atom()),
      Message = term(),
      TRef = tref(),
      Reason = term()

name:send_interval/2
def:send_interval(Time, Message) -> {'ok', TRef} | {'error', Reason}
types:
      Time = time(),
      Message = term(),
      TRef = tref(),
      Reason = term()

name:sleep/1
def:sleep(Time) -> 'ok'
types:
      Time = timeout()

name:start/0
def:start() -> 'ok'

name:start_link/0
def:start_link() -> {'ok', pid()} | {'error', term()}

name:tc/1
def:tc(Fun) -> {Time, Value}
types:
      Fun = function(),
      Time = integer(),
      Value = term()

name:tc/2
def:tc(Fun, Arguments) -> {Time, Value}
types:
      Fun = function(),
      Arguments = [term()],
      Time = integer(),
      Value = term()

name:tc/3
def:tc(Module, Function, Arguments) -> {Time, Value}
types:
      Module = module(),
      Function = atom(),
      Arguments = [term()],
      Time = integer(),
      Value = term()

name:terminate/2
def:terminate(term(), _State) -> 'ok'

