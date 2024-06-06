import datetime
import random
import cyrtranslit


class Student:

    def __init__(self, name, faculty, city, course, group, maildisplay = 0):
        self.first_name = " ".join(name.split()[1:])
        self.password = random.randint(1000, 9999)
        self.last_name = name.split()[0]
        self.city = city
        self.maildisplay = maildisplay
        self.course = course
        self.username = (cyrtranslit.to_latin(faculty +
                                              str(datetime.datetime.now().year) +
                                              self.first_name.split()[0][0] +
                                              self.first_name.split()[1][0] +
                                              self.last_name, "ru")).replace("'", "y", 20)
        self.email = self.username + "@fiztest.gsu.by"
        self.group = (group +
                      (f" ({datetime.datetime.now().year}-{datetime.datetime.now().year + 1})" \
                           if datetime.datetime.now().month > 8 \
                           else f" ({datetime.datetime.now().year - 1}-{datetime.datetime.now().year})"))
