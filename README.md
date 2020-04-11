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
```python
1.add(a): 세트에 a의 값을 추가
2.'~~' in 세트 : 세트에 해당하는 문자열이 있는지 확인
3.remove('a') : 세트에 a문자열 삭제 // 없으면 오류 발생
4.discard('a') : 세트에 a문자열 폐기 // 없어도 오류 발생하지않음
5.pop(): 무작위로 임의 '추출', 함수의 반환 값으로 해당 항목의 값을 반환
6.clear(): 세트 항목 모두 지우기
```

6. 정렬되지 않은 **키**와 **값**의 쌍으로 구성된 데이터 모음인 **딕셔너리**
```python
1.len(a) : a딕셔너리의 항목 개수 확인
2.a['b']=20 : a딕셔너리에 b라는 키와, 20이라는 값을 가진 쌍을 추가
3.a.keys() , a.values() : a딕셔너리의 키와 값을 확인
4.'a' in b : b딕셔너리에 a라는 키가 있나 확인
5. del a['c'] : a딕셔너리에 c라는 키를 삭제
6. clear() : 딕셔너리 항목 모두 지우기
7.dict([][][]) : 튜플 데이터를 딕셔너리 타입으로 반환 / 튜플로 데이터를 빠르게 읽고, 보기 편하게 딕셔너리로 변환 
```

7. 데이터 정렬하기 -sorted() / 튜플, 리스트 : sorted(a) a튜플, 리스트를 올림차순으로 정렬, reverse = True를 입력하면 내림차순. 딕셔너리도 마찬 가지. **sort()는 기존 리스트 값을 바꿔 놓지만, sorted()는 신규 데이터를 만듦**
