# Sabrina Skoric: 100872613
# Assignment 1: Algorithms and Data Structures

# THE TEXT FILE HAS BEEN ALTERED FOR TESTS
print('__        __   _                          ')
print('\ \      / /__| | ___ ___  _________  ___ ')
print(' \ \ /\ / / _ \ |/ __/ _ \|  _   _  |/ _ |')
print('  \ V  V /  __/ | (_| (_) | | | | | |  __/')
print('   \_/\_/ \___|_|\___\___/|_| |_| |_|\___|')

print("\nTO THE ONLINE SHOPPING MANAGEMENT PAGE")

def main():
    global ItemArray 
    ItemArray = []

    # read from product_data.txt
    file = open("product_data.txt", "r")

    # remove unecessary elements from file (new lines)
    for line in file:
        items = [item.strip() for item in line.split(',')]
        ItemArray.append(items)

    file.close()

    counter = 0
    while counter == 0:

        # display options for user
        print("\nWhat operation would you like to perform?")
        print("1 = insert new product")
        print("2 = update existing product")
        print("3 = delete product")
        print("4 = search by product attribute")
        print("5 = sort by price")
        print("6 = exit")
        answer = input("\nOperation: ")

        # insert a new product
        if answer in ['1', 'one', 'ONE']:
            InsertProduct()

        elif answer in ['2', 'two', 'TWO']:
            UpdateProduct()

        elif answer in ['3', 'three', 'THREE']:
            DeleteProduct()

        elif answer in ['4', 'four', 'FOUR']:
            SearchProduct()

        elif answer in ['5', 'five', 'FIVE']:
            SortProduct()

        elif answer in ['6', 'six', 'SIX']:
            print("Ending program...")
            counter += 1

        else:
            print("INVALID INPUT\n")
        
def InsertProduct():

    # get product information from the user
    productInfo = []
    IDcount = 0
    while IDcount == 0:
        productID = input("Enter product ID (5 digits): ")
        if len(productID) != 5:
            print("Length invalid")
        else:
            IDcount +=1

    productName = input("Enter product Name: ")

    PriceCount = 0
    while PriceCount == 0:
        try:
            productPrice = float(input("Enter product Price: "))
            PriceCount += 1
        except:
            print("Invalid price")
    

    productCategory = input("Enter product Category: ")

    # write that new information into product_data.txt
    file = open("product_data.txt", "a")
    file.write('\n' + productID + ', ' + productName + ', ' + str(productPrice) + ', ' + productCategory)
    file.close()

    print("Product inserted")

    # create an array of the information, and append to ItemArray
    productInfo.append(productID)
    productInfo.append(productName)
    productInfo.append(productPrice)
    productInfo.append(productCategory)
    ItemArray.append(productInfo)

def UpdateProduct():

    userProductID = input("Enter the ID of product: ")
    found = False
    for item in ItemArray:
        if item[0] == userProductID:
            found = True

            # display product information to user
            print("Here is the product information:")
            print("Product ID:", item[0])
            print("Product Name:", item[1])
            print("Product Price:", item[2])
            print("Product Category:", item[3])

            update = input("\nWhat field would you like to update: ")

            # to update ID
            if update in ['ID', 'id']:
                count = 0
                while count == 0:
                    edit = input("Enter new product ID (5 digits): ")
                    if len(edit) != 5:
                        print("Length invalid")
                    else:
                        item[0] = edit
                        count +=1

                file = open("product_data.txt", "r")
                lines = file.readlines()
                file.close()
                file = open("product_data.txt", "w")

                for line in lines:
                    if not line.startswith(userProductID):
                        file.write(line)
                file.write(edit + ', ' + item[1] + ', ' + item[2] + ', ' + item[3])

            if update in ['Name', 'name']:
                edit = input("Enter new product name: ")
                item[1] = edit

                file = open("product_data.txt", "r")
                lines = file.readlines()
                file.close()
                file = open("product_data.txt", "w")

                for line in lines:
                    if not line.startswith(userProductID):
                        file.write(line)
                file.write(item[0] + ', ' + edit + ', ' + item[2] + ', ' + item[3])

            if update in ['Price', 'price']:
                edit = input("Enter new product price: ")
                item[2] = edit

                file = open("product_data.txt", "r")
                lines = file.readlines()
                file.close()
                file = open("product_data.txt", "w")

                for line in lines:
                    if not line.startswith(userProductID):
                        file.write(line)
                file.write(item[0] + ', ' + item[1] + ', ' + edit + ', ' + item[3])

            if update in ['Category', 'category']:
                edit = input("Enter new product category: ")
                item[3] = edit

                file = open("product_data.txt", "r")
                lines = file.readlines()
                file.close()
                file = open("product_data.txt", "w")

                for line in lines:
                    if not line.startswith(userProductID):
                        file.write(line)
                file.write(item[0]+ ', ' + item[1] + ', ' + item[2] + ', ' + edit)
    
    if not found:
        print("No such product ID found\n")
    else:
        print("Product updated")

def DeleteProduct():
    userProductID = input("Enter the ID of product: ")
    found = False

    for item in ItemArray:
        if item[0] == userProductID:
            found = True
            ItemArray.remove(item)
            print("Product deleted")

    with open('product_data.txt', 'r') as fr:
        lines = fr.readlines()
 
    with open('product_data.txt', 'w') as fw:
        for line in lines:
            if not line.startswith(userProductID):
                fw.write(line)
    if not found:
        print("No such product ID found\n")

def SearchProduct():
    attribute = input("Attribute to search by: ")

    if attribute in ['ID', 'id']:
        criteria = input("Enter ID: ")
        found = False
        for item in ItemArray:
            if item[0] == criteria:
                found = True
                print("Here are the product details:")
                print(item)
        if not found:
            print("No such product ID found\n")
               
    if attribute in ['Name', 'name']:
        criteria = input("Enter name: ")
        found = False
        for item in ItemArray:
            if item[1] == criteria:
                found = True
                print("Here are the product details:")
                print(item)
        if not found:
            print("No such product name found\n")
               
    if attribute in ['Price', 'price']:
        criteria = input("Enter price: ")
        found = False
        for item in ItemArray:
            if item[2] == criteria:
                found = True
                print("Here are the product details:")
                print(item)
        if not found:
            print("No such product price found\n")
              
    if attribute in ['Category', 'category']:
        criteria = input("Enter category: ")
        found = False
        for item in ItemArray:
            if item[3] == criteria:
                found = True
                print("Here are the product details:")
                print(item)
        if not found:
            print("No such product category found\n")

def SortProduct():

    #import time
    #start = time.time()

    with open('product_data.txt', 'r') as file:
        lines = file.readlines()

    # using bubble sort to order by price (ascending)
    for i in range(len(lines)):
        for j in range(0, len(lines)-i-1):
            # get the prices (third element)
            price1 = float(lines[j].split(', ')[2])
            price2 = float(lines[j+1].split(', ')[2])

            # Swap if the prices are in the wrong order
            if price1 < price2:
                lines[j], lines[j+1] = lines[j+1], lines[j]

    # write sorted list to file
    with open('product_data.txt', 'w') as file:
        file.writelines(lines)
    
    print("File sorted")

    #end = time.time()
    #final = end-start
    #print(final)
        
if __name__ == "__main__":
    main()
