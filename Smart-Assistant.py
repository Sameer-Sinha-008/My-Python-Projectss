from datetime import datetime
from deep_translator import GoogleTranslator

# ------------------ JARVIS GREETING MODULE ------------------
def get_jarvis_greeting():
    now = datetime.now()
    current_hour = now.hour
    
    time_str = now.strftime("%I:%M %p")
    date_str = now.strftime("%d %b, %Y")
    
    if 5 <= current_hour < 12:
        greeting = "Good Morning, Boss!"
    elif 12 <= current_hour < 17:
        greeting = "Good Afternoon, Boss!"
    elif 17 <= current_hour < 21:
        greeting = "Good Evening, Boss!"
    else:
        greeting = "Late Night Coding Session, Boss?"
        
    print(f"\n[AI] {greeting}")
    print(f"[Date] : {date_str}")
    print(f"[Time] : {time_str}")


# ------------------ CALCULATOR MODULE ------------------
def run_calculator():
    calculator = "SAMEER'S CALCULATOR"
    print(f"\n=== {calculator} ===")
    
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))
    
    sum_result = num1 + num2
    sub_result = num1 - num2
    mul_result = num1 * num2
    div_result = num1 / num2
    root1 = num1 ** 0.5
    root2 = num2 ** 0.5
    square1 = num1 * num1
    square2 = num2 * num2
    pow_result = num1 ** num2
    
    print(f"Sum (+) : {sum_result}")
    print(f"Subtraction (-) : {sub_result}")
    print(f"Multiply (x) : {mul_result}")
    print(f"Division (/) : {div_result}")
    print(f"Root (Sqrt) : {root1} and {root2}")
    print(f"Square (Sq) : {square1} and {square2}")
    print(f"Power (Pow) : {pow_result}")


# ------------------ CIPHER MODULE ------------------
class SecretAgentCipher:
    def __init__(self, shift_key=4):
        self.shift = shift_key

    def encrypt(self, message):
        encrypted_text = ""
        for char in message:
            encrypted_text += chr(ord(char) + self.shift)
        return encrypted_text

    def decrypt(self, encrypted_message):
        decrypted_text = ""
        for char in encrypted_message:
            decrypted_text += chr(ord(char) - self.shift)
        return decrypted_text

def run_cipher():
    agent = SecretAgentCipher()

    print("\n--- SECRET AGENT CIPHER SYSTEM ---")
    print("1. Message Encode (Hide)")
    print("2. Message Decode (Reveal)")

    choice = input("\nKya karna chahte ho? (1 ya 2 daalo): ")

    if choice == "1":
        secret_msg = input("\nAsli message likho jo chhupana hai: ")
        code_word = agent.encrypt(secret_msg)
        print(f"\n[LOCKED] Secret Code:\n-> {code_word}")

    elif choice == "2":
        code_word = input("\nWoh secret code yahan paste karo: ")
        asli_msg = agent.decrypt(code_word)
        print(f"\n[UNLOCKED] Asli Message:\n-> {asli_msg}")

    else:
        print("Galat option bhai! 1 ya 2 hi dabana tha.")


# ------------------ TRANSLATOR MODULE ------------------
def run_translator():
    print("\n--- UNIVERSAL TRANSLATOR ---")
    print("Language Codes: en (English), hi (Hindi), es (Spanish), fr (French), auto (Auto Detect)")
    
    try:
        source_lang = input("\nSource Language (e.g. auto, en, hi): ").lower().strip()
        target_lang = input("Target Language (e.g. es, hi, en): ").lower().strip()
        text = input("\nText to translate: ").strip()
        
        translated = GoogleTranslator(source=source_lang, target=target_lang).translate(text)
        
        print(f"\n--- RESULT ({target_lang}) ---")
        print(f"-> {translated}")
        
    except Exception as e:
        print("\n[Error] Network check karo ya Language Code sahi daalo.")


# ------------------ PERMANENT NOTES VAULT MODULE ------------------
def run_notes_vault():
    print("\n--- PERMANENT NOTES VAULT ---")
    print("1. Save New Note")
    print("2. View Saved Notes")
    print("3. Clear All Notes")
    
    choice = input("\nApna option chuno (1, 2, ya 3): ").strip()
    
    if choice == '1':
        note = input("\nWrite your note: ").strip()
        now = datetime.now().strftime("%d-%b-%Y %I:%M %p")
        # File Handling: Append Mode ('a')
        with open("my_assistant_notes.txt", "a") as file:
            file.write(f"[{now}] {note}\n")
        print("[SUCCESS] Note permanently save ho gaya!")
        
    elif choice == '2':
        # File Handling: Read Mode ('r')
        try:
            with open("my_assistant_notes.txt", "r") as file:
                content = file.read()
                if content.strip():
                    print("\n--- YOUR SAVED NOTES ---")
                    print(content)
                else:
                    print("\n[INFO] Vault abhi khali hai!")
        except FileNotFoundError:
            print("\n[INFO] Koi saved notes nahi mile. Pehle kuch note save karo!")
            
    elif choice == '3':
        confirm = input("Kya aap saare notes delete karna chahte ho? (yes/no): ").lower().strip()
        if confirm == 'yes':
            # File Handling: Write Mode ('w') clears existing content
            with open("my_assistant_notes.txt", "w") as file:
                file.write("")
            print("[SUCCESS] Saare notes clear ho gaye!")
        else:
            print("[CANCELLED] Action cancel kar diya gaya.")
            
    else:
        print("[Error] Invalid choice!")


# ------------------ MAIN ASSISTANT LOOP ------------------
print("==========================================")
print("     SMART ASSISTANT SYSTEM v3.0          ")
print("==========================================")

get_jarvis_greeting()

while True:
    print("\n------------------------------------------")
    print("1. Refresh Greeting & Time")
    print("2. Run Calculator")
    print("3. Secret Cipher Encoder")
    print("4. Universal Translator")
    print("5. Mini Notes Vault (File Handling)")
    print("6. Exit Program")
    print("------------------------------------------")
    
    choice = input("Enter Your Choice (1 to 6): ").strip()
    
    if choice == '1':
        get_jarvis_greeting()
    elif choice == '2':
        run_calculator()
    elif choice == '3':
        run_cipher()
    elif choice == '4':
        run_translator()
    elif choice == '5':
        run_notes_vault()
    elif choice == '6':
        print("\n[AI] Goodbye Boss! See you soon.")
        break
    else:
        print("[Error] Invalid Choice! 1 se 6 ke beech option chun-ye.")
  
