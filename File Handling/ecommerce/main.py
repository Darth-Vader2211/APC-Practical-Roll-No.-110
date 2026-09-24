from products.details import product_details
from products.search import search_product

from customers.details import customer_details
from customers.registration import register_customer

from orders.create import create_order
from orders.status import order_status

from payments.payment import make_payment
from payments.refund import refund


print("----- E-COMMERCE APPLICATION -----")

print("\nPRODUCT")
product_details(101, "Laptop", 50000)
search_product("Laptop")

print("\nCUSTOMER")
customer_details(1, "Amit")
register_customer("Amit")

print("\nORDER")
create_order("Amit", "Laptop")
order_status(1001)

print("\nPAYMENT")
make_payment(50000)

print("\nREFUND")
refund(5000)