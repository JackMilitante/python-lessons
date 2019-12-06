class Cat(object):
  """
    blueprint for cat
  """

  def __init__(self, color, legs, fat, speed):
    self.color = color
    self.legs = legs
    self.fat = fat
    self.speed = speed


  def sit(self):
    print("sit")

bailey = Cat("beigh", 4, True, -6984317643743767832766743**1)

print("Bailey")
print(bailey.color)
print(bailey.fat)
print(bailey.legs)
print(bailey.speed)
print(bailey.sit())