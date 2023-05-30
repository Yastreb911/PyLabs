import tkinter as tk


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.reiting = 0

    def open_restaurant(self):
        print("Ресторан открыт")
        return "Ресторан открыт"

    def describe_restaurant(self):
        print(f'{self.restaurant_name} {self.cuisine_type}')
        return (f'{self.restaurant_name} {self.cuisine_type}')

    def rupdate(self, addr):
        self.reiting += addr
        print(self.reiting)
        return self.reiting


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors, place, time):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
        self.place = place
        self.time = time

    def IceCreamTypes(self):
        print(self.flavors)
        Window = tk.Tk()
        Window.title("IceCreamStand")
        ForText = ""
        for text in self.flavors:
            ForText += str(text) + str("\n")
        Label = tk.Label(Window, text=str(ForText))
        Label.grid(column=2, row=1)
        Window.mainloop()
        return self.flavors

    def IceCreamTypesAdd(self, To_Add):
        self.flavors.append(To_Add)
        return self.flavors

    def IceCreamTypesRem(self, To_Del):
        self.flavors.remove(To_Del)
        return self.flavors.remove

    def IceCreamTypesChk(self, To_Chk):
        To_Chk = self.flavors.count(To_Chk)
        if To_Chk > 0:
            print("Есть в наличии")
        else:
            print("Нет в наличии")
        return To_Chk


NewRestaurant = Restaurant("Dom", "Китайская")
ElseRest = Restaurant("The Best", "Японская")
print(NewRestaurant.restaurant_name)
print(NewRestaurant.cuisine_type)
NewRestaurant.describe_restaurant()
NewRestaurant.open_restaurant()
ElseRest.describe_restaurant()
NewRestaurant.rupdate(10)
NewRestaurant.rupdate(20)
print(ElseRest.reiting)

IceCreamStand = IceCreamStand("Fol", "Русская", ["Кремовое", "ванильное", "клубничное"], "Новочеркасский,45", "10:00 - 22:00")
IceCreamStand.IceCreamTypes()
IceCreamStand.IceCreamTypesAdd("шоколадное")
Types = IceCreamStand.IceCreamTypes()
print(Types)

