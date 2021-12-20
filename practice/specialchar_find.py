import re

hi="i this is 123 pradip here @@i$ have interview % & tomarrow ! i try my best do we000ll"
input="i very good guy i need job"

'''finder=re.findall("[@|^&+\-%*/=!>]",hi)
print(finder)'''


finder2=re.compile('[!@#$%^&()<>?/\|:;]')

if (finder2.search(hi)==None):
    print("NO special chara")
else:
    print("string contains special char")