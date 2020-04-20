config = {
    "levels": [
        {"name": "Level 1", "items": [(100, 110), (200, 220), (300, 330)]},
        {"name": "Level 2", "items": [(100, 101), (200, 201), (300, 301), (400, 401)]},
        {"name": "Level 3", "items": [(100, 125), (200, 175)]}
        ]
    }




def parse_item(path, item):
    key, value = item
    if type(item) is dict:
        parse_dict(path, item)
    elif type(item) is tuple and type(key) is int:
        parse_tuple(path, item)
    elif type(value) is list:
        parse_list(path + key, value)
    else:
        print(path + str(key) + "=" + str(value))
    

def parse_tuple(path, t):
    t1, t2 = t
    print(path + "item=" + str(t1) + "-" + str(t2))
    
def parse_list(path, lst):
    print(path + ".numitems=" +str(len(lst)))
    i  = 0
    for item in lst:
        parse_item(path + "." + str(i) + ".", item)
        i = i + 1

def parse_dict(path, d):
    
    for item in d.items():
        parse_item(path, item)
        


parse_dict("", config)
