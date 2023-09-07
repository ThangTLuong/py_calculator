from abc import ABC, abstractmethod

class Operators(ABC):
  def __init__(self) -> None:
    pass
  
  @abstractmethod()
  def execute(first: float, second: float) -> float:
    pass