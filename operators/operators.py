from abc import ABC, abstractmethod

class Operators(ABC):
  def __init__(self) -> None:
    pass
  
  @abstractmethod
  def execute(self, first: float, second: float) -> float:
    pass
  
  @abstractmethod
  def get_priority(self) -> int:
    pass