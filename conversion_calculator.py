"""Final Version"""

def binary_to_decimal(): #This is the function that has the instructions to convert binary to decimal, hence the name
    while True: #While creates a loop, in this case I used it to keep asking the user for a valid binary number (using the "is_binary_valid" function)
        num = input("Enter a Binary Number: ")
        if is_binary_valid(num):
            break #If a valid binary number is inserted then the loop breaks. 
        else:
            print("That's an invalid number, please enter a Binary number") #If the number inserted is not valid then the loop continues and here it asks again for a valid binary number.
            
    b = int(num)
    c = 0
    s = 0
    while b > 0: #This while statement creates another loop that actually executes the conversion
            r = b % 10
            k = r * (2 ** c)
            s = s + k
            b = b // 10
            c = c + 1
    return s #After the conversion is finished, the decimal equivalent is returned to the user

def is_binary_valid(b): #This function checks to make sure that the number provided in the previous function is a binary number
    return all(bit in '01' for bit in b)
    

def decimal_to_binary(): #This second conversion function contains the instructions to convert a decimal number to binary
    while True: #Another loop, this one uses the "is_decimal_valid" function to keep asking the user for a valid decimal number
        num = input("Enter a Decimal number: ")
        if is_decimal_valid(num):
           break
        else:
            print("Thats an invalid number, please enter a Decimal number")

    d = int(num)
    binary = ''
    while d != 0: #This while loop has the calculations that converts the inserted decimal number into a binary number
        binary += str(d % 2)
        d //= 2
    return binary[::-1] #After the decimal to binary conversion, the binary equivalent is returned to the user


def is_decimal_valid(num_str): #Here is the function that is used to check if the inserted number is a valid decimal number in the "decimal_to_binary function
    return num_str.isdigit() and num_str[0] != '0'

def binary_to_hexadecimal(): #This third conversion function contains the instructions to convert a binary number to a hexadecimal number
    while True: #This loop asks the user for a binary number and checks to see if its valid, using the next function (is_valid_binary)
        num = input("Enter a Binary Number: ")

        if is_valid_binary(num):
            break  # Exit the loop if the input is valid
        else:
            print("Thats an invlaid number, please enter a Binary number")
            
    d = 0
    for digit in num:
        d = d * 2 + int(digit)

    hex_digits = ""
    while d > 0: #This is the loop that calculates/converts the inserted binary number into a hexadecimal number
        remainder = d % 16
        if remainder < 10:
            hex_digits = str(remainder) + hex_digits
        else:
            hex_digits = chr(ord('A') + remainder - 10) + hex_digits
        d //= 16
    return hex_digits #The answer to the conversion is returned and the user recieves the hexadecimal equivalent

def is_valid_binary(binary_str):  #This is the function used for the binary_to_hexadecimal function that checks to see if the user inserted a valid binary number
    return all(bit in '01' for bit in binary_str)

def calculator_project(answer): #Once a choice/number is chosen in the main function, here is where the apropriate conversion function is called. The print functions then print a piece of text along with the corresponding answer to the user's conversion
    if answer == 1:
        decimal_result = binary_to_decimal()
        print(f"The Decimal representation is: {decimal_result}")
        
    elif answer == 2:
        binary_result = decimal_to_binary()
        print(f"The Binary representation is: {binary_result}")
        
    elif answer == 3:
        result = binary_to_hexadecimal()
        print(f"The Hexadecimal representation is: {result}")
       
    else:  
        print("Invalid choice")

def main():  #This function lists the conversions available in the program, listed by numbers. This function allows the user to insert their choice of conversion.
  print("Welcome to Kayleen's calculator project!")
  
  while True:
      print("What would you like to do? Pick a Number:")
      print("(1) Convert a Binary Number to Decimal")
      
      print("(2) Convert a Decimal Number to Binary")
      
      print("(3) Convert a Binary Number to Hexadecimal")
      
      print("(q) If you would like to quit the calculator program, simply type 'q'")
     
      answer = input("Enter your choice: ")
      
      if answer == 'q':
          print("Bye bye!")
          break
      else:
          print("That's not a valid option, please try again!")
      
if __name__ == "__main__":
    main()