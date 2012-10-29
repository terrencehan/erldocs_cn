name:decode/1
def:decode(Base64) -> Data
types:
      Base64 = string() | binary(),
      Data = binary()

name:decode_l/1
def:decode_l(string()) -> string()

name:decode_to_string/1
def:decode_to_string(Base64) -> DataString
types:
      Base64 = string() | binary(),
      DataString = string()

name:encode/1
def:encode(Data) -> Base64
types:
      Data = string() | binary(),
      Base64 = binary()

name:encode_l/1
def:encode_l(string()) -> ascii_string()

name:encode_to_string/1
def:encode_to_string(Data) -> Base64String
types:
      Data = string() | binary(),
      Base64String = ascii_string()

name:mime_decode/1
def:mime_decode(Base64) -> Data
types:
      Base64 = string() | binary(),
      Data = binary()

name:mime_decode_l/1
def:mime_decode_l(string()) -> string()

name:mime_decode_to_string/1
def:mime_decode_to_string(Base64) -> DataString
types:
      Base64 = string() | binary(),
      DataString = string()

