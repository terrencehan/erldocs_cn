name:check_childspecs/1
def:check_childspecs(ChildSpecs) -> Result
types:
      ChildSpecs = [child_spec()],
      Result = 'ok' | {'error', Error = term()}

name:code_change/3
def:code_change(term(), state(), term()) ->
        {'ok', state()} | {'error', term()}

name:count_children/1
def:count_children(SupRef) -> PropListOfCounts
types:
      SupRef = sup_ref(),
      PropListOfCounts = [Count],
      Count = {specs, ChildSpecCount = non_neg_integer()}
             | {active, ActiveProcessCount = non_neg_integer()}
             | {supervisors, ChildSupervisorCount = non_neg_integer()}
             |{workers, ChildWorkerCount = non_neg_integer()}

name:delete_child/2
def:delete_child(SupRef, Id) -> Result
types:
      SupRef = sup_ref(),
      Id = child_id(),
      Result = 'ok' | {'error', Error},
      Error = 'running' | 'not_found' | 'simple_one_for_one'

name:handle_call/3
def:handle_call(call(), term(), state()) -> {'reply', term(), state()}

name:handle_cast/2
def:handle_cast('null', state()) -> {'noreply', state()}

name:handle_info/2
def:handle_info(term(), state()) ->
        {'noreply', state()} | {'stop', 'shutdown', state()}

name:init/3
def:init({init_sup_name(), module(), [term()]}) ->
        {'ok', state()} | 'ignore' | {'stop', stop_rsn()}

name:restart_child/2
def:restart_child(SupRef, Id) -> Result
types:
      SupRef = sup_ref(),
      Id = child_id(),
      Result = {'ok', Child = child()}
              | {'ok', Child = child(), Info = term()}
              | {'error', Error},
      Error = 'running' | 'not_found' | 'simple_one_for_one' | term()

name:start_child/2
def:start_child(SupRef, ChildSpec) -> startchild_ret()
types:
      SupRef = sup_ref(),
      ChildSpec = child_spec() | (List = [term()])

name:start_link/2
def:start_link(Module, Args) -> startlink_ret()
types:
      Module = module(),
      Args = term()

name:start_link/3
def:start_link(SupName, Module, Args) -> startlink_ret()
types:
      SupName = sup_name(),
      Module = module(),
      Args = term()

name:terminate/2
def:terminate(term(), state()) -> 'ok'

name:terminate_child/2
def:terminate_child(SupRef, Id) -> Result
types:
      SupRef = sup_ref(),
      Id = pid() | child_id(),
      Result = 'ok' | {'error', Error},
      Error = 'not_found' | 'simple_one_for_one'

name:which_children/1
def:which_children(SupRef) -> [{Id,Child,Type,Modules}]
types:
      SupRef = sup_ref(),
      Id = child_id() | undefined,
      Child = child(),
      Type = worker(),
      Modules = modules()

