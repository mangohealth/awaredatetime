Contributing
============

Guidelines
----------
    - Do not change the CHANGELOG or VERSION files. This is the responsibility of the repo and package owners.
    - Before adding a dependency, open an `issue <https://github.com/mangohealth/awaredatetime/issues>`_ to discuss why the dependency is needed.
    - Follow the `Google Python Style Guide <https://google.github.io/styleguide/pyguide.html>`_.

Steps
-----
1. Setup the development environment
   .. code:: bash
             pip install -U -r requirements.dev.txt
1. Make your changes
1. Add unittests for your changes
1. Ensure unittests are passing
   .. code:: bash
             python setup.py test
1. Ensure that you're meeting the style guide
   .. code:: bash
             flake8 awaredatetime
1. Ensure that your changes have proper test coverage
   .. code:: bash
             coverage run --source=awaredatetime setup.py test; coverage html; ls htmlcov/index.html
1. Open a `PR <https://github.com/mangohealth/awaredatetime/pulls>`_
