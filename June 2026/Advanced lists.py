goods = ["apple", "banana", "pineapple", "grapefruit"] #Creating a new list

while True:
    wish = input("Please type what do you want to buy: ").lower() #We ask the user and make their answer a universal register, applying the answer to the variable "wish"
    if wish == "add" or wish == "new":
    	request = input("What do we need to add?: ").lower() #If the user wanted to add something to the list, we again make the register of his answer universal and through ".append" add a new element to the list
    	goods.append(request)
    	continue
    if wish == "list" or wish == "show all":
        print("Sure! For now we have all these goods in our magazine:") #This case repeats the process of the past "if" however, here it only displays a list of all the values of the list, adding a nice element "—"
        for item in goods:
        	print("— " + item)
        continue
    if wish == "delete" or wish == "remove" or wish == "del" or wish == "rem":
        request = input("What do we need to remove?: ").lower() #This block removes products from the list according to the user's preferences.
        if request in goods:
        	goods.remove(request)
        	continue
        else:
             print("Looks like we doesnt have it yet, so cant remove non-existent")
             continue
    if wish == "":
        continue #Thanks to this, if you accidentally enter empty text or click on "enter" the loop will not show to user error
    if wish == "exit":
        break #We terminate the loop if the user wants to exit
    if wish in goods:
        print("We have it in our magazine!")
    else:
        print("Sorry, we doesnt have it yet, try later") 
        
