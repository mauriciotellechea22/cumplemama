import re

def main():
    file_path = 'C:\\Users\\elfac\\Documents\\Cumple Mamá\\cumpleanos_mama.html'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Darken the gold color slightly for better contrast
    content = re.sub(r'--gold:\s*#d4af37;', r'--gold: #c59b27;', content)

    # 2. Add medium font weight to the body
    body_pattern = r"(body\s*\{[^}]*?font-family:\s*'Montserrat',\s*sans-serif;)"
    if re.search(body_pattern, content):
        content = re.sub(body_pattern, r"\1\n    font-weight: 500;", content, count=1)
        print("Body font-weight updated.")

    # 3. Increase font weight of hero title and soften text-shadow
    hero_title_pattern = r"(\.hero-title\s*\{[^}]*?)font-weight:\s*300;([^}]*?)text-shadow:\s*2px 4px 12px rgba\(139,98,57,0\.1\);"
    if re.search(hero_title_pattern, content):
        content = re.sub(hero_title_pattern, r"\1font-weight: 600;\2text-shadow: 1px 2px 4px rgba(139,98,57,0.15);", content, count=1)
        print("Hero title updated.")

    # 4. Increase font weight of message text and remove shadow
    msg_text_pattern = r"(\.message-text\s*\{[^}]*?)font-weight:\s*300;([^}]*?)text-shadow:\s*1px 1px 5px rgba\(0,0,0,0\.02\);"
    if re.search(msg_text_pattern, content):
        content = re.sub(msg_text_pattern, r"\1font-weight: 500;\2", content, count=1)
        print("Message text updated.")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        print("Write successful.")

if __name__ == '__main__':
    main()
