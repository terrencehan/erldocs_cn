name:bom_to_encoding/1
def:bom_to_encoding(Bin) -> {Encoding, Length}
types:
      Bin = binary(),
      Encoding =  'latin1' | 'utf8'
                 | {'utf16', endian()}
                 | {'utf32', endian()},
      Length = non_neg_integer()

name:characters_to_binary/1
def:characters_to_binary(Data) -> Result
types:
      Data = latin1_chardata() | chardata() | external_chardata(),
      Result = binary()
              | {error, binary(), RestData}
              | {incomplete, binary(), binary()},
      RestData = latin1_chardata() | chardata() | external_chardata()

name:characters_to_binary/3
def:characters_to_binary(Data, InEncoding, OutEncoding) -> Result
types:
      Data = latin1_chardata() | chardata() | external_chardata(),
      InEncoding = encoding(),
      OutEncoding = encoding(),
      Result = binary()
              | {error, binary(), RestData}
              | {incomplete, binary(), binary()},
      RestData = latin1_chardata() | chardata() | external_chardata()

name:characters_to_list/1
def:characters_to_list(Data) -> Result
types:
      Data = latin1_chardata() | chardata() | external_chardata(),
      Result = list()
              | {error, list(), RestData}
              | {incomplete, list(), binary()},
      RestData = latin1_chardata() | chardata() | external_chardata()

name:encoding_to_bom/1
def:encoding_to_bom(InEncoding) -> Bin
types:
      Bin = binary(),
      InEncoding = encoding()

