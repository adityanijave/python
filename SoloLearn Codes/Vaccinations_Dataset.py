# Statement :
'''
 Using the same vaccinations dataset, which includes the number of times people got the
flu vaccine.
The dataset contains the following numbers:
never: 5, once: 8, twice: 4, 3 times: 3
Calculate and output the variance. Declare a list with the data and use a loop to calculate the value.
We will soon learn about easier ways to calculate the variance and other summary statistics using Python.
For now, use Python code to calculate the result using the corresponding equation.
'''

# Code :
dataset = [5,8,4,3]

sum_of_elements_in_dataset = 0
for element in dataset:
    sum_of_elements_in_dataset += element
print(f"The Sum of Elements in Dataset is {sum_of_elements_in_dataset}.")

mean = sum_of_elements_in_dataset / len(dataset)
print(f"The Value of MEAN is {mean}")

for_variance = 0
for element in dataset:
    as_required_sum = (element - mean)**2
    for_variance += as_required_sum

variance = for_variance/(len(dataset) - 1)
print(f"The Variance is {variance}")