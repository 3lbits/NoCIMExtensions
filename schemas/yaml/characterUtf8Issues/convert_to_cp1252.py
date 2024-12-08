# File paths
input_file = "schemas/yaml/core_equipment.linkml.yaml"  # Replace with the path to your YAML file in UTF-8
output_file = "schemas/yaml/core_equipment_cp1252.yaml"  # Path for the CP1252-encoded file

# Read the file in UTF-8 and write it in CP1252
with open(input_file, "r", encoding="utf-8") as infile:
    content = infile.read()

try:
    with open(output_file, "w", encoding="cp1252") as outfile:
        outfile.write(content)
    print(f"File successfully converted to CP1252 and saved as {output_file}.")
except UnicodeEncodeError as e:
    print(f"Encoding error: {e}. Some characters may not be supported in CP1252.")