Constant Field Type for DRF
===========================

A ``ConstantField`` type for Django REST Framework.

Installation
------------

::

    pip install djangorestframework-constant-field

Usage
-----

Using this is really simple, just set the ``value`` attribute on your
serializer:

.. code:: python

    from rest_framework import serializers
    from rest_framework_constant.fields import ConstantField


    class MySerializer(serializers.Serializer):
        """Custom Serializer
        """

        my_value = ConstantField(value='My Value')


    serialized = MySerializer()

    print(serialized.data)

    # {
    #     'my_value': 'My Value',
    # }

Why?
~~~~

This is useful when you're building a serializer to integrate into some
third party system where some of your fields are pre-defined. The above
example is equivalent to:

.. code:: python

    from rest_framework import serializers


    class MySerializer(serializers.Serializer):
        """Custom Serializer
        """

        my_value = serializers.SerializerMethodField()

        def get_my_value(self, obj):
            """Excessive code.
            """
            return 'My Value'

Testing & Contributing
----------------------

To build and test this package, simply fork this repo and:

.. code:: bash

    git clone git@github.com:<yourname>/djangorestframework-constant-field.git

    cd djangorestframework-constant-field
    pip install -r requirements.txt
    python setup.py test

The current app is almost completely contained inside
``rest_framework_constant``.
