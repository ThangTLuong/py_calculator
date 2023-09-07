from typing import Any
from .stack import stack


class stack_handler():
  def __init__(self) -> None:
    self._operator_stack: stack = stack()
    self._operand_stack: stack = stack()

  def operator_push(self, data) -> None:
    self._operator_stack.push(data)

  def operator_pop(self) -> Any | None:
    if self._operator_stack.is_empty():
      return

    return self._operator_stack.pop()

  def operator_peek(self) -> Any | None:
    if self._operator_stack.is_empty():
      return

    return self._operator_stack.peek()

  def operand_push(self, data) -> None:
    self._operand_stack.push(data)

  def operand_pop(self) -> Any | None:
    if self._operand_stack.is_empty():
      return

    return self._operand_stack.pop()

  def operand_peek(self) -> Any | None:
    if self._operand_stack.is_empty():
      return

    return self._operand_stack.peek()


def main(args=None):
  st = stack_handler()
  st.operator_push('+')
  st.operator_push('*')

  for _ in range(2):
    print(st.operator_pop())


if __name__ == '__main__':
  main()
