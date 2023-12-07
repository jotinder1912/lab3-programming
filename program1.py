print("WELCOME TO THE AMANDO SHOPPING SITE")
print("Display a manu \n 1.	Add a product to the cart. \n 2.	Search for a product.\n 3.	Delete a product from the cart. \n 4.	Display the contents of the cart. \n 5.	Purchase items. \n 6.	Quit.")
manu=int(input("choose one option from the menu: "))
shoppingCart={}
brand={}
i=1
j=1
while(manu!=6):
    if(manu==1):
      
        if (len(shoppingCart) <5):
            y=input("Enter the product name: ").lower()
            z=float(input("Enter the product price: "))
            brand=input("Enter the brand name: ").lower()
            shoppingCart.update({y:{"price":z,"brand":brand}})
            print(shoppingCart)                  
        else:
            print("Cart is FULL")
    elif(manu==2):
        b=input("Enter the product name that you want to search: ")
        if b in shoppingCart:
            print(b,"-",shoppingCart[b])
        else:
            print("No product with this name exist in shoppingCart. ")
    elif(manu==3):
        c=input("Enter the product name that you want to delete:")
        if c in shoppingCart:
                shoppingCart.pop(c)
                print(shoppingCart)
        elif len(shoppingCart) ==0:
            print("Cart is empty,no item is found" )
        else:
            print("Product not found in cart.")
    elif(manu==4):
        if not shoppingCart:
            print("Cart is empty.")
        else:
            print(shoppingCart)
    elif(manu==5):
        purchase=input("Complete purchase (Y/N)?").lower()
        if purchase=="y":
            total=0
            for i,j in shoppingCart.items():
                total=total+j["price"]
            print("Thank you for your business.","TOTAL=",total)  
            print("After,purchase the items present in cart:",shoppingCart.clear()) 
        elif purchase=="n":
            print("Please continue shopping.")
        else:
            print("Please answer either Y or N.")

    
    print("Display a manu \n 1.	Add a product to the cart. \n 2.	Search for a product.\n 3.	Delete a product from the cart. \n 4.	Display the contents of the cart. \n 5.	Purchase items. \n 6.	Quit.")
    manu=int(input("choose one option from the menu: "))
else:
    print("Now,you exits from the whole program:-")
    
