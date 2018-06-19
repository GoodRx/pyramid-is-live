pyramid-is-live
===============

.. image:: https://travis-ci.com/GoodRx/pyramid-is-live.svg
   :target: https://travis-ci.com/GoodRx/pyramid-is-live

``pyramid-is-live`` uses a tween to add an ``is_live`` property to Pyramid
requests, which is ``True`` if the request came from a HTTP interaction and
``False`` otherwise, e.g. if the request came from ``pyramid.paster.bootstrap``.

Getting Started
---------------

1. Install this package::

      pip install pyramid-is-live

2. Include it in your application startup:

   .. code-block:: python

      def main(global_config, **settings):
          config = Configurator(...)
          config.include("pyramid_is_live")
          ...

3. Use ``request.is_live`` in your views and scripts!

Contributing
------------

We use `tox <https://tox.readthedocs.io/en/latest/>`_ to run our tests and
linters.

Run ``tox`` to run all tests and linters.

Run ``tox -e format`` to reformat your code using `Black
<https://black.readthedocs.io/en/stable/>`_ and `isort
<https://github.com/timothycrosley/isort>`_.
