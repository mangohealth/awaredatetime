from __future__ import unicode_literals, absolute_import

# import built-in modules
import datetime
import traceback

# import 3rd party modules
import pytz

# import modules within this package
from .config import DEFAULT_TIMEZONE, PYTZ_METHODS_ALLOWED_TO_REPLACE_TZINFO

__version__ = open("VERSION").read().strip()


class AwareDatetime(datetime.datetime):
    """
    A datetime object that is always timezone aware
    If tzinfo is not specified, defaults to UTC
    """

    def __new__(cls, *args, **kwargs):
        """
        Need to override __new__() since datetime uses __new__() instead of __init__()
        """
        tzinfo = DEFAULT_TIMEZONE
        if callable(DEFAULT_TIMEZONE):
            tzinfo = DEFAULT_TIMEZONE()

        # Grab tzinfo if specified via positional args
        if len(args) == 8:
            _tzinfo = args[-1]
            # Protect against tzinfo being specified as None
            if _tzinfo:
                tzinfo = _tzinfo
            args = args[:-1]

        # tzinfo can only be specified via args or kwargs, not both
        # get/set tzinfo via kwargs
        _tzinfo = kwargs.pop("tzinfo", tzinfo)
        # Protect against tzinfo being specified as None
        if _tzinfo:
            tzinfo = _tzinfo

        kwargs["tzinfo"] = tzinfo

        return super(AwareDatetime, cls).__new__(cls, *args, **kwargs)

    @classmethod
    def from_datetime(cls, dt):
        """
        Get an AwareDatetime object from a datetime object.
        Can be used to ensure that a datetime object has a timezone (tzinfo)
        """
        return cls(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, dt.microsecond, dt.tzinfo)

    @classmethod
    def utcnow(cls):
        dt = datetime.datetime.utcnow()
        dt = dt.replace(tzinfo=pytz.utc)  # explicitly set the timezone to utc instead of relying on AwareDatetime's default
        return cls.from_datetime(dt)

    def replace(self, *args, **kwargs):
        """
        .. role:: python(code)
                  :language: python

        Prevents :python:`tzinfo` from being removed (or set to None) via :python:`AwareDatetime.replace()`
        since this result in an unaware :python:`datetime.datetime` object.

        Usage of :python:`AwareDatetime.replace()` is discouraged. Instead, use `datetime.timedelta` to modify :python:`datetime.dateime`
        and :python:`AwareDatetime` objects.

        Note: Replacing :python:`tzinfo` will not convert the timezone since other attributes like :python:`hour` may also
        be specified, resulting in ambiguous behavior.
        """
        tzinfo = pytz.utc

        # Grab tzinfo if specified via positional args
        if len(args) == 8:
            tzinfo = args[-1]

        # tzinfo can only be specified via args or kwargs, not both
        tzinfo = kwargs.get("tzinfo", tzinfo)

        if not tzinfo:
            caller_stack, current_stack = traceback.extract_stack(limit=2)
            filename, lineno, func_name, code = caller_stack
            tzinfo_replacement_allowed = "/pytz/" in filename and func_name in PYTZ_METHODS_ALLOWED_TO_REPLACE_TZINFO
            if not tzinfo_replacement_allowed:
                raise ValueError("tzinfo cannot be removed or set to None for AwareDatetime objects")

        return super(AwareDatetime, self).replace(*args, **kwargs)

# Note: The min/max AwareDatetime should never be normalized (or converted to another timezone),
#       since that may overflow the min/max AwareDatetime
AwareDatetime.min = AwareDatetime.from_datetime(datetime.datetime.min)
AwareDatetime.max = AwareDatetime.from_datetime(datetime.datetime.max)


__all__ = [
    "AwareDatetime",
]
