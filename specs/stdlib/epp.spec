name:close/1
def:close(Epp) -> 'ok'
types:
      Epp = epp_handle()

name:format_error/1
def:format_error(ErrorDescriptor) -> io_lib:chars()
types:
      ErrorDescriptor = term()

name:open/2
def:open(FileName, IncludePath) ->
	{'ok', Epp} | {'error', ErrorDescriptor}
types:
      FileName = file:name(),
      IncludePath = [DirectoryName = file:name()],
      Epp = epp_handle(),
      ErrorDescriptor = term()

name:open/3
def:open(FileName, IncludePath, PredefMacros) ->
	{'ok', Epp} | {'error', ErrorDescriptor}
types:
      FileName = file:name(),
      IncludePath = [DirectoryName = file:name()],
      PredefMacros = macros(),
      Epp = epp_handle(),
      ErrorDescriptor = term()

name:parse_erl_form/1
def:parse_erl_form(Epp) ->
        {'ok', AbsForm} | {'eof', Line} | {error, ErrorInfo}
types:
      Epp = epp_handle(),
      AbsForm = erl_parse:abstract_form(),
      Line = erl_scan:line(),
      ErrorInfo = erl_scan:error_info() | erl_parse:error_info()

name:parse_file/3
def:parse_file(FileName, IncludePath, PredefMacros) ->
                {'ok', [Form]} | {error, OpenError}
types:
      FileName = file:name(),
      IncludePath = [DirectoryName = file:name()],
      Form = erl_parse:abstract_form() | {'error', ErrorInfo} | {'eof',Line},
      PredefMacros = macros(),
      Line = erl_scan:line(),
      ErrorInfo = erl_scan:error_info() | erl_parse:error_info(),
      OpenError = file:posix() | badarg | system_limit

