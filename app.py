print('Welcome to bill calculator!')

# define our prompt function to get the bill, tip and split amount from user input
def get_prompt_amount(question, prompt_type):
    while True:
        try:    
                amount = float(input('%s \n' % question.replace("!@#$%^&*()[]{};:,/<>?\\|`~-=_+", " ")))
        # exit application if keyobard or sys exit commands errors are recognized (i.e. ctr-c)
        except (KeyboardInterrupt, SystemExit):
                print("\nAn exit command was pressed... terminating program. Goodbye!")
                exit()
        # raise exceptions if user input is not recognized or invalid        
        except:
                print("Sorry, I did not understand that %s number. Please try again." % prompt_type)
                continue
        if amount < 0:
                print('Woops! Your %s amount must be higher than 0.' % prompt_type)
                continue
        elif  amount == 0 and (prompt_type == 'bill' or prompt_type == 'tip'):
                if(prompt_type == 'bill'):
                        print('Woops! Your %s amount must be higher than 0.' % prompt_type)
                elif(prompt_type == 'tip'):
                        print('Don\'t be cheap! Your %s amount must be higher than 0.' % prompt_type)
                continue
        else:
                break
    return amount

# calculate the bill and print the results
def calculate_bill(bill, tip, split):
     
     if(split > 0):
             owed_amount = (bill + ((tip / 100) * bill)) / split
             print ('The amount you each owe is: $%s \n' % round(owed_amount,2))    

     else:  
             owed_amount = (bill + ((tip / 100) * bill))
             print('The amount you owe is $%s \n' % round(owed_amount,2))

# allow users to restart the app and calculate another bill when finished
def restart_app():
        try:
                run_again = input('Would you like to calculate another bill? \n Type [Y]es or [N]o \n')
                
                if(run_again.lower() == 'yes' or run_again.lower() == 'y'):
                        application_start()
                elif(run_again.lower() == 'no' or run_again.lower() == 'n'):
                        print('\nThank you for using bill Caculator!') 
                        exit()
                else:
                        print('Sorry, I did not understand that input.')
                        restart_app()
        except (KeyboardInterrupt, SystemExit):
                print("\nAn exit command was pressed... terminating program. Goodbye!")
                exit()

def application_start():
        # get our bill, tip and split amounts from our user input
        bill_amount = get_prompt_amount('\nWhat is your bill amount?', 'bill')
        tip_amount = get_prompt_amount('What percentage would you like to tip?', 'tip')
        split_amount = get_prompt_amount('How many people are you splitting this bill with?', 'split')

        calculate_bill(bill_amount, tip_amount, split_amount)

        restart_app()

application_start()