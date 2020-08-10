# 用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个
class Apple:
    def __init__(self, color, taste, price, place):
        self.color = color
        self.taste = taste
        self.price = price
        self.place = place


class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def run(self):
        print(f"{self.name} is running")

    def eat(self):
        print(f"{self.name} is eating")

    def my_dog(self):
        print(f"My dog's name is {self.name} .")
        print(f"He is {self.age} years old")
        print(f"He is a {self.breed}")


class Computer:
    def __init__(self, cpu, mem, displayer, mainboard, power):
        self.cpu = cpu
        self.mem = mem
        self.displayer = displayer
        self.mainboard = mainboard
        self.power = power

    def start_up(self):
        print("My computer is starting up")

    def shutdown(self):
        print("My computer is power off")

    def run_software(self, software):
        print(f"My computer is runnning {software}")


class kiana:
    def __init__(self, gender, weapon, skill, attribute):
        self.gender = gender
        self.weapon = weapon
        self.skill = skill
        self.attribute = attribute

    def attack(self, enemy):
        print(f"Kiana is running to the {enemy} .\n She will defeat it ! ")

    def change_weapon(self, new_weapon):
        print(f"Kiana changed her weapon from {self.weapon} to {new_weapon}")


class super_saiyan:
    def __init__(self,name, race, skill, status):
        self.name =name
        self.race = race
        self.skill = skill
        self.status = status

    def use_skill(self):
        print(f"{self.name} has used {self.skill} to attack his enemy!")
    def transfiguration(self,stage):
        print(f"{self.name} transforms into a super Saiyan 4 ")