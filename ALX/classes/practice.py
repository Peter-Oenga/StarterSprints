class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        print("(Initializing {})".format(self.name))
        Robot.population += 1
        
    
    def say_hi(self):
        print("Greetings my masters call me {}".format(self.name))

    @classmethod
    def how_many(cls):
        print("We have {} robots".format(cls.population))

    def die(self):
        print("{} is being destroyed".format(self.name))
        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one".format(self.name))
        else:
            print("There are still {} robots working".format(Robot.population))


droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()

Robot.how_many()