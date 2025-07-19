import student, pickle
with open('student.data', 'rb') as f:
    while True:
        try:
            s = pickle.load(f)
            s.display()
        except EOFError:
            break
        except Exception as e:
            print(f"An error occurred: {e}")
    