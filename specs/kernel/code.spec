name:add_path/1
def:add_path(Dir) -> add_path_ret()
types:
      Dir = file:filename()

name:add_patha/1
def:add_patha(Dir) -> add_path_ret()
types:
      Dir = file:filename()

name:add_paths/1
def:add_paths(Dirs) -> 'ok'
types:
      Dirs = [Dir = file:filename()]

name:add_pathsa/1
def:add_pathsa(Dirs) -> 'ok'
types:
      Dirs = [Dir = file:filename()]

name:add_pathsz/1
def:add_pathsz(Dirs) -> 'ok'
types:
      Dirs = [Dir = file:filename()]

name:add_pathz/1
def:add_pathz(Dir) -> add_path_ret()
types:
      Dir = file:filename()

name:all_loaded/0
def:all_loaded() -> [{Module, Loaded}]
types:
      Module = module(),
      Loaded = loaded_filename()

name:clash/0
def:clash() -> 'ok'

name:compiler_dir/0
def:compiler_dir() -> file:filename()

name:del_path/1
def:del_path(NameOrDir) -> boolean() | {'error', What}
types:
      NameOrDir = Name | Dir,
      Name = atom(),
      Dir = file:filename(),
      What = 'bad_name'

name:delete/1
def:delete(Module) -> boolean()
types:
      Module = module()

name:ensure_loaded/1
def:ensure_loaded(Module) -> {module, Module} | {error, What}
types:
      Module = module(),
      What = embedded | badfile | native_code | nofile | on_load

name:get_object_code/1
def:get_object_code(Module) -> {Module, Binary, Filename} | error
types:
      Module = module(),
      Binary = binary(),
      Filename = file:filename()

name:get_path/0
def:get_path() -> Path
types:
      Path = [Dir = file:filename()]

name:is_loaded/1
def:is_loaded(Module) -> {'file', Loaded} | false
types:
      Module = module(),
      Loaded = loaded_filename()

name:is_sticky/1
def:is_sticky(Module) -> boolean()
types:
      Module = module()

name:lib_dir/0
def:lib_dir() -> file:filename()

name:lib_dir/1
def:lib_dir(Name) -> file:filename() | {'error', 'bad_name'}
types:
      Name = atom()

name:lib_dir/2
def:lib_dir(Name, SubDir) -> file:filename() | {'error', 'bad_name'}
types:
      Name = atom(),
      SubDir = atom()

name:load_abs/1
def:load_abs(Filename) -> load_ret()
types:
      Filename = file:filename()

name:load_abs/2
def:load_abs(Filename :: loaded_filename(), Module :: module()) -> load_ret()

name:load_binary/3
def:load_binary(Module, Filename, Binary) ->
                         {module, Module} | {error, What}
types:
      Module = module(),
      Filename = loaded_filename(),
      Binary = binary(),
      What = badarg | load_error_rsn()

name:load_file/1
def:load_file(Module) -> load_ret()
types:
      Module = module()

name:load_native_code_for_all_loaded/0
def:load_native_code_for_all_loaded() -> ok

name:load_native_partial/2
def:load_native_partial(Module :: module(), Binary :: binary()) -> load_ret()

name:load_native_sticky/3
def:load_native_sticky(Module :: module(), Binary :: binary(), WholeModule :: 'false' | binary()) -> load_ret()

name:objfile_extension/0
def:objfile_extension() -> nonempty_string()

name:priv_dir/1
def:priv_dir(Name) -> file:filename() | {'error', 'bad_name'}
types:
      Name = atom()

name:purge/1
def:purge(Module) -> boolean()
types:
      Module = module()

name:rehash/0
def:rehash() -> 'ok'

name:replace_path/2
def:replace_path(Name, Dir) -> 'true' | {'error', What}
types:
      Name= atom(),
      Dir = file:filename(),
      What = 'bad_directory' | 'bad_name' | {'badarg',_}

name:root_dir/0
def:root_dir() -> file:filename()

name:set_path/1
def:set_path(Path) -> 'true' | {'error', What}
types:
      Path = [Dir = file:filename()],
      What = 'bad_directory' | 'bad_path'

name:set_primary_archive/4
def:set_primary_archive(ArchiveFile :: file:filename(),
			  ArchiveBin :: binary(),
			  FileInfo :: file:file_info(),
			  ParserFun :: fun())
			 -> 'ok' | {'error', atom()}

name:soft_purge/1
def:soft_purge(Module) -> boolean()
types:
      Module = module()

name:start_link/0
def:start_link() -> {'ok', pid()} | {'error', 'crash'}

name:start_link/1
def:start_link(Flags :: [atom()]) -> {'ok', pid()} | {'error', 'crash'}

name:stick_dir/1
def:stick_dir(Dir) -> 'ok' | 'error'
types:
      Dir = file:filename()

name:stick_mod/1
def:stick_mod(Module :: module()) -> 'true'

name:stop/0
def:stop() -> no_return()

name:unstick_dir/1
def:unstick_dir(Dir) -> 'ok' | 'error'
types:
      Dir = file:filename()

name:unstick_mod/1
def:unstick_mod(Module :: module()) -> 'true'

name:where_is_file/1
def:where_is_file(Filename) -> non_existing | Absname
types:
      Filename = file:filename(),
      Absname = file:filename()

name:where_is_file/2
def:where_is_file(Path :: file:filename(), Filename :: file:filename()) ->
        file:filename() | 'non_existing'

name:which/1
def:which(Module) -> Which
types:
      Module = module(),
      Which = file:filename() | loaded_ret_atoms() | non_existing

name:which/3
def:which(file:filename(), file:filename(), [file:filename()]) ->
        'non_existing' | file:filename()

