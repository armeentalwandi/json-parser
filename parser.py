from token import TokenType, Token
import sys

class Parser:

  def __init__ (self, tokens):
    self.tokens = tokens
    self.currpos = 0
    self.length = len(tokens)

  def expect_token(self, expected_type):
    if self.currpos >= self.length or self.tokens[self.currpos].type != expected_type:
        print(f"Invalid JSON: Expected {expected_type}")
        sys.exit(1)
    self.currpos += 1
  
  def peek_token(self, expected_type) -> bool:
    if self.currpos < self.length:
      return self.tokens[self.currpos].type == expected_type
    return False
  
  def parse_array(self) -> bool:
    self.expect_token(TokenType.L_BRACKET)

    if self.peek_token(TokenType.R_BRACKET):
      self.expect_token(TokenType.R_BRACKET)
    else:
      self.parse_value()
      while True:
        if self.peek_token(TokenType.COMMA):
          self.expect_token(TokenType.COMMA)
          self.parse_value()
        else:
          self.expect_token(TokenType.R_BRACKET)
          break
      

  def parse_value(self) -> bool:
    if self.currpos < self.length:
      token = self.tokens[self.currpos]
      if token.type in [TokenType.STRING, TokenType.NUMBER, TokenType.BOOLEAN, TokenType.NULL]:
        self.currpos += 1
        return
      elif token.type == TokenType.L_BRACE:
        return self.parse_object()
      elif token.type == TokenType.L_BRACKET:
        return self.parse_array()
    print("Invalid JSON: Expected value")
    sys.exit(1)

  
  def parse_key_value_pair(self):
    self.expect_token(TokenType.STRING)
    self.expect_token(TokenType.COLON)
    self.parse_value()


  def parse_object(self):
    self.expect_token(TokenType.L_BRACE)

    if self.peek_token(TokenType.R_BRACE):
      self.expect_token(TokenType.R_BRACE)
      return
    else:
      while True:
        self.parse_key_value_pair()
        if self.peek_token(TokenType.COMMA):
          self.expect_token(TokenType.COMMA)
        elif self.peek_token(TokenType.R_BRACE):
          self.expect_token(TokenType.R_BRACE)
          break
        else:
          print("Invalid JSON: Expected ',' or '}'")
          sys.exit(1)

  def parse(self) -> bool:
    token = self.tokens[self.currpos]
    if self.currpos < self.length and token.type == TokenType.L_BRACE:
      self.parse_object()
    else:
      print("Invalid JSON: Expected '{' at the beginning")
      sys.exit(1)
    print("Valid JSON")
    sys.exit(0)


