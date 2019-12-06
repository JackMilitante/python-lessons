class Car(object):
  """
    blueprint for car
  """

  def __init__(self, model, color, company, speed_limit):
    self.color = color
    self.company = company
    self.speed_limit = speed_limit
    self.model = model

  def start(self):
    print("started")

  def stop(self):
    print("stopped")

  def accelarate(self):
    print("accelarating...")
    "accelarator functionality here"

  def change_gear(self, gear_type):
    print("gear changed")
    " gear related functionality here"

maruthi_suzuki = Car("ertiga", "black", "suzuki", 60)
audi = Car("A6", "red", "audi", 80)
#swag my dude
lamborgoinoy = Car("Diablo GT 1", "gold", "lamborgoinoy", 1000000000000000000000000 )

# print(maruthi_suzuki.color)
# print(audi.accelarate())
# print(lamborgoinoy.model)
# print(lamborgoinoy.company)

print(lamborgoinoy.accelarate())
print(lamborgoinoy.model)
print(lamborgoinoy.color)
print(lamborgoinoy.company)
print(lamborgoinoy.speed_limit)
print(audi.accelarate())
print(audi.model)
print(audi.color)
print(audi.company)
print(audi.speed_limit)