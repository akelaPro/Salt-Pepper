class Dessert:
    def __init__(self, name=None, calories=0):
        self._name = name
        if isinstance(calories, int):
            self._calories = calories
        else:
            self._calories = 0

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
        if isinstance(value, int):
            self._calories = value
        else:
            self._calories = 0

    def is_healthy(self):
        return self._calories < 200

    def is_delicious(self):
        return True




class JellyBean(Dessert):
    def __init__(self, favor=None, name=None, calories=0):
        super().__init__(name, calories)
        self._favor = favor

    @property
    def favor(self):
        return self._favor

    @favor.setter
    def favor(self, value):
        self._favor = value

    def is_delicious(self):
        return False if self._favor == 'black licorice' else super().is_delicious()
    
