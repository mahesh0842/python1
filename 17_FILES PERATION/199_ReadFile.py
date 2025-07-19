with open('abc.data','rb') as fileread:
    #fileread.write(b'abcdefghi jkl')  # Write bytes to the file
    print(fileread.read(2).decode())  # Read bytes from the file
    fileread.seek(3,1) # Move the cursor to the 3rd byte
    print(fileread.read(10).decode())  # Read bytes from the file
    fileread.seek(-3,1)
    print("NEGATIVE = ",fileread.read(2).decode())  # Read bytes from the file leaving the last 3 bytes

