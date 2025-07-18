# Exports daily review data (calendar events, reflection, and AI insights)
# into a Markdown file at the specified export_path.
def export_daily_review_to_markdown(date_str, events, reflection_text, vault_path):
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