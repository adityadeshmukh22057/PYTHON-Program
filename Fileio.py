def write_to_file():
    open('file.txt', 'w').write('Hello, world!')
    print("File written successfully.")
    write_to_file()