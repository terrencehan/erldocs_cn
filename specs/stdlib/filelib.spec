name:ensure_dir/1
def:ensure_dir(Name) -> 'ok' | {'error', Reason}
types:
      Name = filename() | dirname(),
      Reason = file:posix()

name:file_size/1
def:file_size(Filename) -> non_neg_integer()
types:
      Filename = filename()

name:file_size/2
def:file_size(file:name(), atom()) -> non_neg_integer()

name:fold_files/5
def:fold_files(Dir, RegExp, Recursive, Fun, AccIn) -> AccOut
types:
      Dir = dirname(),
      RegExp = string(),
      Recursive = boolean(),
      Fun = fun((F = file:filename(), AccIn) -> AccOut),
      AccIn = term(),
      AccOut = term()

name:fold_files/5
def:fold_files(file:name(), string(), boolean(), fun((_,_) -> _), _, atom()) -> _

name:is_dir/1
def:is_dir(Name) -> boolean()
types:
      Name = filename() | dirname()

name:is_dir/2
def:is_dir(file:name(), atom()) -> boolean()

name:is_file/1
def:is_file(Name) -> boolean()
types:
      Name = filename() | dirname()

name:is_file/2
def:is_file(file:name(), atom()) -> boolean()

name:is_regular/1
def:is_regular(Name) -> boolean()
types:
      Name = filename()

name:is_regular/2
def:is_regular(file:name(), atom()) -> boolean()

name:last_modified/1
def:last_modified(Name) -> file:date_time() | 0
types:
      Name = filename() | dirname()

name:last_modified/2
def:last_modified(file:name(), atom()) -> file:date_time() | 0

name:wildcard/1
def:wildcard(Wildcard) -> [file:filename()]
types:
      Wildcard = filename() | dirname()

name:wildcard/2
def:wildcard(Wildcard, Cwd) -> [file:filename()]
types:
      Wildcard = filename() | dirname(),
      Cwd = dirname()

name:wildcard/3
def:wildcard(file:name(), file:name(), atom()) -> [file:filename()]

