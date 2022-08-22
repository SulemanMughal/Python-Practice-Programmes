# MATCH PATTER LIKE XXX-XXX-XXXX
import re
print("="*70)
print("MATCH PATTER LIKE XXX-XXX-XXXX")
print("="*70)
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print("Pattern to search : ", end="")
print(phoneNumRegex)
search_string = "'My number is 123-456-7890.'"
mo = phoneNumRegex.search(search_string)
print("Search String : " ,  search_string )
print('Phone number found: ' + mo.group())