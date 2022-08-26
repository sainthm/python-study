a = 'HelloWorld!'

b = 'I Love Futureskill'



i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

j = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]



results_a = ''

results_b = ''



for x in i:

if a[x].isupper() == True:

results_a += a[x]

else:

pass



print(results_a)



for x in j:

if b[x].isupper() == True:

results_b += b[x]

else:

pass



print(results_b)