from operators import Operators

class Multiply(Operators):
  def __init__(self) -> None:
    pass
  
  def execute(first: float, second: float) -> float:
    return first * second