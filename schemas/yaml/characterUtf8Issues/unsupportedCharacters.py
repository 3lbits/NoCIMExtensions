import unicodedata

# File path
file_path = "schemas/yaml/core_equipment_utf8.linkml.yaml"  # Replace with the path to your YAML file

# # Function to find unsupported characters
# def find_unsupported_characters(file_path, encoding="cp1252"):
#     unsupported_chars = set()
#     with open(file_path, "r", encoding="utf-8") as file:
#         content = file.read()
#         for char in content:
#             try:
#                 char.encode(encoding)
#             except UnicodeEncodeError:
#                 # Add the character and its Unicode name for clarity
#                 unsupported_chars.add((char, unicodedata.name(char, "UNKNOWN")))
#     return unsupported_chars

# # Find characters not supported by CP1252
# unsupported_chars = find_unsupported_characters(file_path)

# # Print results
# if unsupported_chars:
#     print("Unsupported characters found:")
#     for char, name in unsupported_chars:
#         print(f"Character: '{char}' (Unicode name: {name})")
# else:
#     print("No unsupported characters found.")

with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()

unsupported_chars = set()

for char in content:
    if char in ['·', '²', '“', '”', '’', '—', '…', '•', '™', '€', '®', '©', '§', '¶', '°', '¡', '¢', '£', '¤', '¥', '¦', '¨', '©', 'ª', '«', '¬', '®', '¯', '°', '±', '²', '³', '´', 'µ', '¶', '·', '¸', '¹', 'º', '»', '¼', '½', '¾', '¿', 'À', 'Á', 'Â', 'Ã', 'Ä', 'Å', 'Æ', 'Ç', 'È', 'É', 'Ê', 'Ë', 'Ì', 'Í', 'Î', 'Ï', 'Ð', 'Ñ', 'Ò', 'Ó', 'Ô', 'Õ', 'Ö', '×', 'Ø', 'Ù', 'Ú', 'Û', 'Ü', 'Ý', 'Þ', 'ß', 'à', 'á', 'â', 'ã', 'ä', 'å', 'æ', 'ç', 'è', 'é', 'ê', 'ë', 'ì', 'í', 'î', 'ï', 'ð', 'ñ', 'ò', 'ó', 'ô', 'õ', 'ö', '÷', 'ø', 'ù', 'ú', 'û', 'ü', 'ý', 'þ', 'ÿ']:
        unsupported_chars.add((char, unicodedata.name(char, "UNKNOWN")))
    # break

print(unsupported_chars)

for char in unsupported_chars:
    new_content = content.replace(char[0], "")

# print(new_content)

# Write the new content to a YAML file
# new_file_path = "schemas/yaml/core_equipment_utf8_cleaned.linkml.yaml"  # Replace with the desired output file path

# with open(new_file_path, "w", encoding="utf-8") as new_file:
#     new_file.write(new_content)

# print(f"Cleaned content written to {new_file_path}")