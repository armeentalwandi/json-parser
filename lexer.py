from token import Token, TokenType

class Lexer:
  def __init__(self, text: str):
    self.text = text
  
  def tokenize(self):
    tokens = []
    for char in self.text:
      if char == "":
        continue
      if char == "{":
        tokens.append( Token( TokenType.L_BRACE, char))
      elif char == "}":
        tokens.append( Token( TokenType.R_BRACE, char))
    return tokens