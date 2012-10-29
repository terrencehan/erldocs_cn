name:attach/1
def:attach(Node) -> 'already_attached' | 'attached'
types:
      Node = node()

name:do_spawn/4
def:do_spawn(pid(), module(), atom(), [term()]) -> term()

name:get_node/0
def:get_node() -> node()

name:get_nodes/0
def:get_nodes() -> [node()]

name:pspawn/3
def:pspawn(Mod, Fun, Args) -> pid()
types:
      Mod = module(),
      Fun = atom(),
      Args = [term()]

name:pspawn_link/3
def:pspawn_link(Mod, Fun, Args) -> pid()
types:
      Mod = module(),
      Fun = atom(),
      Args = [term()]

name:start/1
def:start(Name) -> Nodes
types:
      Name = atom(),
      Nodes = [node()]

name:start/2
def:start(Name, Args) -> Nodes
types:
      Name = atom(),
      Args = string(),
      Nodes = [node()]

name:stop/0
def:stop() -> 'stopped'

