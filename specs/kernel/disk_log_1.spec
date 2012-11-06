name:file_error/3
def:file_error(file:filename(), {'error', file:posix()}) -> no_return()

name:file_error_close/4
def:file_error_close(file:fd(), file:filename(), {'error', file:posix()}) -> no_return()

name:is_head/1
def:is_head(binary()) -> 'yes' | 'yes_not_closed' | 'no'

name:logl/1
def:logl([binary()]) -> {iolist(), non_neg_integer()}

name:mf_int_open/7
def:mf_int_open(FName   :: file:filename(),
		  MaxB    :: integer(),
		  MaxF    :: integer(),
		  Repair  :: dlog_repair(),
		  Mode    :: dlog_mode(),
		  Head    :: dlog_head(),
		  Version :: integer())
      -> {'ok', #handle{}, integer()}
       | {'repaired', #handle{},
	  non_neg_integer(), non_neg_integer(), non_neg_integer()}

name:repair_err/6
def:repair_err(file:io_device(), #cache{}, file:filename(),
		 file:filename(), {'error', file:posix()}) -> no_return()

name:write_cache_close/3
def:write_cache_close(file:fd(), file:filename(), iodata()) -> #cache{}. % | throw(Error)

write_cache_close(Fd, _FileName, []) ->
    #cache{fd = Fd};
write_cache_close(Fd, FileName, C) ->
    case file:write(Fd, C) of
        ok    -> #cache{fd = Fd};
        Error -> file_error_close(Fd, FileName, Error)
    end

