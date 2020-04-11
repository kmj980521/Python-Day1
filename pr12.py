scores = [10,20,30,40,50] #리스트
print (scores[2])
print (scores[-4])
print(scores[-len(scores)])

scores[2]=300
print(scores[2])
scores.append(3040) #뒤에 요소 추가 
print(scores)
scores.append(40)
print(scores)
scores.remove(40) #40이라는 값 제거. 중복되는 값이 존재하면 앞 부분만 제거.

scores.insert(1,300) #index 1에 300삽입.
scores.pop(1) #index 1인 값 삭제
print(scores)

scores.sort() #오름차순
print(scores)
scores.sort(reverse=True) #내림차순
print(scores)
scores.clear()#리스트 항목 모두 지우기
print(scores)
