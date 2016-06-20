from __future__ import unicode_literals, absolute_import

# import built-in modules
import datetime

# import 3rd party modules
import pytz
import unittest2 as unittest

# awaredatetime imports
from awaredatetime import AwareDatetime
from awaredatetime.config import DEFAULT_TIMEZONE


class AwareDatetimeHasTzinfo(unittest.TestCase):
    """
    Test that all instance method, classmethods, and constants in AwareDatetime that return
    datetime.datetime compatible objects are timezone aware
    """
    def setUp(self):
        super(AwareDatetimeHasTzinfo, self).setUp()
        self.datetime = datetime.datetime(2015, 1, 1)
        self.date = datetime.date(2015, 1, 1)
        self.aware_datetime = AwareDatetime(2015, 1, 1)

    def test_aware_datetime_new(self):
        self.assertIsNotNone(self.aware_datetime.tzinfo)

    def test_aware_datetime_today(self):
        self.assertIsNotNone(AwareDatetime.today().tzinfo)

    def test_aware_datetime_now(self):
        self.assertIsNotNone(AwareDatetime.now().tzinfo)

    def test_aware_datetime_utcnow(self):
        self.assertEqual(AwareDatetime.utcnow().tzinfo, pytz.utc)

    def test_aware_datetime_fromtimestamp(self):
        self.assertIsNotNone(AwareDatetime.fromtimestamp(1).tzinfo)

    def test_aware_datetime_utcfromtimestamp(self):
        self.assertIsNotNone(AwareDatetime.utcfromtimestamp(1).tzinfo)

    def test_aware_datetime_fromordinal(self):
        self.assertIsNotNone(AwareDatetime.fromordinal(1).tzinfo)

    def test_aware_datetime_combine(self):
        self.assertIsNotNone(AwareDatetime.combine(self.date, datetime.time()).tzinfo)

    def test_aware_datetime_strptime(self):
        self.assertIsNotNone(AwareDatetime.strptime("20150401", "%Y%m%d").tzinfo)

    def test_aware_datetime_from_datetime(self):
        self.assertIsNotNone(AwareDatetime.from_datetime(self.datetime).tzinfo)
        self.assertIsNotNone(AwareDatetime.from_datetime(self.aware_datetime).tzinfo)

    def test_aware_datetime_time(self):
        self.assertIsNone(self.aware_datetime.time().tzinfo)

    def test_aware_datetime_timetz(self):
        self.assertIsNotNone(self.aware_datetime.timetz().tzinfo)

    def test_aware_datetime_replace_year(self):
        new_year = 2014
        self.assertNotEqual(self.aware_datetime.year, new_year)
        new_aware_datetime = self.aware_datetime.replace(year=new_year)
        self.assertEqual(new_aware_datetime.year, new_year)
        self.assertIsNotNone(new_aware_datetime.tzinfo)

    def test_aware_datetime_replace_month(self):
        new_month = 2
        self.assertNotEqual(self.aware_datetime.month, new_month)
        new_aware_datetime = self.aware_datetime.replace(month=new_month)
        self.assertEqual(new_aware_datetime.month, new_month)
        self.assertIsNotNone(new_aware_datetime.tzinfo)

    def test_aware_datetime_replace_day(self):
        new_day = 2
        self.assertNotEqual(self.aware_datetime.month, new_day)
        new_aware_datetime = self.aware_datetime.replace(day=new_day)
        self.assertEqual(new_aware_datetime.day, new_day)
        self.assertIsNotNone(new_aware_datetime.tzinfo)

    def test_aware_datetime_replace_hour(self):
        new_hour = 1
        self.assertNotEqual(self.aware_datetime.hour, new_hour)
        new_aware_datetime = self.aware_datetime.replace(hour=new_hour)
        self.assertEqual(new_aware_datetime.hour, new_hour)
        self.assertIsNotNone(new_aware_datetime.tzinfo)

    def test_aware_datetime_replace_minute(self):
        new_minute = 1
        self.assertNotEqual(self.aware_datetime.minute, new_minute)
        new_aware_datetime = self.aware_datetime.replace(minute=new_minute)
        self.assertEqual(new_aware_datetime.minute, new_minute)
        self.assertIsNotNone(new_aware_datetime.tzinfo)

    def test_aware_datetime_replace_second(self):
        new_second = 1
        self.assertNotEqual(self.aware_datetime.second, new_second)
        new_aware_datetime = self.aware_datetime.replace(second=new_second)
        self.assertEqual(new_aware_datetime.second, new_second)
        self.assertIsNotNone(new_aware_datetime.tzinfo)

    def test_aware_datetime_replace_microsecond(self):
        new_microsecond = 1
        self.assertNotEqual(self.aware_datetime.microsecond, new_microsecond)
        new_aware_datetime = self.aware_datetime.replace(microsecond=new_microsecond)
        self.assertEqual(new_aware_datetime.microsecond, new_microsecond)
        self.assertIsNotNone(new_aware_datetime.tzinfo)

    def test_aware_datetime_replace_tzinfo(self):
        new_timezone = pytz.timezone("US/Pacific")
        self.assertNotEqual(self.aware_datetime.tzinfo, new_timezone)
        new_aware_datetime = self.aware_datetime.replace(tzinfo=new_timezone)
        self.assertEqual(new_aware_datetime.tzinfo, new_timezone)
        self.assertIsNotNone(new_aware_datetime.tzinfo)

        with self.assertRaisesRegexp(ValueError, "tzinfo cannot be removed or set to None for AwareDatetime objects"):
            self.aware_datetime.replace(tzinfo=None)
        with self.assertRaisesRegexp(ValueError, "tzinfo cannot be removed or set to None for AwareDatetime objects"):
            self.aware_datetime.replace(2014, 2, 2, 1, 1, 1, 1, None)

    def test_aware_datetime_astimezone(self):
        new_timezone = pytz.timezone("EST")
        # new_timezone must an instance of StaticTzInfo to avoid complications with timezone comparison
        self.assertIsInstance(new_timezone, pytz.tzinfo.StaticTzInfo)
        self.assertNotEqual(self.aware_datetime.tzinfo, new_timezone)

        new_aware_datetime = self.aware_datetime.astimezone(tz=new_timezone)
        self.assertEqual(new_aware_datetime.tzinfo, new_timezone)

    def test_aware_datetime_utcoffset(self):
        self.assertEqual(self.aware_datetime.utcoffset(), datetime.timedelta(seconds=0))

    def test_aware_datetime_min(self):
        self.assertEqual(AwareDatetime.min, datetime.datetime.min.replace(tzinfo=DEFAULT_TIMEZONE))

    def test_aware_datetime_max(self):
        self.assertEqual(AwareDatetime.max, datetime.datetime.max.replace(tzinfo=DEFAULT_TIMEZONE))


class AwareDatetimeDefaultTimezone(unittest.TestCase):
    """
    Test that all the different ways the default timezone for AwareDatetime is determined
    """


class AwareDatetimePytzCompatibilityTestCase(unittest.TestCase):
    """
    Test that all the different ways the default timezone for AwareDatetime is determined
    """
    def setUp(self):
        super(AwareDatetimePytzCompatibilityTestCase, self).setUp()
        self.pytz_tzinfo = pytz.timezone("US/Pacific")
        self.aware_datetime = AwareDatetime(2015, 1, 1)

    def test_normalize(self):
        self.assertNotEqual(self.pytz_tzinfo, self.aware_datetime.tzinfo)
        pinned_naive_datetime = datetime.datetime(2015, 1, 1)
        self.assertNotEqual(self.pytz_tzinfo.utcoffset(pinned_naive_datetime), self.aware_datetime.tzinfo.utcoffset(pinned_naive_datetime))

    def test_localize(self):
        self.assertNotEqual(self.pytz_tzinfo, self.aware_datetime.tzinfo)
        pinned_naive_datetime = datetime.datetime(2015, 1, 1)
        self.assertNotEqual(self.pytz_tzinfo.utcoffset(pinned_naive_datetime), self.aware_datetime.tzinfo.utcoffset(pinned_naive_datetime))

    def test_fromutc(self):
        self.assertNotEqual(self.pytz_tzinfo, self.aware_datetime.tzinfo)
        pinned_naive_datetime = datetime.datetime(2015, 1, 1)
        self.assertNotEqual(self.pytz_tzinfo.utcoffset(pinned_naive_datetime), self.aware_datetime.tzinfo.utcoffset(pinned_naive_datetime))

    def test_dst(self):
        self.assertNotEqual(self.pytz_tzinfo, self.aware_datetime.tzinfo)
        pinned_naive_datetime = datetime.datetime(2015, 1, 1)
        self.assertNotEqual(self.pytz_tzinfo.utcoffset(pinned_naive_datetime), self.aware_datetime.tzinfo.utcoffset(pinned_naive_datetime))
