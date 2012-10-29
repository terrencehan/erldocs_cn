name:init/1
def:init([]) ->
        {'ok', {{'simple_one_for_one', 4, 3600},
		[{'dets', {'dets', 'istart_link', []},
		  'temporary', 30000, 'worker', ['dets']}]}}

name:start_link/0
def:start_link() -> {'ok', pid()} | 'ignore' | {'error', term()}

