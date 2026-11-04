from typing import List

def read_integers() -> List[int]:
    ans = input()
    return [int(i) for i in ans.split(",")]

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
