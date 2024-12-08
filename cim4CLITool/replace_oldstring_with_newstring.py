import sys

def replace_string_in_file(file_path, old_string, new_string):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    new_lines = []
    for line in lines:
        new_lines.append(line.replace(old_string, new_string))
    
    with open(file_path, 'w') as file:
        file.writelines(new_lines)

# replace_string_in_file('AO_schema_Test.yaml', "ncno:", "nc-no:")

if __name__ == "__main__":
    yamlSchemaFilePath = sys.argv[1] if len(sys.argv) > 1 else None
    oldString = sys.argv[2] if len(sys.argv) > 2 else None
    newSrtring = sys.argv[3] if len(sys.argv) > 3 else None
    replace_string_in_file(yamlSchemaFilePath, oldString, newSrtring)