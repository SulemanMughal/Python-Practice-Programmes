# MATCH A PARENTHESIS IN YOUR TEXT
import re
print("="*70)
print("MATCH A PARENTHESIS IN YOUR TEXT")
print("="*70)
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
print("Pattern to search : ", end="")
print(phoneNumRegex)
search_string = "'My number is (123) 456-7890.'"
mo = phoneNumRegex.search(search_string)
print("Search String : " ,  search_string )
print("mo.group(1) : ", end="")
print(mo.group(1))
print("mo.group(2) : " , end="")
print(mo.group(2))