from __future__ import absolute_import, print_function, unicode_literals

from django.conf import settings
settings.configure()

from rest_framework import serializers

from rest_framework_constant import fields




class MyObject(object):
    """Simple object to test things work nicely.
    """

    def __init__(self):
        """
        """
        self.object_value = 'Test String'


class MySerializer(serializers.Serializer):
    """Test serializer
    """

    constant_field = fields.ConstantField(value='Constant Value')
    object_value = serializers.CharField()


def test_serializer():
    """Test we can create a serializer.
    """
    obj = MyObject()
    serialized = MySerializer(obj)

    output_dict = {
        'object_value': 'Test String',
        'constant_field': 'Constant Value',
    }

    assert dict(serialized.data) == output_dict
