name:accessible_logs/0
def:accessible_logs() -> {[LocalLog], [DistributedLog]}
types:
      LocalLog = log(),
      DistributedLog = log()

name:alog/2
def:alog(Log, Term) -> notify_ret()
types:
      Log = log(),
      Term = term()

name:alog_terms/2
def:alog_terms(Log, TermList) -> notify_ret()
types:
      Log = log(),
      TermList = [term()]

name:balog/2
def:balog(Log, Bytes) -> notify_ret()
types:
      Log = log(),
      Bytes = bytes()

name:balog_terms/2
def:balog_terms(Log, ByteList) -> notify_ret()
types:
      Log = log(),
      ByteList = [bytes()]

name:bchunk/2
def:bchunk(Log, Continuation) -> bchunk_ret()
types:
      Log = log(),
      Continuation = start | continuation()

name:bchunk/3
def:bchunk(Log, Continuation, N) -> bchunk_ret()
types:
      Log = log(),
      Continuation = start | continuation(),
      N = pos_integer() | infinity

name:block/1
def:block(Log) -> 'ok' | {'error', block_error_rsn()}
types:
      Log = log()

name:block/2
def:block(Log, QueueLogRecords) -> 'ok' | {'error', block_error_rsn()}
types:
      Log = log(),
      QueueLogRecords = boolean()

name:blog/2
def:blog(Log, Bytes) -> ok | {error, Reason :: log_error_rsn()}
types:
      Log = log(),
      Bytes = bytes()

name:blog_terms/2
def:blog_terms(Log, BytesList) ->
                        ok | {error, Reason :: log_error_rsn()}
types:
      Log = log(),
      BytesList = [bytes()]

name:breopen/3
def:breopen(Log, File, BHead) -> 'ok' | {'error', reopen_error_rsn()}
types:
      Log = log(),
      File = file:filename(),
      BHead = bytes()

name:btruncate/2
def:btruncate(Log, BHead) -> 'ok' | {'error', trunc_error_rsn()}
types:
      Log = log(),
      BHead = bytes()

name:change_header/2
def:change_header(Log, Header) -> 'ok' | {'error', Reason}
types:
      Log = log(),
      Header = {head, dlog_head_opt()}
              | {head_func, MFA = {atom(), atom(), list()}},
      Reason = no_such_log | nonode | {read_only_mode, Log}
              | {blocked_log, Log} | {badarg, head}

name:change_notify/3
def:change_notify(Log, Owner, Notify) -> 'ok' | {'error', Reason}
types:
      Log = log(),
      Owner = pid(),
      Notify = boolean(),
      Reason = no_such_log | nonode | {blocked_log, Log}
              | {badarg, notify} | {not_owner, Owner}

name:change_size/2
def:change_size(Log, Size) -> 'ok' | {'error', Reason}
types:
      Log = log(),
      Size = dlog_size(),
      Reason = no_such_log | nonode | {read_only_mode, Log}
              | {blocked_log, Log}
              | {new_size_too_small, CurrentSize = pos_integer()}
              | {badarg, size}
              | {file_error, file:filename(), file_error()}

name:chunk/2
def:chunk(Log, Continuation) -> chunk_ret()
types:
      Log = log(),
      Continuation = start | continuation()

name:chunk/3
def:chunk(Log, Continuation, N) -> chunk_ret()
types:
      Log = log(),
      Continuation = start | continuation(),
      N = pos_integer() | infinity

name:chunk_info/1
def:chunk_info(Continuation) -> InfoList | {error, Reason}
types:
      Continuation = continuation(),
      InfoList = [{node, Node = node()}, ...],
      Reason = {no_continuation, Continuation}

name:chunk_step/3
def:chunk_step(Log, Continuation, Step) ->
                        {'ok', any()} | {'error', Reason}
types:
      Log = log(),
      Continuation = start | continuation(),
      Step = integer(),
      Reason = no_such_log | end_of_log | {format_external, Log}
              | {blocked_log, Log}  | {badarg, continuation}
              | {file_error, file:filename(), file_error()}

name:close/1
def:close(Log) -> 'ok' | {'error', close_error_rsn()}
types:
      Log = log()

name:close_disk_log2/1
def:close_disk_log2(#log{}) -> 'closed'. % | throw(Error)

close_disk_log2(L) ->
    case L of
	#log{format_type = halt_int, mode = Mode, extra = Halt} ->
	    disk_log_1:close(Halt#halt.fdc, L#log.filename, Mode);
	#log{format_type = wrap_int, mode = Mode, extra = Handle} ->
	    disk_log_1:mf_int_close(Handle, Mode);
	#log{format_type = halt_ext, extra = Halt} ->
	    disk_log_1:fclose(Halt#halt.fdc, L#log.filename);
	#log{format_type = wrap_ext, mode = Mode, extra = Handle} ->
	    disk_log_1:mf_ext_close(Handle, Mode)
    end,
    closed

name:compare_arg/6
def:compare_arg(dlog_options(), #arg{}, 
compare_arg([], _A, none, _OrigHead) ->
    % no header option given
    ok;
compare_arg([], _A, Head, OrigHead)
types: Head =/= OrigHead ->
    {error, {arg_mismatch, head, OrigHead, Head}};
compare_arg([], _A, _Head, _OrigHead) ->
    ok;
compare_arg([{Attr, Val} | Tail], A, Head, OrigHead) ->
    case compare_arg(Attr, Val, A) of
	{not_ok, OrigVal} -> 
	    {error, {arg_mismatch, Attr, OrigVal, Val}};
	ok -> 
	    compare_arg(Tail, A, Head, OrigHead);
	Error -> 
	    Error
    end

name:compare_arg/3
def:compare_arg(atom(), _, #arg{}) ->
	     'ok' | {'not_ok', _} | {'error', {atom(), _}}

name:do_exit/4
def:do_exit(#state{}, pid(), _, _) -> no_return()

name:do_fast_exit/3
def:do_fast_exit(#state{}, pid(), _) -> no_return()

name:do_log/2
def:do_log(#log{}, [binary()]) -> integer() | {'error', _, integer()}

name:format_error/1
def:format_error(Error) -> io_lib:chars()
types:
      Error = term()

name:get_near_pid/3
def:get_near_pid([pid(),...], node()) -> pid()

name:inc_wrap_file/1
def:inc_wrap_file(Log) -> 'ok' | {'error', inc_wrap_error_rsn()}
types:
      Log = log()

name:info/1
def:info(Log) -> InfoList | {'error', no_such_log}
types:
      Log = log(),
      InfoList = [dlog_info()]

name:lclose/1
def:lclose(Log) -> 'ok' | {'error', lclose_error_rsn()}
types:
      Log = log()

name:lclose/2
def:lclose(Log, Node) -> 'ok' | {'error', lclose_error_rsn()}
types:
      Log = log(),
      Node = node()

name:ll_open/1
def:ll_open(dlog_options()) -> {'ok', Res :: _, #log{}, Cnt :: _} | Error

name:log/2
def:log(Log, Term) -> ok | {error, Reason :: log_error_rsn()}
types:
      Log = log(),
      Term = term()

name:log_terms/2
def:log_terms(Log, TermList) -> ok | {error, Resaon :: log_error_rsn()}
types:
      Log = log(),
      TermList = [term()]

name:open/1
def:open(ArgL) -> open_ret() | dist_open_ret()
types:
      ArgL = dlog_options()

name:pid2name/1
def:pid2name(Pid) -> {'ok', Log} | 'undefined'
types:
      Pid = pid(),
      Log = log()

name:reopen/2
def:reopen(Log, File) -> 'ok' | {'error', reopen_error_rsn()}
types:
      Log = log(),
      File = file:filename()

name:reopen/3
def:reopen(Log, File, Head) -> 'ok' | {'error', reopen_error_rsn()}
types:
      Log = log(),
      File = file:filename(),
      Head = term()

name:start/0
def:start() -> 'ok'

name:state_err/2
def:state_err(#state{}, dlog_state_error()) -> #state{}

name:sync/1
def:sync(Log) -> 'ok' | {'error', sync_error_rsn()}
types:
      Log = log()

name:system_terminate/4
def:system_terminate(_, _, _, #state{}) -> no_return()

name:truncate/1
def:truncate(Log) -> 'ok' | {'error', trunc_error_rsn()}
types:
      Log = log()

name:truncate/2
def:truncate(Log, Head) -> 'ok' | {'error', trunc_error_rsn()}
types:
      Log = log(),
      Head = term()

name:unblock/1
def:unblock(Log) -> 'ok' | {'error', unblock_error_rsn()}
types:
      Log = log()

