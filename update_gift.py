import re

def main():
    file_path = 'C:\\Users\\elfac\\Documents\\Cumple Mamá\\cumpleanos_mama.html'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. CSS for 3D Gift Box and Fireworks
    css_pattern = r"(</style>)"
    css_insertion = r"""
  /* ===== 3D GIFT BOX ===== */
  .gift-section {
    padding: 60px 20px;
    text-align: center;
    background: linear-gradient(135deg, rgba(250,240,220,0.6) 0%, rgba(252,249,242,0.9) 100%);
    position: relative;
    z-index: 5;
  }
  
  .gift-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(2rem, 5vw, 3rem);
    color: var(--soft-brown);
    margin-bottom: 50px;
    font-style: italic;
  }

  .gift-container {
    perspective: 800px;
    width: 200px;
    height: 200px;
    margin: 0 auto;
    cursor: pointer;
    position: relative;
  }

  .gift-box {
    width: 150px;
    height: 150px;
    position: absolute;
    bottom: 0;
    left: 25px;
    transform-style: preserve-3d;
    transition: transform 0.5s ease;
  }

  .gift-side {
    position: absolute;
    width: 150px;
    height: 150px;
    background: linear-gradient(135deg, var(--gold) 0%, #b58d1f 100%);
    border: 2px solid #a37c15;
    box-shadow: inset 0 0 20px rgba(0,0,0,0.2);
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .gift-side::before {
    content: '';
    position: absolute;
    width: 30px;
    height: 100%;
    background: rgba(255,255,255,0.3);
  }
  .gift-side::after {
    content: '';
    position: absolute;
    width: 100%;
    height: 30px;
    background: rgba(255,255,255,0.3);
  }

  .gift-front  { transform: translateZ(75px); }
  .gift-back   { transform: rotateY(180deg) translateZ(75px); }
  .gift-right  { transform: rotateY(90deg) translateZ(75px); }
  .gift-left   { transform: rotateY(-90deg) translateZ(75px); }
  .gift-bottom { transform: rotateX(-90deg) translateZ(75px); background: #8a6c12; }

  .gift-lid {
    position: absolute;
    width: 160px;
    height: 40px;
    top: -40px;
    left: 20px;
    transform-style: preserve-3d;
    transition: transform 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    transform-origin: bottom right;
    z-index: 10;
  }

  .lid-side {
    position: absolute;
    width: 160px;
    height: 40px;
    background: linear-gradient(135deg, var(--rose) 0%, #cc6a52 100%);
    border: 1px solid #b35640;
  }
  .lid-top {
    position: absolute;
    width: 160px;
    height: 160px;
    background: var(--rose);
    transform: rotateX(90deg) translateZ(20px) translateY(-60px);
  }
  .lid-front  { transform: translateZ(80px); }
  .lid-back   { transform: rotateY(180deg) translateZ(80px); }
  .lid-right  { width: 160px; transform: rotateY(90deg) translateZ(80px); }
  .lid-left   { width: 160px; transform: rotateY(-90deg) translateZ(80px); }

  /* Animation classes */
  .gift-container:hover .gift-box { transform: rotateY(-15deg) rotateX(5deg); }
  .gift-container:hover .gift-lid { transform: translateY(-5px) rotateY(-15deg) rotateX(5deg); }
  
  .gift-container.opened .gift-lid {
    transform: rotateZ(45deg) rotateX(60deg) translateZ(50px) translateY(-100px) translateX(50px);
    opacity: 0;
  }
  .gift-container.opened .gift-box {
    transform: rotateY(-180deg);
  }

  .gift-hint {
    margin-top: 30px;
    font-size: 0.9rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--gold);
    animation: pulseEnv 2s infinite alternate;
  }

  /* Audio player waveform stub */
  .voice-controls {
    display: none;
    margin: 30px auto 0;
    align-items: center;
    justify-content: center;
    gap: 15px;
    background: var(--glass-bg);
    padding: 15px 25px;
    border-radius: 30px;
    width: max-content;
    box-shadow: var(--glass-shadow);
    opacity: 0;
    transform: translateY(20px);
    transition: all 1s ease;
  }
  .voice-controls.show {
    display: flex;
    opacity: 1;
    transform: translateY(0);
  }

  /* ===== FIREWORKS CANVAS ===== */
  #fireworksCanvas {
    position: fixed;
    top: 0; left: 0;
    width: 100vw; height: 100vh;
    pointer-events: none;
    z-index: 9998;
  }
\1"""

    # 2. HTML elements for Audio, Canvas, and Gift Box
    # Adding Audio tags just before <div class="audio-btn">
    audio_pattern = r"(<!-- Audio Button -->)"
    audio_insertion = r"""<audio id="voiceMsg">
  <source src="WhatsApp-Audio-2026-03-16-at-5.24.28-PM.mp3" type="audio/mpeg">
</audio>
<canvas id="fireworksCanvas"></canvas>

\1"""

    # 3. HTML for Gift Box (Insert before cake-section)
    gift_pattern = r"(<!-- INTERACTIVE CAKE SECTION -->)"
    gift_insertion = r"""  <!-- GIFT BOX SECTION -->
  <section class="gift-section" id="giftSection">
    <h3 class="gift-title">Tengo algo más para ti...</h3>
    
    <div class="gift-container" id="giftBox" onclick="openGift()">
      <div class="gift-box">
        <div class="gift-side gift-front"></div>
        <div class="gift-side gift-back"></div>
        <div class="gift-side gift-right"></div>
        <div class="gift-side gift-left"></div>
        <div class="gift-side gift-bottom"></div>
      </div>
      <div class="gift-lid">
        <div class="lid-top"></div>
        <div class="lid-side lid-front"></div>
        <div class="lid-side lid-back"></div>
        <div class="lid-side lid-right"></div>
        <div class="lid-side lid-left"></div>
      </div>
    </div>
    <p class="gift-hint" id="giftHint">Toca la caja</p>

    <!-- Voice controls UI that appears after opening -->
    <div class="voice-controls" id="voiceControls">
      <div class="audio-btn" style="position:relative; right:0; bottom:0; width:40px; height:40px; font-size:1rem;" onclick="toggleVoice()" id="vBtn">
        <span id="vIcon">⏸️</span>
      </div>
      <span style="font-family:'Montserrat',sans-serif; color:var(--dark); font-weight:500;">Mensaje de voz</span>
    </div>
  </section>

\1"""

    # 4. JavaScript for Logic
    js_pattern = r"(// Countdown)"
    js_insertion = r"""  // Gift Box Logic
  function openGift() {
    const box = document.getElementById('giftBox');
    const hint = document.getElementById('giftHint');
    const vControls = document.getElementById('voiceControls');
    const voiceAudio = document.getElementById('voiceMsg');
    const bgAudio = document.getElementById('bgMusic');
    const bgBtn = document.getElementById('audioBtn');
    const bgIcon = document.getElementById('audioIcon');

    if (box.classList.contains('opened')) return; // Already opened

    box.classList.add('opened');
    hint.style.display = 'none';

    // Pause Background music
    if (!bgAudio.paused) {
      bgAudio.pause();
      bgBtn.classList.remove('playing');
      bgIcon.textContent = '▶️';
    }

    // Play Voice Message
    setTimeout(() => {
      vControls.classList.add('show');
      voiceAudio.play().catch(e => console.log('Voice audio blocked', e));
      
      // Burst confetti
      for (let i = 0; i < 40; i++) {
        const p = document.createElement('div');
        p.className = 'petal';
        p.textContent = ['🎉','💖','✨','🎁'][Math.floor(Math.random() * 4)];
        p.style.left = (Math.random() * 100) + 'vw';
        p.style.top = (window.scrollY + window.innerHeight/2) + 'px';
        p.style.animationDuration = (2 + Math.random() * 3) + 's';
        p.style.fontSize = (1 + Math.random() * 1.5) + 'rem';
        document.getElementById('petals').appendChild(p);
      }
    }, 600);

    // When voice ends, switch icon back
    voiceAudio.onended = () => {
      document.getElementById('vIcon').textContent = '▶️';
    };
  }

  function toggleVoice() {
    const voiceAudio = document.getElementById('voiceMsg');
    const vIcon = document.getElementById('vIcon');
    const bgAudio = document.getElementById('bgMusic');
    
    if (voiceAudio.paused) {
        // Pause bg if playing
        if(!bgAudio.paused) toggleAudio();
        voiceAudio.play();
        vIcon.textContent = '⏸️';
    } else {
        voiceAudio.pause();
        vIcon.textContent = '▶️';
    }
  }

  // Simple Fireworks Canvas Setup
  const canvas = document.getElementById('fireworksCanvas');
  const ctx = canvas.getContext('2d');
  let fireworks = [];
  let particles = [];
  
  function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  }
  window.addEventListener('resize', resizeCanvas);
  resizeCanvas();

  function fireworkLoop() {
    requestAnimationFrame(fireworkLoop);
    ctx.globalCompositeOperation = 'destination-out';
    ctx.fillStyle = 'rgba(0, 0, 0, 0.1)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.globalCompositeOperation = 'lighter';

    // Draw fireworks
    if(Math.random() < 0.05 && fireworks.length < 5) { // Spawn rate
        fireworks.push(new Firework());
    }

    fireworks.forEach((fw, i) => {
        fw.update();
        fw.draw();
        if(fw.exploded) fireworks.splice(i, 1);
    });

    particles.forEach((p, i) => {
        p.update();
        p.draw();
        if(p.alpha <= 0) particles.splice(i, 1);
    });
  }

  class Firework {
      constructor() {
          this.x = Math.random() * canvas.width;
          this.y = canvas.height;
          this.targetY = canvas.height * 0.2 + Math.random() * (canvas.height * 0.3);
          this.speed = 3 + Math.random() * 3;
          this.exploded = false;
          this.color = `hsl(${Math.random() * 60 + 10}, 100%, 60%)`; // Gold/Red hues
      }
      update() {
          this.y -= this.speed;
          if(this.y <= this.targetY) {
              this.exploded = true;
              this.explode();
          }
      }
      draw() {
          ctx.beginPath();
          ctx.arc(this.x, this.y, 2, 0, Math.PI * 2);
          ctx.fillStyle = this.color;
          ctx.fill();
      }
      explode() {
          for(let i=0; i<30; i++) {
              particles.push(new Particle(this.x, this.y, this.color));
          }
      }
  }

  class Particle {
      constructor(x, y, color) {
          this.x = x;
          this.y = y;
          this.color = color;
          const angle = Math.random() * Math.PI * 2;
          const velocity = Math.random() * 5 + 2;
          this.vx = Math.cos(angle) * velocity;
          this.vy = Math.sin(angle) * velocity;
          this.alpha = 1;
          this.decay = Math.random() * 0.02 + 0.01;
      }
      update() {
          this.x += this.vx;
          this.y += this.vy;
          this.vy += 0.1; // gravity
          this.alpha -= this.decay;
      }
      draw() {
          ctx.globalAlpha = Math.max(0, this.alpha);
          ctx.beginPath();
          ctx.arc(this.x, this.y, 1.5, 0, Math.PI * 2);
          ctx.fillStyle = this.color;
          ctx.fill();
          ctx.globalAlpha = 1;
      }
  }

  \1"""

    # 5. Patch existing countdown logic
    countdown_pattern = r"(const diff = target - now;\s*if \(diff <= 0\) \{[a-zA-Z0-9\s=\.^\>\\\'\"\;\<\/\-\(\)]+?)(return;)"
    
    countdown_replacement = r"""\1
      // Start fireworks if not running
      if(canvas.style.display !== 'block') {
         canvas.style.display = 'block';
         fireworkLoop();
      }
      return;"""

    if re.search(css_pattern, content):
        content = re.sub(css_pattern, css_insertion, content, count=1)
        print("CSS applied")
        
    if re.search(audio_pattern, content):
        content = re.sub(audio_pattern, audio_insertion, content, count=1)
        print("Audio HTML applied")
        
    if re.search(gift_pattern, content):
        content = re.sub(gift_pattern, gift_insertion, content, count=1)
        print("Gift HTML applied")

    if re.search(js_pattern, content):
        content = re.sub(js_pattern, js_insertion, content, count=1)
        print("JS Functions applied")

    if re.search(countdown_pattern, content):
        content = re.sub(countdown_pattern, countdown_replacement, content, count=1)
        print("JS Countdown patched")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    main()
