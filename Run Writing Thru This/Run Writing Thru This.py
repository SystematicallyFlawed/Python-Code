##Simple script to replace any lone uncapitalized "i"s with capitalized "I"s##
writing = input("Type or paste writing here  ")
writing = writing.replace("i ", "I ")
writing = writing.replace("i've", "I've")
print(writing)
print(" ")
input("Press enter to exit program")