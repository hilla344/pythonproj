# list datastrucyure
from operator import index

fruits=["mangoes","Banana","apples","grapes"]
print(fruits)
print(f"I love eating {fruits[0]}")
numbers=[1,2,3,4,5,0,7,9]
numbers.sort()
numbers.append("pineapples")
numbers.pop(5)
numbers.reverse()
print(numbers)

#tuple datastructures
# immutable
# has index
# ordered
cars=("Mercedes","Nissan","Toyota","Subaru","Range Rover","Mazda","Honda ","Vw")
nambari=(3,9,5,6,-78,56,55,45,12)
print(nambari)
print(f"i love making {cars[6]}")
print(sorted(nambari))

# set datastructure
country={"Kenya","Uganda","Tanzania","Burundi","USA","Dubai","Mexico"}
country.pop()
print(country)
# no index
# unodered

# dictionary data structure
# key vakue pair
student={"name":"Hillary","age":17,"Gender":"Male","Phone Number":115958012}
print(f"My name is {student['name']} am {student['age']} years old.My gender is {student['Gender']}")