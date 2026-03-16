import sys
import codecs

filepath = r"C:\Users\elfac\Documents\Cumple Mamá\cumpleanos_mama.html"

with codecs.open(filepath, "r", "utf-8") as f:
    content = f.read()

start_tag = "<style>"
end_tag = "</style>"
idx1 = content.find(start_tag)
idx2 = content.find(end_tag) + len(end_tag)

new_css = """<style>
  :root {
    --gold: #d4af37;
    --gold-light: #f9e596;
    --cream: #fcf9f2;
    --dark: #1c150d;
    --rose: #e2856e;
    --soft-brown: #8b6239;
    --glass-bg: rgba(255, 255, 255, 0.4);
    --glass-border: rgba(255, 255, 255, 0.4);
    --glass-shadow: 0 8px 32px 0 rgba(139, 111, 71, 0.15);
  }

  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    background: var(--cream);
    color: var(--dark);
    font-family: 'Montserrat', sans-serif;
    overflow-x: hidden;
  }

  /* Animated background */
  body::before {
    content: '';
    position: fixed;
    inset: 0;
    background: 
      radial-gradient(circle at 10% 10%, rgba(212,175,55,0.08) 0%, transparent 50%),
      radial-gradient(circle at 90% 20%, rgba(226,133,110,0.06) 0%, transparent 60%),
      radial-gradient(circle at 50% 80%, rgba(212,175,55,0.06) 0%, transparent 50%);
    pointer-events: none;
    z-index: 0;
  }

  .page { position: relative; z-index: 1; }

  /* ===== HERO ===== */
  .hero {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 60px 20px;
    position: relative;
    background: linear-gradient(135deg, rgba(252,249,242,0.9) 0%, rgba(250,240,220,0.6) 100%);
  }

  .hero-ornament {
    font-size: 2rem;
    color: var(--gold);
    letter-spacing: 0.3em;
    margin-bottom: 24px;
    opacity: 0;
    animation: fadeUp 1s ease forwards 0.3s;
  }

  .hero-subtitle {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(1.2rem, 3.5vw, 1.5rem);
    font-style: italic;
    color: var(--soft-brown);
    letter-spacing: 0.15em;
    margin-bottom: 16px;
    opacity: 0;
    animation: fadeUp 1s ease forwards 0.5s;
  }

  .hero-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(4rem, 15vw, 9rem);
    font-weight: 300;
    line-height: 0.9;
    color: var(--dark);
    margin-bottom: 12px;
    opacity: 0;
    animation: fadeUp 1.2s ease forwards 0.7s;
    text-shadow: 2px 4px 12px rgba(139,98,57,0.1);
  }

  .hero-title em {
    font-style: italic;
    color: var(--gold);
  }

  .hero-personal {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(1.3rem, 3.5vw, 1.8rem);
    font-style: italic;
    color: var(--rose);
    margin: 12px 0 0;
    opacity: 0;
    animation: fadeUp 1s ease forwards 0.9s;
  }

  .hero-age {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(1.4rem, 4vw, 2.2rem);
    color: var(--rose);
    letter-spacing: 0.4em;
    margin: 24px 0 40px;
    opacity: 0;
    animation: fadeUp 1s ease forwards 1s;
  }

  .hero-date {
    font-size: 0.8rem;
    font-weight: 500;
    letter-spacing: 0.35em;
    text-transform: uppercase;
    color: var(--soft-brown);
    opacity: 0;
    animation: fadeUp 1s ease forwards 1.2s;
  }

  /* Divider */
  .divider {
    display: flex;
    align-items: center;
    gap: 20px;
    margin: 60px auto;
    width: min(400px, 80%);
    opacity: 0;
    animation: fadeIn 1s ease forwards 1.5s;
  }
  .divider::before, .divider::after {
    content: '';
    flex: 1;
    height: 1px;
    background: linear-gradient(to right, transparent, var(--gold), transparent);
  }
  .divider-gem {
    color: var(--gold);
    font-size: 1.4rem;
  }

  /* ===== PHOTO GRID ===== */
  .photos-section {
    padding: 40px 20px 80px;
    max-width: 1100px;
    margin: 0 auto;
  }

  .photos-grid {
    column-count: 3;
    column-gap: 20px;
  }

  .photo-card {
    position: relative;
    overflow: hidden;
    opacity: 0;
    transform: translateY(20px);
    transition: all 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    break-inside: avoid;
    margin-bottom: 20px;
    border-radius: 16px;
    animation: fadeUp 0.8s ease forwards;
    box-shadow: var(--glass-shadow);
  }

  .photo-card:hover {
    transform: translateY(-8px) scale(1.02);
    box-shadow: 0 20px 40px rgba(212,175,55,0.25);
    z-index: 2;
  }

  .photo-card img {
    width: 100%;
    height: auto;
    display: block;
    object-fit: cover;
    filter: saturate(0.95);
    transition: filter 0.5s ease, transform 0.5s ease;
  }

  .photo-card:hover img {
    filter: saturate(1.1);
    transform: scale(1.05);
  }

  .photo-card::after {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(to top, rgba(28,21,13,0.4) 0%, transparent 50%);
    pointer-events: none;
    border-radius: 16px;
    transition: opacity 0.5s ease;
  }

  .photo-card:hover::after {
    opacity: 0.7;
  }

  /* ===== MESSAGE ===== */
  .message-section {
    padding: 80px 20px 100px;
    max-width: 800px;
    margin: 0 auto;
    text-align: center;
    background: linear-gradient(180deg, transparent 0%, rgba(252,249,242,0.8) 30%, rgba(252,249,242,0.8) 70%, transparent 100%);
  }

  .message-label {
    font-size: 0.75rem;
    letter-spacing: 0.45em;
    text-transform: uppercase;
    color: var(--gold);
    margin-bottom: 36px;
    opacity: 0;
    animation: fadeIn 1s ease forwards 0.3s;
  }

  .message-text {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(1.6rem, 4vw, 2.4rem);
    font-weight: 300;
    line-height: 1.6;
    color: var(--dark);
    opacity: 0;
    animation: fadeUp 1.2s ease forwards 0.5s;
    text-shadow: 1px 1px 5px rgba(0,0,0,0.02);
  }

  .message-text strong {
    font-weight: 600;
    color: var(--rose);
  }

  .message-text em {
    font-style: italic;
    color: var(--soft-brown);
  }

  /* ===== COUNTDOWN ===== */
  .countdown-section {
    background: var(--dark);
    color: var(--cream);
    padding: 90px 20px;
    text-align: center;
    position: relative;
    overflow: hidden;
  }

  .countdown-section::before {
    content: '';
    position: absolute;
    inset: 0;
    background: 
      radial-gradient(circle at 50% 0%, rgba(212,175,55,0.2) 0%, transparent 70%);
  }

  .countdown-label {
    font-size: 0.75rem;
    letter-spacing: 0.55em;
    text-transform: uppercase;
    color: var(--gold-light);
    margin-bottom: 50px;
    position: relative;
  }

  .countdown-grid {
    display: flex;
    justify-content: center;
    gap: clamp(25px, 6vw, 70px);
    position: relative;
    flex-wrap: wrap;
  }

  .countdown-item {
    text-align: center;
    background: rgba(255,255,255,0.03);
    padding: 20px 25px;
    border-radius: 12px;
    border: 1px solid rgba(255,255,255,0.05);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    transition: transform 0.3s ease;
  }

  .countdown-item:hover {
    transform: translateY(-5px);
    border-color: rgba(212,175,55,0.3);
  }

  .countdown-num {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(3.5rem, 10vw, 6rem);
    font-weight: 300;
    color: var(--gold-light);
    line-height: 1;
    display: block;
    text-shadow: 0 4px 15px rgba(212,175,55,0.3);
  }

  .countdown-unit {
    font-size: 0.7rem;
    letter-spacing: 0.35em;
    text-transform: uppercase;
    color: rgba(252,249,242,0.6);
    margin-top: 12px;
  }

  .countdown-message {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(1.2rem, 3.5vw, 1.8rem);
    font-style: italic;
    color: rgba(252,249,242,0.8);
    margin-top: 60px;
    position: relative;
  }

  /* ===== LETTER ===== */
  .letter-section {
    padding: 90px 20px 80px;
    background: linear-gradient(180deg, var(--cream) 0%, #f7f1e3 50%, var(--cream) 100%);
    position: relative;
  }

  .letter-inner {
    max-width: 700px;
    margin: 0 auto;
    background: var(--glass-bg);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid var(--glass-border);
    border-radius: 16px;
    padding: clamp(40px, 8vw, 80px) clamp(30px, 6vw, 70px);
    box-shadow: var(--glass-shadow);
    position: relative;
  }

  .letter-deco {
    text-align: center;
    color: var(--gold);
    font-size: 1.2rem;
    letter-spacing: 0.6em;
    margin: 0 0 32px;
  }
  .letter-deco:last-child { margin: 32px 0 0; }

  .letter-opening {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(1.8rem, 4.5vw, 2.5rem);
    font-style: italic;
    color: var(--rose);
    margin-bottom: 32px;
  }

  .letter-body p {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(1.2rem, 3vw, 1.55rem);
    font-weight: 400;
    line-height: 1.9;
    color: #2a1e0f;
    margin-bottom: 24px;
  }

  .letter-body strong {
    color: var(--rose);
    font-weight: 600;
  }

  .letter-closing {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(1.3rem, 3.5vw, 1.8rem);
    font-style: italic;
    color: var(--soft-brown);
    margin-top: 40px !important;
  }

  .letter-closing em {
    color: var(--gold);
    font-size: 1.1em;
  }

  /* ===== FOOTER ===== */
  .footer {
    padding: 80px 20px;
    text-align: center;
  }

  .footer-heart {
    font-size: 3rem;
    display: block;
    margin-bottom: 24px;
    animation: pulse 2s ease infinite;
    filter: drop-shadow(0 0 10px rgba(226,133,110,0.4));
  }

  .footer-sig {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(1.4rem, 4.5vw, 2.2rem);
    font-style: italic;
    color: var(--soft-brown);
  }

  .footer-sub {
    font-size: 0.75rem;
    letter-spacing: 0.35em;
    text-transform: uppercase;
    color: var(--gold);
    margin-top: 16px;
  }

  /* ===== ANIMATIONS ===== */
  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(30px); }
    to { opacity: 1; transform: translateY(0); }
  }

  @keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
  }

  @keyframes pulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.15); }
  }

  /* Floating petals */
  .petal {
    position: fixed;
    font-size: 1.5rem;
    pointer-events: none;
    animation: fall linear infinite;
    opacity: 0;
    z-index: 0;
    filter: drop-shadow(0 2px 4px rgba(226,133,110,0.2));
  }

  @keyframes fall {
    0% { transform: translateY(-60px) rotate(0deg) scale(0.8); opacity: 0.8; }
    100% { transform: translateY(110vh) rotate(360deg) scale(1.2); opacity: 0; }
  }

  /* Audio Player Button */
  .audio-btn {
    position: fixed;
    bottom: 30px;
    right: 30px;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    background: var(--glass-bg);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border: 1px solid var(--glass-border);
    box-shadow: var(--glass-shadow);
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    z-index: 100;
    transition: all 0.3s ease;
    color: var(--gold);
    font-size: 1.5rem;
  }

  .audio-btn:hover {
    transform: translateY(-5px) scale(1.1);
    box-shadow: 0 12px 40px rgba(212,175,55,0.3);
    background: var(--cream);
  }

  .audio-btn.playing {
    animation: pulseAudio 2s infinite;
  }

  .audio-btn svg {
    width: 24px;
    height: 24px;
    fill: var(--gold);
  }

  @keyframes pulseAudio {
    0% { box-shadow: 0 0 0 0 rgba(212,175,55,0.4); }
    70% { box-shadow: 0 0 0 15px rgba(212,175,55,0); }
    100% { box-shadow: 0 0 0 0 rgba(212,175,55,0); }
  }

  @media (max-width: 800px) {
    .photos-grid { column-count: 2; }
  }
  @media (max-width: 500px) {
    .photos-grid { column-count: 1; }
    .audio-btn {
      bottom: 20px;
      right: 20px;
      width: 50px;
      height: 50px;
      font-size: 1.2rem;
    }
  }
</style>"""

content = content[:idx1] + new_css + content[idx2:]

# Replace the HTML part for audio right before <script>
marker1 = "</div>\r\n\r\n<script>"
marker2 = "</div>\n\n<script>"
marker3 = "</div>\n<script>"

new_html = """</div>

<audio id="bgMusic" loop>
  <source src="background-music.mp3" type="audio/mpeg">
</audio>

<!-- Audio Button -->
<div class="audio-btn" id="audioBtn" onclick="toggleAudio()">
  <span id="audioIcon">▶️</span>
</div>

<script>
  function toggleAudio() {
    const audio = document.getElementById('bgMusic');
    const btn = document.getElementById('audioBtn');
    const icon = document.getElementById('audioIcon');
    
    if (audio.paused) {
      audio.play();
      btn.classList.add('playing');
      icon.textContent = '⏸️';
    } else {
      audio.pause();
      btn.classList.remove('playing');
      icon.textContent = '▶️';
    }
  }

"""

if marker1 in content:
    content = content.replace(marker1, new_html)
elif marker2 in content:
    content = content.replace(marker2, new_html)
elif marker3 in content:
    content = content.replace(marker3, new_html)

with codecs.open(filepath, "w", "utf-8") as f:
    f.write(content)

print("Updates applied successfully.")
