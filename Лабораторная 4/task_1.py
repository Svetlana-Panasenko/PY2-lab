class Device:
    """
    Базовый класс для всех электронных устройств
    """

    def __init__(self, model: str, manufacturer: str, operating_system: str):
        """
        Конструктор для базового класса Device.

        :param model: Модель устройства.
        :param manufacturer: Производитель устройства.
        :param operating_system: Операционная система устройства.
        """
        self.model = model
        self.manufacturer = manufacturer
        self.operating_system = operating_system
        self._is_on = False  # Инкапсулированный атрибут, поскольку состояние устройства не должно изменяться напрямую

    def turn_on(self) -> None:
        """
        Включает устройство.
        """
        self._is_on = True
        print(f"{self.model} is now on.")

    def turn_off(self) -> None:
        """
        Выключает устройство.
        """
        self._is_on = False
        print(f"{self.model} is now off.")

    def __str__(self) -> str:
        """
        Возвращает строковое представление устройства.
        """
        return (f"Device: {self.model}, Manufacturer: {self.manufacturer}, "
                f"OS: {self.operating_system}, State: {'On' if self._is_on else 'Off'}")

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление устройства.
        """
        return f"Device(model={self.model}, manufacturer={self.manufacturer}, OS={self.operating_system})"


class Smartphone(Device):
    """
    Дочерний класс Smartphone, наследует от Device.
    """

    def __init__(self, model: str, manufacturer: str, operating_system: str, battery_capacity: int):
        """
        Конструктор для класса Smartphone.

        :param model: Модель смартфона.
        :param manufacturer: Производитель смартфона.
        :param operating_system: Операционная система смартфона.
        :param battery_capacity: Емкость аккумулятора смартфона в мАч.
        """
        super().__init__(model, manufacturer, operating_system)
        self.battery_capacity = battery_capacity
        self.__battery_level = 0  # Encapsulated attribute, as the battery level should not be changed directly.

    def charge(self, percent: int) -> None:
        """
        Заряжает смартфон на указанный процент.

        :param percent: Процент заряда, который необходимо добавить.
        """
        if percent < 0 or percent > 100:
            raise ValueError("Charge percentage must be between 0 and 100.")
        self.__battery_level = min(100, self.__battery_level + percent)
        print(f"Smartphone {self.model} is now {self.__battery_level}% charged.")

    def check_battery_level(self) -> int:
        """
        Возвращает текущий уровень заряда батареи.

        :return: Текущий уровень заряда батареи в процентах.
        """
        return self.__battery_level

    def __str__(self) -> str:
        """
        Переопределенный метод для строкового представления смартфона.
        """
        return (f"Smartphone: {self.model}, Manufacturer: {self.manufacturer}, "
                f"OS: {self.operating_system}, Battery Level: {self.__battery_level}%")

    def __repr__(self) -> str:
        """
        Переопределенный метод для официального строкового представления смартфона.
        """
        return (f"Smartphone(model={self.model}, manufacturer={self.manufacturer}, "
                f"OS={self.operating_system}, battery_capacity={self.battery_capacity})")


class Tablet(Device):
    """
    Дочерний класс Tablet, наследует от Device.
    """

    def __init__(self, model: str, manufacturer: str, operating_system: str, screen_size: float):
        """
        Конструктор для класса Tablet.

        :param model: Модель планшета.
        :param manufacturer: Производитель планшета.
        :param operating_system: Операционная система планшета.
        :param screen_size: Размер экрана планшета в дюймах.
        """
        super().__init__(model, manufacturer, operating_system)
        self.screen_size = screen_size
        self.__brightness = 50  # Encapsulated attribute, as brightness should not be changed directly.

    def set_brightness(self, brightness: int) -> None:
        """
        Устанавливает яркость экрана планшета.

        :param brightness: Уровень яркости от 0 до 100.
        """
        if brightness < 0 or brightness > 100:
            raise ValueError("Brightness must be between 0 and 100.")
        self.__brightness = brightness
        print(f"Brightness of tablet {self.model} is set to {self.__brightness}%.")

    def __str__(self) -> str:
        """
        Переопределенный метод для строкового представления планшета.
        """
        return (f"Tablet: {self.model}, Manufacturer: {self.manufacturer}, "
                f"OS: {self.operating_system}, Screen Size: {self.screen_size} inches, "
                f"Brightness: {self.__brightness}%")

    def __repr__(self) -> str:
        """
        Переопределенный метод для официального строкового представления планшета.
        """
        return (f"Tablet(model={self.model}, manufacturer={self.manufacturer}, "
                f"OS={self.operating_system}, screen_size={self.screen_size})")


if __name__ == "__main__":
    # Create objects
    smartphone = Smartphone("Galaxy S21", "Samsung", "Android", 4000)
    tablet = Tablet("iPad Pro", "Apple", "iOS", 12.9)

    # Use methods
    smartphone.turn_on()
    smartphone.charge(80)
    print(smartphone)

    tablet.turn_on()
    tablet.set_brightness(75)
    print(tablet)
