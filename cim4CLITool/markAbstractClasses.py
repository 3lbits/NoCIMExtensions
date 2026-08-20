"""Mark CIM classes as abstract in LinkML YAML schemas."""
import yaml
import os
import glob

SCHEMA_DIR = os.path.join('schemas', 'yaml')

# Classes that are definitively abstract in the CIM UML standard (IEC 61970-301)
KNOWN_ABSTRACT = {
    'IdentifiedObject',
    'PowerSystemResource',
    'Equipment',
    'ConductingEquipment',
    'Conductor',
    'Connector',
    'ACDCTerminal',
    'DCBaseTerminal',
    'ACDCConverter',
    'EnergyConnection',
    'RegulatingCondEq',
    'RotatingMachine',
    'EquivalentEquipment',
    'OperationalLimit',
    'TransformerEnd',
    'TapChanger',
    'PhaseTapChanger',
    'PhaseTapChangerNonLinear',
    'ConnectivityNodeContainer',
    'EquipmentContainer',
    'DCEquipmentContainer',
    'DCConductingEquipment',
    'PowerElectronicsUnit',
    'AuxiliaryEquipment',
    'Sensor',
    'EarthFaultCompensator',
    'TapChangerTablePoint',
    'BasicIntervalSchedule',
    'RegularIntervalSchedule',
    'SeasonDayTypeSchedule',
    'ProtectedSwitch',
    'IOPoint',
    'Control',
    'AnalogControl',
    'MeasurementValue',
    'Measurement',
    'Limit',
    'LimitSet',
    'Quality61850',
    'ShuntCompensator',
    'EnergyConsumer',
    'Curve',
    'LoadGroup',
    'EnergyArea',
}


def mark_abstract_in_file(filepath, dry_run=False):
    """Add abstract: true to known-abstract classes in a single schema file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    data = yaml.safe_load(content)
    if 'classes' not in data or data['classes'] is None:
        return []

    to_mark = []
    for name, cls in data['classes'].items():
        if cls is None:
            continue
        if name in KNOWN_ABSTRACT and not cls.get('abstract', False):
            to_mark.append(name)

    if not to_mark or dry_run:
        return to_mark

    # Line-based insertion: process file line by line
    lines = content.split('\n')
    result_lines = []
    i = 0
    while i < len(lines):
        matched_name = None
        for name in to_mark:
            if lines[i] == f'  {name}:':
                matched_name = name
                break

        if matched_name is None:
            result_lines.append(lines[i])
            i += 1
            continue

        # Found a class to mark - scan ahead for best insertion point
        result_lines.append(lines[i])
        i += 1
        insert_point = len(result_lines)  # fallback: right after class name

        while i < len(lines):
            line = lines[i]
            stripped = line.strip()
            # Stop at empty line or next top-level entry
            if stripped == '' or (not line.startswith('    ') and line.strip() != ''):
                break
            result_lines.append(line)
            i += 1
            if stripped.startswith('class_uri:'):
                insert_point = len(result_lines)
                break
            if stripped.startswith('is_a:'):
                insert_point = len(result_lines)

        # Insert abstract: true at the determined point
        result_lines.insert(insert_point, '    abstract: true')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(result_lines))

    return to_mark


def find_uncertain_parents(filepath):
    """Find classes that are is_a targets but not in KNOWN_ABSTRACT and not already abstract."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    data = yaml.safe_load(content)
    if 'classes' not in data or data['classes'] is None:
        return []

    # Find all is_a targets
    parents = set()
    for name, cls in data['classes'].items():
        if cls and 'is_a' in cls:
            parents.add(cls['is_a'])

    uncertain = []
    for parent in parents:
        if parent in data.get('classes', {}):
            cls = data['classes'][parent]
            if cls and not cls.get('abstract', False) and parent not in KNOWN_ABSTRACT:
                uncertain.append(parent)

    return sorted(uncertain)


def get_all_schemas():
    pattern = os.path.join(SCHEMA_DIR, '*.linkml.yaml')
    return sorted(glob.glob(pattern))


def run(schema=None, dry_run=False, show_uncertain=False):
    """Main entry point."""
    if schema:
        filepath = os.path.join(SCHEMA_DIR, f'{schema}.linkml.yaml')
        if not os.path.exists(filepath):
            raise FileNotFoundError(f'Schema not found: {filepath}')
        files = [filepath]
    else:
        files = get_all_schemas()

    total = 0
    all_uncertain = {}

    for filepath in files:
        basename = os.path.basename(filepath)
        marked = mark_abstract_in_file(filepath, dry_run=dry_run)
        if marked:
            label = 'Would mark' if dry_run else 'Marked'
            print(f'  {label} {len(marked)} classes as abstract in {basename}: {", ".join(sorted(marked))}')
            total += len(marked)
        else:
            print(f'  No changes needed in {basename}')

        if show_uncertain:
            uncertain = find_uncertain_parents(filepath)
            if uncertain:
                all_uncertain[basename] = uncertain

    print(f'\nTotal: {total} class(es) {"would be" if dry_run else ""} marked abstract')

    if show_uncertain and all_uncertain:
        print(f'\nUncertain parent classes (have children but not in known-abstract list):')
        for basename, classes in all_uncertain.items():
            print(f'  {basename}: {", ".join(classes)}')

    return total
