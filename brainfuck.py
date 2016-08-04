import sys
import os

class BrainfuckInterpreter(object):

  def __init__(self):
    self.memory = [0] * 30000
    self.pointer = 0
    self.loop_pointer = 0

  def add_one(self):
    try:
      self.memory[self.pointer] += 1
    except Exception:
      raise Exception("pointer out of bounds: {}".format(self.pointer))

  def minus_one(self):
    try:
      self.memory[self.pointer] -= 1
      if self.memory[self.pointer] < 0:
        raise Exception("Negative memory at location: {}".format(self.pointer))
    except IndexError:
        raise Exception("pointer out of bounds: {}".format(self.pointer))

  def move_right(self):
    self.pointer += 1

  def move_left(self):
    self.pointer -= 1

  def set_loop_pointer(self):
    self.loop_pointer = self.pointer

  def is_loop_done(self):
    return self.memory[self.pointer] == 0

  def read(self, contents):
    skip = False
    i = 0
    print "Total chars: {}".format(len(contents))
    while i < len(contents):
      char = contents[i]
      # print "Index: {}, Char: {}, Point: {}, Memory: {}".format(i, char, self.pointer, self.memory[self.pointer])
      if skip and char != "]":
        i += 1
        continue
      if char == "+":
        self.add_one()
      elif char == "-":
        self.minus_one()
      elif char == ">":
        self.move_right()
      elif char == "<":
        self.move_left()
      elif char == ".":
        sys.stdout.write(unichr(self.memory[self.pointer]))
      elif char == ",":
        self.memory[self.pointer] = ord(sys.stdin.read(size=1))
      elif char == "[":
        if self.is_loop_done():
          skip = True
        else:
          self.loop_pointer = i
      elif char == "]":
        if not self.is_loop_done():
          i = self.loop_pointer
        else:
          skip = False
      i += 1

def get_file_contents(name):
  contents = ""
  with open(name, "r") as of:
    for char in of.read():
      contents += char
  return contents




if __name__ == "__main__":
  try:
    filename = sys.argv[1]
  except Exception:
    raise Exception("Please specify a file to interpret")
  finally:
    contents = get_file_contents(filename)
    bf = BrainfuckInterpreter()
    bf.read(contents)

