"""Fields for outputting Constant Values in your serializers.
"""
from __future__ import absolute_import, print_function, unicode_literals

from rest_framework import serializers


class ConstantField(serializers.Field):
    """Return a Constant in the serializer.

    Usage:
        my_field = ConstantField(value='My Value')

    Now, in your serializer.data, the value of 'my_field' will be 'My Value'.
    """

    def __init__(self, value, *args, **kwargs):
        """Set the value to be returned.
        """
        self._value = value
        kwargs['read_only'] = True

        super(ConstantField, self).__init__(*args, **kwargs)

    def get_attribute(self, obj):  # pylint: disable=W0613
        """Return the value set by the initializer.
        """
        return self._value

    def to_representation(self, value):
        """Output the constant value.
        """
        return value
