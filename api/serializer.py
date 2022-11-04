from rest_framework import serializers
import enum
from rest_enumfield import EnumField


class Operators(enum.Enum):
    ADDITION = "addition"
    SUBTRACTION = "subtraction"
    MULTIPLICATION = "multiplication"


class MathematicSerializer(serializers.Serializer):

    x = serializers.IntegerField()
    y = serializers.IntegerField()
    operation_type = EnumField(choices=Operators)