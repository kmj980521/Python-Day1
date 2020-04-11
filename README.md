# Python-Day1
파이썬배우기 1일차

1.Python은 서로 다른 데이터를 바로 연산 처리할 수 없다. 

2.input을 받은 숫자는 문자열형식이므로 int(변수)를 해줘 **형변환**을 한다.

3.값을 변경할 수 없는 **튜플** . 여러개의 데이터가 하나의 튜플로 포장되어 저장되는 **튜플 패킹**, 항목별로 각각 풀어서 변수에 저장하는 개념 **튜플 언패킹** 
```python
color='red','yellow','green' #패킹
a1,a2,a3=color #언패킹. 순서대로 변수에 대입. 튜플 항목 수와 변수 개수는 동일해야함 
```
4.값을 변경할 수 있는 **리스트** []를 사용
```python
1.append(a) : 리스트에 a의 값을 맨 뒤에 추가
2.remove(a) : a의 값을 가지는 요소 삭제. 단 중복될 시 리스트 앞쪽에 있는 수 삭제
3.insert(a,b): a인덱스에 b라는 요소 삽입
4.pop(a): a인덱스에 요소 삭제
5.sort() : 오름차순으로 정리 / reverse=True를 넣어주면 내림차순
6.clear() : 리스트 항목 모두 지우기
```

5. 중복된 값을 삭제하는 **세트** {} 
