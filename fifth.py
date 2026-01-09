def set_operations(list1,list2):
    set1=set(list1)
    set2=set(list2)

    common=list(set1 & set2)
    difference= list(set1 ^ set2)

    return common,difference


mainstream =[
    "One Punch Man",
    "Attack On Titan",
    "One Piece",
    "Sword Art Online",
    "Bleach",
    "Dragon Ball Z",
    "One Piece"
]

must_watch =[
    "Full Metal Alchemist",
    "Code Geass",
    "Death Note",
    "Stein's Gate",
    "The Devil is a Part Timer!",
    "One Piece",
    "Attack On Titan"
]

intersection,diff = set_operations(mainstream,must_watch)
print(intersection)
print(diff)
