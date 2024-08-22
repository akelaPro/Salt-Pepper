class Dessert:
    def __init__(self, name=None, calories=0):
        self._name = name
        self._calories = calories

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
        self._calories = value


    def is_healthy(self):
        if isinstance(self.calories, str):
            return False
        return self._calories < 200

    def is_delicious(self):
        return True




class JellyBean(Dessert):
    def __init__(self, flavor=None, name=None, calories=0):
        super().__init__(name, calories)
        self._flavor = flavor

    @property
    def flavor(self):
        return self._flavor

    @flavor.setter
    def flavor(self, value):
        self._flavor = value

    def is_delicious(self):
        return False if self._flavor == 'black licorice' else super().is_delicious()
    