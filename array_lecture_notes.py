'''

What is an int?
    - in memory: 4 bytes (32 bits) --- 8 bits in a 1 byte

What is a short?
    - in memory: 

super_short - 4 bits 
0    0 0 0 0
1    0 0 0 1
2    0 0 1 0
3    0 0 1 1
4    0 1 0 0 
5    0 1 0 1

my_array = [3]
    - how many bits should we allocate to an array that holds 3 numbers(super_short ints)?
        - 12 
    - what happens if we print(my_array[0])?
        - its a memory address, and accessing my array at index 0 is for to cell f16, count right (index * data size) then grab data size bits
        - this will print 4 UNLESS someone programs a different result

my_array.append(1) 
    - what can we do?
        - mark the end of the array (4 bits) as in use and write the data there
        - my_array.append(2)? (3)? (4)? (5)?

what happens when the function in which my_array was instantiated exits? i.e. we're done ith my_array
    - in a memory managed language, it gets garbage collected, it notices it not being used anymore and it deallocates it, it's free now, anyone who wants it can take it

what happens if I want to delete my_array(0)? ie pop it?
    - 


'''