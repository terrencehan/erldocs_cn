name:chunk_name/1
def:chunk_name(hipe_architecture()) -> string()

name:is_loaded/1
def:is_loaded(Module::atom()) -> boolean()

name:load/2
def:load(Mod, binary()) -> 'bad_crc' | {'module',Mod}
types: is_subtype(Mod,atom()

name:load_module/3
def:load_module(Mod, binary(), _) -> 'bad_crc' | {'module',Mod}
types: is_subtype(Mod,atom()

name:load_native_code/2
def:load_native_code(Mod, binary()) -> 'no_native' | {'module', Mod}
types: is_subtype(Mod, atom()

name:post_beam_load/1
def:post_beam_load(atom()) -> 'ok'

