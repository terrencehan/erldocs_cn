name:replace/3
def:replace(Subject, RE, Replacement) -> iodata() | unicode:charlist()
types:
      Subject = iodata() | unicode:charlist(),
      RE = mp() | iodata(),
      Replacement = iodata() | unicode:charlist()

name:replace/4
def:replace(Subject, RE, Replacement, Options) -> iodata() | unicode:charlist()
types:
      Subject = iodata() | unicode:charlist(),
      RE = mp() | iodata() | unicode:charlist(),
      Replacement = iodata() | unicode:charlist(),
      Options = [Option],
      Option = anchored | global | notbol | noteol | notempty
              | {offset, non_neg_integer()} | {newline, NLSpec} | bsr_anycrlf
              | bsr_unicode | {return, ReturnType} | CompileOpt,
      ReturnType = iodata | list | binary,
      CompileOpt = compile_option(),
      NLSpec = cr | crlf | lf | anycrlf | any

name:split/2
def:split(Subject, RE) -> SplitList
types:
      Subject = iodata() | unicode:charlist(),
      RE = mp() | iodata(),
      SplitList = [iodata() | unicode:charlist()]

name:split/3
def:split(Subject, RE, Options) -> SplitList
types:
      Subject = iodata() | unicode:charlist(),
      RE = mp() | iodata() | unicode:charlist(),
      Options = [ Option ],
      Option = anchored | notbol | noteol | notempty
              | {offset, non_neg_integer()} | {newline, nl_spec()}
              | bsr_anycrlf | bsr_unicode | {return, ReturnType}
              | {parts, NumParts} | group | trim | CompileOpt,
      NumParts = non_neg_integer() | infinity,
      ReturnType = iodata | list | binary,
      CompileOpt = compile_option(),
      SplitList = [RetData] | [GroupedRetData],
      GroupedRetData = [RetData],
      RetData = iodata() | unicode:charlist() | binary() | list()

