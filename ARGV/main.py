#sys 라는 python package, module를 import
import sys

first_name = sys.argv[1]
last_name = sys.argv[2]
gender = sys.argv[3]

print("성은" + first_name + "입니다")
print("이름은" + last_name + "입니다")
print("성별은" + gender + "입니다")

def plus_one(a):

    result = a + 1

    return result
 plus_one(1)
 

