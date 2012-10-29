name:change_key/2
def:change_key(RegHandle, Key) -> ReturnValue
types:
      RegHandle = reg_handle(),
      Key = string(),
      ReturnValue = 'ok' | {'error', ErrorId = atom()}

name:change_key_create/2
def:change_key_create(RegHandle, Key) -> ReturnValue
types:
      RegHandle = reg_handle(),
      Key = string(),
      ReturnValue = 'ok' | {'error', ErrorId = atom()}

name:close/1
def:close(RegHandle) -> 'ok'
types:
      RegHandle = reg_handle()

name:collect_keys/2
def:collect_keys(port(), string()) -> {'ok', [string()]} | {'error', ErrorId :: atom()}

name:collect_values/3
def:collect_values(port(), [{name(), value()}]) -> 
        {'ok', [{name(), value()}]} | {'error', ErrorId :: atom()}

name:current_key/1
def:current_key(RegHandle) -> ReturnValue
types:
      RegHandle = reg_handle(),
      ReturnValue = {'ok', string()}

name:delete_key/1
def:delete_key(RegHandle) -> ReturnValue
types:
      RegHandle = reg_handle(),
      ReturnValue = 'ok' | {'error', ErrorId = atom()}

name:delete_value/2
def:delete_value(RegHandle, Name) -> ReturnValue
types:
      RegHandle = reg_handle(),
      Name = name(),
      ReturnValue = 'ok' | {'error', ErrorId = atom()}

name:expand/1
def:expand(String) -> ExpandedString
types:
      String = string(),
      ExpandedString = string()

name:format_error/1
def:format_error(ErrorId) -> ErrorString
types:
      ErrorId = atom(),
      ErrorString = string()

name:open/1
def:open(OpenModeList) -> ReturnValue
types:
      OpenModeList = [OpenMode],
      OpenMode = 'read' | 'write',
      ReturnValue = {'ok', RegHandle} | {'error', ErrorId = 'enotsup'},
      RegHandle = reg_handle()

name:set_value/3
def:set_value(RegHandle, Name, Value) -> ReturnValue
types:
      RegHandle = reg_handle(),
      Name = name(),
      Value = value(),
      ReturnValue = 'ok' | {'error', ErrorId = atom()}

name:sub_keys/1
def:sub_keys(RegHandle) -> ReturnValue
types:
      RegHandle = reg_handle(),
      ReturnValue = {'ok', [SubKey]} | {'error', ErrorId = atom()},
      SubKey = string()

name:value/2
def:value(RegHandle, Name) -> ReturnValue
types:
      RegHandle = reg_handle(),
      Name = name(),
      ReturnValue = {'ok', Value = value()} | {'error', ErrorId = atom()}

name:values/1
def:values(RegHandle) -> ReturnValue
types:
      RegHandle = reg_handle(),
      ReturnValue = {'ok', [ValuePair]} | {'error', ErrorId = atom()},
      ValuePair = {Name = name(), Value = value()}

