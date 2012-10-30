name:create/2
def:create(Name, FileList) -> RetValue
types:
      Name     = file:name(),
      FileList = [FileSpec],
      FileSpec = file:name() | {file:name(), binary()}
                | {file:name(), binary(), file:file_info()},
      RetValue = {ok, FileName = file:name()}
                | {ok, {FileName = file:name(), binary()}}
                | {error, Reason = term()})

name:create/3
def:create(Name, FileList, Options) -> RetValue
types:
      Name     = file:name(),
      FileList = [FileSpec],
      FileSpec = file:name() | {file:name(), binary()}
                | {file:name(), binary(), file:file_info()},
      Options  = [Option],
      Option   = memory | cooked | verbose | {comment, Comment}
                | {cwd, CWD} | {compress, What} | {uncompress, What},
      What     = all | [Extension] | {add, [Extension]} | {del, [Extension]},
      Extension = string(),
      Comment  = string(),
      CWD      = string(),
      RetValue = {ok, FileName = file:name()}
                | {ok, {FileName = file:name(), binary()}}
                | {error, Reason = term()})

name:extract/1
def:extract(Archive) -> RetValue
types:
      Archive = file:name() | binary(),
      RetValue = {ok, FileList}
                | {ok, FileBinList}
                | {error, Reason = term()}
                | {error, {Name = file:name(), Reason = term()}},
      FileList = [file:name()],
      FileBinList = [{file:name(),binary()}])

name:extract/2
def:extract(Archive, Options) -> RetValue
types:
      Archive = file:name() | binary(),
      Options = [Option],
      Option  = {file_list, FileList}
               | keep_old_files | verbose | memory |
                 {file_filter, FileFilter} | {cwd, CWD},
      FileList = [file:name()],
      FileBinList = [{file:name(),binary()}],
      FileFilter = fun((ZipFile) -> boolean()),
      CWD = string(),
      ZipFile = zip_file(),
      RetValue = {ok, FileList}
                | {ok, FileBinList}
                | {error, Reason = term()}
                | {error, {Name = file:name(), Reason = term()}})

name:foldl/3
def:foldl(Fun, Acc0, Archive) -> {ok, Acc1} | {error, Reason}
types:
      Fun = fun((FileInArchive, GetInfo, GetBin, AccIn) -> AccOut),
      FileInArchive = file:name(),
      GetInfo = fun(() -> file:file_info()),
      GetBin = fun(() -> binary()),
      Acc0 = term(),
      Acc1 = term(),
      AccIn = term(),
      AccOut = term(),
      Archive = file:name() | {file:name(), binary()},
      Reason = term()

name:list_dir/1
def:list_dir(Archive) -> RetValue
types:
      Archive = file:name() | binary(),
      RetValue = {ok, CommentAndFiles} | {error, Reason = term()},
      CommentAndFiles = [zip_comment() | zip_file()])

name:list_dir/2
def:list_dir(Archive, Options) -> RetValue
types:
      Archive = file:name() | binary(),
      RetValue = {ok, CommentAndFiles} | {error, Reason = term()},
      CommentAndFiles = [zip_comment() | zip_file()],
      Options = [Option],
      Option = cooked)

name:t/1
def:t(Archive) -> ok
types:
      Archive = file:name() | binary() | ZipHandle,
      ZipHandle = pid()

name:table/1
def:table(Archive) -> RetValue
types:
      Archive = file:name() | binary(),
      RetValue = {ok, CommentAndFiles} | {error, Reason = term()},
      CommentAndFiles = [zip_comment() | zip_file()])

name:table/2
def:table(Archive, Options) -> RetValue
types:
      Archive = file:name() | binary(),
      RetValue = {ok, CommentAndFiles} | {error, Reason = term()},
      CommentAndFiles = [zip_comment() | zip_file()],

      Options = [Option],
      Option = cooked)

name:tt/1
def:tt(Archive) -> ok
types:
      Archive = file:name() | binary() | ZipHandle,
      ZipHandle = pid()

name:unzip/1
def:unzip(Archive) -> RetValue
types:
      Archive = file:name() | binary(),
      RetValue = {ok, FileList}
                | {ok, FileBinList}
                | {error, Reason = term()}
                | {error, {Name = file:name(), Reason = term()}},
      FileList = [file:name()],
      FileBinList = [{file:name(),binary()}])

name:unzip/2
def:unzip(Archive, Options) -> RetValue
types:
      Archive = file:name() | binary(),
      Options = [Option],
      Option  = {file_list, FileList}
               | keep_old_files | verbose | memory |
                 {file_filter, FileFilter} | {cwd, CWD},
      FileList = [file:name()],
      FileBinList = [{file:name(),binary()}],
      FileFilter = fun((ZipFile) -> boolean()),
      CWD = string(),
      ZipFile = zip_file(),
      RetValue = {ok, FileList}
                | {ok, FileBinList}
                | {error, Reason = term()}
                | {error, {Name = file:name(), Reason = term()}})

name:zip/2
def:zip(Name, FileList) -> RetValue
types:
      Name     = file:name(),
      FileList = [FileSpec],
      FileSpec = file:name() | {file:name(), binary()}
                | {file:name(), binary(), file:file_info()},
      RetValue = {ok, FileName = file:name()}
                | {ok, {FileName = file:name(), binary()}}
                | {error, Reason = term()})

name:zip/3
def:zip(Name, FileList, Options) -> RetValue
types:
      Name     = file:name(),
      FileList = [FileSpec],
      FileSpec = file:name() | {file:name(), binary()}
                | {file:name(), binary(), file:file_info()},
      Options  = [Option],
      Option   = memory | cooked | verbose | {comment, Comment}
                | {cwd, CWD} | {compress, What} | {uncompress, What},
      What     = all | [Extension] | {add, [Extension]} | {del, [Extension]},
      Extension = string(),
      Comment  = string(),
      CWD      = string(),
      RetValue = {ok, FileName = file:name()}
                | {ok, {FileName = file:name(), binary()}}
                | {error, Reason = term()})

name:zip_close/1
def:zip_close(ZipHandle) -> ok | {error, einval}
types:
      ZipHandle = pid()

name:zip_get/1
def:zip_get(ZipHandle) -> {ok, [Result]} | {error, Reason}
types:
      ZipHandle = pid(),
      Result = file:name() | {file:name(), binary()},
      Reason = term()

name:zip_get/2
def:zip_get(FileName, ZipHandle) -> {ok, Result} | {error, Reason}
types:
      FileName = file:name(),
      ZipHandle = pid(),
      Result = file:name() | {file:name(), binary()},
      Reason = term()

name:zip_list_dir/1
def:zip_list_dir(ZipHandle) -> {ok, Result} | {error, Reason}
types:
      Result = [zip_comment() | zip_file()],
      ZipHandle = pid(),
      Reason = term()

name:zip_open/1
def:zip_open(Archive) -> {ok, ZipHandle} | {error, Reason}
types:
      Archive = file:name() | binary(),
      ZipHandle = pid(),
      Reason = term()

name:zip_open/2
def:zip_open(Archive, Options) -> {ok, ZipHandle} | {error, Reason}
types:
      Archive = file:name() | binary(),
      ZipHandle = pid(),
      Options = [Option],
      Option = cooked | memory | {cwd, CWD = string()},
      Reason = term()

