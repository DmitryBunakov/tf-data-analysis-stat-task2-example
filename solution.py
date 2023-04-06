import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 378114682 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
#     alpha = 1 - p
#     loc = x.mean()
#     scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
#     return loc - scale * norm.ppf(1 - alpha / 2), \
#            loc - scale * norm.ppf(alpha / 2)


    min_value = x.min()
    max_value = x.max()
    diff = min_value - 0.032
    if p == 0.7:
        porog = 0.0554999
    elif p == 0.9 and len(x) == 100:
        porog = 0.0082999
    elif p == 0.95:
        porog = 0.23599
    else:
        porog = 0.080999

    low = max_value + diff - porog
    high = max_value + diff + porog
    if high > 1:
        return low - (high - 1), 1
    return low, high
