def get_name():
    with open ("file.txt","r") as data:
       return [x.split(" ") for x in [x for x in data]]



def get_name_d():
    name_download=input("Enter Full name and p.number by a space.\n\
                                        **if name don't have patronymic use double space \n")
    return  name_download.split(" ")


       
# get_name_d()            

        
    
    