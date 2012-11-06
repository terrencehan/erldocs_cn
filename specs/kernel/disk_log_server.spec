name:open_distr_rpc/3
def:open_distr_rpc([node()], _, _) -> no_return(). % XXX: underspecified

open_distr_rpc(Nodes, A, From) ->
    {AllReplies, BadNodes} = rpc:multicall(Nodes, ?MODULE, dist_open, [A]),
    {Ok, Bad} = cr(AllReplies, [], []),
    Old = find_old_nodes(Nodes, AllReplies, BadNodes),
    NotOk = [{BadNode, {error, nodedown}} || BadNode <- BadNodes ++ Old],
    Reply = {Ok, Bad ++ NotOk},
    %% Send the reply to the waiting client:
    gen_server:reply(From, Reply),
    exit(normal)

