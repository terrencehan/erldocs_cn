name:columns/0
def:columns() -> {'ok', pos_integer()} | {'error', 'enotsup'}

name:columns/1
def:columns(IoDevice) -> {'ok', pos_integer()} | {'error', 'enotsup'}
types:
      IoDevice = device()

name:format/1
def:format(Format) -> 'ok'
types:
      Format = format()

name:format/2
def:format(Format, Data) -> 'ok'
types:
      Format = format(),
      Data = [term()]

name:format/3
def:format(IoDevice, Format, Data) -> 'ok'
types:
      IoDevice = device(),
      Format = format(),
      Data = [term()]

name:fread/2
def:fread(Prompt, Format) -> Result
types:
      Prompt = prompt(),
      Format = format(),
      Result = {'ok', Terms = [term()]} | 'eof' | {'error', What = term()}

name:fread/3
def:fread(IoDevice, Prompt, Format) -> Result
types:
      IoDevice = device(),
      Prompt = prompt(),
      Format = format(),
      Result = {'ok', Terms = [term()]} | 'eof' | {'error', What = term()}

name:fwrite/1
def:fwrite(Format) -> 'ok'
types:
      Format = format()

name:fwrite/2
def:fwrite(Format, Data) -> 'ok'
types:
      Format = format(),
      Data = [term()]

name:fwrite/3
def:fwrite(IoDevice, Format, Data) -> 'ok'
types:
      IoDevice = device(),
      Format = format(),
      Data = [term()]

name:get_chars/2
def:get_chars(Prompt, Count) -> Data | 'eof'
types:
      Prompt = prompt(),
      Count = non_neg_integer(),
      Data = [unicode:unicode_char()] | unicode:unicode_binary()

name:get_chars/3
def:get_chars(IoDevice, Prompt, Count) -> Data | 'eof' | {error, Reason}
types:
      IoDevice = device(),
      Prompt = prompt(),
      Count = non_neg_integer(),
      Reason = term(),
      Data = [unicode:unicode_char()] | unicode:unicode_binary()

name:get_line/1
def:get_line(Prompt) -> Data | 'eof' | {'error', Reason}
types:
      Prompt = prompt(),
      Reason = term(),
      Data = [unicode:unicode_char()] | unicode:unicode_binary()

name:get_line/2
def:get_line(IoDevice, Prompt) -> Data | 'eof' | {'error', term()}
types:
      IoDevice = device(),
      Prompt = prompt(),
      Data = [unicode:unicode_char()] | unicode:unicode_binary()

name:getopts/0
def:getopts() -> [opt_pair()]

name:getopts/1
def:getopts(IoDevice) -> [opt_pair()]
types:
      IoDevice = device()

name:nl/0
def:nl() -> 'ok'

name:nl/1
def:nl(IoDevice) -> 'ok'
types:
      IoDevice = device()

name:parse_erl_exprs/1
def:parse_erl_exprs(Prompt) -> Result
types:
      Prompt = prompt(),
      Result = parse_ret()

name:parse_erl_exprs/2
def:parse_erl_exprs(IoDevice, Prompt) -> Result
types:
      IoDevice = device(),
      Prompt = prompt(),
      Result = parse_ret()

name:parse_erl_exprs/3
def:parse_erl_exprs(IoDevice, Prompt, StartLine) -> Result
types:
      IoDevice = device(),
      Prompt = prompt(),
      StartLine = line(),
      Result = parse_ret()

name:parse_erl_form/1
def:parse_erl_form(Prompt) -> Result
types:
      Prompt = prompt(),
      Result = parse_form_ret()

name:parse_erl_form/2
def:parse_erl_form(IoDevice, Prompt) -> Result
types:
      IoDevice = device(),
      Prompt = prompt(),
      Result = parse_form_ret()

name:parse_erl_form/3
def:parse_erl_form(IoDevice, Prompt, StartLine) -> Result
types:
      IoDevice = device(),
      Prompt = prompt(),
      StartLine = line(),
      Result = parse_form_ret()

name:put_chars/1
def:put_chars(CharData) -> 'ok'
types:
      CharData = unicode:chardata()

name:put_chars/2
def:put_chars(IoDevice, IoData) -> 'ok'
types:
      IoDevice = device(),
      IoData = unicode:chardata()

name:read/1
def:read(Prompt) -> Result
types:
      Prompt = prompt(),
      Result = {'ok', Term = term()}
              | 'eof'
              | {'error', ErrorInfo = erl_scan:error_info()}

name:read/2
def:read(IoDevice, Prompt) -> Result
types:
      IoDevice = device(),
      Prompt = prompt(),
      Result = {'ok', Term = term()}
              | 'eof'
              | {'error', ErrorInfo = erl_scan:error_info()}

name:read/3
def:read(IoDevice, Prompt, StartLine) -> Result
types:
      IoDevice = device(),
      Prompt = prompt(),
      StartLine = line(),
      Result = {'ok', Term = term(), EndLine = line()}
              | {'eof', EndLine = line()}
              | {'error', ErrorInfo = erl_scan:error_info(), ErrorLine = line()}

name:rows/0
def:rows() -> {'ok', pos_integer()} | {'error', 'enotsup'}

name:rows/1
def:rows(IoDevice) -> {'ok', pos_integer()} | {'error', 'enotsup'}
types:
      IoDevice = device()

name:scan_erl_exprs/1
def:scan_erl_exprs(Prompt) -> Result
types:
      Prompt = prompt(),
      Result = erl_scan:tokens_result() | request_error()

name:scan_erl_exprs/2
def:scan_erl_exprs(Device, Prompt) -> Result
types:
      Device = device(),
      Prompt = prompt(),
      Result = erl_scan:tokens_result() | request_error()

name:scan_erl_exprs/3
def:scan_erl_exprs(Device, Prompt, StartLine) -> Result
types:
      Device = device(),
      Prompt = prompt(),
      StartLine = line(),
      Result = erl_scan:tokens_result() | request_error()

name:scan_erl_form/1
def:scan_erl_form(Prompt) -> Result
types:
      Prompt = prompt(),
      Result = erl_scan:tokens_result() | request_error()

name:scan_erl_form/2
def:scan_erl_form(IoDevice, Prompt) -> Result
types:
      IoDevice = device(),
      Prompt = prompt(),
      Result = erl_scan:tokens_result() | request_error()

name:scan_erl_form/3
def:scan_erl_form(IoDevice, Prompt, StartLine) -> Result
types:
      IoDevice = device(),
      Prompt = prompt(),
      StartLine = line(),
      Result = erl_scan:tokens_result() | request_error()

name:setopts/1
def:setopts(Opts) -> 'ok' | {'error', Reason}
types:
      Opts = [setopt()],
      Reason = term()

name:setopts/2
def:setopts(IoDevice, Opts) -> 'ok' | {'error', Reason}
types:
      IoDevice = device(),
      Opts = [setopt()],
      Reason = term()

name:write/1
def:write(Term) -> 'ok'
types:
      Term = term()

name:write/2
def:write(IoDevice, Term) -> 'ok'
types:
      IoDevice = device(),
      Term = term()

