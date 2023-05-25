handler = open("pan_tadeusz.txt")
print(handler.readline())
handler.close()

print("--------------")
with open("pan_tadeusz.txt", "a") as fo:
    #print(fo.read())
    fo.write("ABC TEST2")
    print(fo)


