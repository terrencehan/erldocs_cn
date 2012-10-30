name:cons/2
def:cons(Item :: term(), Q1 :: queue()) -> Q2 :: queue()

name:daeh/1
def:daeh(Q :: queue()) -> Item :: term()

name:drop/1
def:drop(Q1 :: queue()) -> Q2 :: queue()

name:drop_r/1
def:drop_r(Q1 :: queue()) -> Q2 :: queue()

name:filter/2
def:filter(Fun, Q1 :: queue()) -> Q2 :: queue()
types:
      Fun = fun((Item = term()) -> boolean() | list()

name:from_list/1
def:from_list(L :: list()) -> queue()

name:get/1
def:get(Q :: queue()) -> Item :: term()

name:get/2
def:get(list(), list()) -> term()

name:get_r/1
def:get_r(Q :: queue()) -> Item :: term()

name:head/1
def:head(Q :: queue()) -> Item :: term()

name:in/2
def:in(Item :: term(), Q1 :: queue()) -> Q2 :: queue()

name:in_r/2
def:in_r(Item :: term(), Q1 :: queue()) -> Q2 :: queue()

name:init/1
def:init(Q1 :: queue()) -> Q2 :: queue()

name:is_empty/1
def:is_empty(Q :: queue()) -> boolean()

name:is_queue/1
def:is_queue(Term :: term()) -> boolean()

name:join/2
def:join(Q1 :: queue(), Q2 :: queue()) -> Q3 :: queue()

name:lait/1
def:lait(Q1 :: queue()) -> Q2 :: queue()

name:last/1
def:last(Q :: queue()) -> Item :: term()

name:len/1
def:len(Q :: queue()) -> non_neg_integer()

name:liat/1
def:liat(Q1 :: queue()) -> Q2 :: queue()

name:member/2
def:member(Item :: term(), Q :: queue()) -> boolean()

name:new/0
def:new() -> queue()

name:out/1
def:out(Q1 :: queue()) ->
                 {{value, Item :: term()}, Q2 :: queue()} |
                 {empty, Q1 :: queue()}

name:out_r/1
def:out_r(Q1 :: queue()) ->
                   {{value, Item :: term()}, Q2 :: queue()} |
                   {empty, Q1 :: queue()}

name:peek/1
def:peek(Q :: queue()) -> empty | {value,Item :: term()}

name:peek_r/1
def:peek_r(Q :: queue()) -> empty | {value,Item :: term()}

name:reverse/1
def:reverse(Q1 :: queue()) -> Q2 :: queue()

name:snoc/2
def:snoc(Q1 :: queue(), Item :: term()) -> Q2 :: queue()

name:split/2
def:split(N :: non_neg_integer(), Q1 :: queue()) ->
                   {Q2 :: queue(),Q3 :: queue()}

name:tail/1
def:tail(Q1 :: queue()) -> Q2 :: queue()

name:to_list/1
def:to_list(Q :: queue()) -> list()

