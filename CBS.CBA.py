import math
import numpy as np
from typing import Union

def p1(a: str, p: float) -> Union[float, str]:
    capacitate=0
    if a=="CBS":
        capacitate=1+ p*np.log2(p)+(1-p)*np.log2(1-p) if (p!=1 and p!=0) else 1
    elif a=="CBA":
        capacitate=1-p
    else:
        return "Date de intrare invalide!"
    return capacitate
