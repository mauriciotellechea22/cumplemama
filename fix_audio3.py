import re

def main():
    file_path = 'C:\\Users\\elfac\\Documents\\Cumple Mamá\\cumpleanos_mama.html'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # The goal is to change:
    # <audio id="voiceMsg" preload="auto" src="audio cumple mama.mp4"></audio>
    # to:
    # <audio id="voiceMsg" preload="auto" src="voice_message.mp3"></audio>
    
    audio_pattern = r"audio\scumple\smama\.mp4"
    audio_replacement = r"voice_message.mp3"
    
    if re.search(audio_pattern, content):
        content = re.sub(audio_pattern, audio_replacement, content, count=1)
        print("HTML audio source updated to new MP3 encoding.")
    else:
        print("Could not find audio pattern.")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    main()
