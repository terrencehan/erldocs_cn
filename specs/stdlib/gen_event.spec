name:add_handler/3
def:add_handler(emgr_ref(), handler(), term()) -> term()

name:add_sup_handler/3
def:add_sup_handler(emgr_ref(), handler(), term()) -> term()

name:call/3
def:call(emgr_ref(), handler(), term()) -> term()

name:call/4
def:call(emgr_ref(), handler(), term(), timeout()) -> term()

name:delete_handler/3
def:delete_handler(emgr_ref(), handler(), term()) -> term()

name:init_it/6
def:init_it(pid(), 'self' | pid(), emgr_name(), module(), [term()], [_]) -> 
init_it(Starter, self, Name, Mod, Args, Options) ->
    init_it(Starter, self(), Name, Mod, Args, Options);
init_it(Starter, Parent, Name0, _, _, Options) ->
    process_flag(trap_exit, true),
    Debug = gen:debug_options(Options),
    proc_lib:init_ack(Starter, {ok, self()}),
    Name = name(Name0),
    loop(Parent, Name, [], Debug, false)

name:notify/2
def:notify(emgr_ref(), term()) -> 'ok'

name:split/2
def:split(handler(), [#handler{}]) ->
	{atom(), #handler{}, [#handler{}]} | 'error'

name:start/0
def:start() -> start_ret()

name:start/1
def:start(emgr_name()) -> start_ret()

name:start_link/0
def:start_link() -> start_ret()

name:start_link/1
def:start_link(emgr_name()) -> start_ret()

name:stop/1
def:stop(emgr_ref()) -> 'ok'

name:swap_handler/5
def:swap_handler(emgr_ref(), {handler(), term()}, {handler(), term()}) ->
	    'ok' | {'error', term()}

name:swap_sup_handler/5
def:swap_sup_handler(emgr_ref(), {handler(), term()}, {handler(), term()}) ->
	    'ok' | {'error', term()}

name:sync_notify/2
def:sync_notify(emgr_ref(), term()) -> 'ok'

name:system_terminate/4
def:system_terminate(_, _, _, [_]) -> no_return()

name:which_handlers/1
def:which_handlers(emgr_ref()) -> [handler()]

