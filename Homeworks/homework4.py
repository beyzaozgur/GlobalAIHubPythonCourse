#Beyza Özgür

country_names = ["Turkey","Albania","Germany","China","USA","France","Azerbaijan","Thailand",
                 "Uzbekistan","Tunisia","Guatemala","Argentina","Ethiopia","Finland","Spain",
                 "Qatar","Paraguay","Egypt","Russia"]

city_names = ["İzmir","İstanbul","Ankara","London","Paris","Moscow","Dubai","Tokyo","Seoul",
              "Amsterdam","Berlin","Prague","Beijing","Sydney","Miami","Milan","Munich","Bangkok"]

animal_names = ["Squirrel","Chimpanzee","Otter","Parrot","Shrimp","Raven", "Woodpecker","Hippopotamus","Kangaroo",
                "Hedgehog","Jellyfish","Pelican","Lobster","Ladybug","Alligator","Pigeon","Flamingo"]
words = []

for i in range(len(country_names)):
    words.append(country_names[i])

for i in range(len(city_names)):
    words.append(city_names[i])

for i in range(len(animal_names)):
    words.append(animal_names[i])


import random as rnd

class Words():
   def __init__(self):
     self.word_list = words

   def pick_word(self):
     word = rnd.choice(self.word_list)
     return word.upper()

   def play_the_game(self,random_word):

     hangman = Hangman()
     word_spaces = "_" * len(random_word)
     guessed = False
     guessed_letters = []
     guessed_words = []
     incorrect_guesses = 0
     tries = 5

     print("This word has {} letters. You have {} chances.".format(len(random_word),tries))

     while not guessed and tries > 0:
       letter = input("Please guess a letter or word: ").upper()
       print()
       if len(letter) == 1 and letter.isalpha():
         if letter in guessed_letters:
           print("You have already tried this letter", letter)
         elif letter not in random_word:
           print("Oops, " ,letter, " is not in the word.", "You still have " , tries-1, "chance/s")
           tries -= 1
           guessed_letters.append(letter)
           incorrect_guesses += 1
           hangman.hang_the_man(incorrect_guesses,random_word)
         else:
           print("Congrats,", letter, "is in this word! Keep going!")
           guessed_letters.append(letter)
           word_as_list = list(word_spaces)
           indices = [i for i, x in enumerate(random_word) if x == letter ]
           for index in indices:
             word_as_list[index] = letter
           word_spaces = "".join(word_as_list)
           if "_" not in word_spaces:
             guessed = True
       elif len(letter) == len(random_word) and letter.isalpha():
         if letter in guessed_words:
           print("You already guessed the word", letter)
         elif letter != random_word:
           print("Oops, " ,letter, "is not the word.", "You still have " , tries-1, "chance/s")
           tries -= 1
           guessed_words.append(letter)
           incorrect_guesses += 1
           hangman.hang_the_man(incorrect_guesses,random_word)
         else:
           guessed = True
           word_spaces = random_word
       else:
         print("This is not a valid guess.")
       print(word_spaces)
       print("\n")
     if guessed:
       print("You found the word! Congrats, YOU WON!")
       print()
     else:
       hangman.hang_the_man(incorrect_guesses,random_word)
       print()


class CountryNames(Words):
  def __init__(self):
    self.word_list = country_names

class CityNames(Words):
  def __init__(self):
    self.word_list = city_names

class AnimalNames(Words):
  def __init__(self):
    self.word_list = animal_names

class Hangman():
  def __init__(self):
    self.hangman_status = ["","0","O-","O-|","O-|-","O-|-<"]


  def hang_the_man(self, incorrect_guesses, random_word):
    self.hangman = self.hangman_status[incorrect_guesses]
    print("The man's condition: " ,self.hangman)

    if(incorrect_guesses == 5):
      print("You are dead :( The answer was " + random_word + ". Try again to guess another word!")



check = True

while check:
  selection = int(input("Welcome to GUESS THE WORD hangman game.\n If you want to guess the name of:\n COUNTRIES ---> TYPE 1\n CITIES"
           " ---> TYPE 2\n ANIMALS ---> TYPE 3\n\n TYPE 0 (ZERO) TO QUIT"))

  if(selection == 0):
    break

  elif(selection == 1):
    country = CountryNames()
    random_country = country.pick_word()
    country.play_the_game(random_country)


  elif(selection == 2):
    city = CityNames()
    random_city = city.pick_word()
    city.play_the_game(random_city)


  elif (selection == 3):
    animal = AnimalNames()
    random_animal = animal.pick_word()
    animal.play_the_game(random_animal)


  else:
    print("This is not an option, please try again!")
    print()
    continue
