============
Contributing
============

----------
Guidelines
----------
- Do not change the CHANGELOG file or ``__version__`` in ``awaredatetime/__init__.py``. This is the responsibility of the repo and package owners.
- Before adding a dependency, open an `issue <https://github.com/mangohealth/awaredatetime/issues>`_ to discuss why the dependency is needed.
- Follow the `Google Python Style Guide <https://google.github.io/styleguide/pyguide.html>`_.

-----
Steps
-----

#. Setup the development environment

   .. code:: bash

             pip install -U -r requirements.dev.txt

#. Make your changes

#. Add unittests for your changes

#. Run tests, which will also check the coding style

   .. code:: bash

             coverage run --source=awaredatetime setup.py test_dev

#. Once tests pass, ensure that your changes have proper test coverage

   .. code:: bash

             coverage html && ls htmlcov/index.html

#. Open a `PR <https://github.com/mangohealth/awaredatetime/pulls>`_
