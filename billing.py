print ("WELCOME TO PYTHON MART BILLING")

print("")

name = input(" enter you`r name : ")
item1 = input(" enter the first item name : ")
quantity1 = int(input(" enter the quantity : "))
price1 = float(input(" enter the price of 1 unit : "))

print("")

item2 = input(" enter the second item name : ")
quantity2 = int(input(" enter the quantity : "))
price2 = float(input(" enter the price of 1 unit : "))

print("")

total1 = quantity1*price1
total2 = quantity2*price2

print("")

print (" --- BILL SUMMARY ---")

print("")

print ("customer name : ", name)
print("")
print ("item name : ", item1, "| quantity : ", quantity1, "| price per unit : ", price1, "| total : ", total1)
print("")
print ("item name : ", item2, "| quantity : ", quantity2, "| price per unit : ", price2, "| total : ", total2)

print("")

subtotal = total1+total2
gst = (subtotal*18)/100
totalbill = subtotal+gst

print("")

print ("subtotal : ", subtotal)
print ("GST 18% ")
print ("Total Bill : ", totalbill)

print("")

print(" Thnakyou for Shopping")
