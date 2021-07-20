# 1. Write a while loop that is initialized at 0 and stops at 15. If the counter is an even number, append the counter to a list called eve_nums.
count = 0
eve_nums = []

while count <= 15:
    c = count % 2
    if c == 0:
        eve_nums.append(count)
    count += 1
        
print(eve_nums)



# 2. Below, we’ve provided a for loop that sums all the elements of list1. 
# Write code that accomplishes the same task, but instead uses a while loop. Assign the accumulator variable to the name accum.
list1 = [8, 3, 4, 5, 6, 7, 9]

elem = 0
accum = 0
while elem < len(list1):
    accum = accum + list1[elem]
    elem += 1

print(accum)
#tot = 0   
#for elem in list1:
#    tot = tot + elem



# 3. Write a function called stop_at_four that iterates through a list of numbers. 
# Using a while loop, append each number to a new list until the number 4 appears. The function should return the new list.
def stop_at_four(lst):
    new_list = []
    elem = 0
    
    while elem < len(lst):
        if lst[elem] == 4:
            break
        new_list.append(lst[elem])
        elem += 1
    
    print(new_list)    
    return new_list

  
