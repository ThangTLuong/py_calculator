from typing import Any

class stack():
  def __init__(self) -> None:
    self._stack_array: list[Any] = []
    self._count = 0
    
  def push(self, data) -> None:
    self._stack_array.insert(0, data)
    self._count += 1
    
  def pop(self) -> Any | None:
    if self.is_empty():
      return None
    
    data = self._stack_array.pop(0)
    self._count -= 1
    
    return data
  
  def peek(self) -> Any | None:
    if self.is_empty():
      return
    
    return self._stack_array[0]
    
  def is_empty(self) -> bool:
    return len(self._stack_array) == 0
  
  def size(self) -> int:
    return self._count