from datetime import datetime
from typing import Tuple

from pydantic import BaseModel, PositiveInt, validate_call


class NumeroPositivo(BaseModel):
    numero: PositiveInt

@validate_call()
def calculadora(x: PositiveInt, y: PositiveInt) -> PositiveInt:
    return x + y



print(calculadora(1,2))
print(calculadora(4,5))
# print(calculadora(-1,-6))