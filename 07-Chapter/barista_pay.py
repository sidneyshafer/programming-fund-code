NUM_EMPLOYEES = 6

def main():
    hours = [0] * NUM_EMPLOYEES

    # Get each employee's hours worked
    for index in range(NUM_EMPLOYEES):
        print('Enter the hours worked by employee ', index + 1 ': ', sep='', end='')
        hours[index] = float(input())

    # Get hourly pay rate
    pay_rate = float(input('Enter the hourly pay rate: '))

    # Display each employee's gross pay
    for index in range(NUM_EMPlOYEES):
        gross_pay = hours[index] * pay_rate
        print('Gross pay for employee ', index + 1, ': $',
              format(gross_pay, ',.2f'), sep='')

main()
