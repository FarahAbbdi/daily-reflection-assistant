def export_daily_review_to_markdown(date_str, events, reflection_text, vault_path):
    """
    Export daily review data (calendar events, reflection, and AI insights)
    into a Markdown file at the specified export path.

    Args:
        date_str (str): The date for the review, formatted as YYYY-MM-DD.
        events (list): List of event summaries for the day.
        reflection_text (str): The user's reflection text from Google Sheets.
        vault_path (str): The directory path where the markdown file should be saved.

    Returns:
        None: Creates a markdown file with the review content.
    """
    filename = f"{vault_path}/{date_str}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write("## ✅ Events\n\n")
        for event in events:
            f.write(f"{event}\n")
        f.write("\n## 🧠 Reflection\n\n")
        f.write(f"{reflection_text}\n\n")
        f.write("## 📊 AI Analysis\n\n")
        f.write("Grade: Pass ✅\n")
        f.write("Suggestions: Focus more on time-blocking tasks.\n")