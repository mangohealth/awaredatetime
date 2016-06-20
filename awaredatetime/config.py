from __future__ import unicode_literals, absolute_import

import pytz

#: The default timezone to use. May be a tzinfo or a function that returns a tzinfo
DEFAULT_TIMEZONE = pytz.utc

PYTZ_METHODS_ALLOWED_TO_REPLACE_TZINFO = [
    "normalize", "localize", "fromutc", "dst"
]
