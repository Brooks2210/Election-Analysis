Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> type(3)
<class 'int'>
>>> type(73.91)
<class 'float'>
>>> type("Hello World")
<class 'str'>
>>> type(True)
<class 'bool'>
>>> 5+2*3
11
>>> 8//5-3
-2
>>> 8+22*2-4
48
>>> 16-3/2+7-4-1
16.5
>>> 3**3%5
2
>>> counties = ["Arapahoo", "Denver", "Jefferson"]
>>> counties
['Arapahoo', 'Denver', 'Jefferson']
>>> counties[0]
'Arapahoo'
>>> print(counties[-1])
Jefferson
>>> len(counties)
3
>>> counties.append("El Paso")
>>> counties
['Arapahoo', 'Denver', 'Jefferson', 'El Paso']
>>> counties.insert(2, "El Paso")
>>> counties
['Arapahoo', 'Denver', 'El Paso', 'Jefferson', 'El Paso']
>>> counties.pop(4)
'El Paso'
>>> counties.pop(2)
'El Paso'
>>> counties
['Arapahoo', 'Denver', 'Jefferson']
>>> counties[1]
'Denver'
>>> counties[1] = "El Paso"
>>> counties
['Arapahoo', 'El Paso', 'Jefferson']
>>> counties.pop(0)
'Arapahoo'
>>> counties
['El Paso', 'Jefferson']
>>> counties.insert(2, "Denver"0
		
SyntaxError: invalid syntax
>>> counties.insert(2, "Denver")
>>> counties
['El Paso', 'Jefferson', 'Denver']
>>> counties.insert(-1, "Arapahoe")
>>> counties
['El Paso', 'Jefferson', 'Arapahoe', 'Denver']
>>> counties.pop(2)
'Arapahoe'
>>> counties.insert(3, "Arapahoe")
>>> counties
['El Paso', 'Jefferson', 'Denver', 'Arapahoe']
>>> my_tuple = ()
>>> counties_tuple = ("Arapahoe", "Denver", "Jefferson")
>>> len(counties_tuple)
3
>>> counties_tuple[1]
'Denver'
>>> counties_dict ={}
>>> counties_dict counties_dict["Arapahoe"] = 422829
SyntaxError: invalid syntax
>>> counties_dict["Arapahoe"] = 422829
>>> countie_dict
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    countie_dict
NameError: name 'countie_dict' is not defined
>>> counties_dict
{'Arapahoe': 422829}
>>> counties_dict["Denver"] = 463353
>>> counties_dict["Jefferson"] = 432438
>>> counties_dict
{'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}
>>> len(counties_dict)
3
>>> counties_dict.items()
dict_items([('Arapahoe', 422829), ('Denver', 463353), ('Jefferson', 432438)])
>>> counties_dict.keys()
dict_keys(['Arapahoe', 'Denver', 'Jefferson'])
>>> counties_dict.values()
dict_values([422829, 463353, 432438])
>>> counties_dict.get("Denver")
463353
>>> voting_data = ()
>>> voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
AttributeError: 'tuple' object has no attribute 'append'
>>> voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
AttributeError: 'tuple' object has no attribute 'append'
>>> voting_data
()
>>> voting_data = []
>>> voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
>>> voting_data.append({"county":"Denver", "registered_voters": 463353])
SyntaxError: invalid syntax
>>> voting_data.append({"county":"Denver", "registered_voters": 463353})
>>> voting_data.append({"county":"Jefferson", "registered_voters": 432438})
>>> voting_data
[{'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}]
>>> 