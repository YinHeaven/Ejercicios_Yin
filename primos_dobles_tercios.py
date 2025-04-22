
def print_number(txt1, txt2) ->int:
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(number, ": " + txt1 + " y " + txt2)
        elif number %3 == 0 and number % 2 == 0:
            print(number, ": " + txt2 + " y doble", end=", ")
        elif number % 5 == 0 and number % 2 == 0:
            print(number, ": " + txt1 + " y doble", end=", ")
        elif number % 3 == 0:
            print(number, ": " + txt2, end=", ")
        elif number %5 == 0:
         print(number, ": " + txt1, end=", ")
        elif number % 2 == 0:
            print(number, ": " + "doble", end=", ")
        else:
            print(number, ": " "primo", end=", ")

print_number( "quinto",  "tercio")



