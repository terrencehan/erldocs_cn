name:all/0
def:all() -> [tab_name()]

name:bchunk/2
def:bchunk(Name, Continuation) ->
    {Continuation2, Data} | '$end_of_table' | {'error', Reason}
types:
      Name = tab_name(),
      Continuation = 'start' | cont(),
      Continuation2 = cont(),
      Data = binary() | tuple(),
      Reason = term()

name:close/1
def:close(Name) -> 'ok' | {'error', Reason}
types:
      Name = tab_name(),
      Reason = term()

name:delete/2
def:delete(Name, Key) -> 'ok' | {'error', Reason}
types:
      Name = tab_name(),
      Key = term(),
      Reason = term()

name:delete_all_objects/1
def:delete_all_objects(Name) -> 'ok' | {'error', Reason}
types:
      Name = tab_name(),
      Reason = term()

name:delete_object/2
def:delete_object(Name, Object) -> 'ok' | {'error', Reason}
types:
      Name = tab_name(),
      Object = object(),
      Reason = term()

name:first/1
def:first(Name) -> Key | '$end_of_table'
types:
      Name = tab_name(),
      Key = term()

name:foldl/3
def:foldl(Function, Acc0, Name) -> Acc | {'error', Reason}
types:
      Name = tab_name(),
      Function = fun((Object = object(), AccIn) -> AccOut),
      Acc0 = term(),
      Acc = term(),
      AccIn = term(),
      AccOut = term(),
      Reason = term()

name:foldr/3
def:foldr(Function, Acc0, Name) -> Acc | {'error', Reason}
types:
      Name = tab_name(),
      Function = fun((Object = object(), AccIn) -> AccOut),
      Acc0 = term(),
      Acc = term(),
      AccIn = term(),
      AccOut = term(),
      Reason = term()

name:from_ets/2
def:from_ets(Name, EtsTab) -> 'ok' | {'error', Reason}
types:
      Name = tab_name(),
      EtsTab = ets:tab(),
      Reason = term()

name:info/1
def:info(Name) -> InfoList | 'undefined'
types:
      Name = tab_name(),
      InfoList = [InfoTuple],
      InfoTuple = {'file_size', non_neg_integer()}
                 | {'filename', file:name()}
                 | {'keypos', keypos()}
                 | {'size', non_neg_integer()}
                 | {'type', type()}

name:info/2
def:info(Name, Item) -> Value | 'undefined'
types:
      Name = tab_name(),
      Item = 'access' | 'auto_save' | 'bchunk_format'
            | 'hash' | 'file_size' | 'filename' | 'keypos' | 'memory'
            | 'no_keys' | 'no_objects' | 'no_slots' | 'owner' | 'ram_file'
            | 'safe_fixed' | 'size' | 'type' | 'version',
      Value = term()

name:init_table/2
def:init_table(Name, InitFun) -> ok | {'error', Reason}
types:
      Name = tab_name(),
      InitFun = fun((Arg) -> Res),
      Arg = read | close,
      Res = end_of_input | {[object()], InitFun} | {Data, InitFun} | term(),
      Reason = term(),
      Data = binary() | tuple()

name:init_table/3
def:init_table(Name, InitFun, Options) -> ok | {'error', Reason}
types:
      Name = tab_name(),
      InitFun = fun((Arg) -> Res),
      Arg = read | close,
      Res = end_of_input | {[object()], InitFun} | {Data, InitFun} | term(),
      Options = Option | [Option],
      Option = {min_no_slots,no_slots()} | {format,term | bchunk},
      Reason = term(),
      Data = binary() | tuple()

name:insert/2
def:insert(Name, Objects) -> 'ok' | {'error', Reason}
types:
      Name = tab_name(),
      Objects = object() | [object()],
      Reason = term()

name:insert_new/2
def:insert_new(Name, Objects) -> boolean()
types:
      Name = tab_name(),
      Objects = object() | [object()]

name:is_compatible_bchunk_format/2
def:is_compatible_bchunk_format(Name, BchunkFormat) -> boolean()
types:
      Name = tab_name(),
      BchunkFormat = binary()

name:is_dets_file/1
def:is_dets_file(Filename) -> boolean() | {'error', Reason}
types:
      Filename = file:name(),
      Reason = term()

name:lookup/2
def:lookup(Name, Key) -> Objects | {'error', Reason}
types:
      Name = tab_name(),
      Key = term(),
      Objects = [object()],
      Reason = term()

name:match/2
def:match(Name, Pattern) -> [Match] | {'error', Reason}
types:
      Name = tab_name(),
      Pattern = pattern(),
      Match = [term()],
      Reason = term()

name:match/3
def:match(Name, Pattern, N) ->
          {[Match], Continuation} | '$end_of_table' | {'error', Reason}
types:
      Name = tab_name(),
      Pattern = pattern(),
      N = 'default' | non_neg_integer(),
      Continuation = bindings_cont(),
      Match = [term()],
      Reason = term()

name:match/1
def:match(Continuation) ->
          {[Match], Continuation2} | '$end_of_table' | {'error', Reason}
types:
      Continuation = bindings_cont(),
      Continuation2 = bindings_cont(),
      Match = [term()],
      Reason = term()

name:match_delete/2
def:match_delete(Name, Pattern) -> 'ok' | {'error', Reason}
types:
      Name = tab_name(),
      Pattern = pattern(),
      Reason = term()

name:match_object/2
def:match_object(Name, Pattern) -> Objects | {'error', Reason}
types:
      Name = tab_name(),
      Pattern = pattern(),
      Objects = [object()],
      Reason = term()

name:match_object/3
def:match_object(Name, Pattern, N) ->
           {Objects, Continuation} | '$end_of_table' | {'error', Reason}
types:
      Name = tab_name(),
      Pattern = pattern(),
      N = 'default' | non_neg_integer(),
      Continuation = object_cont(),
      Objects = [object()],
      Reason = term()

name:match_object/1
def:match_object(Continuation) ->
           {Objects, Continuation2} | '$end_of_table' | {'error', Reason}
types:
      Continuation = object_cont(),
      Continuation2 = object_cont(),
      Objects = [object()],
      Reason = term()

name:member/2
def:member(Name, Key) -> boolean() | {'error', Reason}
types:
      Name = tab_name(),
      Key = term(),
      Reason = term()

name:next/2
def:next(Name, Key1) -> Key2 | '$end_of_table'
types:
      Name = tab_name(),
      Key1 = term(),
      Key2 = term()

name:open_file/1
def:open_file(Filename) -> {'ok', Reference} | {'error', Reason}
types:
      Filename = file:name(),
      Reference = reference(),
      Reason = term()

name:open_file/2
def:open_file(Name, Args) -> {'ok', Name} | {'error', Reason}
types:
      Name = tab_name(),
      Args = [OpenArg],
      OpenArg  = {'access', access()}
                | {'auto_save', auto_save()}
                | {'estimated_no_objects', non_neg_integer()}
                | {'file', file:name()}
                | {'max_no_slots', no_slots()}
                | {'min_no_slots', no_slots()}
                | {'keypos', keypos()}
                | {'ram_file', boolean()}
                | {'repair', boolean() | 'force'}
                | {'type', type()}
                | {'version', version()},
      Reason = term()

name:pid2name/1
def:pid2name(Pid) -> {'ok', Name} | 'undefined'
types:
      Pid = pid(),
      Name = tab_name()

name:repair_continuation/2
def:repair_continuation(Continuation, MatchSpec) -> Continuation2
types:
      Continuation = select_cont(),
      Continuation2 = select_cont(),
      MatchSpec = match_spec()

name:safe_fixtable/2
def:safe_fixtable(Name, Fix) -> 'ok'
types:
      Name = tab_name(),
      Fix = boolean()

name:select/2
def:select(Name, MatchSpec) -> Selection | {'error', Reason}
types:
      Name = tab_name(),
      MatchSpec = match_spec(),
      Selection = [term()],
      Reason = term()

name:select/3
def:select(Name, MatchSpec, N) ->
          {Selection, Continuation} | '$end_of_table' | {'error', Reason}
types:
      Name = tab_name(),
      MatchSpec = match_spec(),
      N = 'default' | non_neg_integer(),
      Continuation = select_cont(),
      Selection = [term()],
      Reason = term()

name:select/1
def:select(Continuation) ->
          {Selection, Continuation2} | '$end_of_table' | {'error', Reason}
types:
      Continuation = select_cont(),
      Continuation2 = select_cont(),
      Selection = [term()],
      Reason = term()

name:select_delete/2
def:select_delete(Name, MatchSpec) -> N | {'error', Reason}
types:
      Name = tab_name(),
      MatchSpec = match_spec(),
      N = non_neg_integer(),
      Reason = term()

name:slot/2
def:slot(Name, I) -> '$end_of_table' | Objects | {'error', Reason}
types:
      Name = tab_name(),
      I = non_neg_integer(),
      Objects = [object()],
      Reason = term()

name:sync/1
def:sync(Name) -> 'ok' | {'error', Reason}
types:
      Name = tab_name(),
      Reason = term()

name:table/1
def:table(Name) -> QueryHandle
types:
      Name = tab_name(),
      QueryHandle = qlc:query_handle()

name:table/2
def:table(Name, Options) -> QueryHandle
types:
      Name = tab_name(),
      Options = Option | [Option],
      Option = {'n_objects', Limit}
              | {'traverse', TraverseMethod},
      Limit = 'default' | pos_integer(),
      TraverseMethod = 'first_next' | 'select' | {'select', match_spec()},
      QueryHandle = qlc:query_handle()

name:to_ets/2
def:to_ets(Name, EtsTab) -> EtsTab | {'error', Reason}
types:
      Name = tab_name(),
      EtsTab = ets:tab(),
      Reason = term()

name:traverse/2
def:traverse(Name, Fun) -> Return | {'error', Reason}
types:
      Name = tab_name(),
      Fun = fun((Object) -> FunReturn),
      Object = object(),
      FunReturn = 'continue'
                 | {'continue', Val}
                 | {'done', Value}
                 | OtherValue,
      Return = [term()] | OtherValue,
      Val = term(),
      Value = term(),
      OtherValue = term(),
      Reason = term()

name:update_counter/3
def:update_counter(Name, Key, Increment) -> Result
types:
      Name = tab_name(),
      Key = term(),
      Increment = {Pos, Incr} | Incr,
      Pos = integer(),
      Incr = integer(),
      Result = integer()

