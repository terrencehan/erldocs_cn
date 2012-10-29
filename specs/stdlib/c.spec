name:bt/1
def:bt(Pid) -> 'ok' | 'undefined'
types:
      Pid = pid()

name:c/1
def:c(File) -> {'ok', Module} | 'error'
types:
      File = file:name(),
      Module = module()

name:c/2
def:c(File, Options) -> {'ok', Module} | 'error'
types:
      File = file:name(),
      Options = [compile:option()],
      Module = module()

name:cd/1
def:cd(Dir) -> 'ok'
types:
      Dir = file:name()

name:flush/0
def:flush() -> 'ok'

name:help/0
def:help() -> 'ok'

name:i/0
def:i() -> 'ok'

name:i/1
def:i([pid()]) -> 'ok'

name:i/2
def:i([pid()], non_neg_integer()) -> 'ok'

name:i/3
def:i(X, Y, Z) -> [{atom(), term()}]
types:
      X = non_neg_integer(),
      Y = non_neg_integer(),
      Z = non_neg_integer()

name:l/1
def:l(Module) -> code:load_ret()
types:
      Module = module()

name:lc/1
def:lc(Files) -> 'ok' | 'error'
types:
      Files = [File = erl_compile:cmd_line_arg()]

name:lc_batch/0
def:lc_batch() -> no_return()

name:lc_batch/1
def:lc_batch([erl_compile:cmd_line_arg()]) -> no_return()

name:ls/0
def:ls() -> 'ok'

name:ls/1
def:ls(Dir) -> 'ok'
types:
      Dir = file:name()

name:m/0
def:m() -> 'ok'

name:m/1
def:m(Module) -> 'ok'
types:
      Module = module()

name:memory/0
def:memory() -> [{Type, Size}]
types:
      Type = atom(),
      Size = non_neg_integer()

name:memory/1
def:memory(Type) -> Size
types:
               Type = atom(),
               Size = non_neg_integer()
          ; (Types) -> [{Type, Size}] when
               Types = [Type],
               Type = atom(),
               Size = non_neg_integer()

name:nc/1
def:nc(File) -> {'ok', Module} | 'error'
types:
      File = file:name(),
      Module = module()

name:nc/2
def:nc(File, Options) -> {'ok', Module} | 'error'
types:
      File = file:name(),
      Options = [Option] | Option,
      Option= compile:option(),
      Module = module()

name:ni/0
def:ni() -> 'ok'

name:nl/1
def:nl(Module) -> abcast | error
types:
      Module = module()

name:nregs/0
def:nregs() -> 'ok'

name:outdir/1
def:outdir([compile:option()]) -> file:filename()

name:pid/3
def:pid(X, Y, Z) -> pid()
types:
      X = non_neg_integer(),
      Y = non_neg_integer(),
      Z = non_neg_integer()

name:pwd/0
def:pwd() -> 'ok'

name:q/0
def:q() -> no_return()

name:regs/0
def:regs() -> 'ok'

name:xm/1
def:xm(module() | file:filename()) -> xref:m/1 return
xm(M) ->
    appcall(tools, xref, m, [M])

name:y/1
def:y(file:name()) -> yecc:file/2 return
y(File) -> y(File, [])

name:y/2
def:y(file:name(), [yecc:option()]) -> yecc:file/2 return
y(File, Opts) ->
    appcall(parsetools, yecc, file, [File, Opts])

