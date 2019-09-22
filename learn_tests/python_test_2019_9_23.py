a = 5
b = 3
st = "a > b" if a > b else "a < b"
print(st)
print("a > b") if a > b else print("a < b")

c = 6
d = 6
print("c > d") if c > d else (print("c < d") if c < d else print("c == d"))

#st = print("crazyit"); x = 20 if a > b else ""
st = x = 20; print("crazyit") if a > b else ""
print(st)
print(x)
st = 20, print("crazyit") if a > b else ""
print(st[0])
print(st[1])

a_tuple = ("tuple...",)
b_tuple = ("str...")
print(type(a_tuple))
print(type(b_tuple))

a = {1, "c", 1, (1, 2, 3),"c"}
for ele in a:
    print(ele, end=" ")
print("")

str1 = "人生苦短，我用Python" #utf-8汉字和标点符号占三个字节，英文字符占1个字节
print(len(str1.encode()))
print(len(str1.encode("gbk"))) #gbk汉字和标点符号占2个字节, 英文占1个字节

data = [5,8,4,1]
for i in range(len(data) - 1):
    for j in range(len(data) - i - 1):
        if(data[j] > data[j+1]):
            data[j], data[j+1] = data[j+1], data[j]
print("排序后：", data)

###列表，元祖，字典，集合推导式
dictdemo = {"1":1, "2":2, "3":3}
newdemo1 = {x for x , y in dictdemo.items() if y >= 2}
print(newdemo1)
newdemo2 = {x for x in dictdemo.values() if x >= 2}
print(newdemo2)
newdemo3 = {x for x in dictdemo.keys()}
print(newdemo3)

reverse_demo = {v:k for k,v in dictdemo.items()}
print(reverse_demo)

