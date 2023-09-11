import sys

sys.path.append('../')
from dictionary_init import Dictionary_Init as di

arg: str = '*'
expected: int = 2

def check(args):
  return args == expected

def main(args=None):
  dic: di = di()
  
  print(check(dic.get(arg).get_priority()))

if __name__ == '__main__':
  main()