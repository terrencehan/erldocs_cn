name:code_change/3
def:code_change(term(), #state{}, term()) -> {'ok', #state{}}

name:handle_call/2
def:handle_call('null', #state{}) -> {'ok', 'null', #state{}}

name:handle_event/2
def:handle_event(term(), #state{}) -> {'ok', #state{}}

name:handle_info/2
def:handle_info(term(), #state{}) -> {'ok', #state{}}

name:init/3
def:init(Dir, MaxBytes, MaxFiles) -> Args
types:
      Dir = file:filename(),
      MaxBytes = non_neg_integer(), % b()
      MaxFiles = 1..255, % f()
      Args = args()

name:init/4
def:init(Dir, MaxBytes, MaxFiles, Pred) -> Args
types:
      Dir = file:filename(),
      MaxBytes = non_neg_integer(), % b()
      MaxFiles = 1..255, % f()
      Pred = fun((Event = term()) -> boolean()), % pred()
      Args = args()

name:init/4
def:init({file:filename(), non_neg_integer(), f(), pred()}) -> {'ok', #state{}} | {'error', term()}

name:terminate/2
def:terminate(term(), #state{}) -> #state{}

