name:error_message/2
def:error_message(Format, Args) -> 'ok'
types:
      Format = io:format(),
      Args = [term()]

name:eval_str/1
def:eval_str(string() | binary()) -> {'ok', string()} | {'error', string()}

name:flush_receive/0
def:flush_receive() -> 'ok'

name:nonl/1
def:nonl(String1) -> String2
types:
      String1 = string(),
      String2 = string()

name:progname/0
def:progname() -> atom()

name:send/2
def:send(To, Msg) -> Msg
types:
      To = pid() | atom() | {atom(), node()},
      Msg = term()

name:sendw/2
def:sendw(To, Msg) -> Msg
types:
      To = pid() | atom() | {atom(), node()},
      Msg = term()

