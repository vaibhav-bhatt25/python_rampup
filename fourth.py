def switch_key_values(data):
    return {v: k for k, v in data.items()}

data={
    "key1":"value1",
    "key2":"value2",
    "key3":"value3",
    "key4":"value4",
    "key5":"value5"
}

result=switch_key_values(data)
print(result)