# MATCH ONE OF MANY EXPRESSIONS
import re
print("="*70)
print("MATCH ONE OF MANY EXPRESSIONS")
print("="*70)
heroRegex = re.compile (r'Harry|Ron')
print("Pattern to search : ", end="")
print(heroRegex)
search_string = 'Harry and Ron.'
mo1 = heroRegex.search(search_string)
print("Search String : " ,  search_string )
print("mo1.group() : ", end="")
print(mo1.group())
search_string = 'Ron and Harry.'
mo2 = heroRegex.search(search_string)
print("Search String : " ,  search_string )
print("mo2.group() : ", end="")
print(mo2.group())