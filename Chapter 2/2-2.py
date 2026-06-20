# 문자열 슬라이싱
a = "Life is too short"
print(a[3])
print(a[0])
# INDEX는 0부터 시작한다.
print(a[-1])
# -는 역으로

a = "Life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3]
print(b)

a = "Life is too short, You need Python"
print(a[0:4])
# 0 <= a < 4 까지 뽑아낸다(4번째는 포함하지 않음)
a[:]
# [:]은 처음부터 끝까지

a = "Life is too short, You need Python"
b = a[::2]
# [시작:끝:간격] 간격만큼 건너뛰면서 가져온다
print(b)

a = "20230331Rainy"
year = a[:4]
day = a[4:8]
weather = a[8:]
print(year)
print(day)
print(weather)


# 문자열 포매팅
a = "I eat %d apples." % 3
print(a)

a = "I eat %s apples." % "five"
print(a)
# s = 문자열, d = 정수, f = 실수 -> %s는 왠만해서 다 커버가 가능

number = 10
day = "three"
a = "I ate %d apples. so I was sick for %s days." % (number, day)
print(a)

name = '홍길동'
age = 30
a = f'나의 이름은 {name}입니다. 나이는 {age+1}입니다.'
print(a)
# f-string은 문자열 앞에 f를 붙이고, {}안에 변수를 넣으면 된다.

a = "hobby"
print(a.count('b'))
# b가 몇 개 있는지 세어준다.

