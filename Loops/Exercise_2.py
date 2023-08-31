while True:
    try:
        print("Enter Hours: ")
        hours = int(input())
        print("Enter Rate: ")
        price = int(input())
        pay = hours * price
        print("Your Pay is: ", pay)
        break
    except ValueError:
        print("Error, Please enter a numeric Input")
    except TypeError:
        print("Error, Please enter a numeric Input")



