'''
Created on May 8, 2019

@author: Mosarrof Hossain
'''
a = 18
b = int(4.08)

c = a % b
# If condition
if (c==2) :
    
    print("Success")
    
else :
    print("Fail")
 
print("It is true")
print (c)

# for loop  

wel = " Welcome"
for i in wel :
    print(i)
    
for j in range(1,11) :
 print(j)
 
 # while loop 
 
count=0
while(count <= 5):
 count = count + 1
 print(count) 
print(".........................................")
city= "California"
town = "Miami"
print(city.index("i" and "o"))
print(city.count("o"))
print(city[0])
print(city[4:10])
print(city + " & " + town)

# lists 

lists = [1,2,3,4,4,4,8]
lists.append(0)
lists.append(0)
lists.append(0)
 
print(lists)
print(lists.count(4))


print(lists.index(0))
# Dictionary 

d = {'a':'10', 'b':'40'}

print(d)
print(d['a'])

c={}
c['one'] = 40
c['two'] = 40
sum_dict = c['two'] + c['one'] 

print(sum_dict)
print("*"*20)
"""
Nested dictionary and diction 
Please see the below code 
"""
cars = {'bmw': {'model': '550i', 'year': 2016}, 'benz': {'model': 'E350', 'year': 2015}}

bmw_year = cars['bmw']['year']

print(bmw_year)
print(cars['benz']['model'])

