a1=[10,20,30]
a2=[40,50,60]
a3=a1+a2
print(a3)
a1.extend(a2) #확장  데이터 저장 공간을 효율적으로 사용 가능
print(a1)
del a1[2] #인덱스가 2인 값 삭제
print (a1)

b1=[10,20,30]
b2=[40,50,60]
b3=[70,80,90]

b4=[b1,b2,b3]
print(b4)
print(b4[2][2]) #Print 90

c1=[]
c1=list() # 빈 리스트 생성.

ex=list()
for i in range(1,30) :
    if i%5==0:
        ex.append(i)
print (ex)
