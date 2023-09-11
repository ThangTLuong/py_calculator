from operators import Operators

class Exponent(Operators):
  def __init__(self) -> None:
    self._priority: int = 3
  
  def execute(self, first: float, second: float) -> float:
    return first ** second
  
  def get_priority(self) -> int:
    return self._priority
    