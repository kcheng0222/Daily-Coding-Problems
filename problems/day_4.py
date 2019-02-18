arr = [1, 2, 1]

lookingFor = 1 #minimum positive number is 1

arr.sort() #sort the array duh

for x in arr:
    if x > lookingFor: #if the smallest in array is blatantly larger
        break #we foundem
    elif x == lookingFor: #oh no you matched me
        lookingFor += 1 #time to look for the next number
print(lookingFor) #we went through the whole array and couldn't find it. It must be what lookingfor is
