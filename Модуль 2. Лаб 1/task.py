import doctest


class Teacher:
    def __init__(self, first_name: str, last_name: str, subject: str):
        """
        Создание и подготовка к работе объекта "Учитель"

        :param first_name: Имя учителя
        :param last_name: Фамилия учителя
        :param subject: Предмет, который преподает учитель

        Примеры:
        >>> teacher = Teacher('Иван', 'Пупкин', 'Математика')  # инициализация экземпляра класса
        """
        if not isinstance(first_name, str) or not first_name:
            raise ValueError("Имя должно быть непустой строкой")
        if not isinstance(last_name, str) or not last_name:
            raise ValueError("Фамилия должна быть непустой строкой")
        if not isinstance(subject, str) or not subject:
            raise ValueError("Предмет должен быть непустой строкой")

        self.first_name = first_name
        self.last_name = last_name
        self.subject = subject

    def teach(self) -> str:
        """
        Метод, описывающий процесс обучения

        :return: Описание действия

        Примеры:
        >>> teacher = Teacher('Иван', 'Пупкин', 'Математика')
        >>> teacher.teach()
        'Учитель Иван Пупкин проводит урок: Математика.'
        """
        return f'Учитель {self.first_name} {self.last_name} проводит урок: {self.subject}.'

    def get_full_name(self) -> str:
        """
        Метод для получения полного имени преподавателя

        :return: Полное имя преподавателя

        Примеры:
        >>> teacher = Teacher('Иван', 'Иванов', 'Математика')
        >>> teacher.get_full_name()
        'Иван Иванов'
        """
        return f'{self.first_name} {self.last_name}'


class Student:
    def __init__(self, first_name: str, last_name: str, grade_level: int):
        """
        Создание объекта "Ученик"

        :param first_name: Имя ученика
        :param last_name: Фамилия ученика
        :param grade_level: год обучения ученика

        Примеры:
        >>> student = Student('Алексей', 'Смирнов', 10)  # инициализация экземпляра класса
        """
        if not isinstance(first_name, str) or not first_name:
            raise ValueError("Имя должно быть непустой строкой")
        if not isinstance(last_name, str) or not last_name:
            raise ValueError("Фамилия должна быть непустой строкой")
        if not isinstance(grade_level, int) or grade_level <= 0:
            raise ValueError("Уровень класса должен быть положительным числом")

        self.first_name = first_name
        self.last_name = last_name
        self.grade_level = grade_level

    def study(self) -> str:
        """
        Метод, описывающий процесс обучения

        :return: Описание действия

        Примеры:
        >>> student = Student('Алексей', 'Смирнов', 10)
        >>> student.study()
        'Алексей Смирнов учится в 10-м классе.'
        """
        return f'{self.first_name} {self.last_name} учится в {self.grade_level}-м классе.'

    def get_full_name(self) -> str:
        """
        Метод для получения полного имени ученика

        :return: Полное имя ученика

        Примеры:
        >>> student = Student('Алексей', 'Смирнов', 10)
        >>> student.get_full_name()
        'Алексей Смирнов'
        """
        return f'{self.first_name} {self.last_name}'


class OnlineSession:
    def __init__(self, teacher: Teacher, student: Student, date_time: str):
        """
        Создание объекта "Онлайн-сессия"

        :param teacher: Объект преподавателя
        :param student: Объект ученика
        :param date_time: Дата и время сессии

        Примеры:
        >>> teacher = Teacher('Иван', 'Пупкин', 'Математика')
        >>> student = Student('Алексей', 'Смирнов', 10)
        >>> session = OnlineSession(teacher, student, '2023-10-15 14:00')  # инициализация экземпляра класса
        """
        if not isinstance(teacher, Teacher):
            raise TypeError("teacher должен быть экземпляром класса Teacher")
        if not isinstance(student, Student):
            raise TypeError("student должен быть экземпляром класса Student")
        if not isinstance(date_time, str) or not date_time:
            raise ValueError("Дата и время должны быть непустой строкой")

        self.teacher = teacher
        self.student = student
        self.date_time = date_time

    def start_session(self) -> str:
        """
        Метод для начала сессии

        :return: Cообщение о начале урока конкретным учителем с конкретным учеником

        Примеры:
        >>> teacher = Teacher('Иван', 'Пупкин', 'Математика')
        >>> student = Student('Алексей', 'Смирнов', 10)
        >>> session = OnlineSession(teacher, student, '2023-10-15 14:00')
        >>> session.start_session()  # начинает сессию
        'Начал урок Иван Пупкин с Алексей Смирнов: 2023-10-15 14:00.'
        """
        return f"Начал урок {self.teacher.get_full_name()} с {self.student.get_full_name()}: {self.date_time}."

    def end_session(self) -> str:
        """
        Метод для завершения сессии

        :return: Cообщение об окончании урока конкретным учителем с конкретным учеником

        Примеры:
        >>> teacher = Teacher('Иван', 'Пупкин', 'Математика')
        >>> student = Student('Алексей', 'Смирнов', 10)
        >>> session = OnlineSession(teacher, student, '2023-10-15 14:00')
        >>> session.end_session()  # завершает сессию
        'Иван Пупкин завершил урок с Алексей Смирнов.'
        """
        return f"{self.teacher.get_full_name()} завершил урок с {self.student.get_full_name()}."


# Пример тестирования
if __name__ == "__main__":
    doctest.testmod()  # Тестирование примеров в документации
