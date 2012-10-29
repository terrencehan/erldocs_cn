name:file2tab/1
def:file2tab(Filename) -> {'ok', Tab} | {'error', Reason}
types:
      Filename = file:name(),
      Tab = tab(),
      Reason = term()

name:file2tab/2
def:file2tab(Filename, Options) -> {'ok', Tab} | {'error', Reason}
types:
      Filename = file:name(),
      Tab = tab(),
      Options = [Option],
      Option = {'verify', boolean()},
      Reason = term()

name:filter/3
def:filter(tab(), function(), [term()]) -> [term()]

name:foldl/3
def:foldl(Function, Acc0, Tab) -> Acc1
types:
      Function = fun((Element = term(), AccIn) -> AccOut),
      Tab = tab(),
      Acc0 = term(),
      Acc1 = term(),
      AccIn = term(),
      AccOut = term()

name:foldr/3
def:foldr(Function, Acc0, Tab) -> Acc1
types:
      Function = fun((Element = term(), AccIn) -> AccOut),
      Tab = tab(),
      Acc0 = term(),
      Acc1 = term(),
      AccIn = term(),
      AccOut = term()

name:from_dets/2
def:from_dets(Tab, DetsTab) -> 'true'
types:
      Tab = tab(),
      DetsTab = dets:tab_name()

name:fun2ms/1
def:fun2ms(LiteralFun) -> MatchSpec
types:
      LiteralFun = function(),
      MatchSpec = match_spec()

name:i/0
def:i() -> 'ok'

name:i/1
def:i(Tab) -> 'ok'
types:
      Tab = tab()

name:i/2
def:i(tab(), pos_integer()) -> 'ok'

name:i/3
def:i(tab(), pos_integer(), pos_integer()) -> 'ok'

name:init_table/2
def:init_table(Tab, InitFun) -> 'true'
types:
      Tab = tab(),
      InitFun = fun((Arg) -> Res),
      Arg = 'read' | 'close',
      Res = 'end_of_input' | {Objects = [term()], InitFun} | term()

name:match_delete/2
def:match_delete(Tab, Pattern) -> 'true'
types:
      Tab = tab(),
      Pattern = match_pattern()

name:match_spec_run/2
def:match_spec_run([tuple()], comp_match_spec()) -> [term()]

name:repair_continuation/2
def:repair_continuation(Continuation, MatchSpec) -> Continuation
types:
      Continuation = continuation(),
      MatchSpec = match_spec()

name:tab2file/2
def:tab2file(Tab, Filename) -> 'ok' | {'error', Reason}
types:
      Tab = tab(),
      Filename = file:name(),
      Reason = term()

name:tab2file/3
def:tab2file(Tab, Filename, Options) -> 'ok' | {'error', Reason}
types:
      Tab = tab(),
      Filename = file:name(),
      Options = [Option],
      Option = {'extended_info', [ExtInfo]},
      ExtInfo = 'md5sum' | 'object_count',
      Reason = term()

name:tab2list/1
def:tab2list(Tab) -> [Object]
types:
      Tab = tab(),
      Object = tuple()

name:tabfile_info/1
def:tabfile_info(Filename) -> {'ok', TableInfo} | {'error', Reason}
types:
      Filename = file:name(),
      TableInfo = [InfoItem],
      InfoItem = {'name', atom()}
                | {'type', Type}
                | {'protection', Protection}
                | {'named_table', boolean()}
                | {'keypos', non_neg_integer()}
                | {'size', non_neg_integer()}
                | {'extended_info', [ExtInfo]}
                | {'version', {Major = non_neg_integer(),
                               Minor = non_neg_integer()}},
      ExtInfo = 'md5sum' | 'object_count',
      Type = 'bag' | 'duplicate_bag' | 'ordered_set' | 'set',
      Protection = 'private' | 'protected' | 'public',
      Reason = term()

name:table/1
def:table(Tab) -> QueryHandle
types:
      Tab = tab(),
      QueryHandle = qlc:query_handle()

name:table/2
def:table(Tab, Options) -> QueryHandle
types:
      Tab = tab(),
      QueryHandle = qlc:query_handle(),
      Options = [Option] | Option,
      Option = {'n_objects', NObjects}
              | {'traverse', TraverseMethod},
      NObjects = 'default' | pos_integer(),
      TraverseMethod = 'first_next' | 'last_prev'
                      | 'select' | {'select', MatchSpec = match_spec()}

name:test_ms/2
def:test_ms(Tuple, MatchSpec) -> {'ok', Result} | {'error', Errors}
types:
      Tuple = tuple(),
      MatchSpec = match_spec(),
      Result = term(),
      Errors = [{'warning'|'error', string()}]

name:to_dets/2
def:to_dets(Tab, DetsTab) -> DetsTab
types:
      Tab = tab(),
      DetsTab = dets:tab_name()

