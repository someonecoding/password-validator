from abc import ABC, abstractclassmethod



class AbstractBaseValidator(ABC):

    value_type = str
    
    class ValidationError(Exception):
        def __init__(self, message):
            self.message = message

    class ValueTypeError(Exception):
        def __init__(self, message):
            self.message = message

    @abstractclassmethod
    def validate_type(cls, value):
        if not isinstance(value, cls.value_type):
            raise cls.ValueTypeError(f'Value type must be {cls.value_type}.')

    @abstractclassmethod
    def validate(cls, value):
        cls.validate_type(value)


class MinLengthValidator(AbstractBaseValidator):

    min_length = 4

    @classmethod
    def validate(cls, value):
        super().validate(value)
        if not len(value) >= cls.min_length:
            raise cls.ValidationError(f'Length must be at least {cls.min_length}')


class MaxLengthValidator(AbstractBaseValidator):

    max_length = 6

    @classmethod
    def validate(cls, value):
        super().validate(value)
        if not len(value) <= cls.max_length:
            raise cls.ValidationError(f'Length must be not bigger than {cls.max_length}')


if __name__ == '__main__':
    pass