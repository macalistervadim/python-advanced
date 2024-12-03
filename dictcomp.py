"""
listcmop/dictcomp/setcomp
"""

dial_codes = [
    (800, "Bangladesh"),
    (55, "Brazil"),
    (90, "China"),
    (100, "Russia"),
]

dictcomp = {country: code for code, country in dial_codes}
print(dictcomp)
dictcomp2 = {code: country for code, country in dial_codes}
print(dictcomp2)
