name:code_change/3
def:code_change(term(), state(), term()) -> {'ok', state()}

name:cookie/0
def:cookie() -> Cookie
types:
      Cookie = cookie()

name:cookie/1
def:cookie(TheCookie) -> 'true'
types:
      TheCookie = Cookie | [Cookie],
      Cookie = cookie()

name:get_cookie/0
def:get_cookie() -> 'nocookie' | cookie()

name:get_cookie/1
def:get_cookie(Node :: node()) -> 'nocookie' | cookie()

name:handle_call/4
def:handle_call(calls(), {pid(), term()}, state()) ->
        {'reply', 'hello' | 'true' | 'nocookie' | cookie(), state()}

name:handle_cast/4
def:handle_cast({'print', string(), [term()]}, state()) ->
        {'noreply', state()}

name:handle_info/2
def:handle_info(term(), state()) -> {'noreply', state()}

name:init/1
def:init([]) -> {'ok', state()}

name:is_auth/1
def:is_auth(Node) -> 'yes' | 'no'
types:
      Node = node()

name:node_cookie/2
def:node_cookie(Cookies :: [node() | cookie(),...]) -> 'yes' | 'no'

name:node_cookie/2
def:node_cookie(Node, Cookie) -> 'yes' | 'no'
types:
      Node = node(),
      Cookie = cookie()

name:print/3
def:print(Node :: node(), Format :: string(), Args :: [_]) -> 'ok'

name:set_cookie/1
def:set_cookie(Cookie :: cookie()) -> 'true'

name:set_cookie/2
def:set_cookie(Node :: node(), Cookie :: cookie()) -> 'true'

name:start_link/0
def:start_link() -> {'ok',pid()} | {'error', term()} | 'ignore'

name:sync_cookie/0
def:sync_cookie() -> any()

name:terminate/2
def:terminate(term(), state()) -> 'ok'

