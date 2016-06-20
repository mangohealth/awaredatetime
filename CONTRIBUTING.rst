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

#. Ensure unittests are passing

   .. code:: bash

             python setup.py test

#. Ensure that you're meeting the style guide

   .. code:: bash

             flake8 awaredatetime

#. Ensure that your changes have proper test coverage

   .. code:: bash

             coverage run --source=awaredatetime setup.py test; coverage html; ls htmlcov/index.html

#. Open a `PR <https://github.com/mangohealth/awaredatetime/pulls>`_
