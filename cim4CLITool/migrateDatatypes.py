"""Migrate CIM datatype classes from classes: to types: section in LinkML YAML schemas."""
import yaml
import os
import glob

SCHEMA_DIR = os.path.join('schemas', 'yaml')
# Attributes that identify a CIM datatype class (only these, no is_a, no other attributes)
DATATYPE_ATTRS = {'value', 'unit', 'multiplier'}


def detect_datatype_classes(yaml_data):
    """Auto-detect CIM datatype classes: classes with only value/unit/multiplier attributes and no is_a."""
    if 'classes' not in yaml_data or yaml_data['classes'] is None:
        return []

    datatypes = []
    for name, cls in yaml_data['classes'].items():
        if cls is None:
            continue
        if 'is_a' in cls:
            continue
        attrs = cls.get('attributes')
        if attrs is None:
            continue
        if set(attrs.keys()).issubset(DATATYPE_ATTRS) and len(attrs) > 0:
            datatypes.append(name)
    return datatypes


def migrate_file(filepath, dry_run=False):
    """Migrate CIM datatype classes from classes: to types: in a single schema file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    data = yaml.safe_load(content)
    datatype_names = detect_datatype_classes(data)

    if not datatype_names:
        return []

    # Check if types: section already has these
    existing_types = set()
    if 'types' in data and data['types']:
        existing_types = set(data['types'].keys())

    to_migrate = [n for n in datatype_names if n not in existing_types]
    if not to_migrate:
        return []

    if dry_run:
        return to_migrate

    # Build type entries from the class definitions
    types_entries = {}
    for name in to_migrate:
        cls = data['classes'][name]
        description = cls.get('description', '')
        class_uri = cls.get('class_uri', f'cim:{name}')
        types_entries[name] = {
            'uri': 'xsd:float',
            'base': 'float',
            'description': description,
            'cim_uri': class_uri,
        }

    # Text-based manipulation to preserve formatting
    lines = content.split('\n')

    # Remove datatype class blocks from classes: section
    lines_to_remove = set()
    i = 0
    while i < len(lines):
        for name in to_migrate:
            if lines[i] == f'  {name}:':
                start = i
                i += 1
                while i < len(lines):
                    if lines[i] and not lines[i].startswith('   ') and lines[i].strip() != '':
                        break
                    if lines[i] == '' and i + 1 < len(lines) and not lines[i + 1].startswith('   '):
                        lines_to_remove.add(i)
                        i += 1
                        break
                    lines_to_remove.add(i)
                    i += 1
                for j in range(start, min(i, len(lines))):
                    lines_to_remove.add(j)
                break
        else:
            i += 1

    new_lines = [lines[i] for i in range(len(lines)) if i not in lines_to_remove]

    # Build types: section text
    types_text_lines = ['', 'types:']
    for name in sorted(types_entries.keys()):
        entry = types_entries[name]
        types_text_lines.append('')
        types_text_lines.append(f'  {name}:')
        types_text_lines.append(f'    uri: {entry["uri"]}')
        types_text_lines.append(f'    base: {entry["base"]}')
        types_text_lines.append(f'    description: "{entry["description"]}"')
        types_text_lines.append(f'    annotations:')
        types_text_lines.append(f'      cim_data_type: true')
        types_text_lines.append(f'      uri: {entry["cim_uri"]}')

    # Insert types: section before enums:
    result_lines = []
    inserted = False
    for line in new_lines:
        if line.strip() == 'enums:' and not inserted:
            result_lines.extend(types_text_lines)
            result_lines.append('')
            inserted = True
        result_lines.append(line)

    # If no enums: section, append at end
    if not inserted:
        result_lines.extend(types_text_lines)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(result_lines))

    return to_migrate


def get_all_schemas():
    """Return all .linkml.yaml files in the schemas directory."""
    pattern = os.path.join(SCHEMA_DIR, '*.linkml.yaml')
    return sorted(glob.glob(pattern))


def run(schema=None, dry_run=False):
    """Main entry point. Migrate one schema or all schemas."""
    if schema:
        filepath = os.path.join(SCHEMA_DIR, f'{schema}.linkml.yaml')
        if not os.path.exists(filepath):
            raise FileNotFoundError(f'Schema not found: {filepath}')
        files = [filepath]
    else:
        files = get_all_schemas()

    total = 0
    for filepath in files:
        migrated = migrate_file(filepath, dry_run=dry_run)
        if migrated:
            label = 'Would migrate' if dry_run else 'Migrated'
            print(f'  {label} {len(migrated)} datatypes in {os.path.basename(filepath)}: {", ".join(sorted(migrated))}')
            total += len(migrated)
        else:
            print(f'  No datatypes to migrate in {os.path.basename(filepath)}')

    print(f'\nTotal: {total} datatype(s) {"would be" if dry_run else ""} migrated')
    return total
