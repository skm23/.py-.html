print("""
请选择你要求的边:
1.直角三角形的直角短边
2.直角三角形的直角长边
3.直角三角形的斜边
""")
def share(): #求直角三角形的直角短边
    hook = int(input("请输入直角三角形的直角长边"))
    string = int(input("请输入三角形斜边"))
    share = (string ** 2) - (hook ** 2)
    share1 = pow((string ** 2) - (hook ** 2), 0.5)
    if int(share1) == share1:
        print(f"{share1}")
    else:
        print(f"√{share}")
def hook(): #求直角三角形的直角长边
    share = int(input("请输入直角三角形的直角短边"))
    string = int(input("请输入三角形斜边"))
    hook = (string ** 2) - (share ** 2)
    hook1 = pow((string ** 2) - (share ** 2), 0.5)
    if int(hook1) == hook1:
        print(f"{hook1}")
    else:
        print(f"√{hook}")
def string(): #求直角三角形的斜边
    share = int(input("请输入直角三角形的直角短边"))
    hook = int(input("请输入直角三角形的直角长边"))
    string = (share ** 2) + (hook ** 2)
    string1 = pow((share ** 2) + (hook ** 2), 0.5)
    if int(string1) == string1:
        print(f"{string1}")
    else:
        print(f"√{string}")
a = int(input())
if a == 1:
    share()
elif a == 2:
    hook()
elif a == 3:
    string()
