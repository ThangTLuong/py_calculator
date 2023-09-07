from operators import Operators

class Subtract(Operators):
  def __init__(self) -> None:
    pass
  
  def execute(first: float, second: float) -> float:
    return first - second