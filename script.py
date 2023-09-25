import json

def increment_key(n):
    with open("CS663_Project_Data.json", 'r') as f:
        data = json.load(f)

    new_data = {}
    for key, value in data.items():
        new_key = int(key) + n
        new_data[str(new_key)] = value

    with open('CS663_Project_Data.json', 'w') as file:
        json.dump(new_data, file, indent=4)

def beautify():
    with open("CS663_Project_Data.json", 'r') as f:
        data = json.load(f)

    with open('CS663_Project_Data.json', 'w') as file:
        json.dump(data, file, indent=4)





def merge_json(file1, file2):
    with open(file1, 'r') as f:
        data = json.load(f)

    file1_data = {}
    for key, value in data.items():
        file1_data[key] = value
    increment = len(data.items())
    
    print(increment)

    increment_key(increment)

    with open(file2, 'r') as f:
        data2 = json.load(f)

    file2_data = {}
    for key, value in data2.items():
        file2_data[key] = value
    
    # file2_data.update(file1_data)

    # with open('CS663_Project_Data.json', 'w') as file:
    #     json.dump(file2_data, file, indent=4)

#merge_json('gptCommands.json', 'CS663_Project_Data2.json')

def write_numbers(file):
    with open(file, 'r') as f:
        data = json.load(f)
        print(len(data))
    
    new_data = {}
    for i in range(len(data)):
        
        new_data[str(i)] = data[i]
    print(new_data)

    with open(file, 'w') as file:
        json.dump(new_data, file, indent=4) 



#merge_json('gptCommands.json', 'CS663_Project_Data.json')


def fix_key_number(file):
    with open(file, 'r') as f:
        data = json.load(f)
    
    new_data = {}
    count = 1
    for key, value in data.items():
        new_key = count
        new_data[str(new_key)] = value
        count += 1

    with open(file, 'w') as file:
        json.dump(new_data, file, indent=4)

#fix_key_number('CS663_Project_Data.json')

import re
def clean_paths(file):
    regex = re.compile(r"(/[^\s]+)")

    with open(file, 'r') as f:
        data = json.load(f)
    
    new_data = {}
    for key, value in data.items():
        val = value
        val["invocation"] = re.sub(regex, "[PATH]", value["invocation"])
        new_data[key] = val

    with open(file, 'w') as file:
        json.dump(new_data, file, indent=4)

clean_paths('CS663_Project_Data.json')
