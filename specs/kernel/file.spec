name:advise/4
def:advise(IoDevice, Offset, Length, Advise) -> ok | {error, Reason}
types:
      IoDevice = io_device(),
      Offset = integer(),
      Length = integer(),
      Advise = posix_file_advise(),
      Reason = posix() | badarg

name:altname/1
def:altname(Name :: name()) -> any()

name:change_group/2
def:change_group(Filename, Gid) -> ok | {error, Reason}
types:
      Filename = name(),
      Gid = integer(),
      Reason = posix() | badarg

name:change_mode/2
def:change_mode(Filename, Mode) -> ok | {error, Reason}
types:
      Filename = name(),
      Mode = integer(),
      Reason = posix() | badarg

name:change_owner/2
def:change_owner(Filename, Uid) -> ok | {error, Reason}
types:
      Filename = name(),
      Uid = integer(),
      Reason = posix() | badarg

name:change_owner/3
def:change_owner(Filename, Uid, Gid) -> ok | {error, Reason}
types:
      Filename = name(),
      Uid = integer(),
      Gid = integer(),
      Reason = posix() | badarg

name:change_time/2
def:change_time(Filename, Mtime) -> ok | {error, Reason}
types:
      Filename = name(),
      Mtime = date_time(),
      Reason = posix() | badarg

name:change_time/3
def:change_time(Filename, Atime, Mtime) -> ok | {error, Reason}
types:
      Filename = name(),
      Atime = date_time(),
      Mtime = date_time(),
      Reason = posix() | badarg

name:close/1
def:close(IoDevice) -> ok | {error, Reason}
types:
      IoDevice = io_device(),
      Reason = posix() | badarg | terminated

name:consult/1
def:consult(Filename) -> {ok, Terms} | {error, Reason}
types:
      Filename = name(),
      Terms = [term()],
      Reason = posix() | badarg | terminated | system_limit
              | {Line = integer(), Mod = module(), Term = term()}

name:copy/2
def:copy(Source, Destination) -> {ok, BytesCopied} | {error, Reason}
types:
      Source = io_device() | Filename | {Filename, Modes},
      Destination = io_device() | Filename | {Filename, Modes},
      Filename = name(),
      Modes = [mode()],
      BytesCopied = non_neg_integer(),
      Reason = posix() | badarg | terminated

name:copy/3
def:copy(Source, Destination, ByteCount) ->
             {ok, BytesCopied} | {error, Reason}
types:
      Source = io_device() | Filename | {Filename, Modes},
      Destination = io_device() | Filename | {Filename, Modes},
      Filename = name(),
      Modes = [mode()],
      ByteCount = non_neg_integer() | infinity,
      BytesCopied = non_neg_integer(),
      Reason = posix() | badarg | terminated

name:datasync/1
def:datasync(IoDevice) -> ok | {error, Reason}
types:
      IoDevice = io_device(),
      Reason = posix() | badarg | terminated

name:del_dir/1
def:del_dir(Dir) -> ok | {error, Reason}
types:
      Dir = name(),
      Reason = posix() | badarg

name:delete/1
def:delete(Filename) -> ok | {error, Reason}
types:
      Filename = name(),
      Reason = posix() | badarg

name:eval/1
def:eval(Filename) -> ok | {error, Reason}
types:
      Filename = name(),
      Reason = posix() | badarg | terminated | system_limit
              | {Line = integer(), Mod = module(), Term = term()}

name:eval/2
def:eval(Filename, Bindings) -> ok | {error, Reason}
types:
      Filename = name(),
      Bindings = erl_eval:binding_struct(),
      Reason = posix() | badarg | terminated | system_limit
              | {Line = integer(), Mod = module(), Term = term()}

name:format_error/1
def:format_error(Reason) -> Chars
types:
      Reason = posix() | badarg | terminated | system_limit
              | {Line = integer(), Mod = module(), Term = term()},
      Chars = string()

name:get_cwd/0
def:get_cwd() -> {ok, Dir} | {error, Reason}
types:
      Dir = filename(),
      Reason = posix()

name:get_cwd/1
def:get_cwd(Drive) -> {ok, Dir} | {error, Reason}
types:
      Drive = string(),
      Dir = filename(),
      Reason = posix() | badarg

name:list_dir/1
def:list_dir(Dir) -> {ok, Filenames} | {error, Reason}
types:
      Dir = name(),
      Filenames = [filename()],
      Reason = posix() | badarg

name:make_dir/1
def:make_dir(Dir) -> ok | {error, Reason}
types:
      Dir = name(),
      Reason = posix() | badarg

name:make_link/2
def:make_link(Existing, New) -> ok | {error, Reason}
types:
      Existing = name(),
      New = name(),
      Reason = posix() | badarg

name:make_symlink/2
def:make_symlink(Existing, New) -> ok | {error, Reason}
types:
      Existing = name(),
      New = name(),
      Reason = posix() | badarg

name:open/2
def:open(Filename, Modes) -> {ok, IoDevice} | {error, Reason}
types:
      Filename = name(),
      Modes = [mode()],
      IoDevice = io_device(),
      Reason = posix() | badarg | system_limit

name:path_consult/2
def:path_consult(Path, Filename) -> {ok, Terms, FullName} | {error, Reason}
types:
      Path = [Dir],
      Dir = name(),
      Filename = name(),
      Terms = [term()],
      FullName = filename(),
      Reason = posix() | badarg | terminated | system_limit
              | {Line = integer(), Mod = module(), Term = term()}

name:path_eval/2
def:path_eval(Path, Filename) -> {ok, FullName} | {error, Reason}
types:
      Path = [Dir = name()],
      Filename = name(),
      FullName = filename(),
      Reason = posix() | badarg | terminated | system_limit
              | {Line = integer(), Mod = module(), Term = term()}

name:path_eval/3
def:path_eval(Path, Filename, Bindings) ->
             {ok, FullName} | {error, Reason}
types:
      Path = [Dir = name()],
      Filename = name(),
      Bindings = erl_eval:binding_struct(),
      FullName = filename(),
      Reason = posix() | badarg | terminated | system_limit
              | {Line = integer(), Mod = module(), Term = term()}

name:path_open/3
def:path_open(Path, Filename, Modes) ->
             {ok, IoDevice, FullName} | {error, Reason}
types:
      Path = [Dir = name()],
      Filename = name(),
      Modes = [mode()],
      IoDevice = io_device(),
      FullName = filename(),
      Reason = posix() | badarg | system_limit

name:path_script/2
def:path_script(Path, Filename) ->
             {ok, Value, FullName} | {error, Reason}
types:
      Path = [Dir = name()],
      Filename = name(),
      Value = term(),
      FullName = filename(),
      Reason = posix() | badarg | terminated | system_limit
              | {Line = integer(), Mod = module(), Term = term()}

name:path_script/3
def:path_script(Path, Filename, Bindings) ->
          {ok, Value, FullName} | {error, Reason}
types:
      Path = [Dir = name()],
      Filename = name(),
      Bindings = erl_eval:binding_struct(),
      Value = term(),
      FullName = filename(),
      Reason = posix() | badarg | terminated | system_limit
              | {Line = integer(), Mod = module(), Term = term()}

name:pid2name/1
def:pid2name(Pid) -> {ok, Filename} | undefined
types:
      Filename = filename(),
      Pid = pid()

name:position/2
def:position(IoDevice, Location) -> {ok, NewPosition} | {error, Reason}
types:
      IoDevice = io_device(),
      Location = location(),
      NewPosition = integer(),
      Reason = posix() | badarg | terminated

name:pread/2
def:pread(IoDevice, LocNums) -> {ok, DataL} | eof | {error, Reason}
types:
      IoDevice = io_device(),
      LocNums = [{Location = location(), Number = non_neg_integer()}],
      DataL = [Data],
      Data = string() | binary() | eof,
      Reason = posix() | badarg | terminated

name:pread/3
def:pread(IoDevice, Location, Number) ->
             {ok, Data} | eof | {error, Reason}
types:
      IoDevice = io_device(),
      Location = location(),
      Number = non_neg_integer(),
      Data = string() | binary(),
      Reason = posix() | badarg | terminated

name:pwrite/2
def:pwrite(IoDevice, LocBytes) -> ok | {error, {N, Reason}}
types:
      IoDevice = io_device(),
      LocBytes = [{Location = location(), Bytes = iodata()}],
      N = non_neg_integer(),
      Reason = posix() | badarg | terminated

name:pwrite/3
def:pwrite(IoDevice, Location, Bytes) -> ok | {error, Reason}
types:
      IoDevice = io_device(),
      Location = location(),
      Bytes = iodata(),
      Reason = posix() | badarg | terminated

name:read/2
def:read(IoDevice, Number) -> {ok, Data} | eof | {error, Reason}
types:
      IoDevice = io_device() | atom(),
      Number = non_neg_integer(),
      Data = string() | binary(),
      Reason = posix() | badarg | terminated

name:read_file/1
def:read_file(Filename) -> {ok, Binary} | {error, Reason}
types:
      Filename = name(),
      Binary = binary(),
      Reason = posix() | badarg | terminated | system_limit

name:read_file_info/1
def:read_file_info(Filename) -> {ok, FileInfo} | {error, Reason}
types:
      Filename = name(),
      FileInfo = file_info(),
      Reason = posix() | badarg

name:read_file_info/2
def:read_file_info(Filename, Opts) -> {ok, FileInfo} | {error, Reason}
types:
      Filename = name(),
      Opts = [file_info_option()],
      FileInfo = file_info(),
      Reason = posix() | badarg

name:read_line/1
def:read_line(IoDevice) -> {ok, Data} | eof | {error, Reason}
types:
      IoDevice = io_device() | atom(),
      Data = string() | binary(),
      Reason = posix() | badarg | terminated

name:read_link/1
def:read_link(Name) -> {ok, Filename} | {error, Reason}
types:
      Name = name(),
      Filename = filename(),
      Reason = posix() | badarg

name:read_link_info/1
def:read_link_info(Name) -> {ok, FileInfo} | {error, Reason}
types:
      Name = name(),
      FileInfo = file_info(),
      Reason = posix() | badarg

name:read_link_info/2
def:read_link_info(Name, Opts) -> {ok, FileInfo} | {error, Reason}
types:
      Name = name(),
      Opts = [file_info_option()],
      FileInfo = file_info(),
      Reason = posix() | badarg

name:rename/2
def:rename(Source, Destination) -> ok | {error, Reason}
types:
      Source = name(),
      Destination = name(),
      Reason = posix() | badarg

name:script/1
def:script(Filename) -> {ok, Value} | {error, Reason}
types:
      Filename = name(),
      Value = term(),
      Reason = posix() | badarg | terminated | system_limit
              | {Line = integer(), Mod = module(), Term = term()}

name:script/2
def:script(Filename, Bindings) -> {ok, Value} | {error, Reason}
types:
      Filename = name(),
      Bindings = erl_eval:binding_struct(),
      Value = term(),
      Reason = posix() | badarg | terminated | system_limit
              | {Line = integer(), Mod = module(), Term = term()}

name:sendfile/5
def:sendfile(RawFile, Socket, Offset, Bytes, Opts) ->
   {'ok', non_neg_integer()} | {'error', inet:posix() | 
				closed | badarg | not_owner}
types:
      RawFile = file:fd(),
      Socket = inet:socket(),
      Offset = non_neg_integer(),
      Bytes = non_neg_integer(),
      Opts = [sendfile_option()]

name:sendfile/2
def:sendfile(Filename, Socket) ->
   {'ok', non_neg_integer()} | {'error', inet:posix() | 
				closed | badarg | not_owner}
types: Filename = file:name(),
	   Socket = inet:socket()

name:set_cwd/1
def:set_cwd(Dir) -> ok | {error, Reason}
types:
      Dir = name(),
      Reason = posix() | badarg

name:sync/1
def:sync(IoDevice) -> ok | {error, Reason}
types:
      IoDevice = io_device(),
      Reason = posix() | badarg | terminated

name:truncate/1
def:truncate(IoDevice) -> ok | {error, Reason}
types:
      IoDevice = io_device(),
      Reason = posix() | badarg | terminated

name:write/2
def:write(IoDevice, Bytes) -> ok | {error, Reason}
types:
      IoDevice = io_device() | atom(),
      Bytes = iodata(),
      Reason = posix() | badarg | terminated

name:write_file/2
def:write_file(Filename, Bytes) -> ok | {error, Reason}
types:
      Filename = name(),
      Bytes = iodata(),
      Reason = posix() | badarg | terminated | system_limit

name:write_file/3
def:write_file(Filename, Bytes, Modes) -> ok | {error, Reason}
types:
      Filename = name(),
      Bytes = iodata(),
      Modes = [mode()],
      Reason = posix() | badarg | terminated | system_limit

name:write_file_info/2
def:write_file_info(Filename, FileInfo) -> ok | {error, Reason}
types:
      Filename = name(),
      FileInfo = file_info(),
      Reason = posix() | badarg

name:write_file_info/3
def:write_file_info(Filename, FileInfo, Opts) -> ok | {error, Reason}
types:
      Filename = name(),
      Opts = [file_info_option()],
      FileInfo = file_info(),
      Reason = posix() | badarg

