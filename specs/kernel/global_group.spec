name:global_groups/0
def:global_groups() -> {GroupName, GroupNames} | undefined
types:
      GroupName = group_name(),
      GroupNames = [GroupName]

name:info/0
def:info() -> [info_item()]

name:monitor_nodes/1
def:monitor_nodes(Flag) -> 'ok'
types:
      Flag = boolean()

name:own_nodes/0
def:own_nodes() -> Nodes
types:
      Nodes = [Node = node()]

name:registered_names/1
def:registered_names(Where) -> Names
types:
      Where = where(),
      Names = [Name = name()]

name:send/2
def:send(Name, Msg) -> pid() | {'badarg', {Name, Msg}}
types:
      Name = name(),
      Msg = term()

name:send/3
def:send(Where, Name, Msg) -> pid() | {'badarg', {Name, Msg}}
types:
      Where = where(),
      Name = name(),
      Msg = term()

name:sync/0
def:sync() -> 'ok'

name:sync_check_init/6
def:sync_check_init(_, _, _, _, _, _) -> no_return()

name:sync_check_init/8
def:sync_check_init(_, _, _, _, _, _, _, _) -> no_return()

name:sync_init/4
def:sync_init(_, _, _, _) -> no_return()

name:whereis_name/1
def:whereis_name(Name) -> pid() | 'undefined'
types:
      Name = name()

name:whereis_name/2
def:whereis_name(Where, Name) -> pid() | 'undefined'
types:
      Where = where(),
      Name = name()

