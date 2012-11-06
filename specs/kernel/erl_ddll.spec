name:format_error/1
def:format_error(ErrorDesc) -> string()
types:
      ErrorDesc = term()

name:info/1
def:info(Name) -> InfoList
types:
      Name = driver(),
      InfoList = [InfoItem, ...],
      InfoItem = {Tag = atom(), Value = term()}

name:info/0
def:info() -> AllInfoList
types:
      AllInfoList = [DriverInfo],
      DriverInfo = {DriverName, InfoList},
      DriverName = string(),
      InfoList = [InfoItem],
      InfoItem = {Tag = atom(), Value = term()}

name:load/2
def:load(Path, Name) -> 'ok' | {'error', ErrorDesc}
types:
      Path = path(),
      Name = driver(),
      ErrorDesc =term()

name:load_driver/2
def:load_driver(Path, Name) -> 'ok' | {'error', ErrorDesc}
types:
      Path = path(),
      Name = driver(),
      ErrorDesc = term()

name:reload/2
def:reload(Path, Name) -> 'ok' | {'error', ErrorDesc}
types:
      Path = path(),
      Name = driver(),
      ErrorDesc = pending_process | OpaqueError,
      OpaqueError = term()

name:reload_driver/2
def:reload_driver(Path, Name) -> 'ok' | {'error', ErrorDesc}
types:
      Path = path(),
      Name = driver(),
      ErrorDesc = pending_process | OpaqueError,
      OpaqueError = term()

name:start/0
def:start() -> {'error', {'already_started', 'undefined'}}

name:stop/0
def:stop() -> 'ok'

name:unload/1
def:unload(Name) -> 'ok' | {'error', ErrorDesc}
types:
      Name = driver(),
      ErrorDesc = term()

name:unload_driver/1
def:unload_driver(Name) -> 'ok' | {'error', ErrorDesc}
types:
      Name = driver(),
      ErrorDesc = term()

