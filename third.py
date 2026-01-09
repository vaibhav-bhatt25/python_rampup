def sorting(data,choice):
    data.sort(key= lambda x:x[choice])
    return data

data=[
    {"fruit": "orange", "color": "orange"},
    {"fruit": "apple", "color": "red"},
    {"fruit": "banana", "color": "yellow"},
    {"fruit": "blueberry", "color": "blue"}
]
sorting(data,"fruit")
print("Data after Sorting:")
print(data)