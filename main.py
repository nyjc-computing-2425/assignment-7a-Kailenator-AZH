# Write a function to convert numbers to text numerals

def text_numeral(num: int) -> str:
  """
  Converts a specified number into text numerals

  Parameter
  ----------
  num: int
    The number to be converted

  Return
  -----------
  str
    The converted number in text numerals
  """
  NUM_WORD = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eigth', 9:'nine', 10:'ten', 11:'eleven', 12:'tweleve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'}
  outp = ''
  n = 1
  while num != 0:
    largest_NUM_WORD = sorted([i for i in NUM_WORD.keys()])[-n]
    if num >= largest_NUM_WORD:
      num -= largest_NUM_WORD
      outp += NUM_WORD[largest_NUM_WORD]+' '
    else:
      n += 1
  return outp.strip()
#print(text_numeral(1700))