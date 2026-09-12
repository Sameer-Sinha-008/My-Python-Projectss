from deep_translator import GoogleTranslator

def start_translator():
    print("=" * 45)
    print("       DYNAMIC UNIVERSAL TRANSLATOR ")
    print("=" * 45)
    print("Language Codes: en (English), hi (Hindi), es (Spanish), fr (French), auto (Auto Detect)\n")

    while True:
        print("-" * 45)
        print("1. Translate Text ")
        print("2. Exit Program ")
        
        choice = input("\nApna option chuno (1 ya 2): ").strip()

        if choice == '2':
            print("\n Translator Band Ho Raha Hai... Bye Bye! ")
            break
            
        elif choice == '1':
            source_lang = input("\nSource Language (e.g. 'auto', 'en', 'hi'): ").lower().strip()
            target_lang = input("Target Language (e.g. 'es', 'hi', 'en'): ").lower().strip()
            text = input("Translate karne wala Text likho: ").strip()

            try:
                print("\n Translating...")
                translated = GoogleTranslator(source=source_lang, target=target_lang).translate(text)
                
                print("\n --- RESULT --- ")
                print(f"Original Text : {text}")
                print(f"Translated    : {translated}\n")
                
            except Exception as e:
                print("\n Error: Internet connection check karo ya Language Code sahi daalo!")
                
        else:
            print("\n Invalid option! Bus 1 ya 2 dabao.")

# Run Translator
start_translator()
