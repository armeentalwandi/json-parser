from enum import Enum

class TokenType(Enum):
  L_BRACE = 1
  R_BRACE = 2
  STRING = 3
  NUMBER = 4
  BOOLEAN = 5
  NULL = 6
  COMMA = 7
  COLON = 8

class Token:
  def __init__(self, type: TokenType, value: str):
    self.type = type
    self.value = value

