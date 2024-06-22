# We will first create the list

menu = ['croisant', 'latte', 'biscuits', 'cake']

# We will create the dictionary to contain the stock

stock = {'croisant':  2,
         'latte':     5,
         'biscuits':  200,
         'cake':      20
         }
# Next we will create a second dictionary containing the price
price = {'croisant':  1.20,
         'latte':     2.50,
         'biscuits':  1.20,
         'cake':      4.50
         }

# Next we will calculate the total_stock worth in the caffe 
# We will use the for loop
total = 0
for items in menu:
    total += stock[items] * price[items]
print(total)
      

         
