name:all_chunks/1
def:all_chunks(beam()) -> {'ok', 'beam_lib', [{chunkid(), dataB()}]}

name:chunks/2
def:chunks(Beam, ChunkRefs) ->
                    {'ok', {module(), [chunkdata()]}} |
                    {'error', 'beam_lib', chnk_rsn()}
types:
      Beam = beam(),
      ChunkRefs = [chunkref()]

name:chunks/3
def:chunks(Beam, ChunkRefs, Options) ->
                    {'ok', {module(), [ChunkResult]}} |
                    {'error', 'beam_lib', chnk_rsn()}
types:
      Beam = beam(),
      ChunkRefs = [chunkref()],
      Options = ['allow_missing_chunks'],
      ChunkResult = chunkdata() | {ChunkRef = chunkref(), 'missing_chunk'}

name:clear_crypto_key_fun/0
def:clear_crypto_key_fun() -> 'undefined' | {'ok', Result}
types:
      Result = 'undefined' | term()

name:cmp/2
def:cmp(Beam1, Beam2) -> 'ok' | {'error', 'beam_lib', cmp_rsn()}
types:
      Beam1 = beam(),
      Beam2 = beam()

name:cmp_dirs/2
def:cmp_dirs(Dir1, Dir2) ->
           {Only1, Only2, Different} | {'error', 'beam_lib', Reason}
types:
      Dir1 = atom() | file:filename(),
      Dir2 = atom() | file:filename(),
      Only1 = [file:filename()],
      Only2 = [file:filename()],
      Different = [{Filename1 = file:filename(), Filename2 = file:filename()}],
      Reason = {'not_a_directory', term()} | info_rsn()

name:code_change/3
def:code_change(term(), #state{}, term()) -> {'ok', #state{}}

name:crypto_key_fun/1
def:crypto_key_fun(CryptoKeyFun) -> 'ok' | {'error', Reason}
types:
      CryptoKeyFun = crypto_fun(),
      Reason = badfun | exists | term()

name:diff_dirs/2
def:diff_dirs(Dir1, Dir2) -> 'ok' | {'error', 'beam_lib', Reason}
types:
      Dir1 = atom() | file:filename(),
      Dir2 = atom() | file:filename(),
      Reason = {'not_a_directory', term()} | info_rsn()

name:error/1
def:error(term()) -> no_return()

name:file_error/3
def:file_error(file:filename(), {'error',atom()}) -> no_return()

name:format_error/1
def:format_error(Reason) -> io_lib:chars()
types:
      Reason = term()

name:handle_call/4
def:handle_call(calls(), {pid(), term()}, #state{}) ->
        {'noreply', #state{}} |
	{'reply', 'error' | {'error','badfun' | 'exists'}, #state{}} |
	{'stop', 'normal', 'undefined' | {'ok', term()}, #state{}}

name:handle_cast/2
def:handle_cast(term(), #state{}) -> {'noreply', #state{}}

name:handle_info/2
def:handle_info(term(), #state{}) -> {'noreply', #state{}}

name:info/1
def:info(Beam) -> [InfoPair] | {'error', 'beam_lib', info_rsn()}
types:
      Beam = beam(),
      InfoPair = {'file', Filename = file:filename()}
                | {'binary', Binary = binary()}
                | {'module', Module = module()}
                | {'chunks', [{ChunkId = chunkid(),
                               Pos = non_neg_integer(),
                               Size = non_neg_integer()}]}

name:init/1
def:init([]) -> {'ok', #state{}}

name:make_crypto_key/2
def:make_crypto_key(mode(), string()) ->
        {binary(), binary(), binary(), binary()}

name:md5/1
def:md5(Beam) ->
        {'ok', {module(), MD5}} | {'error', 'beam_lib', chnk_rsn()}
types:
      Beam = beam(),
      MD5 = binary()

name:strip/1
def:strip(Beam1) ->
        {'ok', {module(), Beam2}} | {'error', 'beam_lib', info_rsn()}
types:
      Beam1 = beam(),
      Beam2 = beam()

name:strip_files/1
def:strip_files(Files) ->
        {'ok', [{module(), Beam}]} | {'error', 'beam_lib', info_rsn()}
types:
      Files = [beam()],
      Beam = beam()

name:strip_release/1
def:strip_release(Dir) ->
        {'ok', [{module(), file:filename()}]}
      | {'error', 'beam_lib', Reason}
types:
      Dir = atom() | file:filename(),
      Reason = {'not_a_directory', term()} | info_rsn()

name:terminate/2
def:terminate(term(), #state{}) -> 'ok'

name:version/1
def:version(Beam) ->
                     {'ok', {module(), [Version :: term()]}} |
                     {'error', 'beam_lib', chnk_rsn()}
types:
      Beam = beam()

