#1~45까지 숫자 중 중복되지 않은 6개의 숫자 출력해야함

import random

def lotto_number():
    l = range(1,46)

    lotto = sorted(random.sample(l,6))

    return lotto