def converted_temp(temp , unit):
    if unit == 'C':
        return temp *9/5 + 32
    elif unit =='F':
        return (temp-32)*5/9
    else:
        return "Invalid unit"
    
print(converted_temp(100, 'C'))
print(converted_temp(212, 'F'))

## password checker function

def is_strong_password(password):
    if len(password)<8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char in '!@#$%^&*()_+' for char in password):
        return False
    
    return True

print(is_strong_password("St#122323"))


def total_cost(cart):
    tcost = 0
    for item in cart:
        tcost += item['price']*item['quantity']
    return tcost

cart=[

    {"name":"Apple" , "price" :100 , "quantity":2},
    {"name":"Banana" , "price" :50 , "quantity":3},
    {"name":"Orange" , "price" :80 , "quantity":1}
]
 
print(total_cost(cart))
 

def check_pallindrome(s):
    s=s.lower().replace(" " , "")
    return s == s[::-1]

print(check_pallindrome("A man a plan a canal Panama"))
print(check_pallindrome("Hello"))
print(check_pallindrome("121"))
     
def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(8))

## function to read a file and count the frequency of each word

def count_word(file_path):
    word_count = {}
    with open(file_path , 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word=word.lower().strip('.,!?;:"\'')
                word_count[word] = word_count.get(word,0)+1

    return word_count

filepath ='sample.txt'
word_freq = count_word(filepath)
print(word_freq)


## validate email address
import re
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern , email) is not None

print(is_valid_email("test@example.com"))
print(is_valid_email("invalid-email"))