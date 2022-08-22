import re

print(re.findall("\d{4}", "12345678 654 654 1 2 3 4 1235"))


numStr = "123 1234 12345 123456 1234567 12345678"
print(re.findall("\d{5,7}", numStr))
