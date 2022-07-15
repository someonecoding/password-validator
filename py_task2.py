from abc import ABC, abstractclassmethod
import re



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


class AbstractRegExValidator(AbstractBaseValidator, ABC):
    re_pattern = r'.'
    has_to_contain = True
    error_message = 'Pattern validation failed!'

    @abstractclassmethod
    def validate(cls, value):
        super().validate(value)
        if not cls.has_to_contain == bool(re.findall(cls.re_pattern, value)):
            raise cls.ValidationError(cls.error_message)


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


class ValidatorsGroup(ABC):

    validators = []

    @abstractclassmethod
    def validate(cls, value):
        errors = []

        for validator in cls.validators:
            try:
                validator.validate(value)
            except AbstractBaseValidator.ValidationError as e:
                errors.append(e.message)

        return errors


class PasswordValidatorsGroup(ValidatorsGroup):
    validators = [AbstractRegExValidator]



if __name__ == '__main__':
    pass