def string_both_ends(str):
    if len(str) < 2:
        return ''
    return str[0:2] + str[-2:]

def findNum(n1,n2):
    numlist=[]
    if n1==n2:
        return numlist
    for i in range(n1,n2):
        if i%7==0 and i%5 != 0:
            numlist.append(i)
    return numlist

def combineDict(dict1, dict2):
    dict3={}
    for i in dict2.keys():
        if i in dict1.keys():
            dict3[i] = dict1[i] + dict2 [i]
    dict3 = dict2 | dict3
    dict3 = dict1 | dict3
    return dict3

def printInvoice(n):
    if n<1:
        return
    itemList=[]
    i = 0
    while i<n :
        itemStr = input("Input item and price:  ")
        itemInfo= itemStr.split()
        itemDict = {
            "name" : itemInfo[0],
            "count" : int(itemInfo[1])
            }
        itemList.append(itemDict)
        i += 1
    #Sorting a list of dictionaries by key, code from GeekOfGeeks
    #https://www.geeksforgeeks.org/ways-sort-list-dictionaries-values-python-using-lambda-function/
    itemList = sorted(itemList, key=lambda i: i["count"])

    print(itemList)
    for item in itemList:
        print(item["name"] , item["count"])

def main():
  
    #1
    string = input("Please enter a string: ")
    stringToReturn = string_both_ends(string)
    print(stringToReturn)

    #2
    n1 = input("Please enter first number: ")
    n2 = input("Please enter second number: ")
    nlist = findNum(int(n1), int(n2))
    #print(nlist)

    #3
    dict1 = input("Input first dictionary: ")
    dict2 = input("Input second dictionary: ")
    dictCombined = combineDict(dict1, dict2)
    print(dictCombined)

    #4
    count = input("Number of items: ")
    printInvoice(int(count))

if __name__ == "__main__":
    main()



