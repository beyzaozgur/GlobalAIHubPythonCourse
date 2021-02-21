#Beyza Özgür

class Food():
    def __init__(self):
        self.ingredients = []
        self.cooking_time = cooking_time

    def cook(self, cooking_time):
        print("Your food is being cooked... It will take {} minutes...".format(cooking_time))

    def add_salt(self):
        print("More salt is being added to your food...")

    def add_ketchup(self):
        print("Ketchup is being added to your food...")
        self.ingredients.append("ketchup")

    def add_mayonnaise(self):
        print("Mayonnaise is being added to your food...")
        self.ingredients.append("mayonnaise")

    def add_ingredient(self, ingredient):
        print("{} is being added to your food...".format(ingredient))
        self.ingredients.append(ingredient)

    def remove_ingredient(self, ingredient):
        index = self.ingredients.index(ingredient)
        print("{} is being removed from your food...".format(ingredient))
        self.ingredients.pop(index)

    def show_ingredients(self):
        print("INGREDIENTS:\n")
        for i in range(len(self.ingredients)):
            print(self.ingredients[i])
        print()


class Kumpir(Food):
    def __init__(self):
        self.ingredients = ["1 potato", "2 table spoon butter", "cheese", "salt"]

    def add_haydari(self):
        print("Haydari is being added to your kumpir...")
        self.ingredients.append("haydari")

    def add_italian_salad(self):
        print("Italian salad is being added to your kumpir...")
        self.ingredients.append("italian salad")

    def add_russian_salad(self):
        print("Russian salad is being added to your kumpir...")
        self.ingredients.append("russian salad")

    def add_olive(self):
        print("Olives are being added to your kumpir...")
        self.ingredients.append("olive")


class Pizza(Food):
    def __init__(self):
        self.ingredients = ["flour", "olive oil", "tomato sauce", "cheese", "olive", "salami", "mushroom"]

    def cut_to_slices(self, slice_number):
        print("Your pizza is being cut to {} slices.".format(slice_number))


class Hamburger(Food):
    def __init__(self):
        self.ingredients = ["hamburger bread", "lettuce", "cheddar cheese"]

    def choose_menu(self, size, meat_option):
        print("{} size {} hamburger menu is being prepared for you...".format(size, meat_option))
        self.ingredients.append(meat_option)


# cooking/preparing kumpir
kumpir = Kumpir()
print("1) Kumpir")
kumpir.show_ingredients()
kumpir.cook(10)
kumpir.add_haydari()
kumpir.add_olive() # italian or russian salad can also be added by using other methods
kumpir.add_salt()
print()
kumpir.show_ingredients()

# cooking/preparing pizza
pizza = Pizza()
print("2) Pizza")
pizza.show_ingredients()
pizza.cook(30)
pizza.add_ketchup()
pizza.add_mayonnaise()
pizza.cut_to_slices(6)
print()
pizza.show_ingredients()

# cooking/preparing hamburger
hamburger = Hamburger()
print("3) Hamburger")
hamburger.show_ingredients()
hamburger.choose_menu("big", "chicken meat") # we can add another type of meat or choose another size by using the same method
hamburger.cook(20)
print()
hamburger.add_ketchup()
hamburger.add_mayonnaise()
print()
hamburger.show_ingredients()