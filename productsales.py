# 13 08 2026

# product sales analysis system
# table_data = ("Product_ID","Product_Name","Quantity_Sold","Price_Per_Unit")

products = [
    ('P101',"Laptop",5,50000),
    ('P102',"Mouse",20,500),
    ('P103',"Keyboard",15,1200),
    ('P104',"Monitor",8,15000),
    ('P105',"Headphones",12,2000)
]


# 1. display all product details
print("---------Product Details---------")

for product in products:
    product_id,product_name,quantity_sold,price_per_unit = product

    print("Product Id:",product_id)
    print("Product Name:",product_name)
    print("Quality Sold:",quantity_sold)
    print("Price Per Unit:",price_per_unit)
    print("----------------------------------")

# 2. Total Sales for each product
print("\nTotal Sales for Each Product")

for product in products:
    product_id, product_name, quantity_sold, price_per_unit = product

    total_sales = quantity_sold * price_per_unit
    print(product_name, "=", total_sales)


# 3. find product with highest sales
highest_sale = 0
highest_product = ""

for product in products:
    product_id, product_name, quantity_sold, price_per_unit = product

    total_sales = quantity_sold * price_per_unit

    if total_sales > highest_sale:
        highest_sale = total_sales
        highest_product = product_name

print("\n----Highest Sales----")
print("Product:",highest_product)
print("Total Sales:",highest_sale)


# 4. find product with lowest sales
lowest_sales = None
lowest_product = ""

for product in products:
    product_id, product_name, quantity_sold, price_per_unit = product

    total_sales = quantity_sold * price_per_unit

    if lowest_sales is None or total_sales < lowest_sales:
        lowest_sales = total_sales
        lowest_product = product_name

print("\n----Lowest Sales----")
print("Product:",lowest_product)
print("Total Sales:",lowest_sales)


# 5. calculate total sales of the stores
store_total_sales = 0

for product in products:
    product_id, product_name, quantity_sold, price_per_unit = product

    total_sales = quantity_sold * price_per_unit
    store_total_sales += total_sales

print("\n----Total Sales----")
print("Total Store Sales:",store_total_sales)


# 6. display product with sales above 50000
print("\n----Products with Sales above 50000----")

for product in products:
    product_id,product_name, quantity_sold, price_per_unit = product

    total_sales = quantity_sold * price_per_unit

    if total_sales > 50000:
        print(product_name, "=", total_sales)


# 7. Search for a product by product name
search_name = input("\nEnter product name to search: ")

found = False

for product in products:
    product_id, product_name, quantity_sold, price_per_unit = product

    if product_name.lower() == search_name.lower():
        print("\n----- PRODUCT FOUND -----")
        print("Product ID:", product_id)
        print("Product Name:", product_name)
        print("Quantity Sold:", quantity_sold)
        print("Price Per Unit:", price_per_unit)

        found = True
        break

if found == False:
    print("Product not found.")


# 8. Add a new product
print("\n----- ADD NEW PRODUCT -----")

new_id = input("Enter Product ID: ")
new_name = input("Enter Product Name: ")
new_quantity = int(input("Enter Quantity Sold: "))
new_price = float(input("Enter Price Per Unit: "))

# Create tuple
new_product = (new_id, new_name, new_quantity, new_price)

# Add tuple to list
products.append(new_product)

print("New product added successfully.")


# 9. Count total number of products
print("\n----- TOTAL PRODUCTS -----")
print("Total Number of Products:", len(products))


# Challenge Task
# Create sales_report list

sales_report = []

for product in products:
    product_id, product_name, quantity_sold, price_per_unit = product

    total_sales = quantity_sold * price_per_unit

    report = (product_name, total_sales)

    sales_report.append(report)


print("\n----- SALES REPORT -----")

for report in sales_report:
    product_name, total_sales = report

    print("Product:", product_name)
    print("Total Sales:", total_sales)
    print("-----------------------")