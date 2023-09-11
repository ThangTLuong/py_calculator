arg: list[str] = ['3.1+3', '*38', '/5.1/', '3']
expected = ['3.1', '+', '3', '*', '38', '/', '5.1', '/', '3']

def check(list_of_args):
  return list_of_args == expected

def main(args=None):
  operators: list[str] = ['+', '-', '*', '/', '^']
  list_of_args: list[str] = []
  operand: str = ''
  
  for index in arg:
    for value in index:
      if not value in operators:
        operand += value
      else:
        list_of_args.append(operand)
        list_of_args.append(value)
        operand = ''
  list_of_args.append(operand)
  
  print(check(list_of_args))

if __name__ == '__main__':
  main()