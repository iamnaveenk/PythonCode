#Problem 2

#Measures of Averages

#Mean of a group is defined as the sum of the elements in the group divided by the number of elements in the group.
#Median is the middle number in a sorted, ascending or descending, list of numbers. 

#If the list has  N  numbers where  N  is odd, then median is the element in the middle i.e,  (N+12)th  element. 
#If  N  is even, then median is the mean of  (N2)th  and  (N2+1)th  elements

#solution:

# List of product prices

prod_price_list = [400, 250, 800, 550, 600, 820, 720, 15000, 360,250]
sum(prod_price_list)
len(prod_price_list)

# Calculate the mean of the product prices. Use list functions. Also print the mean_price

mean_price = sum(prod_price_list)/len(prod_price_list)
mean_price

#Calculate the median price

# Step 1 - Obtain the sorted list. Print the sorted_prices
sorted_prices = sorted(prod_price_list)
print(sorted_prices)

# Check if the number of elements in the list is even or odd
N=len(sorted_prices)
print(N)


# Use the corresponding formula to calculate the median and print the median
median_price = (sorted_prices[int(N/2)-1]+sorted_prices[int(N/2)])/2
median_price

# Check which is greater, mean or median
mean_price>= median_price