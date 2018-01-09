list_one1 = [1,2,5,6,2]
list_two1 = [1,2,5,6,2]

list_one2 = [1,2,5,6,5]
list_two2 = [1,2,5,6,5,3]

list_one3 = [1,2,5,6,5,16]
list_two3 = [1,2,5,6,5]

list_one4 = ['celery','carrots','bread','milk']
list_two4 = ['celery','carrots','bread','cream']

def listCompare ( list1, list2 ):
    if list1 == list2:
        print "The lists are the same."

    else:
        print "The lists are not the same."

listCompare(list_one1, list_two1)
listCompare(list_one2, list_two2)
listCompare(list_one3, list_two3)
listCompare(list_one4, list_two4)