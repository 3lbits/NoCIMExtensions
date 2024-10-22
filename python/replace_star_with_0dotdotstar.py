import os

def replace_in_file(file_path, search_text, replace_text):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    content = content.replace(search_text, replace_text)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def traverse_and_replace(directory, search_text, replace_text):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                replace_in_file(file_path, search_text, replace_text)

if __name__ == "__main__":
    docs_directory = 'docs/'
    search_text = ' | * '
    replace_text = ' | 0..* '
    traverse_and_replace(docs_directory, search_text, replace_text)
