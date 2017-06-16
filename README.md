# Constant Field Type for DRF

A `ConstantField` type for Django REST Framework.

## Installation

```
pip install djangorestframework-constant-field
```

## Usage

Using this is really simple, just set the `value` attribute on your serializer:

```python
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
```

### Why?

This is useful when you're building a serializer to integrate into some third
party system where some of your fields are pre-defined. The above example is
equivalent to:

```python
from rest_framework import serializers


class MySerializer(serializers.Serializer):
    """Custom Serializer
    """

    my_value = serializers.SerializerMethodField()

    def get_my_value(self, obj):
        """Excessive code.
        """
        return 'My Value'
```