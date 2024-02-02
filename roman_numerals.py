roman_numeral = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}
def to_roman(num):
    # write your code here!
    pass


print(to_roman(5))

"""
(P)arameters: (One) para that take in a Number
(R)eturn: (One) a concatated string of the roman numberas
(E)xample: 5 -> V , 6 -> VI, 58 -> LVIII
(P)seudocode:
 - Data type will be a number (input)
 - Data type will be a string (output)
 - Create a data structure that hold a key and value 
 - compare the input to values 
 - return the keys for the values as an output *maybe solve with an if..statment*
 -
 -
# 1. Write a method TO_ROMAN, TO_ROMAN takes in INPUT_NUMBER (an arabic number)

# 2. Create a OUTPUT string, set to ''

# 3. Create a ROMAN_NUMERAL_TO_ARABIC_MAP that includes roman numerals as keys, arabic numbers as values

# 4. Iterate over ROMAN_NUMERAL_TO_ARABIC_MAP, keep track of ROMAN_NUMERAL and ARABIC_NUMBER

# 5. Set EVENLY_DIVISIBLE_TIMES = INPUT_NUMBER / ARABIC_NUMBER:

# 6. If EVENLY_DIVISIBLE_TIMES >= 1
  # 6a. Append ROMAN_NUMERAL to OUTPUT EVENLY_DIVISIBLE_TIMES
  # 6b. Subtract ARABIC_NUMBER from INPUT_NUMBER EVENLY_DIVISIBLE_TIMES
  
# 7. Return OUTPUT
    """