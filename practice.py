# 퀴즈 

from random import *

my_list = range(1,21) # range 형태임
print(type(my_list))

my_list = list(my_list) # range 를 list 로 바꿔줘야지 list 관련 함수 사용 가능
print(type(my_list))
print(my_list)

shuffle(my_list)
print(my_list)

lucky = sample(my_list, 4)
print(lucky)

print("--- 당첨자 발표 ---")
print("치킨 당첨자 : {0}" .format(lucky[0]))
print("커피 당첨자 : {0}" .format(lucky[1:]))
print("-- 축하합니다 --")




