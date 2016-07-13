# PSEUDOCODE FOR CALCULATING a^b where a and b are positive integers
# Here [x] denotes the floor function, that is, the largest integer less than or equal to x.

# FastPower(a,b) :
#   if b = 1
#     return a
#   else
#     c := a*a
#     ans := FastPower(c,[b/2])
#   if b is odd
#     return a*ans
#   else return ans
# end


# check the runtime of FastPower()
def FastPower(a,b):
    global count
    if b == 1:
        count += 1
        return a
    else:
        count +=2
        c = a*a
        ans = FastPower(c,b/2)
    if b%2 == 1:
        count +=1
        return a*ans
    else:
        count +=1
        return ans
count = 0
print FastPower(2,9), count

count = 0
print FastPower(2,8), count

count = 0
print FastPower(2,7), count

count = 0
print FastPower(2,6), count

count = 0
print FastPower(2,5), count

count = 0
print FastPower(2,4), count

count = 0
print FastPower(2,3), count

count = 0
print FastPower(2,2), count

count = 0
print FastPower(2,1000), count