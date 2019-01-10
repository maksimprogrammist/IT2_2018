import sys

# for i in range(10):
#     print(i)

g = sys.platform
k = "\\"
print(sys.prefix)
print(f"{(sys.prefix).split(sep=k)[2]}, теперь я знаю твоё имя............")
if "linux" in g:
    print("оу май...")

print('Hello мир')


