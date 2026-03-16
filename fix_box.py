import re

def main():
    file_path = 'C:\\Users\\elfac\\Documents\\Cumple Mamá\\cumpleanos_mama.html'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update CSS to fix the 3D box geometry and add styling for the text
    css_pattern = r"(\.gift-container\s*\{[\s\S]*?)(/\* Animation classes \*/)"
    
    css_replacement = r"""
  .gift-container {
    perspective: 800px;
    width: 200px;
    height: 200px;
    margin: 0 auto;
    cursor: pointer;
    position: relative;
    /* Adjust initial rotation to see it better */
    transform: rotateX(-10deg) rotateY(-15deg);
    transform-style: preserve-3d;
    transition: transform 0.5s ease;
  }

  .gift-container:hover {
    transform: rotateX(-5deg) rotateY(-25deg);
  }

  .gift-box {
    width: 150px;
    height: 150px;
    position: absolute;
    bottom: 0;
    left: 25px;
    transform-style: preserve-3d;
  }

  /* Box Sides */
  .gift-side {
    position: absolute;
    width: 150px;
    height: 150px;
    background: linear-gradient(135deg, var(--gold) 0%, #a37c15 100%);
    border: 1px solid #8a6c12;
    box-shadow: inset 0 0 40px rgba(0,0,0,0.3);
    display: flex;
    align-items: center;
    justify-content: center;
  }

  /* Ribbons on box */
  .gift-side::before, .gift-side::after {
    content: '';
    position: absolute;
    background: rgba(255,255,255,0.4);
    box-shadow: 0 0 5px rgba(0,0,0,0.1);
  }
  .gift-side::before { width: 30px; height: 100%; }
  .gift-side::after { width: 100%; height: 30px; }

  /* Positioning Box Sides */
  .gift-front  { transform: translateZ(75px); }
  .gift-back   { transform: rotateY(180deg) translateZ(75px); }
  .gift-right  { transform: rotateY(90deg) translateZ(75px); }
  .gift-left   { transform: rotateY(-90deg) translateZ(75px); }
  
  /* Text on the front of the box */
  .gift-text {
    position: absolute;
    z-index: 10;
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.8rem;
    font-weight: 700;
    color: var(--dark);
    text-align: center;
    line-height: 1.1;
    text-shadow: 1px 1px 2px rgba(255,255,255,0.5);
    background: rgba(255,255,255,0.85);
    padding: 5px 15px;
    border-radius: 5px;
    border: 1px solid var(--gold);
    /* Push text slightly entirely out of ribbon */
    transform: translateZ(2px);
  }

  /* Inside bottom */
  .gift-bottom { transform: rotateX(-90deg) translateZ(75px); background: #3a2a05; }

  /* Lid Container - ensuring it sits correctly on top */
  .gift-lid {
    position: absolute;
    width: 160px;
    height: 40px;
    top: -40px; /* Sits perfectly above the 150px box */
    left: 20px; /* (200 container - 160 lid)/2 */
    transform-style: preserve-3d;
    transition: transform 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    transform-origin: bottom right;
    z-index: 10;
  }

  /* Lid Sides */
  .lid-side {
    position: absolute;
    width: 160px;
    height: 40px;
    background: linear-gradient(135deg, var(--rose) 0%, #b35640 100%);
    border: 1px solid #8c4130;
    display: flex;
    justify-content: center;
  }
  
  /* Ribbons on lid sides */
  .lid-side::before {
    content: '';
    position: absolute;
    width: 30px;
    height: 100%;
    background: rgba(255,255,255,0.4);
  }

  .lid-top {
    position: absolute;
    width: 160px;
    height: 160px;
    background: linear-gradient(135deg, #e6917c 0%, var(--rose) 100%);
    transform: rotateX(90deg) translateZ(20px) translateY(-60px);
    border: 1px solid #b35640;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  
  /* Ribbon cross on lid top */
  .lid-top::before, .lid-top::after {
    content: '';
    position: absolute;
    background: rgba(255,255,255,0.4);
  }
  .lid-top::before { width: 30px; height: 100%; }
  .lid-top::after { width: 100%; height: 30px; }

  /* Positioning Lid Sides */
  .lid-front  { transform: translateZ(80px); }
  .lid-back   { transform: rotateY(180deg) translateZ(80px); }
  .lid-right  { width: 160px; transform: rotateY(90deg) translateZ(80px); }
  .lid-left   { width: 160px; transform: rotateY(-90deg) translateZ(80px); }

  \2"""

    if re.search(css_pattern, content):
        content = re.sub(css_pattern, css_replacement, content, count=1)
        print("CSS geometry updated")
    else:
        print("CSS Geometry pattern NOT FOUND")

    # Fix animation classes targeting container correctly now
    anim_pattern = r"(\.gift-container:hover .gift-box \{).*?(\}\s*\.gift-container:hover .gift-lid \{).*?(\})"
    anim_replacement = r"/* Handled in main hover now */"
    if re.search(anim_pattern, content):
        content = re.sub(anim_pattern, anim_replacement, content, count=1)
        print("CSS hover cleaned")

    # 2. Add 'Feliz Cumple' text to the Front face HTML
    html_pattern = r"(<div class=\"gift-side gift-front\">)(</div>)"
    html_replacement = r"\1<div class=\"gift-text\">Feliz<br>Cumple</div>\2"
    
    if re.search(html_pattern, content):
        content = re.sub(html_pattern, html_replacement, content, count=1)
        print("HTML Feliz Cumple added")
    else:
        print("HTML pattern NOT FOUND")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    main()
