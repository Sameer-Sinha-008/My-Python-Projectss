g = "Chemistry's Valency"
print(g)


with open("Chemistry.txt", "w") as f:
    f.write("Hydrogen:1\n")
    f.write("Oxygen:2\n")
    f.write("Sodium:1\n")
    f.write("Magnesium:2\n")
print("Everything is in System Now.")


check_answer = lambda user_ans, real_ans: user_ans.strip() == real_ans.strip()


with open("Chemistry.txt", "r") as f:
    data = f.readlines()

print("\n---- 🧪 STARTING VALENCY QUIZ 🧪 ----\n")

for line in data:

    element, valency = line.split(":")
    
    
    user_input = input(f"Batao Sameer, {element} ki valency kya hai? : ")
    

    if check_answer(user_input, valency):
        print("✅ Wah bhai! Ekdum sahi jawab.\n")
    else:
        print(f"❌ Oops! Galat jawab. Sahi valency {valency.strip()} hai.\n")

print("---- QUIZ FINISHED ----")
