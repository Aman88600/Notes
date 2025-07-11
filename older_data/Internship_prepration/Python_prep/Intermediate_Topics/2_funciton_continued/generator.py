def sum_nums(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    sum = 0
    for i in nums:
        sum += i
    return sum
print(sum_nums(10))

# This is a genetator funciton because of yield keyword
def produce_nums(n):
    i = 0
    while i < n:
        yield i
        i += 1 

x = iter(produce_nums(10000)) # making a iterator to iterate over the generator
while True:
    try:
        print(next(x)) # next keyword allows us to go to the next iteration
    except:
        break