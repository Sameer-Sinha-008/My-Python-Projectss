import random

my_dict = {"Hola": "Hello", "Aquí": "Here", "Allí": "There", "Papa": "Potato", "Papá": "Father"}
score = 0

for spanish_word, english_meaning in my_dict.items():
  all_meanings = list(my_dict.values())  
  wrong_options = all_meanings.copy()
  wrong_options.remove(english_meaning)
  options = random.sample(wrong_options, 3)
  options.append(english_meaning)
  random.shuffle(options)
  
  print(f"\nWhat is the meaning of '{spanish_word}'?")
  print(f"1. {options[0]}")
  print(f"2. {options[1]}")
  print(f"3. {options[2]}")
  print(f"4. {options[3]}")
  
  user_choice = int(input("Enter Choice (1-4): "))
  
  if options[user_choice - 1] == english_meaning:
      print("Correct!")
      score += 1
  else:
      print("Wrong!")
      
print("\n" + "=" * 30)
print(f"Game Over!! Your Final Score: {score}/{len(my_dict)}")
print("=" * 30)
