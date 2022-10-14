def arithmetic_arranger(problems, answer=None):
  Operator = False
  Numbers = False
  Size = False
  
  if len(problems) > 5:
    return "Error: Too many problems."

  for operations in problems:
    if operations.split()[1] == "+" or operations.split()[1] == "-":
      pass
    else:
      Operator = True
  
    for digits in operations.split()[0::2]:
      if not digits.isnumeric():
        Numbers = True
      if len(digits) > 4:
        Size = True
  
  if Operator is True:
    return "Error: Operator must be '+' or '-'."
  if Numbers is True:
    return "Error: Numbers must only contain digits."
  if Size is True:
    return "Error: Numbers cannot be more than four digits."

  line_1 = ''
  line_2 = ''
  line_3 = ''
  line_4 = ''
  count = 0
  
  for operations in problems:
    if count == 0:
      numbers_len = [len(digits) for digits in operations.split()]
      max_len = max(numbers_len) + 2
      line_1 += operations.split()[0].rjust(max_len, " ")
      line_2 += operations.split()[1] + operations.split()[2].rjust(max_len-1, " ")
      line_3 += "-" * max_len
  
      if answer:
        if operations.split()[1] == "+":
          result = int(operations.split()[0]) + int(operations.split()[2])
          line_4 += str(result).rjust(max_len, " ")
        else:
          result = int(operations.split()[0]) - int(operations.split()[2])
          line_4 += str(result).rjust(max_len, " ")
      count = 1
    else:
      numbers_len = [len(digits) for digits in operations.split()]
      max_len = max(numbers_len) + 2
      line_1 += " " * 4 + operations.split()[0].rjust(max_len, " ")
      line_2 += " " * 4 + operations.split()[1] + operations.split()[2].rjust(max_len-1, " ")
      line_3 += " " * 4 + "-" * max_len
  
      if answer:
        if operations.split()[1] == "+":
          result = int(operations.split()[0]) + int(operations.split()[2])
          line_4 += " " * 4 + str(result).rjust(max_len, " ")
        else:
          result = int(operations.split()[0]) - int(operations.split()[2])
          line_4 += " " * 4 + str(result).rjust(max_len, " ")
    
  if answer:
    return line_1 + "\n" + line_2 + "\n" + line_3 + "\n" + line_4
  else:
    return line_1 + "\n" + line_2 + "\n" + line_3

    
  arranged_problems = 0

  return arranged_problems