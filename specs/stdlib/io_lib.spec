name:char_list/1
def:char_list(Term) -> boolean()
types:
      Term = term()

name:deep_char_list/1
def:deep_char_list(Term) -> boolean()
types:
      Term = term()

name:deep_unicode_char_list/1
def:deep_unicode_char_list(term()) -> boolean()

name:format/2
def:format(Format, Data) -> chars() | UnicodeList
types:
      Format = io:format(),
      Data = [term()],
      UnicodeList = [unicode:unicode_char()]

name:format_prompt/1
def:format_prompt(term()) -> chars()

name:fread/2
def:fread(Format, String) -> Result
types:
      Format = string(),
      String = string(),
      Result = {'ok', InputList = [term()], LeftOverChars = string()}
              | {'more', RestFormat = string(),
                 Nchars = non_neg_integer(),
                 InputStack = chars()}
              | {'error', What = term()}

name:fread/3
def:fread(Continuation, CharSpec, Format) -> Return
types:
      Continuation = continuation() | [],
      CharSpec = string() | eof,
      Format = string(),
      Return = {'more', Continuation1 = continuation()}
              | {'done', Result, LeftOverChars = string()},
      Result = {'ok', InputList = [term()]}
              | 'eof'
              | {'error', What = term()}

name:fwrite/2
def:fwrite(Format, Data) -> chars() | UnicodeList
types:
      Format = io:format(),
      Data = [term()],
      UnicodeList = [unicode:unicode_char()],
      Data = [term()]

name:indentation/2
def:indentation(String, StartIndent) -> integer()
types:
      String = string(),
      StartIndent = integer()

name:nl/0
def:nl() -> string()

name:print/1
def:print(Term) -> chars()
types:
      Term = term()

name:print/4
def:print(Term, Column, LineLength, Depth) -> chars()
types:
      Term = term(),
      Column = non_neg_integer(),
      LineLength = non_neg_integer(),
      Depth = depth()

name:printable_list/1
def:printable_list(Term) -> boolean()
types:
      Term = term()

name:printable_unicode_list/1
def:printable_unicode_list(term()) -> boolean()

name:quote_atom/2
def:quote_atom(atom(), chars()) -> boolean()

name:unicode_char_list/1
def:unicode_char_list(term()) -> boolean()

name:write/1
def:write(Term) -> chars()
types:
      Term = term()

name:write/3
def:write(term(), depth(), boolean()) -> chars()

name:write/2
def:write(Term, Depth) -> chars()
types:
      Term = term(),
      Depth = depth()

name:write_atom/1
def:write_atom(Atom) -> chars()
types:
      Atom = atom()

name:write_char/1
def:write_char(Char) -> chars()
types:
      Char = char()

name:write_string/1
def:write_string(String) -> chars()
types:
      String = string()

name:write_string/2
def:write_string(string(), char()) -> chars()

