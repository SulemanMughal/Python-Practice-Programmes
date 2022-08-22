# MATCH ONE OF SEVERAL PATTERNS AS PART OF YOUR REGEX
import re
print("="*70)
print("# MATCH ONE OF SEVERAL PATTERNS AS PART OF YOUR REGEX")
print("="*70)
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
print("Pattern to search : ", end="")
print(batRegex)
search_string = "Batmobile lost a wheel"
mo = batRegex.search(search_string)
print("Search String : " ,  search_string )
print("mo.group() : ", end="")
print(mo.group())
print("mo.group(1) : ", end="")
print(mo.group(1))