import re

def main():
    file_path = 'C:\\Users\\elfac\\Documents\\Cumple Mamá\\cumpleanos_mama.html'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update the Audio source parameter to ensure preload
    audio_pattern = r"(<audio id=\"voiceMsg\">[\s\S]*?<source src=\"WhatsApp-Audio-2026-03-16-at-5\.24\.28-PM\.mp3\" type=\"audio/mpeg\">[\s\S]*?</audio>)"
    audio_replacement = r"""<audio id="voiceMsg" preload="auto">
  <source src="WhatsApp-Audio-2026-03-16-at-5.24.28-PM.mp3" type="audio/mpeg">
</audio>"""
    
    if re.search(audio_pattern, content):
        content = re.sub(audio_pattern, audio_replacement, content, count=1)
        print("1. Audio tag added preload attribute")
    else:
        # Fallback regex if formatting slightly differs
        audio_pattern_2 = r"(<audio id=\"voiceMsg\">)"
        if re.search(audio_pattern_2, content):
            content = re.sub(audio_pattern_2, r"<audio id=\"voiceMsg\" preload=\"auto\">", content, count=1)
            print("1. Audio tag added preload attribute (fallback)")

    # 2. Update the Javascript playback logic to be more robust
    js_pattern = r"(vControls\.classList\.add\('show'\);\s*voiceAudio\.play\(\)\.catch\(e => console\.log\('Voice audio blocked', e\)\);)"
    
    js_replacement = r"""vControls.classList.add('show');
      
      // Ensure audio is loaded and then play explicitly handling the promise
      document.getElementById('vIcon').textContent = '⏸️'; // Immediately show pause icon (playing state)
      
      let playPromise = voiceAudio.play();
      if (playPromise !== undefined) {
          playPromise.then(_ => {
              console.log("Audio playing successfully");
          })
          .catch(error => {
              console.log("Autoplay prevented or audio load error:", error);
              document.getElementById('vIcon').textContent = '▶️'; // Revert to play if failed
          });
      }"""

    if re.search(js_pattern, content):
        content = re.sub(js_pattern, js_replacement, content, count=1)
        print("2. JavaScript logic updated")
    else:
        print("JS pattern not found, trying fallback...")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    main()
