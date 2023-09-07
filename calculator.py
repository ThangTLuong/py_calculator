import sys

def parse_args(args=None) -> str | None:
  if args == None:
    return None

  list_of_valid_args: str = ''
  for arg in args:
    for subarg in arg:
      if subarg.isnumeric() or subarg in ['+', '-', '*', '/', '^']:
        list_of_valid_args += subarg
  
  return list_of_valid_args

def main(args=None):
  if args == None:
    args = sys.argv
    
  problem = parse_args(args)
  print(problem)