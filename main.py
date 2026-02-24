import sys
from lexer import Lexer
from parser import Parser

def main():
  if len(sys.argv) != 2:
    print("Usage: python main.py <json_file>")
    sys.exit(1)

  json_file = sys.argv[1]

  try:
    with open(json_file, 'r') as f:
      text = f.read()
  except FileNotFoundError:
    print(f"File not found: {json_file}")
    sys.exit(1)

  if len(text) == 0:
    print("Invalid JSON: Empty file")
    sys.exit(1)
  lexer = Lexer(text)
  tokens = lexer.tokenize()

  parser = Parser(tokens)
  parser.parse()



if __name__ == "__main__":
  main()


