# Demoindexing.py
strA = "Python is very powerful"
print( strA[0])
print( strA[1])
print( strA[0:3])
print( strA[:3])
#디버깅하지 않고 바로 실행 : ctrl + F5
print( strA[-3:])
print( strA[-8:])

#리스트연습
colors = ["red","blue","green"]
print( colors )
print( len(colors))
print( colors[0])

#디버깅할때 중단점(Breaking point)
for item in colors:
    print(item)

colors.append("white")
print(colors)
colors.insert(1, "pink")
print(colors)
print(colors.index("red"))
colors += "red"
print(colors)
print( colors.pop() )
print(colors)
print( colors.pop() )
print(colors)
print( colors.pop(1) )
print(colors)
colors.extend(["black","red","white","pink"])
print(colors)
colors.remove("black")
print(colors)
colors.sort()
print(colors)
colors.reverse()
print(colors)

