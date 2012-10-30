name:attributes_info/1
def:attributes_info(Attributes) -> AttributesInfo
types:
      Attributes = attributes(),
      AttributesInfo = [AttributeInfoTuple = attribute_info()]

name:attributes_info/2
def:attributes_info(Attributes, AttributeItem) ->
                        AttributeInfo | 'undefined'
types:
      Attributes = attributes(),
      AttributeItem = attribute_item(),
      AttributeInfo = AttributeInfoTuple = attribute_info();
                     (Attributes, AttributeItems) -> [AttributeInfo] when
      Attributes = attributes(),
      AttributeItems = [AttributeItem],
      AttributeItem = attribute_item(),
      AttributeInfo = [AttributeInfoTuple = attribute_info()]

name:format_error/1
def:format_error(ErrorDescriptor) -> string()
types:
      ErrorDescriptor = error_description()

name:reserved_word/1
def:reserved_word(Atom :: atom()) -> boolean()

name:set_attr/3
def:set_attr('line', attributes(), fun((line()) -> line())) -> attributes()

name:set_attribute/3
def:set_attribute(AttributeItem, Attributes, SetAttributeFun) -> Attributes
types:
      AttributeItem = 'line',
      Attributes = attributes(),
      SetAttributeFun = fun((info_line()) -> info_line()

name:string/1
def:string(String) -> Return
types:
      String = string(),
      Return = {'ok', Tokens = tokens(), EndLocation}
              | {'error', ErrorInfo = error_info(), ErrorLocation},
      EndLocation = location(),
      ErrorLocation = location()

name:string/2
def:string(String, StartLocation) -> Return
types:
      String = string(),
      Return = {'ok', Tokens = tokens(), EndLocation}
              | {'error', ErrorInfo = error_info(), ErrorLocation},
      StartLocation = location(),
      EndLocation = location(),
      ErrorLocation = location()

name:string/3
def:string(String, StartLocation, Options) -> Return
types:
      String = string(),
      Options = options(),
      Return = {'ok', Tokens = tokens(), EndLocation}
              | {'error', ErrorInfo = error_info(), ErrorLocation},
      StartLocation = location(),
      EndLocation = location(),
      ErrorLocation = location()

name:token_info/1
def:token_info(Token) -> TokenInfo
types:
      Token = token(),
      TokenInfo = [TokenInfoTuple = token_info()]

name:token_info/2
def:token_info(Token, TokenItem) -> TokenInfo | 'undefined'
types:
      Token = token(),
      TokenItem = token_item(),
      TokenInfo = TokenInfoTuple = token_info();
                (Token, TokenItems) -> [TokenInfo] when
      Token = token(),
      TokenItems = [TokenItem],
      TokenItem = token_item(),
      TokenInfo = [TokenInfoTuple = token_info()]

name:tokens/3
def:tokens(Continuation, CharSpec, StartLocation) -> Return
types:
      Continuation = return_cont() | [],
      CharSpec = char_spec(),
      StartLocation = location(),
      Return = {'done',Result = tokens_result(),LeftOverChars = char_spec()}
              | {'more', Continuation1 = return_cont()}

name:tokens/4
def:tokens(Continuation, CharSpec, StartLocation, Options) -> Return
types:
      Continuation = return_cont() | [],
      CharSpec = char_spec(),
      StartLocation = location(),
      Options = options(),
      Return = {'done',Result = tokens_result(),LeftOverChars = char_spec()}
              | {'more', Continuation1 = return_cont()}

