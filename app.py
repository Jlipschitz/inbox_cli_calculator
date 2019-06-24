print('Welcome to bill calculator! \n')

# define our prompt function to get the bill, tip and split amount
# TODO: Add logic for split amount being 0 and tip/bill not allowed to be 0
## can also add several error handlers for specific error responses
### strip away $ and other special characters (exclude .) from user input
def get_prompt_amount(question):
    while True:
        try:    
                amount = float(input('%s \n' % question))
        except:
                print("Sorry, I did not understand that number. \n")
                continue
        if amount < 0:
                print('Sorry, please enter a number higher than 0. \n')
                continue
        else:
                break
    return amount

# add logic for singular response or multiple if the amount is being split by multiple people
def calculate_bill(bill, tip, split):
     owed_amount = (bill + ((tip / 100) * bill)) / split # convert results to two decimal places
     
     print('The amount you owe is %s' % owed_amount)
#      print ('The amount you each owe is: $%s' % owed_amount)

# get our bill, tip and split amounts from our user input
bill_amount = get_prompt_amount('What is your bill amount?')
tip_amount = get_prompt_amount('How much would you like to tip?')
split_amount = get_prompt_amount('How many are you splitting with?')

calculate_bill(bill_amount, tip_amount, split_amount)

