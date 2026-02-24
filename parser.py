from token import TokenType, Token
import sys

class Parser:

  def __init__ (self, tokens):
    self.tokens = tokens
    self.braces_stack = []
    self.previous_token = None
  
  def parse(self):
    for idx, token in enumerate(self.tokens):

      if idx == 0 and token.type != TokenType.L_BRACE:
        print("Invalid JSON: Must start with an opening brace")
        sys.exit(1)
      if idx == len(self.tokens) - 1 and token.type != TokenType.R_BRACE:
        print("Invalid JSON: Must end with a closing brace")
        sys.exit(1)

      if token.type == TokenType.L_BRACE:
        self.braces_stack.append(token)
      elif token.type == TokenType.R_BRACE:
        if len(self.braces_stack) == 0:
          print("Invalid JSON: Unmatched closing brace")
          sys.exit(1)
        self.braces_stack.pop()
    
    if len(self.braces_stack) > 0:
      print("Invalid JSON: Unmatched opening brace(s)")
      sys.exit(1)
    print("JSON is valid")
    sys.exit(0)


