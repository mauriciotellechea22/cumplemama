import re

def main():
    file_path = 'C:\\Users\\elfac\\Documents\\Cumple Mamá\\cumpleanos_mama.html'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix lid position container (top: -40px -> top: 10px)
    # The gift container is 200px tall. gift box is 150 tall at bottom: 0. 
    # That means top of gift box is 50px away from container top. 
    # gift lid is 40px height. To rest precisely on Y=50px, top must be 10px.
    content = re.sub(
        r"(\.gift-lid\s*\{[\s\S]*?top:\s*)-40px;", 
        r"\g<1>10px;", 
        content, 
        count=1
    )

    # Fix lid top face geometry.
    # We need to center the 160px tall plane into the 40px deep container, so top: -60px.
    # Then rotateX 90deg and translateZ(20px) to shift it 20px "up" into position.
    old_lid_top = r"(transform:\s*rotateX\(90deg\)\s*translateZ\(20px\)\s*translateY\(-60px\);)"
    new_lid_top = r"top: -60px;\n    transform: rotateX(90deg) translateZ(20px);"
    
    if re.search(old_lid_top, content):
        content = re.sub(old_lid_top, new_lid_top, content, count=1)
        print("Lid top geometry fixed")
    else:
        print("Lid top NOT found")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    main()
