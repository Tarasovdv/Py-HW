import interface as i

def welcome():
    print("Welcome to the phone book")
    while True:
        menu=input("What do you want?\n\
        Download the phone book from a file - enter 1\n\
        Record a contact manually - enter 2\n\
        Exit - enter 3\n")
        try: 
            n=int(menu)
            if n==1:
                print("Attention! Now the download is accessible only from a txt file")
                i.name_view()
                print("\nThe information is included in the directory ")
            elif n==2:
                i.name_view_d()
                print("\nThe information is included in the directory ")
            elif n==3:
                break
                         
        except ValueError:
            print("\nYou enter wrong number. Try again!") 
       
            