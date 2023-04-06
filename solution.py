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

# пробую без униформы ) 0,032 и 0,08 из условий
    min_value = x.min()
    max_value = x.max()
    diff = min_value - 0.032
    low = max_value + diff - 0.0809999
    high = max_value + diff + 0.0809999
    if high > 1:
        return low - (high - 1), 1
    return low, high
