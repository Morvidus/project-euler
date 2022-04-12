# euler palindromic product

# largest palindromic of two 2-dig nos is 9009 (91x99), find for 3

# func to check palindromic
def check_palin(prod):
    return str(prod) == str(prod)[::-1]
                
# gen two lists of 3 digit nums
bot=100
top=1000
list1=[]
list2=[]

for i in range(bot, top):
    list1.append(i)
    list2.append(i)

##def largest(bot, top):
##    z = 0
##    for x in range(top, bot, -1):
##        for y in range(top,bot, -1):
##            if check_palin(x*y):
##                if x*y > z:
##                    z = x*y
##    return z
##print(largest(bot, top))

## compare both lists for palindromes
prod=0
for num in list1:
    for num2 in list2:
        if check_palin(num*num2):
            if num*num2 > prod:
                prod=num*num2

print(prod)
