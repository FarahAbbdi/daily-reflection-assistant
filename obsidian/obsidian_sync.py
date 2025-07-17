# Save daily revew data (events and reflections) as a m
# markdown file in the specified obsidian value
def save_markdown_to_obsidian(date_str, events, reflection_text, vault_path):
    filename = f"{vault_path}/{date_str}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write("## Events\n")
        for event in events:
            f.write(f"- {event}\n")
        f.write("\n## Reflection\n")
        f.write(reflection_text)