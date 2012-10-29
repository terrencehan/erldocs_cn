name:append_values/2
def:append_values(Key, List) -> List
types:
      Key = term(),
      List = [term()]

name:compact/1
def:compact(List) -> List
types:
      List = [property()]

name:delete/2
def:delete(Key, List) -> List
types:
      Key = term(),
      List=[term()]

name:expand/2
def:expand(Expansions, List) -> List
types:
      Expansions = [{Property = property(), Expansion = [term()]}],
      List = [term()]

name:get_all_values/2
def:get_all_values(Key, List) -> [term()]
types:
      Key = term(),
      List = [term()]

name:get_bool/2
def:get_bool(Key, List) -> boolean()
types:
      Key = term(),
      List = [term()]

name:get_keys/1
def:get_keys(List) -> [term()]
types:
      List = [term()]

name:get_value/2
def:get_value(Key, List) -> term()
types:
      Key = term(),
      List = List=[term()]

name:get_value/3
def:get_value(Key, List, Default) -> term()
types:
      Key = term(),
      List = [term()],
      Default = term()

name:is_defined/2
def:is_defined(Key, List) -> boolean()
types:
      Key = term(),
      List = [term()]

name:lookup/2
def:lookup(Key, List) -> 'none' | tuple()
types:
      Key = term(),
      List = [term()]

name:lookup_all/2
def:lookup_all(Key, List) -> [tuple()]
types:
      Key = term(),
      List = [term()]

name:normalize/2
def:normalize(List, Stages) -> List
types:
      List = [term()],
      Stages = [Operation],
      Operation = {'aliases', Aliases}
                 | {'negations', Negations}
                 | {'expand', Expansions},
      Aliases = [{Key, Key}],
      Negations = [{Key, Key}],
      Expansions = [{Property = property(), Expansion = [term()]}]

name:property/1
def:property(Property) -> Property
types:
      Property = property()

name:property/2
def:property(Key, Value) -> Property
types:
      Key = term(),
      Value = term(),
      Property = atom() | {term(), term()}

name:split/2
def:split(List, Keys) -> {Lists, Rest}
types:
      List = [term()],
      Keys = [term()],
      Lists = [[term()]],
      Rest = [term()]

name:substitute_aliases/2
def:substitute_aliases(Aliases, List) -> List
types:
      Aliases = [{Key, Key}],
      Key = term(),
      List=[term()]

name:substitute_negations/2
def:substitute_negations(Negations, List) -> List
types:
      Negations = [{Key, Key}],
      Key = term(),
      List = [term()]

name:unfold/1
def:unfold(List) -> List
types:
      List = [term()]

