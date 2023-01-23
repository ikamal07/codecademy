import random

class Car:
  def __init__(self, name, speed):
    self.name = name
    self.speed = speed
  
  def race(self):
    distance = random.uniform(0, 100)
    time = distance / self.speed
    print(f"{self.name} raced {distance:.2f} miles in {time:.2f} hours")

car1 = Car("Red Car", 50)
car2 = Car("Blue Car", 60)
car3 = Car("Green Car", 70)

car1.race()
car2.race()
car3.race()
