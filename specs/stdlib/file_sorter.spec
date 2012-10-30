name:check/1
def:check(FileName) -> Reply
types:
      FileName = file_name(),
      Reply = {ok, [Result]} | {error, reason()},
      Result = {FileName, TermPosition, term()},
      TermPosition = pos_integer()

name:check/2
def:check(FileNames, Options) -> Reply
types:
      FileNames = file_names(),
      Options = options(),
      Reply = {ok, [Result]} | {error, reason()},
      Result = {FileName, TermPosition, term()},
      FileName = file_name(),
      TermPosition = pos_integer()

name:file_error/4
def:file_error(_, {'error',atom()}, #w{}) -> no_return()

name:keycheck/2
def:keycheck(KeyPos, FileName) -> Reply
types:
      KeyPos = key_pos(),
      FileName = file_name(),
      Reply = {ok, [Result]} | {error, reason()},
      Result = {FileName, TermPosition, term()},
      TermPosition = pos_integer()

name:keycheck/3
def:keycheck(KeyPos, FileNames, Options) -> Reply
types:
      KeyPos = key_pos(),
      FileNames = file_names(),
      Options = options(),
      Reply = {ok, [Result]} | {error, reason()},
      Result = {FileName, TermPosition, term()},
      FileName = file_name(),
      TermPosition = pos_integer()

name:keymerge/3
def:keymerge(KeyPos, FileNames, Output) -> Reply
types:
      KeyPos = key_pos(),
      FileNames = file_names(),
      Output = output(),
      Reply = ok | {error, reason()} | output_reply()

name:keymerge/4
def:keymerge(KeyPos, FileNames, Output, Options) -> Reply
types:
      KeyPos = key_pos(),
      FileNames = file_names(),
      Output = output(),
      Options = options(),
      Reply = ok | {error, reason()} | output_reply()

name:keysort/2
def:keysort(KeyPos, FileName) -> Reply
types:
      KeyPos = key_pos(),
      FileName = file_name(),
      Reply = ok | {error, reason()} | input_reply() | output_reply()

name:keysort/3
def:keysort(KeyPos, Input, Output) -> Reply
types:
      KeyPos = key_pos(),
      Input = input(),
      Output = output(),
      Reply = ok | {error, reason()} | input_reply() | output_reply()

name:keysort/4
def:keysort(KeyPos, Input, Output, Options) -> Reply
types:
      KeyPos = key_pos(),
      Input = input(),
      Output = output(),
      Options = options(),
      Reply = ok | {error, reason()} | input_reply() | output_reply()

name:merge/2
def:merge(FileNames, Output) -> Reply
types:
      FileNames = file_names(),
      Output = output(),
      Reply = ok | {error, reason()} | output_reply()

name:merge/3
def:merge(FileNames, Output, Options) -> Reply
types:
      FileNames = file_names(),
      Output = output(),
      Options = options(),
      Reply = ok | {error, reason()} | output_reply()

name:sort/1
def:sort(FileName) -> Reply
types:
      FileName = file_name(),
      Reply = ok | {error, reason()} | input_reply() | output_reply()

name:sort/2
def:sort(Input, Output) -> Reply
types:
      Input = input(),
      Output = output(),
      Reply = ok | {error, reason()} | input_reply() | output_reply()

name:sort/3
def:sort(Input, Output, Options) -> Reply
types:
      Input = input(),
      Output = output(),
      Options = options(),
      Reply = ok | {error, reason()} | input_reply() | output_reply()

