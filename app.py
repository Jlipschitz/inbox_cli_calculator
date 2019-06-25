# TODO: error handling for functions and add testing before app runs
## implement a help input function for users
## allow users to to keep running app if they want to calcultate another bill and can add option to store & display their most recent calculations

print('Welcome to bill calculator! \n')

# define our prompt function to get the bill, tip and split amount
def get_prompt_amount(question, prompt_type):
    while True:
        try:    
                amount = float(input('%s \n' % question.replace("!@#$%^&*()[]{};:,/<>?\|`~-=_+", " ")))
        except:
                print("Sorry, I did not understand that %s number. Please try again." % prompt_type)
                continue
        if amount < 0:
                print('Woops! Your %s amount must be higher than 0.' % prompt_type)
                continue
        elif  amount == 0 and (prompt_type == 'bill' or prompt_type == 'tip') :
                print('Woops! Your %s amount must be higher than 0.' % prompt_type)
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
     print('Thank you for using bill Caculator!')    

# get our bill, tip and split amounts from our user input
bill_amount = get_prompt_amount('What is your bill amount?', 'bill')
tip_amount = get_prompt_amount('How much would you like to tip?', 'tip')
split_amount = get_prompt_amount('How many people are you splitting this bill with?', 'split')

calculate_bill(bill_amount, tip_amount, split_amount)

