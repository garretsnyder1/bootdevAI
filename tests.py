from functions.get_files_info import get_files_info

test1 = get_files_info("calculator", ".")
test2 = get_files_info("calculator", "pkg")
test3 = get_files_info("calculator", "/bin")
test4 = get_files_info("calculator", "../")

tests = [test1, test2, test3, test4]

for test in tests:
    print(test)