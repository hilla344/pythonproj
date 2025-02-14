num=1
while num<10:
    print(num)
    num+=1

for num in range(1,11):
    print(num)
fruits=["Bananaas","Oranges","Bananas","Ovacados"]
for fruit in fruits:
    print(fruit)

namme="hillary"
for namme in namme:
    print(namme)

number=[4,-7,-4,9,2,1,6,2,4,7,6,5,8,10,12]
sum_even=0
sum_odd=0

for y in number:
    if y % 2 == 0:
        sum_even+=y
    else:
        sum_odd+=y
print(f"the sum of even is {sum_even}")
print(f"the sum of odd is {sum_odd}")


