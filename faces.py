

def convert(text):

    return text.replace(":)", "🙂").replace(":(", "🙁")

def main():
    user_input = input("Enter a message: ")
    print(convert(user_input))


main()
