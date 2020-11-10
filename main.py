import re
source = open('src.txt', 'r')
source_string = source.read()
result_list = re.findall(r'\b79\d{9}\b', source_string)
with open('res.txt', 'w') as result:
    print(*result_list, file=result, sep="\n")
source.close()
result.close()