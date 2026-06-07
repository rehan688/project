import os
import pathlib
import re
from urllib.parse import urlsplit, urlunsplit

root = pathlib.Path(__file__).parent

def resolve_relative_path(current_file, href):
    """Resolve a relative href from the current file's perspective."""
    # Remove anchors
    href_clean = href.split('#')[0].strip()
    if not href_clean:
        return None
    
    # Get the directory of the current file
    current_dir = pathlib.Path(current_file).parent
    
    # Resolve the relative path
    try:
        resolved = (current_dir / href_clean).resolve()
        # Check if it exists and is under root
        if resolved.exists() and str(resolved).startswith(str(root)):
            return resolved.relative_to(root).as_posix()
    except:
        pass
    
    return None

def normalize_html_links(html_path):
    """Fix relative paths in HTML file."""
    with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    original = content
    
    # Find all href values
    def replace_href(match):
        href = match.group(1)
        
        # Skip external links and special protocols
        if href.startswith(('http://', 'https://', 'mailto:', 'tel:', '#', 'javascript:', 'ftp://')):
            return match.group(0)
        
        # Try to resolve relative path
        resolved = resolve_relative_path(html_path, href)
        if resolved:
            # Convert back to relative path from current file
            current_dir = pathlib.Path(html_path).parent
            target_path = root / resolved
            
            try:
                rel = target_path.relative_to(current_dir)
                new_href = rel.as_posix()
                if new_href != href:
                    return f'href="{new_href}"'
            except ValueError:
                pass
        
        return match.group(0)
    
    # Replace href values
    content = re.sub(r'href=["\']([^"\']+)["\']', replace_href, content)
    
    if content != original:
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

# Process all HTML files
fixed = 0
for html_file in sorted(root.rglob('*.html')):
    if normalize_html_links(html_file):
        print(f"Fixed relative paths in {html_file.relative_to(root)}")
        fixed += 1

print(f"\nProcessed {sum(1 for _ in root.rglob('*.html'))} HTML files, fixed {fixed} files with relative path issues.")
