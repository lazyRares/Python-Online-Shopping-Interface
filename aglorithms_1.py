# Variables
datafile = open("product_data.txt", "r")

with open("product_data.txt", "r") as file:
             lines = file.readlines()

productID = []
productName = []
productPrice = []
productCategory = []

for line in lines:
             
             data_into_list = line.split(",")
             
             productID.append(int(data_into_list[0]))
             productName.append(data_into_list[1])
             productPrice.append(float(data_into_list[2]))
             productCategory.append(data_into_list[3].strip())


lengthList = len(productPrice)
swapped = False

def bubbleSort(productList):
             
             for i in range(lengthList - 1):
                          for j in range(0, lengthList-i-1):
                                       if productList[j] > productList[j + 1]:
                                                    swapped = True
                                                    productList[j], productList[j+1] = productList[j+1], productList[j]
                          if not swapped:
                                       return


bubbleSort(productPrice)

done = "false"

#Main Loop

while done == "false":
             #Check To Exit
             #Input
             print("Are You Finished:  (Y/N)")
             checkDone = input()
             if checkDone == "Y":
                          done = "true"
                          print("Exiting")
                          exit()
             else:
                          done = "false"

             #Input For Options
             print("What Would You Like To Do?")
             print("Options Are: \nInsert\nUpdate\nDelete\nSearch\nView")
             option = input()

             if option.lower() == "insert":
                          
                          print("Time To Add A Product, Begin By Typing The ID, Maximum 5 Digits")
                          print("ID:")
                          addID = input()
                          truncatedAddID = (addID[:5]) if len(addID) > 5 else addID
                          print("Product So Far: " + truncatedAddID+",")
                         
                          print("Type The Product's Name")
                          print("Name:")
                          addName = input()
                          print("Product So Far: " + truncatedAddID+", "+ addName+", ")
                          
                          print("Type The Product's Price")
                          print("Price:")
                          addPrice = input()
                          
                          if ".0" in addPrice:
                                       addPrice
                          else:
                                       if any(char.isdigit() for char in addPrice) and not "." in addPrice:
                                                    addPriceDecimal = addPrice + ".0"
                                                    print("Product So Far: " + truncatedAddID+", "+ addName+", "+ addPriceDecimal+", ")
                                       else:
                                                    print("Product So Far: " + truncatedAddID+", "+ addName+", "+ addPrice+", ")

                          print("Type The Product's Category")
                          print("Category:")
                          addCategory = input()
                          try:
                                       addPriceDecimal
                          except NameError:
                                       print("Final Product: " + truncatedAddID+", "+ addName+", "+ addPrice+", "+ addCategory)
                          else:
                                       print("Final Product: " + truncatedAddID+", "+ addName+", "+ addPriceDecimal+", "+ addCategory)

                          print("Adding To List...")
                          productID.append(truncatedAddID)
                          productName.append(addName)
                          try:
                                       addPriceDecimal
                          except NameError:
                                       productPrice.append(addPrice)
                          else:
                                       productPrice.append(addPriceDecimal)
                          productCategory.append(addCategory)
                          
             elif option.lower() == "update":
                          
                          print("Modifiying Product Details...")
                          print("Printing All Products, Choose One To Modify")
                          for i in range(len(productID)):
                                       print(str(i)+". "+str(productID[i])+", "+str(productName[i])+", "+str(productPrice[i])+", "+str(productCategory[i]))
                                       
                          print("\n")
                          print("Type Product Number, NOT The ID\n")
                          numberChosen = input()
                          print("Chosen Product:")
                          print(str(productID[int(numberChosen)])+", "+str(productName[int(numberChosen)])+", "+str(productPrice[int(numberChosen)])+", "+str(productCategory[int(numberChosen)]))

                          #Re-using Insert Code

                          print("Editing Product...")
                          print("ID:")
                          addID = input()
                          truncatedAddID = (addID[:5]) if len(addID) > 5 else addID
                          print("Product So Far: " + truncatedAddID+",")
                         
                          print("Type The Product's Name")
                          print("Name:")
                          addName = input()
                          print("Product So Far: " + truncatedAddID+", "+ addName+", ")
                          
                          print("Type The Product's Price")
                          print("Price:")
                          addPrice = input()
                          
                          if ".0" in addPrice:
                                       addPrice
                          else:
                                       if any(char.isdigit() for char in addPrice) and not "." in addPrice:
                                                    addPriceDecimal = addPrice + ".0"
                                                    print("Product So Far: " + truncatedAddID+", "+ addName+", "+ addPriceDecimal+", ")
                                       else:
                                                    print("Product So Far: " + truncatedAddID+", "+ addName+", "+ addPrice+", ")

                          print("Type The Product's Category")
                          print("Category:")
                          addCategory = input()
                          try:
                                       addPriceDecimal
                          except NameError:
                                       print("Final Product: " + truncatedAddID+", "+ addName+", "+ addPrice+", "+ addCategory)
                          else:
                                       print("Final Product: " + truncatedAddID+", "+ addName+", "+ addPriceDecimal+", "+ addCategory)

                          print("Replacing Product Number "+ str(numberChosen)+ "...")
                          productID[int(numberChosen)] = truncatedAddID
                          productName[int(numberChosen)] = addName
                          try:
                                       addPriceDecimal
                          except NameError:
                                       productPrice[int(numberChosen)] = addPrice
                          else:
                                       productPrice[int(numberChosen)] = addPriceDecimal
                          productCategory[int(numberChosen)] = addCategory

                          print("Done!")
                          
             elif option.lower() == "delete":

                          print("Delete From List...")
                          print("Printing All Products, Choose One To Delete")
                          for i in range(len(productID)):
                                       print(str(i)+". "+str(productID[i])+", "+str(productName[i])+", "+str(productPrice[i])+", "+str(productCategory[i]))
                                       
                          print("\n")
                          print("Type Product Number, NOT The ID\n")
                          numberChosen = input()
                          print("Chosen Product:")
                          print(str(productID[int(numberChosen)])+", "+str(productName[int(numberChosen)])+", "+str(productPrice[int(numberChosen)])+", "+str(productCategory[int(numberChosen)]))

                          print("Deleting!")
                          productID.remove(productID[int(numberChosen)])
                          productName.remove(productName[int(numberChosen)])
                          productPrice.remove(productPrice[int(numberChosen)])
                          productCategory.remove(productCategory[int(numberChosen)])
                          print("Gone!")
                          
                          
             elif option.lower() == "search":

                          print("Search...")
                          print("What Do You Want To Search By?")
                          print("ID\nName\nPrice\nCategory\n")
                          chosenMethod = input()

                          #ID
                          if chosenMethod.lower() == "id":
                                       print("Type The ID")
                                       idChosen = input()
                                       for i in range(len(productID)):
                                                    if int(productID[i]) == int(idChosen):
                                                                 print("Found Item, Printing!")
                                                                 numberChosen = productID.index(int(idChosen))
                                                                 print(str(productID[int(numberChosen)])+", "+str(productName[int(numberChosen)])+", "+str(productPrice[int(numberChosen)])+", "+str(productCategory[int(numberChosen)]))
                                                                 break
                                       else:
                                                    print("This Could Not Be Found.")
                                                                 
                          #Name
                          if chosenMethod.lower() == "name":
                                       print("Type The Name")
                                       nameChosen = input()
                                       for i in range(len(productName)):
                                                    productName[i] = productName[i].strip()
                                                    if str(productName[i]).lower() == str(nameChosen).lower():
                                                                 print("Found Item, Printing!")
                                                                 print(str(productID[i])+", "+str(productName[i])+", "+str(productPrice[i])+", "+str(productCategory[i]))
                                                                 break
                                       else:
                                                    print("This Could Not Be Found.")

                          #Price
                          if chosenMethod.lower() == "price":
                                       print("Type The Price")
                                       priceChosen = input()
                                       for i in range(len(productPrice)):
                                                    if float(productPrice[i]) == float(priceChosen):
                                                                 print("Found Item, Printing!")
                                                                 numberChosen = productPrice.index(float(priceChosen))
                                                                 print(str(productID[int(numberChosen)])+", "+str(productName[int(numberChosen)])+", "+str(productPrice[int(numberChosen)])+", "+str(productCategory[int(numberChosen)]))
                                                                 break
                                       else:
                                                    print("This Could Not Be Found.")

                          #Category
                          if chosenMethod.lower() == "category":
                                       print("Type The Category")
                                       categoryChosen = input()
                                       if categoryChosen not in productCategory:
                                                    print("This Category Doesn't Exist.")
                                       else:
                                                    print("Printing All Items In Category.")
                                                    for i in range(len(productCategory)):
                                                                 productCategory[i] = productCategory[i].strip()
                                                                 if str(productCategory[i]).lower() == str(categoryChosen).lower():
                                                                              print(str(productID[i])+", "+str(productName[i])+", "+str(productPrice[i])+", "+str(productCategory[i]))
                          
             elif option.lower() == "view":
                          
                          print("Viewing Lists...")
                          print("\n")
                          for i in range(len(productID)):
                                       print(str(productID[i])+", "+str(productName[i])+", "+str(productPrice[i])+", "+str(productCategory[i]))
                          
             

