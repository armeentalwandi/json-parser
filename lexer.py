from token import Token, TokenType
import sys

class Lexer:
  def __init__(self, text: str):
    self.text = text
    self.position = 0
    self.length = len(text)
  
  def is_whitespace(self, char):
    return char in [' ', '\t', '\n', '\r']
  
  def tokenize(self):
    tokens = []
    while self.position < self.length:

      char = self.text[self.position]

      if self.is_whitespace(char):
        self.position += 1
        continue

      if char == "{":
        tokens.append( Token( TokenType.L_BRACE, char))
        
      elif char == "}":
        tokens.append( Token( TokenType.R_BRACE, char))

      elif char == ",":
        tokens.append( Token( TokenType.COMMA, char))

      elif char == ":":
        tokens.append( Token( TokenType.COLON, char))

      elif char == '"':
        start = self.position + 1
        self.position += 1

        while self.position < self.length and self.text[self.position] != '"':
          self.position += 1
        if self.position >= self.length:
          print("Invalid JSON: Unterminated string")
          sys.exit(1)

        value = self.text[start:self.position]
        tokens.append( Token( TokenType.STRING, value))

      elif char == '[':
        tokens.append( Token(TokenType.L_BRACKET, char))

      elif char == ']':
        tokens.append( Token(TokenType.R_BRACKET, char))

      elif char.isdigit() or char == '-':
        start = self.position
        if char == '-':
          self.position += 1
          if self.position >= self.length or not self.text[self.position].isdigit():
            print("Invalid JSON: Invalid number format")
            sys.exit(1)

        while self.position < self.length and (self.text[self.position].isdigit()):
          self.position += 1
        # decimals --> . followed by digits. don't need a number before. but if there is a dot, it must be followed by digits
        if self.position < self.length and self.text[self.position] == '.':
          self.position += 1
          if self.position >= self.length or not self.text[self.position].isdigit():
            print("Invalid JSON: Invalid number format")
            sys.exit(1)
          while self.position < self.length and self.text[self.position].isdigit():
            self.position += 1
        # exponents --> e or E followed by optional + or - and digits
        if self.position < self.length and self.text[self.position] in ['e', 'E']:
          self.position += 1
          if self.position < self.length and self.text[self.position] in ['+', '-']:
            self.position += 1
          if self.position >= self.length or not self.text[self.position].isdigit():
            print("Invalid JSON: Invalid number format")
            sys.exit(1)
          while self.position < self.length and self.text[self.position].isdigit():
            self.position += 1
        value = self.text[start:self.position]
        tokens.append( Token(TokenType.NUMBER, value))
        continue

      elif self.text.startswith("true", self.position):
        tokens.append( Token(TokenType.BOOLEAN, "true"))
        self.position += 4
        continue

      elif self.text.startswith("false", self.position):
        tokens.append( Token(TokenType.BOOLEAN, "false"))
        self.position += 5
        continue

      elif self.text.startswith("null", self.position):
        tokens.append( Token(TokenType.NULL, "null"))
        self.position += 4
        continue

      else:
        print(f"Invalid JSON: Unexpected character '{char}' at position {self.position}")
        sys.exit(1)
  
      self.position += 1
    return tokens