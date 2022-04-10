#Program_2
#A list contains the average daily temperature(in degree Celsius) of a city over a particular week. 
#Write a Python code to swap the highest and the lowest temperatures


# A list containing average daily temperature over a week 
temperatures = [34, 40, 29, 33, 42, 37, 39 ]

# The expected output 
# output_temperatures = [34, 40, 42, 33, 29, 37, 39]

#solution:

# Store the highest temperature
max_temp = max(temperatures)
print(max_temp)

# Index of the element with the highest temperature
max_temp_index =temperatures.index(max_temp)
max_temp_index

# Store the lowest temperature 
min_temp = min(temperatures)
print(min_temp)

# Index of the element with the lowest temperature
min_temp_index =temperatures.index(min_temp)
print(min_temp_index)

# Swap the highest and the lowest temperatures

temperatures[max_temp_index]=min_temp
temperatures[min_temp_index]=max_temp

# Print the output list
print(temperatures)