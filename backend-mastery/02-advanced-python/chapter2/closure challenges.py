# challenge 1: counter

def outer(count):
    
    def inner(new_count):
        new_count = count*4
        return new_count
    return inner

number = outer(4)
print(number(0))


# challenge 2: validator

def max_lenth(n):
    def validator(text):
        return len(text) <= n
    return validator

def min_length(n):
    def validator(text):
        return len(text) >= n
    return validator

def contains_digits():
    def validator(text):
        return any(char.isdigit() for char in text)
    return validator

max = max_lenth(70)
print(max("huihhhbhbykjahshdgshdgs"))

min = min_length(8)
print(min("ytgujuuuuuuuuuu"))

contains_dig = contains_digits()
print(contains_dig("uyihhhhbb45"))

# challenge 3: running average
