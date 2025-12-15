from functions.write_file_content import write_file

test1 = [write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"), "calculator/lorem.txt", "lorem.txt"]
test2 = [write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"), "calculator/pgk/morelorem.txt", "morelorem.txt"]
test3 = [write_file("calculator", "/tmp/temp.txt", "this should not be allowed"), "/tmp/temp.txt", "temp.txt"]

tests = [test1, test2, test3]

for test in tests:
    print(f"Result for '{test[2]}': {test[0]}")