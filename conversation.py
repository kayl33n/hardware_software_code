

def conversation () :
        print ("Welcome to my conversation")
        print ("Do you like coding?")
        
        answer = input ("Answer yes or no")
        if answer.lower == "yes":
            print ("Thats good")
        elif answer.lower () == "no":
            print ("That sucks")
        else:
            print ("Thats too bad!")
            print ("Thanks for talking with me")
            
def main () :
    conversation ()
if __name__ == "__main__":
    main ()