name:add_report_handler/1
def:add_report_handler(Handler) -> any()
types:
      Handler = module()

name:add_report_handler/2
def:add_report_handler(Handler, Args) -> Result
types:
      Handler = module(),
      Args = gen_event:handler_args(),
      Result = gen_event:add_handler_ret()

name:delete_report_handler/1
def:delete_report_handler(Handler) -> Result
types:
      Handler = module(),
      Result = gen_event:del_handler_ret()

name:error_info/1
def:error_info(Error :: any()) -> 'ok'

name:error_msg/1
def:error_msg(Format) -> 'ok'
types:
      Format = string()

name:error_msg/2
def:error_msg(Format, Data) -> 'ok'
types:
      Format = string(),
      Data = list()

name:error_report/1
def:error_report(Report) -> 'ok'
types:
      Report = report()

name:error_report/2
def:error_report(Type, Report) -> 'ok'
types:
      Type = term(),
      Report = report()

name:format/2
def:format(Format, Data) -> 'ok'
types:
      Format = string(),
      Data = list()

name:handle_call/2
def:handle_call(term(), state()) -> {'ok', {'error', 'bad_query'}, state()}

name:handle_event/2
def:handle_event(term(), state()) -> {'ok', state()}

name:handle_info/2
def:handle_info(term(), state()) -> {'ok', state()}

name:info_msg/1
def:info_msg(Format) -> 'ok'
types:
      Format = string()

name:info_msg/2
def:info_msg(Format, Data) -> 'ok'
types:
      Format = string(),
      Data = list()

name:info_report/1
def:info_report(Report) -> 'ok'
types:
      Report = report()

name:info_report/2
def:info_report(Type, Report) -> 'ok'
types:
      Type = any(),
      Report = report()

name:init/1
def:init(term()) -> {'ok', state() | []}

name:logfile/2
def:logfile(Request :: {open, Filename}) -> ok | {error, OpenReason}
types:
                  Filename =file:name(),
                  OpenReason = allready_have_logfile | open_error()
           ; (Request = close) -> ok | {error, CloseReason} when
                  CloseReason = module_not_found
	   ; (Request = filename) -> Filename | {error, FilenameReason} when
                  Filename = file:name(),
                  FilenameReason = no_log_file

name:notify/5
def:notify({msg_tag(), pid(), {pid(), any(), any()}}) -> 'ok'

name:start/0
def:start() -> {'ok', pid()} | {'error', any()}

name:start_link/0
def:start_link() -> {'ok', pid()} | {'error', any()}

name:swap_handler/1
def:swap_handler(Type :: swap_handler_type()) -> any()

name:terminate/2
def:terminate(term(), state()) -> {'error_logger', [term()]}

name:tty/1
def:tty(Flag) -> 'ok'
types:
      Flag = boolean()

name:warning_msg/1
def:warning_msg(Format) -> 'ok'
types:
      Format = string()

name:warning_msg/2
def:warning_msg(Format, Data) -> 'ok'
types:
      Format = string(),
      Data = list()

name:warning_report/1
def:warning_report(Report) -> 'ok'
types:
      Report = report()

name:warning_report/2
def:warning_report(Type, Report) -> 'ok'
types:
      Type = any(),
      Report = report()

