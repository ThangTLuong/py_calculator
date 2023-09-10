arg: list[str] = ['.//main', '1.1', '.5', '2.']
expected: list[str] = ['1.1', '.5']

def check(list_of_args):
  return list_of_args == expected

def main(args=None):
  list_of_args: list[str] = []
  
  for index in arg:
    try:
      if index[index.find('.')+1].isnumeric():
        list_of_args.append(index)
    except:
      continue
      
  print(check(list_of_args))

if __name__ == '__main__':
  main()