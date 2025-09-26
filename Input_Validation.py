while True:
    global ui
    ui = input("Enter the number: ")
    if not ui:
        print("Enter the input")
    else:
        break
print(ui)
if __name__ == '__main__':
    print("Hello world")