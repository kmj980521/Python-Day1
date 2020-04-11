color = { 'red', 'blue', 'purple','green','red'} #세트 . 중복된 값 x
print (color)

color2= set()
color2.add('red')
color2.add('purple')
color2.add('green')
color2.add('blue')
color2.add('red')
print (color2)
print ('red' in color2) #'red'가 있는지
print ( 'black' not in color2) #'black'이 없는지

color2.remove('red') #만약 값이 없으면 오류 
print (color2)
color2.discard('black') #값이 없어도 오류발생 X
print (color2)

color2.pop() #임의로 하나 '추출' 반환일 때 사용.remove와 비슷
print (color2)
color2.clear()
print (color2)
