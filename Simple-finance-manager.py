print("   STUDENT FINANCE MANAGER...made by Sameer Sinha")

total_money = float(input("Enter Your Budget: "))
Room_Rent = 0
Food_Expenses = 0
Other_Expenses = 0

while True:
    print("\n1. Add All Expenses")
    print("2. View Deep Budget Analysis")
    print("3. Exit")
    
    choice = input("Batao Bro 1, 2, ya 3? ")
    
    if choice == "1":
        Room_Rent = float(input("Room_Rent?: "))
        Food_Expenses = float(input("Food_Expenses?: "))
        Other_Expenses = float(input("Other_Expenses?: "))
        
    elif choice == "2":
        total_expenses = Room_Rent + Food_Expenses + Other_Expenses
        
        if total_expenses == 0:
            print("Bro, Pahle Option 1 Choose Kar Ke Expenses Batao!")
        else:
            rent_p = (Room_Rent / total_money) * 100
            food_p = (Food_Expenses / total_money) * 100
            other_p = (Other_Expenses / total_money) * 100
            total_p = (total_expenses / total_money) * 100

            print(f"\nTotal Expense: {total_expenses} ({total_p:.1f}%)")
            print(f"Savings Left: {total_money - total_expenses}")
            print(f"--- Breakdown ---")
            print(f"Rent: {rent_p:.1f}%")
            print(f"Food: {food_p:.1f}%")
            print(f"Other: {other_p:.1f}%")

            if rent_p > 30:
                print("⚠️ Rent 30% se zyada hai, flatmate dhoondo!")

            if food_p > 30:
                print("⚠️ Khana peena budget se bahar jaa raha hai!")

            if other_p > 15:
                print("⚠️ Faltu kharcho par control karo!")

            if total_p > 70:
                print("⚠️ Bro! Mahine ke end me dikkat aane wali hai!")
                
    elif choice == "3":
        print("Bye Bro!")
        break
        
    else:
        print("Bro, only 1,2 or 3!")
