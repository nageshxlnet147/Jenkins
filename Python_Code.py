def Jenkins():
    print("My first Jenkin setup testing")
    return 200

a = Jenkins()
print(a)

# second check

class JenkinsCtl:
    k = a
    print("Recursion call")
m = JenkinsCtl()
print(m)
