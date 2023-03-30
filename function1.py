# simple function

def total(a,b):
    return a+b

c = total(3,4)
print(c)
print(total(5,6))


def vowelcount(txt):
    vowels = 'aeiouAEIOU'
    counter = 0
    for char in txt:
        if char in vowels:
            counter+=1
    return counter




print(vowelcount("hello"))

def vowelcount2(txt):
    vowels = 'aeiou'
    counter = 0
    for char in txt.lower():
        if char in vowels:
            counter+=1
    return counter


def average(a):
    return sum(a)/len(a)

print(average([1,2,3]))


#write a function names uniq_word_count that takes a filename as input
#and returns the number of uniq words

def uniq_word_count(filename):
    with open(filename,'r') as f:
        text = f.read()
    wordcount = len(set(text.split()))
    return wordcount

print(uniq_word_count("sample2.txt"))


def add_fqdn(servername):
    domain = ".ent.wfb.bank.com"
    return  servername + domain

print(add_fqdn("printsvr1"))
