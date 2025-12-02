from functions.get_file_content import get_file_content

test1 = [get_file_content("calculator", "main.py"), "calculator", "main.py"]
test2 = [get_file_content("calculator", "pkg/calculator.py"), "calculator", "pkg/calculator.py"]
test3 = [get_file_content("calculator", "/bin/cat"), "calculator", "/bin/cat"]
test4 = [get_file_content("calculator", "pkg/does_not_exist.py"), "calculator", "pkg/does_not_exist.py"]

tests = [test1, test2, test3, test4]

for test in tests:
    print(f"Result for '{test[2]}':\n{test[0]}")