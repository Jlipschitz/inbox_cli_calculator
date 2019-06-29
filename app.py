import re
print('Welcome to bill calculator!')

# define list store users recently calculated bills
recent_bills = []


# define our prompt function to get the bill, tip and split amount from user input
def get_prompt_amount(question, prompt_type):
    while True:
        try:
            amount = round(
                float(input('%s \n' % question).replace('$', '').replace(' ', '')))
        # exit application if keyobard or sys exit commands errors are recognized (i.e. ctr-c)
        except (KeyboardInterrupt, SystemExit):
            print('\nAn exit command was pressed... terminating program. Goodbye!')
            exit()
        # raise exceptions if user input is not recognized or invalid
        except:
            print(
                'Sorry, I did not understand that %s number. Please try again.' % prompt_type)
            continue

        if amount < 0:
            print('Woops! Your %s amount must be higher than 0.' % prompt_type)
            continue
        elif amount == 0 and (prompt_type == 'bill' or prompt_type == 'tip'):
            if(prompt_type == 'bill'):
                print('Woops! Your %s amount must be higher than 0.' %
                      prompt_type)
            elif(prompt_type == 'tip'):
                print(
                    'Don\'t be cheap! Your %s amount must be higher than 0.' % prompt_type)
            continue
        else:
            break
    return amount


def calculate_bill(bill, tip, split):
    def check_split(value):
        if split > 1:
            return value
        else:
            return 0

    if(split > 1):
        owed_amount = round((bill + ((tip / 100) * bill)) / split, 2)
        print('\nThe amount you each owe is: $%s \n' % owed_amount)
    else:
        owed_amount = round(bill + ((tip / 100) * bill), 2)
        print('\nThe amount you owe is $%s \n' % owed_amount)

    recent_bills.append({
        'bill': round(bill),
        'tip': round((tip / 100) * bill),
        'split': check_split(split),
        'total': owed_amount})


# allow users to restart the app and calculate another bill when finished
def restart_app():
    try:
        run_again = input(
            '\nWould you like to calculate another bill? \n Type [Y]es to continue || [N]o to Exit || [V]iew for recent bills \n')
    except (KeyboardInterrupt, SystemExit):
        print('\nAn exit command was pressed... terminating program. Goodbye!')
        exit()
    if(run_again.lower() in ['yes', 'y']):
        application_start()
    elif(run_again.lower() in ['no', 'n', 'e', 'exit', 'end']):
        print('\nThank you for using bill Caculator!')
        exit()
    elif(run_again.lower() in ['view', 'v', 'recent']):
        print('\nRecent bills:')
        for index, value in enumerate(recent_bills):
            if index == 0:
                print('1. Bill amount: $%s | Tip amount: $%s | Split with: %s people | Total: $%s' %
                      (value['bill'], value['tip'], value['split'], value['total']))
            else:
                print('%s. Bill amount: $%s | Tip amount: $%s | Split with: %s people | Total: $%s' %
                      (index+1, value['bill'], value['tip'], value['split'], value['total']))

        restart_app()
    else:
        print('Sorry, I did not understand that input.')
        restart_app()


def application_start():
    # get our bill, tip and split amounts from our user input
    bill_amount = get_prompt_amount('\nWhat is your bill amount?', 'bill')
    tip_amount = get_prompt_amount(
        'What percentage would you like to tip?', 'tip')
    split_amount = get_prompt_amount(
        'How many people are you splitting this bill with? Enter 0 if none.', 'split')

    calculate_bill(bill_amount, tip_amount, split_amount)

    restart_app()


application_start()
