import re

def parse_where(where):
  res = ''
  for key in where:
    if type(where[key]) is list:
      res += f' {key} '.join(where[key])

  return res

def format_alias(string):
  return re.sub(r"\s|-", "_", string)