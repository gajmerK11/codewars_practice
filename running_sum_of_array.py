# Example 1:
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

# Example 2:
# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

# Example 3:
# Input: nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]

def running_sum_array(list_input):
    output_list = []
    output_list.append(list_input[0])
    for each_number in list_input[1:]:
        add = each_number + output_list[-1]
        output_list.append(add)
    return output_list
print(running_sum_array([1,1,1,1,1]))
    
         

        
        

    