filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    message = "Sorry, the file " + filename + " does not exist."
    print(message)
else:
    # Count the approximate number of words in the file
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")