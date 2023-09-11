import dependencies as dp
import dictionary_init as di
import sys

class calculator():
  def __init__(self) -> None:
    self._list_of_valid_args: list[str] = []
    self._sh = dp.stack_handler()
    self._operators: list[str] = ['+', '-', '*', '/', '^']
    
  def parse(self, args: list[str] = None) -> list[str] | None:
    if args == None:
      return None
    
    list_of_valid_args: list[str] = []
    
    for arg in args:
      try:
        if arg[arg.find('.')+1].isnumeric():
          list_of_valid_args.append(arg)
      except IndexError:
        continue
    
    return list_of_valid_args
  
  def parse_args(self, args: list[str] = None) -> list[str] | None:
    if args == None:
      return None

    list_of_valid_args: list[str] = []
    operand: str = ''
    args = self.parse(args)
    
    for arg in args:
      for value in arg:
        if not value in self._operators:
          operand += value
        else:
          list_of_valid_args.append(operand)
          list_of_valid_args.append(value)
          operand = ''
    list_of_valid_args.append(operand)
    
    self._list_of_valid_args = list_of_valid_args
    return list_of_valid_args
    
  def is_number(self, value) -> float | None:
    try:
      return float(value)
    except ValueError:
      return
    
  def start(self) -> None:
    # Separate operators and operands
    # Addition and Subtraction have the lowest priority
    # Multiplication and Division have the middle priority
    # Exponential has the highest priority
    
    # if the current operator has a priority equal to or greater than the previous, keep pushing
    # else pop and execute before pushing the current operator
    for arg in self._list_of_valid_args:
      if self.is_number(arg):
        self._sh.operand_push(arg)
      else:
        self._sh.operator_push(arg)
      

def main(args=None):
  if args == None:
    args = sys.argv

  calc = calculator()
  
  problem = calc.parse_args(args)
  print(problem)