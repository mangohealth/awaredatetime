.. image:: https://img.shields.io/travis/mangohealth/awaredatetime.svg
    :alt: Build Status
    :target: https://travis-ci.org/mangohealth/awaredatetime/

=============
awaredatetime
=============
Module providing a timezone aware ``datetime.datetime`` compatible object.
Supports CPython 2.6 - 3.5 and PyPy.

----------
Motivation
----------
``datetime.datetime`` objects aren't aware by default.
New projects should always use timezone aware ``datetime.datetime`` objects, but the Python standard library doesn't make that easy.
``AwareDatetime`` is here to help!

You may also have existing code that needs to become timezone aware and migrating code to become timezone aware is tricky.
Using ``AwareDatetime`` will help you track what code has been migrated to support timezone.

---------------------------
awaredatetime.AwareDatetime
---------------------------
A drop-in replacement for ``datetime.datetime`` that always provide timezone aware objects.

Example Usage
=============
.. code:: python

          >>> from awaredatetime import AwareDatetime
          >>> AwareDatetime(2016, 1, 1)
          AwareDatetime(2016, 1, 1, 0, 0, tzinfo=<UTC>)
          >>> import datetime
          >>> AwareDatetime.from_datetime(datetime.datetime(2016, 1, 1))
          AwareDatetime(2016, 1, 1, 0, 0, tzinfo=<UTC>)
          >>>

-----------------------
awaredatetime.AwareTime
-----------------------
Not implemented since times with a timezone don't make sense.
e.g. What's the expected behavior for coverting ``24:00:00+00:00`` to positive UTC offset?

============
Dependencies
============
The only dependency is ``pytz``. We recommend that you use the latest version of ``pytz``, but this package will not force that upon you.

=======================
Migrating Existing Code
=======================


============
Similar work
============
- `datetime_tz`_
  - Another timezone aware drop-in replacement for the ``datetime`` module, but overrides more datetime behavior

.. _`datetime_tz`: https://github.com/mithro/python-datetime-tz
