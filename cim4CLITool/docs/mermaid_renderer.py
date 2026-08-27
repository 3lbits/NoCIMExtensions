import os
import re
import subprocess
import shutil
import sys


def check_mmdc_installed():
    """Returns True if node and puppeteer are available for rendering."""
    return shutil.which("node") is not None


def _fix_svg_links(svg_path):
    """Adds target="_top" to links and ensures xlink namespace is declared."""
    with open(svg_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Add xlink namespace if missing
    if 'xmlns:xlink' not in content:
        content = content.replace('<svg ', '<svg xmlns:xlink="http://www.w3.org/1999/xlink" ', 1)
    content = re.sub(
        r'<a ([^>]*?)>',
        lambda m: f'<a {m.group(1)} target="_top">' if 'target=' not in m.group(1) else m.group(0),
        content
    )
    with open(svg_path, 'w', encoding='utf-8') as f:
        f.write(content)


def _strip_mermaid_fences(mermaid_string):
    """Strips ```mermaid and ``` fences from a mermaid code block."""
    lines = mermaid_string.strip().split('\n')
    if lines[0].strip().startswith('```mermaid'):
        lines = lines[1:]
    if lines[-1].strip() == '```':
        lines = lines[:-1]
    return '\n'.join(lines)


def prepare_mermaid_file(mermaid_string, class_name, profile_name):
    """Writes a .mmd file and returns the object tag for the markdown. No rendering yet."""
    mermaid_code = _strip_mermaid_fences(mermaid_string)

    diagrams_dir = os.path.join("docs", "Models", "Profiles", profile_name, "diagrams")
    os.makedirs(diagrams_dir, exist_ok=True)

    mmd_path = os.path.join(diagrams_dir, f"{class_name}.mmd")
    with open(mmd_path, 'w', encoding='utf-8') as f:
        f.write(mermaid_code)

    svg_filename = f"{class_name}.svg"
    relative_path = f"../../diagrams/{svg_filename}"
    return f'\n<object type="image/svg+xml" data="{relative_path}">{class_name} class diagram</object>\n'


def render_all_svgs(profile_name):
    """Renders all .mmd files in a profile's diagrams dir to SVGs in a single subprocess."""
    diagrams_dir = os.path.join("docs", "Models", "Profiles", profile_name, "diagrams")
    mmd_files = [f for f in os.listdir(diagrams_dir) if f.endswith('.mmd')] if os.path.isdir(diagrams_dir) else []

    if not mmd_files:
        return

    print(f"Rendering {len(mmd_files)} diagrams to SVG...")

    abs_dir = os.path.abspath(diagrams_dir)
    script_path = os.path.join(os.path.dirname(__file__), "render_diagrams.mjs")

    try:
        kwargs = {"capture_output": True, "text": True}
        if sys.platform == "win32":
            si = subprocess.STARTUPINFO()
            si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            si.wShowWindow = subprocess.SW_HIDE
            kwargs["startupinfo"] = si
        result = subprocess.run(
            ["node", script_path, abs_dir],
            **kwargs
        )
        if result.stdout:
            print(result.stdout.strip())
        if result.returncode != 0 and result.stderr:
            print(f"Render error: {result.stderr}")
    except FileNotFoundError:
        print("ERROR: node not found. Install Node.js to enable SVG diagram rendering.")
        return

    # Post-process SVGs and clean up .mmd files
    success = 0
    for mmd_file in mmd_files:
        svg_path = os.path.join(abs_dir, mmd_file.replace('.mmd', '.svg'))
        mmd_path = os.path.join(abs_dir, mmd_file)
        if os.path.exists(svg_path):
            _fix_svg_links(svg_path)
            success += 1
        os.unlink(mmd_path)

    print(f"Rendered {success}/{len(mmd_files)} diagrams successfully")
