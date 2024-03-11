import math
import random
import numpy as np

lotto = sorted(np.random.choice(np.arange(1,46), size=6, replace= False))

bonus = np.random.choice([i for i in range(1,46) if i not in lotto])

print(f'로또 번호 = {lotto}')
print(f'보너스 번호 = {bonus}')v
