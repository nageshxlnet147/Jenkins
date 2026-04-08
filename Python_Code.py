def Jenkins():
    print("My first Jenkin setup testing")
    return "status code: 200"

a = Jenkins()
print(a)

# second check

class JenkinsCtl:
    k = a
    print("Recursion call")
    print()
    print(a)
m = JenkinsCtl()
print(m)
