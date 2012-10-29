name:seed/0
def:seed() -> ran()

name:seed/3
def:seed({A1, A2, A3}) -> 'undefined' | ran()
types:
      A1 = integer(),
      A2 = integer(),
      A3 = integer()

name:seed/3
def:seed(A1, A2, A3) -> 'undefined' | ran()
types:
      A1 = integer(),
      A2 = integer(),
      A3 = integer()

name:seed0/0
def:seed0() -> ran()

name:seed_put/1
def:seed_put(ran()) -> 'undefined' | ran()

name:uniform/0
def:uniform() -> float()

name:uniform/1
def:uniform(N) -> pos_integer()
types:
      N = pos_integer()

name:uniform_s/1
def:uniform_s(State0) -> {float(), State1}
types:
      State0 = ran(),
      State1 = ran()

name:uniform_s/2
def:uniform_s(N, State0) -> {integer(), State1}
types:
      N = pos_integer(),
      State0 = ran(),
      State1 = ran()

