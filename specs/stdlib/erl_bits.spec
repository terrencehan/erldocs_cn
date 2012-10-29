name:as_list/1
def:as_list(#bittype{}) ->
    [bt_endian() | bt_sign() | bt_type() | {'unit', 'undefined' | bt_unit()}]

name:set_bit_type/2
def:set_bit_type('default' | size(), 'default' | [type()]) ->
        {'ok', 'undefined' | size(), #bittype{}} |
        {'error', {'undefined_bittype', term()}} |
        {'error', {'bittype_mismatch', term(), term(), string()}}

name:system_bitdefault/0
def:system_bitdefault() -> 'no_system_bitdefault'

name:system_bittypes/0
def:system_bittypes() -> 'no_system_types'

