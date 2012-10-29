name:centre/2
def:centre(String, Number) -> Centered
types:
      String = string(),
      Centered = string(),
      Number = non_neg_integer()

name:centre/3
def:centre(String, Number, Character) -> Centered
types:
      String = string(),
      Centered = string(),
      Number = non_neg_integer(),
      Character = char()

name:chars/2
def:chars(Character, Number) -> String
types:
      Character = char(),
      Number = non_neg_integer(),
      String = string()

name:chars/3
def:chars(Character, Number, Tail) -> String
types:
      Character = char(),
      Number = non_neg_integer(),
      Tail = string(),
      String = string()

name:chr/2
def:chr(String, Character) -> Index
types:
      String = string(),
      Character = char(),
      Index = non_neg_integer()

name:concat/2
def:concat(String1, String2) -> String3
types:
      String1 = string(),
      String2 = string(),
      String3 = string()

name:copies/2
def:copies(String, Number) -> Copies
types:
      String = string(),
      Copies = string(),
      Number = non_neg_integer()

name:cspan/2
def:cspan(String, Chars) -> Length
types:
      String = string(),
      Chars = string(),
      Length = non_neg_integer()

name:equal/2
def:equal(String1, String2) -> boolean()
types:
      String1 = string(),
      String2 = string()

name:join/2
def:join(StringList, Separator) -> String
types:
      StringList = [string()],
      Separator = string(),
      String = string()

name:left/2
def:left(String, Number) -> Left
types:
      String = string(),
      Left = string(),
      Number = non_neg_integer()

name:left/3
def:left(String, Number, Character) -> Left
types:
      String = string(),
      Left = string(),
      Number = non_neg_integer(),
      Character = char()

name:len/1
def:len(String) -> Length
types:
      String = string(),
      Length = non_neg_integer()

name:rchr/2
def:rchr(String, Character) -> Index
types:
      String = string(),
      Character = char(),
      Index = non_neg_integer()

name:right/2
def:right(String, Number) -> Right
types:
      String = string(),
      Right = string(),
      Number = non_neg_integer()

name:right/3
def:right(String, Number, Character) -> Right
types:
      String = string(),
      Right = string(),
      Number = non_neg_integer(),
      Character = char()

name:rstr/2
def:rstr(String, SubString) -> Index
types:
      String = string(),
      SubString = string(),
      Index = non_neg_integer()

name:span/2
def:span(String, Chars) -> Length
types:
      String = string(),
      Chars = string(),
      Length = non_neg_integer()

name:str/2
def:str(String, SubString) -> Index
types:
      String = string(),
      SubString = string(),
      Index = non_neg_integer()

name:strip/1
def:strip(string()) -> string()

name:strip/2
def:strip(String, Direction) -> Stripped
types:
      String = string(),
      Stripped = string(),
      Direction = left | right | both

name:strip/3
def:strip(String, Direction, Character) -> Stripped
types:
      String = string(),
      Stripped = string(),
      Direction = left | right | both,
      Character = char()

name:sub_string/2
def:sub_string(String, Start) -> SubString
types:
      String = string(),
      SubString = string(),
      Start = pos_integer()

name:sub_string/3
def:sub_string(String, Start, Stop) -> SubString
types:
      String = string(),
      SubString = string(),
      Start = pos_integer(),
      Stop = pos_integer()

name:sub_word/2
def:sub_word(String, Number) -> Word
types:
      String = string(),
      Word = string(),
      Number = integer()

name:sub_word/3
def:sub_word(String, Number, Character) -> Word
types:
      String = string(),
      Word = string(),
      Number = integer(),
      Character = char()

name:substr/2
def:substr(String, Start) -> SubString
types:
      String = string(),
      SubString = string(),
      Start = pos_integer()

name:substr/3
def:substr(String, Start, Length) -> SubString
types:
      String = string(),
      SubString = string(),
      Start = pos_integer(),
      Length = non_neg_integer()

name:to_lower/1
def:to_lower(String) -> Result
types:
                  String = string(),
                  Result = string()
	    ; (Char) -> CharResult when
                  Char = char(),
                  CharResult = char()

name:to_upper/1
def:to_upper(String) -> Result
types:
                  String = string(),
                  Result = string()
	    ; (Char) -> CharResult when
                  Char = char(),
                  CharResult = char()

name:tokens/2
def:tokens(String, SeparatorList) -> Tokens
types:
      String = string(),
      SeparatorList = string(),
      Tokens = [Token = nonempty_string()]

name:words/1
def:words(String) -> Count
types:
      String = string(),
      Count = pos_integer()

name:words/2
def:words(String, Character) -> Count
types:
      String = string(),
      Character = char(),
      Count = pos_integer()

