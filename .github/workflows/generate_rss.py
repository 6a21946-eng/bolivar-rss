import requests
from bs4 import BeautifulSoup
from datetime import datetime

URL = "https://example.com"  # <-- luego cambias esto por la web real

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

items = []

# Tomamos los primeros 10 enlaces como titulares de ejemplo
for i, link in enumerate(soup.find_all("a")[:10]):
    title = link.get_text(strip=True)
    href = link.get("href")
    if title and href:
        items.append(f"""
        <item>
            <title>{title}</title>
            <link>{href}</link>
            <pubDate>{datetime.utcnow()}</pubDate>
        </item>
        """)

rss_content = f"""<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
<channel>
    <title>Mi RSS automático</title>
    <link>{URL}</link>
    <description>Titulares automáticos</description>
    {''.join(items)}
</channel>
</rss>
"""

with open("rss.xml", "w", encoding="utf-8") as f:
    f.write(rss_content)
