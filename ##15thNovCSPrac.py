n=int(input('Enter the Number whose table you want'))
if n > 10:
    print('Please enter a number between 0-10')
i=0
while i<=10:
    ans=n*i
    print('3 x ' ,i ,'=',ans)
    i = i + 1 