emli = []
for i in range(4):
    emli.append(int(input("Enter an integer: ")))
emli.sort()
print("가장큰수=", max(emli))
emli.remove(max(emli))
print(emli)
