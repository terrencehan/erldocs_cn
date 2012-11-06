name:concat/2
def:concat(package_name(), package_name()) -> string()

name:concat/1
def:concat([package_name()]) -> string()

name:find_modules/1
def:find_modules(package_name()) -> [string()]

name:find_modules/2
def:find_modules(package_name(), [string()]) -> [string()]

name:first/1
def:first(package_name()) -> [string()]

name:is_segmented/1
def:is_segmented(package_name()) -> boolean()

name:is_valid/1
def:is_valid(package_name()) -> boolean()

name:last/1
def:last(package_name()) -> string()

name:split/1
def:split(package_name()) -> [string()]

name:strip_last/1
def:strip_last(package_name()) -> string()

name:to_string/1
def:to_string(package_name()) -> string()

