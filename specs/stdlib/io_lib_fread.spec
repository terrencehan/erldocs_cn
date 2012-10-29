name:fread/3
def:fread(Continuation, String, Format) -> Return
types:
      Continuation = io_lib:continuation() |  [],
      String = string(),
      Format = string(),
      Return = {'more', Continuation1 = io_lib:continuation()}
              | {'done', Result, LeftOverChars = string()},
      Result = {'ok', InputList = io_lib:chars()}
              | 'eof'
              | {'error', What = term()}

name:fread/2
def:fread(Format, String) -> Result
types:
      Format = string(),
      String = string(),
      Result = {'ok', InputList = io_lib:chars(), LeftOverChars = string()}
              | {'more', RestFormat = string(),
                 Nchars = non_neg_integer(),
                 InputStack = io_lib:chars()}
              | {'error', What = term()}

