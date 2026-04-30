my_lst = [1,2,3,4,5]

for i in my_lst:
    print(i)


iterator = iter(my_lst)

print(type(iterator))

print(iterator)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))


try:
    print(next(iterator))
    # print(next(iterator))
    # print(next(iterator))
    # print(next(iterator))
    # print(next(iterator))
    # print(next(iterator))
except StopIteration:
    print("There are no elements in the iterator")


my_str = "Hello"
str_iterator = iter(my_str)

print(next(str_iterator))
print(next(str_iterator))


class Mynumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 10:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = Mynumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
