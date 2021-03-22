class person():
    def __init__(self, name):
        self.name = name
    
    def say_name(self):
        print("My name is {}".format(self.name))

class teacher(person):
    def __init__(self, name, job):
        super(teacher, self).__init__(name)
        self.job = job

    def say_name(self):
        super(teacher, self).say_name()
        print("My salary is 70000 and my job is {}".format(self.job))


#johnny = person('Johnny').say_name
johnny = teacher('johnny','teaching')
johnny.say_name()