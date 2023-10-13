import re

email="gbugyb234@cdscs.cdsc"
regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

if  not (re.fullmatch(regex,email)):
    print("valid")
else:
    print("not ")