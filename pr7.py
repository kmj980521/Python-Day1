a= ' '

while a!='예' :
    a=input('땅 주인이 있나요? 예/아니오')
    if a=='예':
        print('통행료를 지불하세요')
    else:
        print('그냥 통과!')
        print('주사위를 던져서 다음 땅으로 이동하세요')

print ('게임을 종료합니다')
