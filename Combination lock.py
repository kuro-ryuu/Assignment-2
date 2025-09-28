import random 
lock1 = [random.randint(0, 9) for _ in range(3)]
lock2 = [random.randint(1, 6) for _ in range(4)]
lock1 = int("".join(map(str, lock1)))
lock2 = int("".join(map(str, lock2)))
print(f"Lock 1: {lock1:03d}\n"
      f"Lock 2: {lock2}")
