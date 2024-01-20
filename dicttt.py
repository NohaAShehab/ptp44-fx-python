

""" dictionary """


info = ['noha', 31, 'iti', 'fx']


""" represntation data in form of labeled data """

### representation data in for of labeled data  ---> dictionary


d = {}

myd = dict()

""" data in the dict ---> key value pair """

myinfo  = {
    "name":"Noha",
    "age": 31,
    "track": "fx",
    "work": "iti"
}

print(myinfo)
""" dict is mutable data type"""

myinfo["name"]= 'Noha Shehab'
print(myinfo)


myinfo['city']= 'Cairo'  # key not exists ---> add it to the dict
print(myinfo)




