name:replace/3
def:replace(Subject, Pattern, Replacement) -> Result
types:
      Subject = binary(),
      Pattern = binary() | [ binary() ] | cp(),
      Replacement = binary(),
      Result = binary()

name:replace/4
def:replace(Subject, Pattern, Replacement, Options) -> Result
types:
      Subject = binary(),
      Pattern = binary() | [ binary() ] | cp(),
      Replacement = binary(),
      Options = [Option],
      Option = global | {scope, part()} | {insert_replaced, InsPos},
      InsPos = OnePos | [ OnePos ],
      OnePos = non_neg_integer(),
      Result = binary()

name:split/2
def:split(Subject, Pattern) -> Parts
types:
      Subject = binary(),
      Pattern = binary() | [binary()] | cp(),
      Parts = [binary()]

name:split/3
def:split(Subject, Pattern, Options) -> Parts
types:
      Subject = binary(),
      Pattern = binary() | [binary()] | cp(),
      Options = [Option],
      Option = {scope, part()} | trim | global,
      Parts = [binary()]

