class Dog(object):
  """
    blueprint for dog
  """

  def __init__(self, color, legs, mix, breed):
    self.color = color
    self.legs = legs
    self.mix = mix
    self.breed = breed


  def whine(self):
    print("whine")

  def poooop(self):
    print("poooop")

luna = Dog("white", 4, True, "BorderCollie")

print(luna.color)
print(luna.legs)
print(luna.mix)
print(luna.breed)