# Test Practical
# Name: Rohith Yerragunta
# student id: 100936904


# constants declaration
TOTAL_NUMBER_OF_SERVERS = 3
MAX_TOTAL_ACCOUNTS = 50

continue_loop = True
# while loop to ask user if they want to continue
while continue_loop:
    
    # variables to store input
    accounts_for_first_server = int(input('enter the number of account for first server: '))
    accounts_for_second_server = int(input('enter the number of account for second server: '))
    
    # variable to store accounts entered on each server
    total_entered_accounts = accounts_for_first_server + accounts_for_second_server
    
    # variable to store the remaining number of accounts
    server_3 = MAX_TOTAL_ACCOUNTS - total_entered_accounts
    
    
    # if conditions to check different conditions
    if total_entered_accounts > MAX_TOTAL_ACCOUNTS:
        print(" You have exceeded the maximum allowable accounts: ")
        
    
    if total_entered_accounts == MAX_TOTAL_ACCOUNTS:
        print('There are no additional accounts allowed. ')
       
    
    if total_entered_accounts < MAX_TOTAL_ACCOUNTS:
         print('accounts for server 1: ', accounts_for_first_server) 
         print('accounts for server 2: ', accounts_for_second_server)
         print(f'There are {server_3} accounts still available')
    
    # takes user input to continue or to exit   
    ask_user = input("do you still want to continue: yes/no: ").lower()
    
    # if condition to come exit
    if ask_user == 'no':
        continue_loop = False
    
        
    

   

        
    
