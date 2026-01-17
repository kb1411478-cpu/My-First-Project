import json

# All Balance Data
def all_data():
    try:
        with open("ATM_data.txt", "r") as file:
            data=json.load(file)
            return data
    except FileNotFoundError:
        return []

def save_data(money):
    with open("ATM_data.txt","w") as file:
        json.dump(money,file)


# Total Balance show Function
def total_balance(money):
    print("*"*40)
    for index,balance in enumerate(money,start=1):
        print(f"{index}. Total Balance {balance['Balance']}")
    print("*"*40)

# Deposit Function
def deposit(money):
    user = float(input("Enter The Money You Can Deposit: ")) 
    if money:  
        current_balance = float(money[-1]['Balance'])  
        new_balance = current_balance + user 
        money[-1]['Balance'] = str(new_balance)  
    else:
        money.append({'Balance': str(user)})  

    save_data(money)
    

# Withdraw Function
def withdraw(money):
    user = float(input("Enter The Money You Can Withdraw: ")) 
    if money:  
        current_balance = float(money[-1]['Balance'])  
        new_balance = current_balance - user 
        money[-1]['Balance'] = str(new_balance)  
    else:
        money.append({'Balance': str(user)})  

    save_data(money)

def main():
    attemp=0
    max_attemp=4
    while attemp < max_attemp:
        password=int(input("Enter Your Password Pin: "))
        attemp += 1 
        if(password == 2005):
            money=all_data()
            while True:
                print("1. Total Balance")
                print("2. Money Deposit")
                print("3. Money Withdraw")
                print("4. Exit")
                choice=input("Enter These Chose: ")
                if(choice == "1"):
                    total_balance(money)
                elif(choice == "2"):
                    deposit(money)
                elif(choice == "3"):
                    withdraw(money)
                elif(choice == "4"):
                    break
                else:
                    print("Invalid Number || Your number b/w 1 to 4")
                
                
                    
        else:
            print("Please Enter The Correct Password")
               
            
    if attemp == max_attemp:
        print("Sorry, you've used all  attempts.")





if __name__ == "__main__":
    print("\n")
    print("*"*55)
    print("*"+"Welcome To ATM".center(53)+"*")
    print("*"*55)
    main()