import re

def main():
    file_path = 'C:\\Users\\elfac\\Documents\\Cumple Mamá\\cumpleanos_mama.html'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # The goal is to change:
    # WhatsApp-Audio-2026-03-16-at-5.24.28-PM.mp3
    # to:
    # audio cumple mama.mp4
    
    # And optionally add type="audio/mp4" to be safe.
    
    audio_pattern = r"(<audio id=\"voiceMsg\" preload=\"auto\" src=\")WhatsApp-Audio-2026-03-16-at-5\.24\.28-PM\.mp3(\"></audio>)"
    audio_replacement = r'\1audio cumple mama.mp4\2'
    
    if re.search(audio_pattern, content):
        content = re.sub(audio_pattern, audio_replacement, content, count=1)
        print("Audio tag source updated to audio cumple mama.mp4")
    else:
        # Fallback regex if it differs slightly
        audio_pattern_2 = r"WhatsApp-Audio-2026-03-16-at-5\.24\.28-PM\.mp3"
        if re.search(audio_pattern_2, content):
            content = re.sub(audio_pattern_2, "audio cumple mama.mp4", content)
            print("Replaced WhatsApp audio with mp4 using string match.")
            
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    main()
