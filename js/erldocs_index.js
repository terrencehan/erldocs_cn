var index = [
  ['app', 'kernel', 'kernel', '[application]'],
  ['mod', 'kernel', 'application', []],
  ['fun', 'kernel', 'application:get_all_env/0', []],
  ['fun', 'kernel', 'application:get_all_env/1', []],
  ['fun', 'kernel', 'application:get_all_key/0', []],
  ['fun', 'kernel', 'application:get_all_key/1', []],
  ['fun', 'kernel', 'application:get_application/0', []],
  ['fun', 'kernel', 'application:get_application/1', []],
  ['fun', 'kernel', 'application:get_env/1', []],
  ['fun', 'kernel', 'application:get_env/2', []],
  ['fun', 'kernel', 'application:get_key/1', []],
  ['fun', 'kernel', 'application:get_key/2', []],
  ['fun', 'kernel', 'application:load/1', []],
  ['fun', 'kernel', 'application:load/2', []],
  ['fun', 'kernel', 'application:loaded_applications/0', []],
  ['fun', 'kernel', 'application:permit/2', []],
  ['fun', 'kernel', 'application:set_env/3', []],
  ['fun', 'kernel', 'application:set_env/4', []],
  ['fun', 'kernel', 'application:start/1', []],
  ['fun', 'kernel', 'application:start/2', []],
  ['fun', 'kernel', 'application:start_type/0', []],
  ['fun', 'kernel', 'application:stop/1', []],
  ['fun', 'kernel', 'application:takeover/2', []],
  ['fun', 'kernel', 'application:unload/1', []],
  ['fun', 'kernel', 'application:unset_env/2', []],
  ['fun', 'kernel', 'application:unset_env/3', []],
  ['fun', 'kernel', 'application:which_applications/0', []],
  ['fun', 'kernel', 'application:which_applications/1', []],
  ['mod', 'kernel', 'file', []],
  ['fun', 'kernel', 'file:advise/4', []],
  ['fun', 'kernel', 'file:change_group/2', []],
  ['fun', 'kernel', 'file:change_mode/2', []],
  ['fun', 'kernel', 'file:change_owner/2', []],
  ['fun', 'kernel', 'file:change_owner/3', []],
  ['fun', 'kernel', 'file:change_time/2', []],
  ['fun', 'kernel', 'file:change_time/3', []],
  ['fun', 'kernel', 'file:close/1', []],
  ['fun', 'kernel', 'file:consult/1', []],
  ['fun', 'kernel', 'file:copy/2', []],
  ['fun', 'kernel', 'file:copy/3', []],
  ['fun', 'kernel', 'file:del_dir/1', []],
  ['fun', 'kernel', 'file:delete/1', []],
  ['fun', 'kernel', 'file:eval/1', []],
  ['fun', 'kernel', 'file:eval/2', []],
  ['fun', 'kernel', 'file:file_info/1', []],
  ['fun', 'kernel', 'file:format_error/1', []],
  ['fun', 'kernel', 'file:get_cwd/0', []],
  ['fun', 'kernel', 'file:get_cwd/1', []],
  ['fun', 'kernel', 'file:list_dir/1', []],
  ['fun', 'kernel', 'file:make_dir/1', []],
  ['fun', 'kernel', 'file:make_link/2', []],
  ['fun', 'kernel', 'file:make_symlink/2', []],
  ['fun', 'kernel', 'file:native_name_encoding/0', []],
  ['fun', 'kernel', 'file:open/2', []],
  ['fun', 'kernel', 'file:path_consult/2', []],
  ['fun', 'kernel', 'file:path_eval/2', []],
  ['fun', 'kernel', 'file:path_open/3', []],
  ['fun', 'kernel', 'file:path_script/2', []],
  ['fun', 'kernel', 'file:path_script/3', []],
  ['fun', 'kernel', 'file:pid2name/1', []],
  ['fun', 'kernel', 'file:position/2', []],
  ['fun', 'kernel', 'file:pread/2', []],
  ['fun', 'kernel', 'file:pread/3', []],
  ['fun', 'kernel', 'file:pwrite/2', []],
  ['fun', 'kernel', 'file:pwrite/3', []],
  ['fun', 'kernel', 'file:read/2', []],
  ['fun', 'kernel', 'file:read_file/1', []],
  ['fun', 'kernel', 'file:read_file_info/1', []],
  ['fun', 'kernel', 'file:read_file_info/2', []],
  ['fun', 'kernel', 'file:read_line/1', []],
  ['fun', 'kernel', 'file:read_link/1', []],
  ['fun', 'kernel', 'file:read_link_info/1', []],
  ['fun', 'kernel', 'file:read_link_info/2', []],
  ['fun', 'kernel', 'file:rename/2', []],
  ['fun', 'kernel', 'file:script/1', []],
  ['fun', 'kernel', 'file:script/2', []],
  ['fun', 'kernel', 'file:set_cwd/1', []],
  ['fun', 'kernel', 'file:sync/1', []],
  ['fun', 'kernel', 'file:datasync/1', []],
  ['fun', 'kernel', 'file:truncate/1', []],
  ['fun', 'kernel', 'file:sendfile/2', []],
  ['fun', 'kernel', 'file:sendfile/5', []],
  ['fun', 'kernel', 'file:write/2', []],
  ['fun', 'kernel', 'file:write_file/2', []],
  ['fun', 'kernel', 'file:write_file/3', []],
  ['fun', 'kernel', 'file:write_file_info/2', []],
  ['fun', 'kernel', 'file:write_file_info/3', []],
  ['app', 'stdlib', 'stdlib', '[application]'],
  ['mod', 'stdlib', 'base64', []],
  ['fun', 'stdlib', 'base64:encode/1', []],
  ['fun', 'stdlib', 'base64:encode_to_string/1', []],
  ['fun', 'stdlib', 'base64:decode/1', []],
  ['fun', 'stdlib', 'base64:decode_to_string/1', []],
  ['fun', 'stdlib', 'base64:mime_decode/1', []],
  ['fun', 'stdlib', 'base64:mime_decode_to_string/1', []],
  ['mod', 'stdlib', 'c', []],
  ['fun', 'stdlib', 'c:bt/1', []],
  ['fun', 'stdlib', 'c:c/1', []],
  ['fun', 'stdlib', 'c:c/2', []],
  ['fun', 'stdlib', 'c:cd/1', []],
  ['fun', 'stdlib', 'c:flush/0', []],
  ['fun', 'stdlib', 'c:help/0', []],
  ['fun', 'stdlib', 'c:i/0', []],
  ['fun', 'stdlib', 'c:ni/0', []],
  ['fun', 'stdlib', 'c:i/3', []],
  ['fun', 'stdlib', 'c:l/1', []],
  ['fun', 'stdlib', 'c:lc/1', []],
  ['fun', 'stdlib', 'c:ls/0', []],
  ['fun', 'stdlib', 'c:ls/1', []],
  ['fun', 'stdlib', 'c:m/0', []],
  ['fun', 'stdlib', 'c:m/1', []],
  ['fun', 'stdlib', 'c:memory/0', []],
  ['fun', 'stdlib', 'c:memory/1', []],
  ['fun', 'stdlib', 'c:nc/1', []],
  ['fun', 'stdlib', 'c:nc/2', []],
  ['fun', 'stdlib', 'c:nl/1', []],
  ['fun', 'stdlib', 'c:pid/3', []],
  ['fun', 'stdlib', 'c:pwd/0', []],
  ['fun', 'stdlib', 'c:q/0', []],
  ['fun', 'stdlib', 'c:regs/0', []],
  ['fun', 'stdlib', 'c:nregs/0', []],
  ['fun', 'stdlib', 'c:xm/1', []],
  ['fun', 'stdlib', 'c:y/1', []],
  ['fun', 'stdlib', 'c:y/2', []],
  ['mod', 'stdlib', 'calendar', []],
  ['fun', 'stdlib', 'calendar:date_to_gregorian_days/1', []],
  ['fun', 'stdlib', 'calendar:date_to_gregorian_days/3', []],
  ['fun', 'stdlib', 'calendar:datetime_to_gregorian_seconds/1', []],
  ['fun', 'stdlib', 'calendar:day_of_the_week/1', []],
  ['fun', 'stdlib', 'calendar:day_of_the_week/3', []],
  ['fun', 'stdlib', 'calendar:gregorian_days_to_date/1', []],
  ['fun', 'stdlib', 'calendar:gregorian_seconds_to_datetime/1', []],
  ['fun', 'stdlib', 'calendar:is_leap_year/1', []],
  ['fun', 'stdlib', 'calendar:iso_week_number/0', []],
  ['fun', 'stdlib', 'calendar:iso_week_number/1', []],
  ['fun', 'stdlib', 'calendar:last_day_of_the_month/2', []],
  ['fun', 'stdlib', 'calendar:local_time/0', []],
  ['fun', 'stdlib', 'calendar:local_time_to_universal_time/1', []],
  ['fun', 'stdlib', 'calendar:local_time_to_universal_time_dst/1', []],
  ['fun', 'stdlib', 'calendar:now_to_local_time/1', []],
  ['fun', 'stdlib', 'calendar:now_to_universal_time/1', []],
  ['fun', 'stdlib', 'calendar:now_to_datetime/1', []],
  ['fun', 'stdlib', 'calendar:seconds_to_daystime/1', []],
  ['fun', 'stdlib', 'calendar:seconds_to_time/1', []],
  ['fun', 'stdlib', 'calendar:time_difference/2', []],
  ['fun', 'stdlib', 'calendar:time_to_seconds/1', []],
  ['fun', 'stdlib', 'calendar:universal_time/0', []],
  ['fun', 'stdlib', 'calendar:universal_time_to_local_time/1', []],
  ['fun', 'stdlib', 'calendar:valid_date/1', []],
  ['fun', 'stdlib', 'calendar:valid_date/3', []],
  ['mod', 'stdlib', 'dict', []],
  ['fun', 'stdlib', 'dict:append/3', []],
  ['fun', 'stdlib', 'dict:append_list/3', []],
  ['fun', 'stdlib', 'dict:erase/2', []],
  ['fun', 'stdlib', 'dict:fetch/2', []],
  ['fun', 'stdlib', 'dict:fetch_keys/1', []],
  ['fun', 'stdlib', 'dict:filter/2', []],
  ['fun', 'stdlib', 'dict:find/2', []],
  ['fun', 'stdlib', 'dict:fold/3', []],
  ['fun', 'stdlib', 'dict:from_list/1', []],
  ['fun', 'stdlib', 'dict:is_key/2', []],
  ['fun', 'stdlib', 'dict:map/2', []],
  ['fun', 'stdlib', 'dict:merge/3', []],
  ['fun', 'stdlib', 'dict:new/0', []],
  ['fun', 'stdlib', 'dict:size/1', []],
  ['fun', 'stdlib', 'dict:store/3', []],
  ['fun', 'stdlib', 'dict:to_list/1', []],
  ['fun', 'stdlib', 'dict:update/3', []],
  ['fun', 'stdlib', 'dict:update/4', []],
  ['fun', 'stdlib', 'dict:update_counter/3', []],
  ['mod', 'stdlib', 'digraph', []],
  ['fun', 'stdlib', 'digraph:add_edge/3', []],
  ['fun', 'stdlib', 'digraph:add_edge/4', []],
  ['fun', 'stdlib', 'digraph:add_edge/5', []],
  ['fun', 'stdlib', 'digraph:add_vertex/1', []],
  ['fun', 'stdlib', 'digraph:add_vertex/2', []],
  ['fun', 'stdlib', 'digraph:add_vertex/3', []],
  ['fun', 'stdlib', 'digraph:del_edge/2', []],
  ['fun', 'stdlib', 'digraph:del_edges/2', []],
  ['fun', 'stdlib', 'digraph:del_path/3', []],
  ['fun', 'stdlib', 'digraph:del_vertex/2', []],
  ['fun', 'stdlib', 'digraph:del_vertices/2', []],
  ['fun', 'stdlib', 'digraph:delete/1', []],
  ['fun', 'stdlib', 'digraph:edge/2', []],
  ['fun', 'stdlib', 'digraph:edges/1', []],
  ['fun', 'stdlib', 'digraph:edges/2', []],
  ['fun', 'stdlib', 'digraph:get_cycle/2', []],
  ['fun', 'stdlib', 'digraph:get_path/3', []],
  ['fun', 'stdlib', 'digraph:get_short_cycle/2', []],
  ['fun', 'stdlib', 'digraph:get_short_path/3', []],
  ['fun', 'stdlib', 'digraph:in_degree/2', []],
  ['fun', 'stdlib', 'digraph:in_edges/2', []],
  ['fun', 'stdlib', 'digraph:in_neighbours/2', []],
  ['fun', 'stdlib', 'digraph:info/1', []],
  ['fun', 'stdlib', 'digraph:new/0', []],
  ['fun', 'stdlib', 'digraph:new/1', []],
  ['fun', 'stdlib', 'digraph:no_edges/1', []],
  ['fun', 'stdlib', 'digraph:no_vertices/1', []],
  ['fun', 'stdlib', 'digraph:out_degree/2', []],
  ['fun', 'stdlib', 'digraph:out_edges/2', []],
  ['fun', 'stdlib', 'digraph:out_neighbours/2', []],
  ['fun', 'stdlib', 'digraph:vertex/2', []],
  ['fun', 'stdlib', 'digraph:vertices/1', []],
  ['mod', 'stdlib', 'digraph_utils', []],
  ['fun', 'stdlib', 'digraph_utils:arborescence_root/1', []],
  ['fun', 'stdlib', 'digraph_utils:components/1', []],
  ['fun', 'stdlib', 'digraph_utils:condensation/1', []],
  ['fun', 'stdlib', 'digraph_utils:cyclic_strong_components/1', []],
  ['fun', 'stdlib', 'digraph_utils:is_acyclic/1', []],
  ['fun', 'stdlib', 'digraph_utils:is_arborescence/1', []],
  ['fun', 'stdlib', 'digraph_utils:is_tree/1', []],
  ['fun', 'stdlib', 'digraph_utils:loop_vertices/1', []],
  ['fun', 'stdlib', 'digraph_utils:postorder/1', []],
  ['fun', 'stdlib', 'digraph_utils:preorder/1', []],
  ['fun', 'stdlib', 'digraph_utils:reachable/2', []],
  ['fun', 'stdlib', 'digraph_utils:reachable_neighbours/2', []],
  ['fun', 'stdlib', 'digraph_utils:reaching/2', []],
  ['fun', 'stdlib', 'digraph_utils:reaching_neighbours/2', []],
  ['fun', 'stdlib', 'digraph_utils:strong_components/1', []],
  ['fun', 'stdlib', 'digraph_utils:subgraph/2', []],
  ['fun', 'stdlib', 'digraph_utils:subgraph/3', []],
  ['fun', 'stdlib', 'digraph_utils:topsort/1', []],
  ['mod', 'stdlib', 'epp', []],
  ['fun', 'stdlib', 'epp:open/2', []],
  ['fun', 'stdlib', 'epp:open/3', []],
  ['fun', 'stdlib', 'epp:close/1', []],
  ['fun', 'stdlib', 'epp:parse_erl_form/1', []],
  ['fun', 'stdlib', 'epp:parse_file/3', []],
  ['fun', 'stdlib', 'epp:format_error/1', []],
  ['mod', 'stdlib', 'erl_parse', []],
  ['fun', 'stdlib', 'erl_parse:parse_form/1', []],
  ['fun', 'stdlib', 'erl_parse:parse_exprs/1', []],
  ['fun', 'stdlib', 'erl_parse:parse_term/1', []],
  ['fun', 'stdlib', 'erl_parse:format_error/1', []],
  ['fun', 'stdlib', 'erl_parse:tokens/1', []],
  ['fun', 'stdlib', 'erl_parse:tokens/2', []],
  ['fun', 'stdlib', 'erl_parse:normalise/1', []],
  ['fun', 'stdlib', 'erl_parse:abstract/1', []],
  ['mod', 'stdlib', 'file_sorter', []],
  ['fun', 'stdlib', 'file_sorter:sort/1', []],
  ['fun', 'stdlib', 'file_sorter:sort/2', []],
  ['fun', 'stdlib', 'file_sorter:sort/3', []],
  ['fun', 'stdlib', 'file_sorter:keysort/2', []],
  ['fun', 'stdlib', 'file_sorter:keysort/3', []],
  ['fun', 'stdlib', 'file_sorter:keysort/4', []],
  ['fun', 'stdlib', 'file_sorter:merge/2', []],
  ['fun', 'stdlib', 'file_sorter:merge/3', []],
  ['fun', 'stdlib', 'file_sorter:keymerge/3', []],
  ['fun', 'stdlib', 'file_sorter:keymerge/4', []],
  ['fun', 'stdlib', 'file_sorter:check/1', []],
  ['fun', 'stdlib', 'file_sorter:check/2', []],
  ['fun', 'stdlib', 'file_sorter:keycheck/2', []],
  ['fun', 'stdlib', 'file_sorter:keycheck/3', []],
  ['mod', 'stdlib', 'filelib', []],
  ['fun', 'stdlib', 'filelib:ensure_dir/1', []],
  ['fun', 'stdlib', 'filelib:file_size/1', []],
  ['fun', 'stdlib', 'filelib:fold_files/5', []],
  ['fun', 'stdlib', 'filelib:is_dir/1', []],
  ['fun', 'stdlib', 'filelib:is_file/1', []],
  ['fun', 'stdlib', 'filelib:is_regular/1', []],
  ['fun', 'stdlib', 'filelib:last_modified/1', []],
  ['fun', 'stdlib', 'filelib:wildcard/1', []],
  ['fun', 'stdlib', 'filelib:wildcard/2', []],
  ['mod', 'stdlib', 'filename', []],
  ['fun', 'stdlib', 'filename:absname/1', []],
  ['fun', 'stdlib', 'filename:absname/2', []],
  ['fun', 'stdlib', 'filename:absname_join/2', []],
  ['fun', 'stdlib', 'filename:basename/1', []],
  ['fun', 'stdlib', 'filename:basename/2', []],
  ['fun', 'stdlib', 'filename:dirname/1', []],
  ['fun', 'stdlib', 'filename:extension/1', []],
  ['fun', 'stdlib', 'filename:flatten/1', []],
  ['fun', 'stdlib', 'filename:join/1', []],
  ['fun', 'stdlib', 'filename:join/2', []],
  ['fun', 'stdlib', 'filename:nativename/1', []],
  ['fun', 'stdlib', 'filename:pathtype/1', []],
  ['fun', 'stdlib', 'filename:rootname/1', []],
  ['fun', 'stdlib', 'filename:rootname/2', []],
  ['fun', 'stdlib', 'filename:split/1', []],
  ['fun', 'stdlib', 'filename:find_src/1', []],
  ['fun', 'stdlib', 'filename:find_src/2', []],
  ['mod', 'stdlib', 'io_lib', []],
  ['fun', 'stdlib', 'io_lib:nl/0', []],
  ['fun', 'stdlib', 'io_lib:write/1', []],
  ['fun', 'stdlib', 'io_lib:write/2', []],
  ['fun', 'stdlib', 'io_lib:print/1', []],
  ['fun', 'stdlib', 'io_lib:print/4', []],
  ['fun', 'stdlib', 'io_lib:fwrite/2', []],
  ['fun', 'stdlib', 'io_lib:format/2', []],
  ['fun', 'stdlib', 'io_lib:fread/2', []],
  ['fun', 'stdlib', 'io_lib:fread/3', []],
  ['fun', 'stdlib', 'io_lib:write_atom/1', []],
  ['fun', 'stdlib', 'io_lib:write_string/1', []],
  ['fun', 'stdlib', 'io_lib:write_char/1', []],
  ['fun', 'stdlib', 'io_lib:indentation/2', []],
  ['fun', 'stdlib', 'io_lib:char_list/1', []],
  ['fun', 'stdlib', 'io_lib:deep_char_list/1', []],
  ['fun', 'stdlib', 'io_lib:printable_list/1', []],
  ['mod', 'stdlib', 'lists', []],
  ['fun', 'stdlib', 'lists:all/2', []],
  ['fun', 'stdlib', 'lists:any/2', []],
  ['fun', 'stdlib', 'lists:append/1', []],
  ['fun', 'stdlib', 'lists:append/2', []],
  ['fun', 'stdlib', 'lists:concat/1', []],
  ['fun', 'stdlib', 'lists:delete/2', []],
  ['fun', 'stdlib', 'lists:dropwhile/2', []],
  ['fun', 'stdlib', 'lists:duplicate/2', []],
  ['fun', 'stdlib', 'lists:filter/2', []],
  ['fun', 'stdlib', 'lists:flatlength/1', []],
  ['fun', 'stdlib', 'lists:flatmap/2', []],
  ['fun', 'stdlib', 'lists:flatten/1', []],
  ['fun', 'stdlib', 'lists:flatten/2', []],
  ['fun', 'stdlib', 'lists:foldl/3', []],
  ['fun', 'stdlib', 'lists:foldr/3', []],
  ['fun', 'stdlib', 'lists:foreach/2', []],
  ['fun', 'stdlib', 'lists:keydelete/3', []],
  ['fun', 'stdlib', 'lists:keyfind/3', []],
  ['fun', 'stdlib', 'lists:keymap/3', []],
  ['fun', 'stdlib', 'lists:keymember/3', []],
  ['fun', 'stdlib', 'lists:keymerge/3', []],
  ['fun', 'stdlib', 'lists:keyreplace/4', []],
  ['fun', 'stdlib', 'lists:keysearch/3', []],
  ['fun', 'stdlib', 'lists:keysort/2', []],
  ['fun', 'stdlib', 'lists:keystore/4', []],
  ['fun', 'stdlib', 'lists:keytake/3', []],
  ['fun', 'stdlib', 'lists:last/1', []],
  ['fun', 'stdlib', 'lists:map/2', []],
  ['fun', 'stdlib', 'lists:mapfoldl/3', []],
  ['fun', 'stdlib', 'lists:mapfoldr/3', []],
  ['fun', 'stdlib', 'lists:max/1', []],
  ['fun', 'stdlib', 'lists:member/2', []],
  ['fun', 'stdlib', 'lists:merge/1', []],
  ['fun', 'stdlib', 'lists:merge/2', []],
  ['fun', 'stdlib', 'lists:merge/3', []],
  ['fun', 'stdlib', 'lists:merge3/3', []],
  ['fun', 'stdlib', 'lists:min/1', []],
  ['fun', 'stdlib', 'lists:nth/2', []],
  ['fun', 'stdlib', 'lists:nthtail/2', []],
  ['fun', 'stdlib', 'lists:partition/2', []],
  ['fun', 'stdlib', 'lists:prefix/2', []],
  ['fun', 'stdlib', 'lists:reverse/1', []],
  ['fun', 'stdlib', 'lists:reverse/2', []],
  ['fun', 'stdlib', 'lists:seq/2', []],
  ['fun', 'stdlib', 'lists:seq/3', []],
  ['fun', 'stdlib', 'lists:sort/1', []],
  ['fun', 'stdlib', 'lists:sort/2', []],
  ['fun', 'stdlib', 'lists:split/2', []],
  ['fun', 'stdlib', 'lists:splitwith/2', []],
  ['fun', 'stdlib', 'lists:sublist/2', []],
  ['fun', 'stdlib', 'lists:sublist/3', []],
  ['fun', 'stdlib', 'lists:subtract/2', []],
  ['fun', 'stdlib', 'lists:suffix/2', []],
  ['fun', 'stdlib', 'lists:sum/1', []],
  ['fun', 'stdlib', 'lists:takewhile/2', []],
  ['fun', 'stdlib', 'lists:ukeymerge/3', []],
  ['fun', 'stdlib', 'lists:ukeysort/2', []],
  ['fun', 'stdlib', 'lists:umerge/1', []],
  ['fun', 'stdlib', 'lists:umerge/2', []],
  ['fun', 'stdlib', 'lists:umerge/3', []],
  ['fun', 'stdlib', 'lists:umerge3/3', []],
  ['fun', 'stdlib', 'lists:unzip/1', []],
  ['fun', 'stdlib', 'lists:unzip3/1', []],
  ['fun', 'stdlib', 'lists:usort/1', []],
  ['fun', 'stdlib', 'lists:usort/2', []],
  ['fun', 'stdlib', 'lists:zip/2', []],
  ['fun', 'stdlib', 'lists:zip3/3', []],
  ['fun', 'stdlib', 'lists:zipwith/3', []],
  ['fun', 'stdlib', 'lists:zipwith3/4', []],
  ['mod', 'stdlib', 'math', []],
  ['fun', 'stdlib', 'math:pi/0', []],
  ['fun', 'stdlib', 'math:sin/1', []],
  ['fun', 'stdlib', 'math:cos/1', []],
  ['fun', 'stdlib', 'math:tan/1', []],
  ['fun', 'stdlib', 'math:asin/1', []],
  ['fun', 'stdlib', 'math:acos/1', []],
  ['fun', 'stdlib', 'math:atan/1', []],
  ['fun', 'stdlib', 'math:atan2/2', []],
  ['fun', 'stdlib', 'math:sinh/1', []],
  ['fun', 'stdlib', 'math:cosh/1', []],
  ['fun', 'stdlib', 'math:tanh/1', []],
  ['fun', 'stdlib', 'math:asinh/1', []],
  ['fun', 'stdlib', 'math:acosh/1', []],
  ['fun', 'stdlib', 'math:atanh/1', []],
  ['fun', 'stdlib', 'math:exp/1', []],
  ['fun', 'stdlib', 'math:log/1', []],
  ['fun', 'stdlib', 'math:log10/1', []],
  ['fun', 'stdlib', 'math:pow/2', []],
  ['fun', 'stdlib', 'math:sqrt/1', []],
  ['fun', 'stdlib', 'math:erf/1', []],
  ['fun', 'stdlib', 'math:erfc/1', []],
  ['mod', 'stdlib', 're', []],
  ['fun', 'stdlib', 're:compile/1', []],
  ['fun', 'stdlib', 're:compile/2', []],
  ['fun', 'stdlib', 're:run/2', []],
  ['fun', 'stdlib', 're:run/3', []],
  ['fun', 'stdlib', 're:replace/3', []],
  ['fun', 'stdlib', 're:replace/4', []],
  ['fun', 'stdlib', 're:split/2', []],
  ['fun', 'stdlib', 're:split/3', []],
  ['mod', 'stdlib', 'string', []],
  ['fun', 'stdlib', 'string:len/1', []],
  ['fun', 'stdlib', 'string:equal/2', []],
  ['fun', 'stdlib', 'string:concat/2', []],
  ['fun', 'stdlib', 'string:chr/2', []],
  ['fun', 'stdlib', 'string:rchr/2', []],
  ['fun', 'stdlib', 'string:str/2', []],
  ['fun', 'stdlib', 'string:rstr/2', []],
  ['fun', 'stdlib', 'string:span/2', []],
  ['fun', 'stdlib', 'string:cspan/2', []],
  ['fun', 'stdlib', 'string:substr/2', []],
  ['fun', 'stdlib', 'string:substr/3', []],
  ['fun', 'stdlib', 'string:tokens/2', []],
  ['fun', 'stdlib', 'string:join/2', []],
  ['fun', 'stdlib', 'string:chars/2', []],
  ['fun', 'stdlib', 'string:chars/3', []],
  ['fun', 'stdlib', 'string:copies/2', []],
  ['fun', 'stdlib', 'string:words/1', []],
  ['fun', 'stdlib', 'string:words/2', []],
  ['fun', 'stdlib', 'string:sub_word/2', []],
  ['fun', 'stdlib', 'string:sub_word/3', []],
  ['fun', 'stdlib', 'string:strip/1', []],
  ['fun', 'stdlib', 'string:strip/2', []],
  ['fun', 'stdlib', 'string:strip/3', []],
  ['fun', 'stdlib', 'string:left/2', []],
  ['fun', 'stdlib', 'string:left/3', []],
  ['fun', 'stdlib', 'string:right/2', []],
  ['fun', 'stdlib', 'string:right/3', []],
  ['fun', 'stdlib', 'string:centre/2', []],
  ['fun', 'stdlib', 'string:centre/3', []],
  ['fun', 'stdlib', 'string:sub_string/2', []],
  ['fun', 'stdlib', 'string:sub_string/3', []],
  ['fun', 'stdlib', 'string:to_float/1', []],
  ['fun', 'stdlib', 'string:to_integer/1', []],
  ['fun', 'stdlib', 'string:to_lower/1', []],
  ['fun', 'stdlib', 'string:to_upper/1', []],
  ['mod', 'stdlib', 'timer', []],
  ['fun', 'stdlib', 'timer:start/0', []],
  ['fun', 'stdlib', 'timer:apply_after/4', []],
  ['fun', 'stdlib', 'timer:send_after/2', []],
  ['fun', 'stdlib', 'timer:send_after/3', []],
  ['fun', 'stdlib', 'timer:kill_after/1', []],
  ['fun', 'stdlib', 'timer:kill_after/2', []],
  ['fun', 'stdlib', 'timer:exit_after/2', []],
  ['fun', 'stdlib', 'timer:exit_after/3', []],
  ['fun', 'stdlib', 'timer:apply_interval/4', []],
  ['fun', 'stdlib', 'timer:send_interval/2', []],
  ['fun', 'stdlib', 'timer:send_interval/3', []],
  ['fun', 'stdlib', 'timer:cancel/1', []],
  ['fun', 'stdlib', 'timer:sleep/1', []],
  ['fun', 'stdlib', 'timer:tc/1', []],
  ['fun', 'stdlib', 'timer:tc/2', []],
  ['fun', 'stdlib', 'timer:tc/3', []],
  ['fun', 'stdlib', 'timer:now_diff/2', []],
  ['fun', 'stdlib', 'timer:seconds/1', []],
  ['fun', 'stdlib', 'timer:minutes/1', []],
  ['fun', 'stdlib', 'timer:hours/1', []],
  ['fun', 'stdlib', 'timer:hms/3', []],
];