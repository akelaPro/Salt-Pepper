class Dessert:
    def __init__(self, name=None, calories=0):
        self._name = name
        self._calories = self.validate(calories)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def calories(self):
        return self._calories

    @calories.setter
    def calories(self, value):
        self._calories = self.validate(value)

    @staticmethod
    def validate(value):
        if isinstance(value, str) and value.isdigit():
            return int(value)
        elif isinstance(value, int):
            return value
        else:
            raise ValueError()

    def is_healthy(self):
        return self._calories < 200

    def is_delicious(self):
        return True

