# PROGRAMMING WITH MOSH

# numbers = [1, 3, 8, 7, 4, 2, 5, 9, 6]
# #numbers.sort()
# #numbers.reverse()
# num = numbers.copy()
# numbers.append(10)
# num.append(11)
# print(num)
# print("I am happy :)")

message = input("> ")
words = message.split(" ")
emojis = {
    ":)": "😀",
    ":(": "😒",
}

output = ""
for word in words:
    output += emojis.get(words, words) + " "
    
print(output)