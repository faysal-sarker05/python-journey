countries = ["BD", "JP", "IN", "FR"]

for index, country in enumerate(countries):
    print(index, country)


animals = ["Cat", "Dog"]

for index, animal in enumerate(animals):
    print(index + 1, animal)



fruits = ["Apple", "Cherry", "Banana"]

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)



students = ["Faysal", "Abdullah", "Abdur Rahman"]

for number, student in enumerate(students, start=1):
    print(number, "-", student)