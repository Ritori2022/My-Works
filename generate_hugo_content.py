#!/usr/bin/env python3
"""Parse source files and generate Hugo content sections"""

import re
import os
from collections import defaultdict

BASE = "/home/user/My-Works"
SITE_CONTENT = "/home/user/My-Works/site/content"


def get_year(month):
    """Months 9-12 are 2025, months 1-8 are 2026"""
    return 2025 if month >= 9 else 2026


def parse_file(filepath):
    """
    Parse a file with dated entries.
    Returns dict: "YYYY-MM-DD" -> list of content strings (one per entry block)
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    entries = defaultdict(list)
    current_date = None
    current_block = []

    # Strict date: a line that contains ONLY a date like "10.29" or " 2.26 "
    strict_date_re = re.compile(r'^\s*(\d{1,2})\.(\d{1,2})\s*$')

    def flush():
        if current_date is not None and current_block:
            text = '\n'.join(current_block).strip()
            if text:
                entries[current_date].append(text)
        current_block.clear()

    for line in lines:
        m = strict_date_re.match(line)
        if m:
            flush()
            month = int(m.group(1))
            day = int(m.group(2))
            year = get_year(month)
            current_date = f"{year}-{month:02d}-{day:02d}"
        elif current_date is not None:
            # Handle edge case: content line ending with an inline date (typo in source)
            # e.g. "...数学结构的涌现10.25"
            inline = re.search(r'(\d{1,2})\.(\d{1,2})$', line)
            if inline:
                pm = int(inline.group(1))
                pd = int(inline.group(2))
                # Only treat as date if it looks like a valid month.day AND
                # there's no Chinese char or period before it (i.e. it's standalone)
                char_before = line[inline.start()-1] if inline.start() > 0 else ''
                if (1 <= pm <= 12 and 1 <= pd <= 31 and
                        char_before not in '，。、！？,.。：:；;'):
                    content_part = line[:inline.start()].rstrip()
                    if content_part:
                        current_block.append(content_part)
                    flush()
                    year = get_year(pm)
                    current_date = f"{year}-{pm:02d}-{pd:02d}"
                    continue
            current_block.append(line)

    flush()
    return entries


def format_display_date(date_key):
    """Convert "2025-10-29" to "10.29" """
    parts = date_key.split('-')
    month = int(parts[1])
    day = int(parts[2])
    return f"{month}.{day}"


def escape_yaml(s):
    """Escape string for YAML front matter"""
    return s.replace('"', '\\"')


def create_section(section_id, section_name, section_desc, entries):
    """Create Hugo content files for a section"""
    section_dir = os.path.join(SITE_CONTENT, section_id)
    os.makedirs(section_dir, exist_ok=True)

    # Create _index.md
    index_md = f"""---
title: "{escape_yaml(section_name)}"
description: "{escape_yaml(section_desc)}"
---
"""
    with open(os.path.join(section_dir, '_index.md'), 'w', encoding='utf-8') as f:
        f.write(index_md)

    # Create one .md file per date (all entries for that date combined)
    count = 0
    for date_key in sorted(entries.keys()):
        blocks = entries[date_key]
        display_date = format_display_date(date_key)
        filename = f"{date_key}.md"
        filepath = os.path.join(section_dir, filename)

        # Combine all blocks for this date with a horizontal rule separator
        combined = '\n\n---\n\n'.join(blocks)

        md = f"""---
title: "{display_date}"
date: {date_key}
categories: ["{escape_yaml(section_name)}"]
---

{combined}
"""
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(md)
        count += 1

    print(f"  [{section_name}] Created {count} date-files in {section_dir}")
    return count


def main():
    sections = [
        {
            "id": "thoughts",
            "name": "思考",
            "desc": "碎片与闪光——随机涌现的思维记录",
            "file": os.path.join(BASE, "思考"),
        },
        {
            "id": "theater",
            "name": "概念剧场",
            "desc": "以对话形式上演的哲学与观念剧",
            "file": os.path.join(BASE, "概念剧场"),
        },
        {
            "id": "notes",
            "name": "笔记",
            "desc": "阅读与思考的结构化沉淀",
            "file": os.path.join(BASE, "笔记"),
        },
    ]

    total = 0
    for s in sections:
        print(f"Parsing {s['file']}...")
        entries = parse_file(s['file'])
        print(f"  Found {len(entries)} unique dates")
        n = create_section(s['id'], s['name'], s['desc'], entries)
        total += n

    print(f"\nTotal: {total} content files created.")


if __name__ == "__main__":
    main()
