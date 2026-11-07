from faker import Faker
f = Faker()
def namemybaby():
    my_name = input("Enter your name: ").capitalize()
    my_son = input("Is your child a boy or a girl: ").capitalize()
    for x in range(50):
     if my_son == "Boy":
      print(f.first_name_male(),my_name)
     elif my_son == "Girl":
       print(f.first_name_female(),my_name)
     else:
       print("Please select the correct gender")
       break
namemybaby()
