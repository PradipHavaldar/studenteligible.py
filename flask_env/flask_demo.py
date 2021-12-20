
def convert_multi_tostr(values):
    #values = ["A","B","C"]
    finalvalues = ''
    for ind,item in enumerate(values):
        if ind == 0:
            finalvalues = item
        else:
            finalvalues = finalvalues +','+item
    print(finalvalues)
    return finalvalues
convert_multi_tostr(["A","B","C",'12','Z'])