amount = float(input('Enter the amount to debit : '))

if amount > 0:
    if amount % 500 == 0:
        five_thousand_notes = amount // 5000
        remaining_amount    = amount - (five_thousand_notes * 5000)
        thousand_notes      = remaining_amount // 1000
        remaining_amount    = remaining_amount - (thousand_notes * 1000)
        five_hundred_notes = remaining_amount // 500

        print(f'The amount debited : {five_thousand_notes} x 5000 + {thousand_notes} x 1000 + {five_hundred_notes} x 500')
    else:
        print('Amount has to be divisible by 500.')
else:
    print('Amount can not be negative.')
