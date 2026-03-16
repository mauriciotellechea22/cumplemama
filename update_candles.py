import re

def main():
    file_path = 'C:\\Users\\elfac\\Documents\\Cumple Mamá\\cumpleanos_mama.html'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update HTML for candles
    html_pattern = r"(<div class=\"candles\">\s*<div class=\"candle\"><div class=\"flame\"></div><div class=\"smoke\"></div></div>\s*<div class=\"candle\"><div class=\"flame\"></div><div class=\"smoke\"></div></div>\s*<div class=\"candle\"><div class=\"flame\"></div><div class=\"smoke\"></div></div>\s*</div>)"
    html_replacement = r"""<div class="candles">
        <div class="candle num-5">5<div class="flame"></div><div class="smoke"></div></div>
        <div class="candle num-3">3<div class="flame"></div><div class="smoke"></div></div>
      </div>"""
    
    if re.search(html_pattern, content):
        content = re.sub(html_pattern, html_replacement, content, count=1)
        print("HTML for candles updated.")
    else:
        print("HTML for candles NOT found.")

    # 2. Update CSS for candles
    css_pattern = r"(\.candle\s*\{[^}]*?width:\s*12px;[^}]*?height:\s*45px;[^}]*?background:\s*repeating-linear-gradient[^}]*?\})"
    css_replacement = r""".candle {
    position: relative;
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
    font-size: 3rem;
    color: transparent;
    background: repeating-linear-gradient(45deg, #fff, #fff 5px, var(--gold) 5px, var(--gold) 10px);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-stroke: 1px var(--gold);
    line-height: 1;
    text-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    /* padding top to create space for flame */
    padding-top: 15px; 
  }
  /* Remove old background/border-radius from original .candle */"""
    
    if re.search(css_pattern, content):
        content = re.sub(css_pattern, css_replacement, content, count=1)
        print("CSS for original candle updated.")
    else:
        print("CSS for original candle NOT found.")


    # 3. Fix Flame and Smoke positioning for the text-based candles
    flame_pattern = r"(\.flame\s*\{[^}]*?top:\s*)-20px;"
    if re.search(flame_pattern, content):
        content = re.sub(flame_pattern, r"\1 0px;", content, count=1)
        print("Flame top position updated.")

    smoke_pattern = r"(\.smoke\s*\{[^}]*?top:\s*)-20px;"
    if re.search(smoke_pattern, content):
        content = re.sub(smoke_pattern, r"\1 0px;", content, count=1)
        print("Smoke top position updated.")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    main()
