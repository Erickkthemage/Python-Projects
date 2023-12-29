tesla=219.37
rent=73.75
vacation=25
car_insurance=40

while True:
    try:
        paycheck=float(input('How much did you get paid? '))
        if paycheck<=0:
            print('Pleases enter a positive number.')
            continue
    except ValueError:
        print('Please enter a valid number.')
        continue
    break

while True:
    try:
        current_balance=float(input('How much is currently in your checking? '))
        if current_balance<=0:
            print('Please enter a positive number.')
            continue
    except ValueError:
        print('Please enter a valid number.')
        continue
    break

left_over_paycheck=paycheck-tesla-rent-vacation-car_insurance
transfer=current_balance-left_over_paycheck

print('You should transfer ',round(transfer,2),' to your savings.')