
import csv
from tabulate import tabulate
shoe_list = []
class Shoes:
    def __init__(self,country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

#Function to get the cost of the shoe
    def get_cost(self):
        return self.cost

    def set_quantity(self):
        self.quantity += quantity

#function to get 
    def get_quanty(self):
        return self.quantity

#functions to return the attribute of the Shoe class
    def __str__(self):
        return (self.country + "," + self.code + "," + self.product + "," + str(self.cost) + "," + str(self.quantity))

#defining the read shoe data
def read_shoes_data():
    shoe_list = []
    filename = "inventory.txt"
    try:
        lineNo = 0
        # Open the file in read mode
        with open('inventory.txt', 'rt') as f:
            # iterate though the file contents
            for line in f:
                if lineNo != 0:
                    # storing the read data by spliting by ","
                    (country, code, product, cost, quantity) = line.rstrip('\n').strip().split(',')
                    # add the data to list
                    shoe_list.append(Shoes(self.country,self.code,self.product,int(self.cost),int(self.quantity)))
                    lineNo += 1
            print("Read Data from inventory.txt files")
            print(shoe_list)
    except FileNotFoundError:
        print("File ", filename, " not accessible")
    
# capture method
def capture_shoes():
    shoe_country = input("Enter the country:\n")
    shoe_code = input("Enter the code:\n")
    shoe_product = input("Enter the product:\n")
    shoe_cost = float(input("enter the shoe cost:\n"))
    shoe_quantity = int(input("Enter the quantity:\n"))
    shoe =  Shoes(shoe_country, shoe_code, shoe_product, shoe_cost, shoe_quantity)
    shoe_list.append(shoe)
    
#view all method
def view_all():
    shoe_list = []
    with open('inventory.txt', 'r') as read_obj:
        csv_reader = csv.reader(read_obj)
        shoe_list = list(csv_reader)
        print('Welcome to shoe inventory')
        print(tabulate(shoe_list, headers = ["Country", "Code", "Product", "Price", "Quantity", ]))
        
# method that will determine which shoe to restock
def re_stock():
    with open("inventory.txt", 'r+') as ofile:
        quanty_list = []
        for line in ofile:
            lines = line.strip().split(",")
            quanty_list.append(lines[4])
            new_list = quanty_list[1:]
            new_list_1 = [int(x) for x in new_list]
        mini = min(new_list_1)
        print(f'the lowest quantity is found is : {mini}')
        restock = input("would you like to restock the shoe, input yes or no\n").lower()
        if restock == 'no':
            breakpoint
        elif restock == 'yes':
            with open('inventory.txt', 'r+') as file:
                cont = ""
                content = ""
                for line in file:
                    content = line.strip().split(",")
                restock_value = int(input("Enter the amount you would like to restock with.\n"))
                update_value = restock_value + mini
                print(f"the updated value is: {update_value} ")
                for line in content:
                    if line.find(content[-1]) == "2":
                        cont = file.repalce("2", update_value)
                        file.write(cont)
                        
#function to search the avialibility of the shoe
def seach_shoe():
    code = input("Enter code to search, for axamples SKU76000:\n")
    with open("inventory.txt", 'rt') as file:
        file.readlines()
        count = 0
        index = 0
        line = ""
    for line in open("inventory.txt", 'rt'):
        index += 1
        if code in line:
            count = 1
            break
    if count == 0:
        print("the code does not exist")
    else:
        print(code, "Code Found : ", line, )

#prints out the value of the items
def value_per_item():
    with open("inventory.txt",'r') as file:
        value = []
        cost_list = []
        quantity_list = []
        code_1 = []
        for line in file:
            lines = line.strip().split(",")
            cost_list.append(lines[-2]) # adding all the cost in the list
            nw_cost_list = cost_list[1:] # remove the heading cost from the list
            code_1.append(lines[1])
            code = code_1[1:]
            
            quantity_list.append(lines[-1]) # add all the quantitys on the list
            nw_q_list = quantity_list[1:] # remove the heading list
            new_list = [int(x) for x in nw_q_list] # convert all the cost numbers from strings to intergers
            new_list_1 = [int(x) for x in nw_cost_list]# convert all the quantity numbers from string to intergers
            code1 = enumerate(code, start = 1) # enumerate the code for the shoes to corespond to their value
            value1 = enumerate(value, start = 1)# enumerate the values of the shoes to corespond to the codes
        for num1, num2 in zip(new_list, new_list_1): # use a for loop to print them all out
            value.append(num1 * num2)
        for i, j in zip(code1, value1):
            print(f'The value of shoe with code {i} is {j}')

#function that return the shoe type that has the highest quantity
def highest_qty():
    highest_quantity = shoe_list[0]
    for shoe in shoe_list:
        if shoe.get_quanty() > highest_quantity.get_quanty():
            highest_quantity = shoe
    print(str(highest_quantity))

#excuting the function using a while loop
if __name__ == '__main__':
    choice = 0
    while True:
        print("1. Read shoes data")
        print("2. Capture shoes")
        print("3. View all Shoes")
        print("4. Restock Shoes")
        print("5. Search Shoe")
        print("6. Get Total value of Stock")
        print("7. Quit")
        # get choice from user
        choice = int(input("Enter choice: "))
        # based on user choice call appropriate functions
        if choice == 1:
            read = read_shoes_data()
            print(read)
        elif choice == 2:
            capture = capture_shoes()
            print(capture)
        elif choice == 3:
            view_all()
        elif choice == 4:
            re_stock()
        elif choice == 5:
            print(str(seach_shoe()))
        elif choice == 6:
            value_per_item()
        elif choice == 7:
            print("Thank you.")
            break
        else:
            print("Invalid choice")
#reference
#https://www.w3schools.com/python/python
#https://realpython.com/python
#https://www.w3schools.com/python/python
                
