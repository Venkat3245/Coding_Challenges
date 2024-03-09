def subsets_2_elements(given_list, target_sum): #creating a functio to calculate number of subsets with 2 elements which equal to target sum
    subsets = [] #creating subsets with an empty list
    n = len(given_list) # required for the next part
    for i in range(n): # this takes all index values from 0 to n-1 for the first element also this loops goes till n-1 index
        for j in range(i + 1, n): # taking the second element for the subset from i+1 to n-1
            subset_sum = given_list[i] + given_list[j] # calculating the sum of the two elements 
            if subset_sum == target_sum: 
                subset_final = (given_list[i], given_list[j]) # if the sum is equal to target sum then making their subset
                subsets.append(subset_final) # appendind it to the subsets list
    return subsets


given_list = input("Enter a list of numbers separated by spaces: ").split() # taking the user input and sperating them by spaces
given_list = [int(x) for x in given_list]# converting each number into an integer and [] used to make it a list


target_number = int(input("Enter the target number: ")) # getting the target sum from the user

result = subsets_2_elements(given_list, target_number) # calling the function
if result: # simple if and else used to give outputs where the subsets exist or if subsets don't
    print("Subsets with 2 elements that equal to target number: ",result)
else:
    print("No subsets found with 2 elements that sum up to the target number.")
    
