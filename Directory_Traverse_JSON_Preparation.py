"""
📁 Directory Structure JSON Generator for Badger-Icons Repository

🔗 Repository: https://github.com/madhurimarawat/Badger-Icons
👩‍💻 Author: Madhurima Rawat
📅 Date: 2025-06-01

This script generates a JSON representation of a directory structure,
adding descriptions for folders based on a custom dictionary.

✨ Features:
- The `_description` field is added only to subdirectories (not the root).
- Uses custom descriptions from the `CUSTOM_DESCRIPTIONS` dictionary 📚.
- For unknown folders, creates a generic description with the folder name.
- Generates friendly file descriptions based on folder topics.
- Excludes specified directories (like 'json') during processing.

Usage:
Run from the command line with optional parameters for base directory,
excluded folders, and output JSON path.

Example:
python generate_directory_structure.py --base assets --exclude json --output assets/json/directory-structure_1.json
"""

import os
import json
import re

# Dictionary of custom descriptions for known folders 📝
CUSTOM_DESCRIPTIONS = {
    "databases": "Icons and logos for different database technologies.",
    "mongodb": "Icons and logos representing MongoDB, a NoSQL database.",
    "mysql": "Icons and logos representing MySQL, a relational database management system.",
    "greetings": "Icons and logos for different greetings.",
    "thank_you": "Icons and logos representing the thank you greeting.",
    "job_roles": "Icons and logos for different job roles in tech.",
    "ai_research": "Icons and logos representing AI research concepts.",
    "data_analyst": "Icons and logos for the Data Analyst role.",
    "data_engineer": "Icons and logos for the Data Engineer role.",
    "data_scientist": "Icons and logos for the Data Scientist role.",
    "network_engineer": "Icons and logos for the Network Engineer role.",
    "open_source": "Icons and logos for open-source projects.",
    "contributor": "Icons and logos for contributors.",
    "github": "Icons and logos for GitHub.",
    "programming_languages": "Icons and logos for programming languages.",
    "c": "Icons and logos for C programming language.",
    "c++": "Icons and logos for C++ programming language.",
    "python": "Icons and logos for Python programming language.",
    "ruby": "Icons and logos for Ruby programming language.",
    "subjects": "Icons related to academic subjects.",
    "algorithmic-gaming-theory": "Icons for Algorithmic Gaming Theory.",
    "management-information-system": "Icons for Management Information System.",
    "website_status": "Status of the website.",
    "active": "Status of the website is active.",
    "403_forbidden": "403 Forbidden error page.",
    "500_internal_server": "500 Internal Server Error page.",
    "cors": "CORS error page.",
    "error_404": "404 Not Found error page.",
}


def clean_description(desc):
    """
    🔍 Clean up descriptions by:
    - Removing generic intro phrases like 'Icons and logos for'
    - Removing trailing 'page' or 'error page'
    Returns a concise topic description.
    """
    # Remove intro phrases (case insensitive)
    desc = re.sub(
        r"^(Icons (and logos)? (for|representing)\s*)", "", desc, flags=re.IGNORECASE
    )
    # Remove trailing ' page' or ' error page' or ' page.' at the end
    desc = re.sub(r"\s+(\s+)?page\.?$", "", desc, flags=re.IGNORECASE)
    return desc.strip()


def describe_file(file_name, parent_desc):
    """
    🖼️ Generate a user-friendly description for a file based on
    its name and the description of its parent folder.

    Args:
    - file_name: the filename string
    - parent_desc: description of the containing folder

    Returns a string like:
    "filename.png (Transparent Logo for databases)"
    """
    topic = clean_description(parent_desc)

    base_name = file_name.lower()
    if "transparent" in base_name and "logo" in base_name:
        prefix = "Transparent Logo"
    elif "transparent" in base_name and "icon" in base_name:
        prefix = "Transparent Icon"
    elif "logo" in base_name:
        prefix = "Logo"
    elif "icon" in base_name:
        prefix = "Icon"
    else:
        prefix = "Image"

    return f"{file_name} ({prefix} for {topic})"


def process_dir(path, rel_path="", exclude_dirs=None):
    """
    🔄 Recursively process a directory to:
    - Add descriptions to subdirectories (_description)
    - List files with friendly descriptions
    - Skip excluded directories

    Args:
    - path: current directory absolute path
    - rel_path: relative path for recursion tracking (empty string for root)
    - exclude_dirs: list of folder names to skip

    Returns a dict representing the directory structure.
    """
    folder = os.path.basename(path)
    raw_desc = CUSTOM_DESCRIPTIONS.get(
        folder, f"Icons and logos for {folder.replace('_', ' ')}."
    )
    result = {}

    # Add _description only for subdirectories (not root)
    if rel_path:
        result["_description"] = raw_desc

    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        entry_rel_path = os.path.join(rel_path, entry).replace("\\", "/")

        # Skip excluded directories
        if os.path.isdir(full_path):
            if exclude_dirs and entry in exclude_dirs:
                continue
            # Recurse into subdirectory
            result[entry] = process_dir(full_path, entry_rel_path, exclude_dirs)
        else:
            # Add file descriptions under "files" list
            if "files" not in result:
                result["files"] = []
            result["files"].append(describe_file(entry, raw_desc))

    return result


def build_structure(base_path, exclude_dirs=None):
    """
    🏗️ Build the entire directory JSON structure from base_path,
    excluding specified directories.

    Adds metadata about generator and base folder name.
    """
    return {
        "Generated by": "Madhurima Rawat",
        "Local Directory": os.path.basename(base_path),
        "directories": process_dir(base_path, rel_path="", exclude_dirs=exclude_dirs),
    }


# --- USAGE ---
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Generate JSON from directory structure."
    )
    parser.add_argument(
        "--base", default="assets", help="Base directory (default: assets) 📂"
    )
    parser.add_argument(
        "--exclude", nargs="*", default=["json"], help="Folders to exclude 🚫"
    )
    parser.add_argument(
        "--output",
        default="assets/json/directory-structure.json",
        help="Output JSON file path 💾",
    )

    args = parser.parse_args()

    # Build directory JSON structure
    json_data = build_structure(args.base, exclude_dirs=args.exclude)

    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(args.output), exist_ok=True)

    # Write JSON file with pretty indentation
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(json_data, f, indent=2)

    print(f"✅ JSON structure written to {args.output}")
