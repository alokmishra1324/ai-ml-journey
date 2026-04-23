# with open('example.txt' , 'r') as file:
#     content = file.read()
#     print(content)


# with open('example.txt' ,'r') as file:
#     for line in file:
#         print(line)
 
# with open('example.txt' ,'r') as file:
#     for line in file:
#         print(line.strip()) ## remove the newline character

##writing a file

# with open('example.txt' ,'w') as file:
#     file.write('Hello World!\n')
#     file.write("This is new line") ## overwrite the entire content


# with open('example.txt' , 'a') as file:
#     file.write(" Append operation taking place! ")

## writin list lines to a file
# lines = ['First line\n' , 'Second line\n', 'Third line\n']

# with open('example.txt' , 'a') as file:
#     file.writelines(lines)


##Binary files
# data = b'\x00\x01\x02\x03\x04'
# with open('example.bin' ,'wb') as file:
#     file.write(data)


# with open('example.bin' , 'rb') as file:
#     content = file.read()
#     print(content)

##Read the content from source file and write to a destination file
# with open('source.txt' ,'r') as s_file:
#     content = s_file.read()

# with open('destination.txt' ,'w') as de_file:
#     de_file.write(content)


def count_text_file(file_path):
    with open(file_path , 'r') as file:
        lines = file.readlines()
        line_count = len(lines)
        word_count = sum(len(line.split()) for line in lines)
        char_count = sum(len(line) for line in lines)
    return line_count , word_count , char_count

file_path = 'example.txt'
liness , words, characters = count_text_file(file_path)
print(f'Lines:{liness} , Words :{words} , Characters :{characters}')


with open('source.txt' , 'w+') as file:
    file.write("Hello Rahul , how are you ")
    file.write("Please start preparing for switch")

    file.seek(0)
    file.write("He")
    content = file.read()
    print(content)