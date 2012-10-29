name:absname/1
def:absname(Filename) -> file:filename()
types:
      Filename = file:name()

name:absname/2
def:absname(Filename, Dir) -> file:filename()
types:
      Filename = file:name(),
      Dir = file:filename()

name:absname_join/2
def:absname_join(Dir, Filename) -> file:filename()
types:
      Dir = file:filename(),
      Filename = file:name()

name:append/2
def:append(file:filename(), file:name()) -> file:filename()

name:basename/1
def:basename(Filename) -> file:filename()
types:
      Filename = file:name()

name:basename/2
def:basename(Filename, Ext) -> file:filename()
types:
      Filename = file:name(),
      Ext = file:name()

name:dirname/1
def:dirname(Filename) -> file:filename()
types:
      Filename = file:name()

name:extension/1
def:extension(Filename) -> file:filename()
types:
      Filename = file:name()

name:find_src/1
def:find_src(Beam) -> {SourceFile, Options}
                      | {error, {ErrorReason, Module}}
types:
      Beam = Module | Filename,
      Filename = atom() | string(),
      Module = module(),
      SourceFile = string(),
      Options = [Option],
      Option = {'i', Path = string()}
              | {'outdir', Path = string()}
              | {'d', atom()},
      ErrorReason = 'non_existing' | 'preloaded' | 'interpreted'

name:find_src/2
def:find_src(Beam, Rules) -> {SourceFile, Options}
                             | {error, {ErrorReason, Module}}
types:
      Beam = Module | Filename,
      Filename = atom() | string(),
      Rules = [{BinSuffix = string(), SourceSuffix = string()}],
      Module = module(),
      SourceFile = string(),
      Options = [Option],
      Option = {'i', Path = string()}
              | {'outdir', Path = string()}
              | {'d', atom()},
      ErrorReason = 'non_existing' | 'preloaded' | 'interpreted'

name:flatten/1
def:flatten(Filename) -> file:filename()
types:
      Filename = file:name()

name:join/1
def:join(Components) -> file:filename()
types:
      Components = [file:filename()]

name:join/2
def:join(Name1, Name2) -> file:filename()
types:
      Name1 = file:filename(),
      Name2 = file:filename()

name:nativename/1
def:nativename(Path) -> file:filename()
types:
      Path = file:filename()

name:pathtype/1
def:pathtype(Path) -> 'absolute' | 'relative' | 'volumerelative'
types:
      Path = file:name()

name:rootname/1
def:rootname(Filename) -> file:filename()
types:
      Filename = file:name()

name:rootname/2
def:rootname(Filename, Ext) -> file:filename()
types:
      Filename = file:name(),
      Ext = file:name()

name:split/1
def:split(Filename) -> Components
types:
      Filename = file:name(),
      Components = [file:filename()]

