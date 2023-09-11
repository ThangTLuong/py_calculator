from typing import Any

class Dictionary():
  def __init__(self) -> None:
    self._dict: dict = {}
    
  def put(self, key, value) -> None:
    self._dict[key] = value
    
  def get(self, key) -> Any:
    return self._dict[key]