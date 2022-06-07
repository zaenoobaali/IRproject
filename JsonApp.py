import json

def tojson(filename, i):
        dict1 = {}
        cont =[]
        # fields in the sample file
        fields = ['.I', '.T', '.A', '.W']
        with open(filename) as input_file:
            # content = ""
            dict1[fields[0]] = i
            for line in input_file:
                if line.startswith('.T'):
                    content = ""
                elif line.startswith('.A'):
                    if dict1.get(fields[1]):
                        cont.append(content)
                        dict1[fields[2]]= cont
                        #print(content)
                        content = ''
                    else:
                        dict1[fields[1]] = content
                        content = ""
                elif line.startswith('.W'):
                    cont.append(content)
                    dict1[fields[2]] = cont
                    content = ""
                else:
                    content += line
            dict1[fields[3]] = content

        # creating json file
        out_file = open("JsonFiles/jsonDoc"+str(i)+".json", "w")
        json.dump(dict1, out_file, indent=4)
        out_file.close()

def from_text(n):
    print()
    for i in range(1, n):
        filename = "Documents/Document"+str(i)+".txt"
        tojson(filename, i)
