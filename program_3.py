#Problem 3
#Having a nested list sometimes might be a bit problematic. 
#An individual was asked to collect the names of companies in the technology sector. 
$While creating the list, by mistake the last three companies were subsumed in a list as shown below. You are required to get rid of the nesting

# The list of tech companies curated by the individual
tech_companies = ['Qualcomm','Google','Apple',['Nvidia','Cisco','Samsung']]


# The final list that we want
# correct_tech_companies = ['Qualcomm','Google','Apple','Nvidia','Cisco','Samsung']


#solution:

# Write  code below
tech_companies[ : -1]+tech_companies[-1]

# Do the same task another way
tech_companies = ['Qualcomm','Google','Apple',['Nvidia','Cisco','Samsung']]
last_element=tech_companies.pop()
tech_companies.extend(last_element)
print(tech_companies)