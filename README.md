# Shoe Inventory Management System

This Python program implements a shoe inventory management system. It allows users to perform various operations such as reading shoe data from a file, capturing new shoe details, viewing all shoes, restocking shoes, searching for a shoe, and calculating the total value of the stock.

## Files

* `inventory.txt`: A text file containing the shoe inventory data in CSV format (comma-separated values).
* `shoe_inventory.py`: The Python script containing the inventory management system code.
* `README.md`: This file, providing documentation for the project.

## Libraries

* `csv`: Used for reading and writing CSV files.
* `tabulate`: Used for displaying tabular data in a formatted way.

## Class `Shoes`

The `Shoes` class represents a shoe item with the following attributes:

* `country`: The country where the shoe is made.
* `code`: The unique code of the shoe.
* `product`: The name of the shoe product.
* `cost`: The cost of the shoe.
* `quantity`: The quantity of the shoe in stock.

It also includes the following methods:

* `__init__(self, country, code, product, cost, quantity)`: Constructor to initialize the `Shoes` object.
* `get_cost(self)`: Returns the cost of the shoe.
* `set_quantity(self)`: Sets the quantity of the shoe.
* `get_quanty(self)`: Returns the quantity of the shoe.
* `__str__(self)`: Returns a string representation of the `Shoes` object.

## Functions

The program includes the following functions:

* `read_shoes_data()`: Reads shoe data from `inventory.txt` and creates `Shoes` objects, storing them in a list.
* `capture_shoes()`: Captures new shoe details from user input and creates a `Shoes` object, adding it to the list.
* `view_all()`: Reads and displays all shoe data from `inventory.txt` in a tabular format.
* `re_stock()`: Determines the shoe with the lowest quantity, prompts the user to restock, and updates the quantity in `inventory.txt`.
* `seach_shoe()`: Searches for a shoe by code and displays its details.
* `value_per_item()`: Calculates and displays the total value of each shoe item (cost * quantity).
* `highest_qty()`: Finds and displays the shoe with the highest quantity.

## How to Run

1.  Ensure you have Python 3 installed.
2.  Create an `inventory.txt` file in the same directory as `shoe_inventory.py`. The file should contain shoe data in CSV format, with the first line as a header.
3.  Run the `shoe_inventory.py` script from the command line: `python shoe_inventory.py`.
4.  Follow the menu prompts to perform various operations.

## `inventory.txt` File Format

The `inventory.txt` file should be formatted as follows:

```csv
Country,Code,Product,Cost,Quantity
USA,SKU12345,Running Shoes,50.00,10
UK,SKU67890,Formal Shoes,80.00,5
...
