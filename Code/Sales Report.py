count = 0
total = 0
highest_sale = None
lowest_sale = None
big_sale=0
small_sale=0

while True:
    sales = input("Enter product price ")

    if sales == "done":
        break

    try: 
        sale = float(sales)
    except:
        print("Invalid input")
        continue

    if sale > 5000 or sale < 1:
        print("Sale must be between 1 and 5000")
        continue
    
    count+=1
    total+=sale
    
    if highest_sale is None or highest_sale < sale :
        highest_sale = sale
    if lowest_sale is None or lowest_sale> sale:
        lowest_sale= sale
        
        
    if sale > 1000:
        big_sale+=1
    else:
        small_sale+=1
        
if count>0:
    average=total/count
    big_sale_percentage= (big_sale/count)*100
    small_sale_percentage= (small_sale/count)*100
    
    print("Highest sale is ", highest_sale)
    print("Lowest sale is ", lowest_sale)
    print("Big sale is ", big_sale)
    print("Small sale is ", small_sale)
    print("Big sale Percentage is ", big_sale_percentage)
    print("Small sale Percentage is ", small_sale_percentage)
    print(" Average is ", average)
    
else:
    print("No sales inserted")
