name:change_code/4
def:change_code(Name, Module, OldVsn, Extra) -> 'ok' | {error, Reason}
types:
      Name = name(),
      Module = module(),
      OldVsn = 'undefined' | term(),
      Extra = term(),
      Reason = term()

name:change_code/5
def:change_code(Name, Module, OldVsn, Extra, Timeout) ->
                         'ok' | {error, Reason}
types:
      Name = name(),
      Module = module(),
      OldVsn = 'undefined' | term(),
      Extra = term(),
      Timeout = timeout(),
      Reason = term()

name:debug_options/1
def:debug_options(Options) -> [dbg_opt()]
types:
      Options = [Opt],
      Opt = 'trace' | 'log' | 'statistics' | {'log_to_file', FileName}
           | {'install', FuncSpec},
      FileName = file:name(),
      FuncSpec = {Func, FuncState},
      Func = dbg_fun(),
      FuncState = term()

name:get_debug/3
def:get_debug(Item, Debug, Default) -> term()
types:
      Item = 'log' | 'statistics',
      Debug = [dbg_opt()],
      Default = term()

name:get_status/1
def:get_status(Name) -> Status
types:
      Name = name(),
      Status = {status, Pid = pid(), {module, Module = module()}, [SItem]},
      SItem = (PDict = [{Key = term(), Value = term()}])
             | (SysState = 'running' | 'suspended')
             | (Parent = pid())
             | (Dbg = dbg_opt())
             | (Misc = term()

name:get_status/2
def:get_status(Name, Timeout) -> Status
types:
      Name = name(),
      Timeout = timeout(),
      Status = {status, Pid = pid(), {module, Module = module()}, [SItem]},
      SItem = (PDict = [{Key = term(), Value = term()}])
             | (SysState = 'running' | 'suspended')
             | (Parent = pid())
             | (Dbg = dbg_opt())
             | (Misc = term()

name:handle_debug/4
def:handle_debug(Debug, FormFunc, Extra, Event) -> [dbg_opt()]
types:
      Debug = [dbg_opt()],
      FormFunc = dbg_fun(),
      Extra = term(),
      Event = system_event()

name:handle_system_msg/6
def:handle_system_msg(Msg, From, Parent, Module, Debug, Misc) -> Void
types:
      Msg = term(),
      From = {pid(), Tag = _},
      Parent = pid(),
      Module = module(),
      Debug = [dbg_opt()],
      Misc = term(),
      Void = term()

name:install/2
def:install(Name, FuncSpec) -> Void
types:
      Name = name(),
      FuncSpec = {Func, FuncState},
      Func = dbg_fun(),
      FuncState = term(),
      Void = term()

name:install/3
def:install(Name, FuncSpec, Timeout) -> Void
types:
      Name = name(),
      FuncSpec = {Func, FuncState},
      Func = dbg_fun(),
      FuncState = term(),
      Timeout = timeout(),
      Void = term()

name:log/2
def:log(Name, Flag) -> 'ok' | {'ok', [system_event()]}
types:
      Name = name(),
      Flag = 'true' |
              {'true', N = pos_integer()}
            | 'false' | 'get' | 'print'

name:log/3
def:log(Name, Flag, Timeout) -> 'ok' | {'ok', [system_event()]}
types:
      Name = name(),
      Flag = 'true' |
              {'true', N = pos_integer()}
            | 'false' | 'get' | 'print',
      Timeout = timeout()

name:log_to_file/2
def:log_to_file(Name, Flag) -> 'ok' | {'error','open_file'}
types:
      Name = name(),
      Flag = (FileName = string()) | 'false'

name:log_to_file/3
def:log_to_file(Name, Flag, Timeout) -> 'ok' | {'error','open_file'}
types:
      Name = name(),
      Flag = (FileName = string()) | 'false',
      Timeout = timeout()

name:no_debug/1
def:no_debug(Name) -> 'ok'
types:
      Name = name()

name:no_debug/2
def:no_debug(Name, Timeout) -> 'ok'
types:
      Name = name(),
      Timeout = timeout()

name:print_log/1
def:print_log(Debug) -> Void
types:
      Debug = [dbg_opt()],
      Void = term()

name:remove/2
def:remove(Name, Func) -> Void
types:
      Name = name(),
      Func = dbg_fun(),
      Void = term()

name:remove/3
def:remove(Name, Func, Timeout) -> Void
types:
      Name = name(),
      Func = dbg_fun(),
      Timeout = timeout(),
      Void = term()

name:resume/1
def:resume(Name) -> Void
types:
      Name = name(),
      Void = term()

name:resume/2
def:resume(Name, Timeout) -> Void
types:
      Name = name(),
      Timeout = timeout(),
      Void = term()

name:statistics/2
def:statistics(Name, Flag) -> 'ok' | {'ok', Statistics}
types:
      Name = name(),
      Flag = 'true' | 'false' | 'get',
      Statistics = [StatisticsTuple] | no_statistics,
      StatisticsTuple = {'start_time', DateTime1}
                       | {'current_time', DateTime2}
                       | {'reductions', non_neg_integer()}
                       | {'messages_in', non_neg_integer()}
                       | {'messages_out', non_neg_integer()},
      DateTime1 = file:date_time(),
      DateTime2 = file:date_time()

name:statistics/3
def:statistics(Name, Flag, Timeout) -> 'ok' | {'ok', Statistics}
types:
      Name = name(),
      Flag = 'true' | 'false' | 'get',
      Statistics = [StatisticsTuple] | no_statistics,
      StatisticsTuple = {'start_time', DateTime1}
                       | {'current_time', DateTime2}
                       | {'reductions', non_neg_integer()}
                       | {'messages_in', non_neg_integer()}
                       | {'messages_out', non_neg_integer()},
      DateTime1 = file:date_time(),
      DateTime2 = file:date_time(),
      Timeout = timeout()

name:suspend/1
def:suspend(Name) -> Void
types:
      Name = name(),
      Void = term()

name:suspend/2
def:suspend(Name, Timeout) -> Void
types:
      Name = name(),
      Timeout = timeout(),
      Void = term()

name:trace/2
def:trace(Name, Flag) -> 'ok'
types:
      Name = name(),
      Flag = boolean()

name:trace/3
def:trace(Name, Flag, Timeout) -> 'ok'
types:
      Name = name(),
      Flag = boolean(),
      Timeout = timeout()

