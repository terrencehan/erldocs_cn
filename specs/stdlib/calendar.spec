name:date_to_gregorian_days/3
def:date_to_gregorian_days(Year, Month, Day) -> Days
types:
      Year = year(),
      Month = month(),
      Day = day(),
      Days = non_neg_integer()

name:date_to_gregorian_days/1
def:date_to_gregorian_days(Date) -> Days
types:
      Date = date(),
      Days = non_neg_integer()

name:datetime_to_gregorian_seconds/1
def:datetime_to_gregorian_seconds(DateTime) -> Seconds
types:
      DateTime = datetime(),
      Seconds = non_neg_integer()

name:day_of_the_week/3
def:day_of_the_week(Year, Month, Day) -> daynum()
types:
      Year = year(),
      Month = month(),
      Day = day()

name:day_of_the_week/1
def:day_of_the_week(Date) -> daynum()
types:
      Date= date()

name:day_to_year/1
def:day_to_year(non_neg_integer()) -> {year(), day_of_year()}

name:df/2
def:df(year(), month()) -> 0 | 1

name:dm/1
def:dm(month()) ->
	     0 | 31 | 59 | 90 | 120 | 151 | 181 | 212 | 243 | 273 | 304 | 334

name:dty/3
def:dty(year(), non_neg_integer(), non_neg_integer()) ->
		{year(), non_neg_integer()}

name:dy/1
def:dy(integer()) -> non_neg_integer()

name:gregorian_days_of_iso_w01_1/1
def:gregorian_days_of_iso_w01_1(year()) -> non_neg_integer()

name:gregorian_days_to_date/1
def:gregorian_days_to_date(Days) -> date()
types:
      Days = non_neg_integer()

name:gregorian_seconds_to_datetime/1
def:gregorian_seconds_to_datetime(Seconds) -> datetime()
types:
      Seconds = non_neg_integer()

name:is_leap_year/1
def:is_leap_year(Year) -> boolean()
types:
      Year = year()

name:is_leap_year1/1
def:is_leap_year1(year()) -> boolean()

name:iso_week_number/0
def:iso_week_number() -> yearweeknum()

name:iso_week_number/1
def:iso_week_number(Date) -> yearweeknum()
types:
      Date = date()

name:last_day_of_the_month/2
def:last_day_of_the_month(Year, Month) -> LastDay
types:
      Year = year(),
      Month = month(),
      LastDay = ldom()

name:last_day_of_the_month1/2
def:last_day_of_the_month1(year(),month()) -> ldom()

name:local_time/0
def:local_time() -> datetime()

name:local_time_to_universal_time/1
def:local_time_to_universal_time(DateTime1) -> DateTime2
types:
      DateTime1 = datetime1970(),
      DateTime2 = datetime1970()

name:local_time_to_universal_time/2
def:local_time_to_universal_time(datetime1970(),
				   'true' | 'false' | 'undefined') ->
                                          datetime1970()

name:local_time_to_universal_time_dst/1
def:local_time_to_universal_time_dst(DateTime1) -> [DateTime]
types:
      DateTime1 = datetime1970(),
      DateTime = datetime1970()

name:now_to_datetime/1
def:now_to_datetime(Now) -> datetime1970()
types:
      Now = erlang:timestamp()

name:now_to_local_time/1
def:now_to_local_time(Now) -> datetime1970()
types:
      Now = erlang:timestamp()

name:now_to_universal_time/1
def:now_to_universal_time(Now) -> datetime1970()
types:
      Now = erlang:timestamp()

name:seconds_to_daystime/1
def:seconds_to_daystime(Seconds) -> {Days, Time}
types:
      Seconds = integer(),
      Days = integer(),
      Time = time()

name:seconds_to_time/1
def:seconds_to_time(Seconds) -> time()
types:
      Seconds = secs_per_day()

name:time_difference/2
def:time_difference(T1, T2) -> {Days, Time}
types:
      T1 = datetime(),
      T2 = datetime(),
      Days = integer(),
      Time = time()

name:time_to_seconds/1
def:time_to_seconds(Time) -> secs_per_day()
types:
      Time = time()

name:universal_time/0
def:universal_time() -> datetime()

name:universal_time_to_local_time/1
def:universal_time_to_local_time(DateTime) -> datetime()
types:
      DateTime = datetime1970()

name:valid_date/3
def:valid_date(Year, Month, Day) -> boolean()
types:
      Year = integer(),
      Month = integer(),
      Day = integer()

name:valid_date/1
def:valid_date(Date) -> boolean()
types:
      Date = date()

name:valid_date1/3
def:valid_date1(integer(), integer(), integer()) -> boolean()

name:year_day_to_date/2
def:year_day_to_date(year(), day_of_year()) -> {month(), day()}

name:year_day_to_date2/2
def:year_day_to_date2(0 | 1, day_of_year()) -> {month(), 0..30}

