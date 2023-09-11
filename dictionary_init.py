from dependencies import Dictionary as dt
import operators as op

class Dictionary_Init():
  def __init__(self) -> None:
    self._dt: dt = dt()
    
    self._dt.put('+', op.Add())
    self._dt.put('-', op.Subtract())
    self._dt.put('*', op.Multiply())
    self._dt.put('/', op.Divide())
    self._dt.put('^', op.Exponent())
    
  def get(self, key) -> op:
    return self._dt.get(key)