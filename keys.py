"""
Write three functions:
sort1(languages)
sort2(languages)
sort3(langauges)
Goal: Print exactly the below w/ three functions:
1:
    Arabic
    English
    Koine Greek
    Latin
    Romanian
    C++
    JavaScript
    Python
    R
2:
    R
    C++
    Latin
    Arabic
    Python
    English
    Romanian
    JavaScript
    Koine Greek
3:
    JavaScript
    R
    Latin
    Python
    Romanian
    Koine Greek
    English
    Arabic
    C++
"""
languages = {'JavaScript': 'P',
             'Arabic': 'N',
             'R': 'P',
             'Python': 'P',
             'C++': 'P',
             'Koine Greek': 'N',
             'Latin': 'N',
             'Romanian': 'N',
             'English': 'N'}

def sort1(languages):
    lst = sorted(sorted(languages, key=languages.__getitem__))
    for x in lst:
        print("\t" + x) #print tab

def sort1b(d):
    import operator
    lst = sorted(sorted(d.items()), key=operator.itemgetter(0))
    print("1: ")
    for languages, type_ in lst:
        print("\t" + languages) #print tab

def sort2(languages):
    lst1 = sorted(languages)
    lst2 = sorted(lst1, key=len)
    print(lst2)

def last_char(string):
    return string[-1].lower()

def sort3(d):
    lst = sorted(sorted(d), key=last_char, reverse=True)
    print("3: ")
    for item in lst:
        print("\t" + item)


sort1b(languages)
sort2(languages)
sort3(languages)
