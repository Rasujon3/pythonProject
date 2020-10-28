from collections import deque

bank = deque(["Sujon","Naim","Arin"])
print(bank)
bank.popleft()
print(bank)

bank.popleft()
print(bank)

bank.popleft()
if not bank:
    print("No person left.")