def extension_finder(ext_type,files):
    ext_dict={}
    pairs=ext_type.split(';')
    for i in pairs:
        if ',' in i:
            ext,f_type=i.split(',')
            ext_dict[ext]=f_type

    result={}
    for j in files:
        if '.' in j:
            extension=j.split('.')[-1]
            result[j]=ext_dict.get(extension,"unknown")

        else:
            result[j]="unknown"

    return result


ext_type="xls,spreadsheet;xlsx,spreadsheet;jpg,image"
files=["abc.jpg", "xyz.xls", "text.csv", "123"]
output=extension_finder(ext_type,files)
print(output)