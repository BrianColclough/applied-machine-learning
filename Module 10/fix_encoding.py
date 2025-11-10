#!/usr/bin/env python3
"""
Script to fix encoding issues in CSV files by replacing Windows-1252 characters
with UTF-8 compatible alternatives.
"""

import os
import shutil
from pathlib import Path

def fix_encoding(file_path, backup=True, replace_char=b'-'):
    """
    Fix encoding issues by replacing problematic bytes.
    
    Args:
        file_path: Path to the CSV file
        backup: Whether to create a backup of the original file
        replace_char: Byte(s) to replace 0x96 with (default: b'-' for regular dash)
    """
    file_path = Path(file_path)
    
    if not file_path.exists():
        print(f"Error: File {file_path} does not exist!")
        return False
    
    print(f"Processing: {file_path}")
    
    # Create backup if requested
    if backup:
        backup_path = file_path.with_suffix('.csv.backup')
        print(f"Creating backup: {backup_path}")
        shutil.copy2(file_path, backup_path)
    
    # Read file in binary mode
    print("Reading file...")
    with open(file_path, 'rb') as f:
        data = f.read()
    
    # Count occurrences
    count = data.count(b'\x96')
    print(f"Found {count} occurrences of byte 0x96 (en-dash)")
    
    if count == 0:
        print("No problematic characters found. File should be fine!")
        return True
    
    # Replace problematic byte
    print(f"Replacing 0x96 with {replace_char.decode('utf-8', errors='replace')}...")
    fixed_data = data.replace(b'\x96', replace_char)
    
    # Write back
    print("Writing fixed file...")
    with open(file_path, 'wb') as f:
        f.write(fixed_data)
    
    print(f"✓ Successfully fixed {count} occurrences!")
    return True

if __name__ == "__main__":
    # File to fix
    file_to_fix = "./TrafficLabelling/Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv"
    
    # You can change replace_char to:
    # - b'-' for regular dash (current)
    # - b'\xe2\x80\x93' for UTF-8 en-dash (–)
    # - b' ' for space
    replace_char = b'-'  # Regular dash
    
    fix_encoding(file_to_fix, backup=True, replace_char=replace_char)
    
    print("\nDone! You can now read the file with pandas using UTF-8 encoding.")

