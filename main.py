import time
from loguru import logger

logger.add("log.log")
logger.success("Программа запущена!")


class HowTime:
    speeds = {
        "Рыбе": 2.5,
        "Человеку": 4,
        "Велосипеду": 30,
        "Горилле": 34,
        "Слону": 40,
        "Лосю": 45,
        "Носорогу": 48,
        "Кенгуру": 56,
        "Собаке": 72,
        "Соколу": 80,
        "Лошади": 88,
        "Гепарду": 120,
        "Автомобилю": 200,
        "Мотоциклу": 350,
        "Истребителю": 3700
              }

    def __init__(self):
        self.distance = 0
        self.answer = ""
        logger.info("Рабочий экземпляр создан")

    def ask_distance(self):
        time.sleep(0.5)
        distance = input("Введи расстояние в метрах → ")
        if not distance.isnumeric():
            logger.error(f"Пользователь ввёл не число — {distance}")
            return False
        self.distance = float(distance)
        if self.distance == 0:
            logger.warning("Пользователь ввёл число 0")
        else:
            logger.info(f"Пользователь ввёл число — {self.distance}")
        return True

    def min_to_hours(self, sec):
        logger.info("Запущен перевод секунд в часы и минуты")
        sec = sec % (24 / 3600)
        hour = sec // 3600
        sec %= 3600
        min = sec // 60
        sec %= 60
        temp = "%02d:%02d:%02d" % (hour, min, sec)
        logger.info(f"Получили результат — {temp}")
        return temp

    def math(self):
        logger.info("Начинаем подсчёт")
        for name, speed in self.speeds.items():
            t = (self.distance / 1000) / speed
            t *= 60
            logger.info(f"Подсчёт успешен — {name}, {t}")
            t = self.min_to_hours(t)
            self.final(t, name)
        logger.success("Подсчёт окончен!")
        time.sleep(1)
        print(self.answer)

    def final(self, result: str, name: str):
        temp = f"Для прохождения {int(self.distance)} метров {name} понадобится {result} времени\n"
        logger.info("в результат добавилась строка")
        self.answer += temp


if __name__ == '__main__':
    hw = HowTime()
    good = hw.ask_distance()
    if good:
        hw.math()
    else:
        logger.critical("Ответа от метода нет. Решение не получено.")
