name:allow/1
def:allow(Nodes) -> ok | error
types:
      Nodes = [node()]

name:connect_node/1
def:connect_node(Node) -> boolean() | ignored
types:
      Node = node()

name:get_net_ticktime/0
def:get_net_ticktime() -> Res
types:
      Res = NetTicktime | {ongoing_change_to, NetTicktime} | ignored,
      NetTicktime = pos_integer()

name:monitor_nodes/1
def:monitor_nodes(Flag) -> ok | Error
types:
      Flag = boolean(),
      Error = error | {error, term()}

name:monitor_nodes/2
def:monitor_nodes(Flag, Options) -> ok | Error
types:
      Flag = boolean(),
      Options = [Option],
      Option = {node_type, NodeType}
              | nodedown_reason,
      NodeType = visible | hidden | all,
      Error = error | {error, term()}

name:set_net_ticktime/2
def:set_net_ticktime(NetTicktime, TransitionPeriod) -> Res
types:
      NetTicktime = pos_integer(),
      TransitionPeriod = non_neg_integer(),
      Res = unchanged
           | change_initiated
           | {ongoing_change_to, NewNetTicktime},
      NewNetTicktime = pos_integer()

name:set_net_ticktime/1
def:set_net_ticktime(NetTicktime) -> Res
types:
      NetTicktime = pos_integer(),
      Res = unchanged
           | change_initiated
           | {ongoing_change_to, NewNetTicktime},
      NewNetTicktime = pos_integer()

name:stop/0
def:stop() -> ok | {error, Reason}
types:
      Reason = not_allowed | not_found

