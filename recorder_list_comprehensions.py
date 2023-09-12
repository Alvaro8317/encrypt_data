# newlist = [expression for item in iterable if condition == True]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist1 = [x for x in fruits if x != "apple"]
newlist2 = [fruit.upper() for fruit in fruits]
# print(newlist2)
old_list = [{
    "lastloginsucess": "2020-02-04T18:32:58Z",
    "maincustomerid": 418077.0,
    "nickname": "leyrod24",
                "status": "Activo",
                "userid": 1632.0,
                "usernames": "LEYVA RODRIGUEZ"
},
    {
    "lastloginsucess": "2020-06-22T21:16:25Z",
    "maincustomerid": 70900581.0,
    "nickname": "marauz06",
                "status": "Activo",
                "userid": 1637.0,
                "usernames": "MANUEL ARAÚZ"
},
    {
    "lastloginsucess": "2020-07-03T14:44:58Z",
    "maincustomerid": 230464.0,
    "nickname": "itza25",
                "status": "Activo",
                "userid": 1639.0,
                "usernames": "ITZA MORALES"
}]
newlist3 = [person['nickname'] for person in old_list]
print(newlist3)