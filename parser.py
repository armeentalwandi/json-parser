from token import TokenType, Token
import sys

class Parser:

  def __init__ (self, tokens):
    self.tokens = tokens
    self.braces_stack = []
    self.currpos = 0
    self.length = len(tokens)
  
  def peek_token(self) -> Token:
    if self.currpos + 1 < self.length:
      return self.tokens[self.currpos + 1]
    return None
  
  def parse_object(self) -> bool:
    self.currpos += 1
    while self.currpos < self.length:
      token = self.tokens[self.currpos]
      if token.type == TokenType.R_BRACE:
        return True
      if token.type != TokenType.STRING:
        return False
      

  def parse(self) -> None:
    while self.currpos < self.length:
      token = self.tokens[self.currpos]

      if token.type == TokenType.L_BRACE:
        self.braces_stack.append(token)
        isValidObject = self.parse_object()
        if not isValidObject:
          print("Invalid JSON: Invalid object structure")
          sys.exit(1)

      elif token.type == TokenType.R_BRACE:
        if len(self.braces_stack) == 0:
          print("Invalid JSON: Unmatched closing brace")
          sys.exit(1)
        self.braces_stack.pop()
      self.currpos += 1

    if len(self.braces_stack) > 0:
      print("Invalid JSON: Unmatched opening brace")
      sys.exit(1)
    


