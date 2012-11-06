name:get_system_tracer/0
def:get_system_tracer() -> Tracer
types:
      Tracer = tracer()

name:get_token/0
def:get_token() -> [] | token()

name:get_token/1
def:get_token(Component) -> {Component, Val}
types:
      Component = component(),
      Val = value()

name:print/1
def:print(TraceInfo) -> 'ok'
types:
      TraceInfo = term()

name:print/2
def:print(Label, TraceInfo) -> 'ok'
types:
      Label = integer(),
      TraceInfo = term()

name:reset_trace/0
def:reset_trace() -> 'true'

name:set_system_tracer/1
def:set_system_tracer(Tracer) -> OldTracer
types:
      Tracer = tracer(),
      OldTracer = tracer()

name:set_token/1
def:set_token(Token) -> PreviousToken | 'ok'
types:
      Token = [] | token(),
      PreviousToken = [] | token()

name:set_token/2
def:set_token(Component, Val) -> {Component, OldVal}
types:
      Component = component(),
      Val = value(),
      OldVal = value()

