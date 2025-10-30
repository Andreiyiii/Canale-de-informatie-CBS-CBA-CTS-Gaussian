import numpy as np
from typing import List, Union
def p2(lp: List[float]) -> Union[List[float], str]:
    rez=[]
    for i in lp:
        if i < 0 or i > 1:
            return "Date de intrare invalide!"
        elif i == 0:
            rez.append(np.log2(3))
        elif i == 1:
            rez.append(np.log2(3) + np.log2(1 / 2))
        else:
            rez.append(np.log2(3) + (1 - i) * np.log2(1 - i) + i * np.log2(i / 2))
        return rez