import os

def export_ai_report_to_markdown(date_str, markdown_text, export_path):
    """
    Save AI-generated markdown report to a .md file in the given export_path.
    Filename is based on the date (e.g., 2025-07-18.md).

    Args:
        date_str (str): Date string for filename (YYYY-MM-DD).
        markdown_text (str): The markdown content to save.
        export_path (str): Directory path where file will be saved.

    Returns:
        str: Full path to the saved markdown file.
    """
    if not os.path.exists(export_path):
        os.makedirs(export_path)  # Create folder if doesn't exist

    filename = f"{date_str}.md"
    filepath = os.path.join(export_path, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(markdown_text)

    return filepath