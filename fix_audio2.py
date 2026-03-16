import re

def main():
    file_path = 'C:\\Users\\elfac\\Documents\\Cumple Mamá\\cumpleanos_mama.html'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # The goal is to change:
    # <audio id="voiceMsg" preload="auto">
    #   <source src="WhatsApp-Audio-2026-03-16-at-5.24.28-PM.mp3" type="audio/mpeg">
    # </audio>
    # to:
    # <audio id="voiceMsg" src="WhatsApp-Audio-2026-03-16-at-5.24.28-PM.mp3" preload="auto"></audio>
    
    audio_pattern = r"(<audio id=\"voiceMsg\" preload=\"auto\">[\s\S]*?<source src=\"WhatsApp-Audio-2026-03-16-at-5\.24\.28-PM\.mp3\" type=\"audio/mpeg\">[\s\S]*?</audio>)"
    audio_replacement = r"""<audio id="voiceMsg" preload="auto" src="WhatsApp-Audio-2026-03-16-at-5.24.28-PM.mp3"></audio>"""
    
    if re.search(audio_pattern, content):
        content = re.sub(audio_pattern, audio_replacement, content, count=1)
        print("Audio tag rewritten without explicit type constraint.")
    else:
        # Fallback regex if it differs slightly
        audio_pattern_2 = r"(<audio id=\"voiceMsg\">[\s\S]*?<source src=\"WhatsApp-Audio-2026-03-16-at-5\.24\.28-PM\.mp3\" [^>]*>[\s\S]*?</audio>)"
        if re.search(audio_pattern_2, content):
            content = re.sub(audio_pattern_2, audio_replacement, content, count=1)
            print("Audio tag rewritten using fallback regex.")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    main()
