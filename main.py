asteriks = "*" * 25

class Budget:
    def __init__(self):
        self.section_list = []  
        self.section_balance = {}   
    
    
   # Launch of the App
    
    def app_main(self):
        print(asteriks + "Welcom to Baso Budget App".upper() + asteriks)
        if not(self.section_list and self.section_balance):
            print("Your Sections are empty, please add sections")
            self.create_sections()
        else:
            self.operation()
        
   
       

   
    def create_sections(self):
        number_of_sections = int(input("How many sections do you want to create?: "))
        for num in range(1, number_of_sections+1):
            supply_section = input(f"Supply Section Name {num}: ")
            self.section_list.append(supply_section)
            
            
        for section in self.section_list:
            self.section_balance[section] = 0
        print(asteriks + "Sections have been successfully created" + asteriks)
        print(f"List and Balance: {self.section_balance}\n")
        self.operation()

    
    # To perform basic operations
    def operation(self):
        print("""These are the operations that can be performed\n
            [1] - DEPOSIT TO SECTION.
            [2] - WITHDRAWAL FROM SECTION.
            [3] - GET CATEGORY BALANCE.
            [4] - TRANSFER BETWEEN SECTION.
            [5] - CREATE NEW SECTION.
            [6] - CANCEL A SECTION
            [7] - TOTAL BALANCE.
            [0] - EXIT.
        """)
        try:
            action = int(input("Which operation do you want to perform, type 1,2----7: "))
            if action == 1:
                self.deposit_funds()
                
            elif action == 2:
                self.withdraw_funds()
                
            elif action == 3:
                self.get_balance()
                
            elif action == 4:
                self.transfer_funds()
                
            elif action == 5:
                self.add_new_section()

            elif action == 6:
                self.remove_section
                
            elif action == 7:
                self.get_total_balance()
                
            elif action == 0:
                self.exit_app()
                
            else:
                print("You have supplied an invalid input, please try again\n")
                self.operation()   
        except ValueError:
            print("Digit is expected")
            self.operation()


    # Deposit funds to any section
    def deposit_funds(self):
        print("The below are the sections available for deposit?")
        for section in self.section_list:
            print(self.section_list.index(section)+1, section) 
        try:
            select_section = int(input("Select a section to deposit funds to: "))
            selected_section = select_section - 1 
            section = self.section_list[selected_section] 
            print(f"you have chosen to deposit funds to  {section}".capitalize())
            deposit_amount = int(input(f"How much do you want to deposit to {section}: "))
            self.section_balance[section] += deposit_amount
            print(f"You have deposited {deposit_amount} to {section}")
            print(f"Your New Balance:  {self.section_balance}")
            try:
                reply = input("would you like to perform another operation? type yes or no: ".lower())
                if reply == "yes" :
                    self.operation()  
                elif reply =="no" :
                    print(asteriks + "Thanks for using this app" + asteriks)
                    exit()  
                else:
                    print("invalid input")
            except ValueError:
                print("A string is expected, please try again")
        except:
            print("Digit Expected")
            self.operation()

        
    # Withdraw funds from any section
    def withdraw_funds(self):
        print("The below are the sections available for deposit?")
        for section in self.section_list:
            print(self.section_list.index(section)+1, section) 
        try:
            select_section = int(input("Select a section to withdraw funds from: "))
            selected_section = select_section - 1 
            section = self.section_list[selected_section]
            print(f"you have chosen to withdraw funds from  {section}")
            withdrawal_amount = int(input(f"How much do you want to Withdraw from {section}: "))
            if withdrawal_amount >= self.section_balance[section] or self.section_balance[section] <= 0:
                print(f"Insufficient funds, your current balance is {self.section_balance[section]}")
                try:
                    response = input("Would you like to make a deposit? type yes or no: ".lower()) 
                    if response == "yes":
                        self.deposit_funds()
                    elif response == "no":
                        try:
                            reply = input("would you like to perform another operation? type yes or no: ".lower())
                            if reply == "yes" :
                                self.operation()
                            elif reply =="no" :
                                print(asteriks + "Thanks for using this app" + asteriks)
                                exit()
                            else:
                                print("invalid value supplied")
                                self.operation() 
                        except ValueError:
                            print("A string value Expected")
                            self.operation()
                       
                    else:
                        print("invalid parameter supplied")
                        self.operation()   
                except ValueError:
                    print("A string value Expected")
                    self.operation()
            else:
                self.section_balance[section] -= withdrawal_amount
                print(f"{withdrawal_amount} successfully withdrawn from {section}")
                print(f"Updated List and Balance:  {self.section_balance}")
                try:
                    reply = input("would you like to perform another operation? type yes or no: ".lower())
                    if reply == "yes" :
                        self.operation()
                    elif reply =="no" :
                        print(asteriks + "Thanks for using this app" + asteriks)
                        exit()
                    else:
                        print("invalid value supplied")
                        self.operation()
                except ValueError:
                    print("String value Expected")
                    self.operation()           
        except ValueError:
            print("Digit value expected")
            self.operation()


    # Transfer funds from one section to the other
    def transfer_funds(self):
        try:
            # Section sending funds
            print("The below are the sections available for deposit?")
            for section in self.section_list:
                print(self.section_list.index(section)+1, section.upper())
            selected_section1 = int(input("Select a section to transfer funds from: "))
            sending_section = selected_section1 - 1
            section1 = self.section_list[sending_section]
            
            # Section receiving funds
            selected_section2 = int(input("Select category to transfer funds to:"))
            for section in self.section_list:
                print(self.section_list.index(section)+1, section)
            receiving_section =  selected_section2 - 1
            section2 = self.section_list[receiving_section]
            
            
            print(f"you have chosen to transfer funds from  {section1} to {section2}")
            withdrawal_amount = int(input(f"How much do you want to transfer from {section1} to {section2}: "))
            if withdrawal_amount >= self.section_balance[section1] or self.section_balance[section1] <= 0:
                print(f"Insufficient funds, your current balance is {self.section_balance[section1]}")
                try:
                    response = input("Would you like to make a deposit? type yes or no: ".lower()) 
                    if response == "yes" :
                        self.deposit_funds()
                    elif response == "no" :
                        try:
                            reply = input("would you like to perform another operation? type yes or no: ".lower())
                            if reply == "yes" :
                                self.operation()
                            elif reply =="no" :
                                print(asteriks + "Thanks for using this app" + asteriks)
                                exit()
                            else:
                                print("invalid value supplied")
                                self.operation()
                        except ValueError:
                            print("A string value Expected")
                            self.operation()
                    else:
                        print("invalid parameter supplied")
                        self.deposit_funds()   
                except ValueError:
                    print("A string value Expected")
                    self.deposit_funds()
            else:
                self.section_balance[section1] -= withdrawal_amount
                self.section_balance[section2] += withdrawal_amount
                print(f"{withdrawal_amount} Successfully transfered from {section1} to {section2}")
                print(f"Updated List and Balance:  {self.section_balance}")
                try:
                    response = input("Would you like to make another transfer? type yes or no: ".lower()) 
                    if response == "yes" :
                        self.transfer_funds()
                    elif response == "no" :
                        try:
                            reply = input("would you like to perform another operation? type yes or no: ".lower())
                            if reply == "yes" :
                                self.operation()
                            elif reply =="no" :
                                print(asteriks + "Thanks for using this app" + asteriks)
                                self.operation()
                            else:
                                print("invalid value supplied")
                                self.operation() 
                        except ValueError:
                            print("A string value Expected")
                            self.operation()
                    else:
                        print("invalid parameter supplied")
                        self.operation()   
                except ValueError:
                    print("A string value Expected")
                    self.operation()
        except ValueError:
            print("Digit value Expected")
            self.transfer_funds()
     
    
    # Getting balances for each section
    def get_balance(self):
        for section in self.section_balance:
            balance = self.section_balance[section]
        print(f"{section} balance: # {balance}")
        try:
            response = input("would you like to perform another operation? type yes or no: ".lower())
            if response == "yes" :
                self.operation()
            elif response =="no" :
                print(asteriks + "Thanks for using this app" + asteriks)
                exit()
            else:
                print("input not found, please try again")
                self.get_balance() 
        except ValueError:
            print("A string value Expected")
            self.operation()

    
    # Getting the summative balance for all sections    
    def get_total_balance(self):
        total_balance = 0
        for section in self.section_balance:
            balance = self.section_balance[section]
            total_balance += balance
            print(f"Total Balance : # { total_balance}")
            try:
                response = input("would you like to perform another operation? type yes or no: ".lower())
                if response == "yes" :
                    self.operation()  
                elif response =="no" :
                    print(asteriks + "Thanks for using this app" + asteriks)
                    exit()
                else:
                    print("input not found, please try again")
                    self.get_total_balance()
            except ValueError:
                print("A string value Expected")
                self.operation()
        
    
    # To add new sections
    def add_new_section(self):
        supply_section = input(f"Supply section Name: ")
        self.section_list.append(supply_section)
        self.section_balance[supply_section] = 0
        print(asteriks + "New Section successfully added" + asteriks)
        print(f"New Section List: {self.section_list} \nNew List and Balance:  {self.section_balance}.\n")
        
        try:
            response = input("Would you like to add another section? type yes or no: ".lower()) 
            if response == "yes" :
                self.add_new_section()
            elif response == "no" :
                try:
                    reply = input("would you like to perform other operations? type yes or no: ".lower())
                    if reply == "yes" :
                        self.operation()
                    elif reply =="no" :
                        print("Thanks for using this app")
                        exit()
                    else:
                        print("input not found, operation complete")
                        self.operation() 
                except ValueError:
                    print("A string value Expected")
                    self.operation()

                    
            else:
                print("Invalid value Supplied")
                self.operation()    
        except ValueError:
            print("A string value Expected")
            self.operation()
    def exit_app(self):
        print(f"{asteriks}Thanks for using this app{asteriks}\n".upper())
        exit()
Budget().app_main()

