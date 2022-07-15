from abc import ABC, abstractclassmethod



class AbstractBaseValidator(ABC):
    
    class ValidationError(Exception):
        def __init__(self, message):
            self.message = message

    @abstractclassmethod
    def validate(cls, value):
        pass





if __name__ == '__main__':
    pass
