import re

def main():
    file_path = 'C:\\Users\\elfac\\Documents\\Cumple Mamá\\cumpleanos_mama.html'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # We will replace everything from <script> to </script> with a clean version
    script_pattern = r"(<script>)([\s\S]*?)(</script>)"
    
    clean_script = r"""<script>
  // Envelope Logic
  function openEnvelope() {
    const envelope = document.getElementById('envelopeOverlay');
    const audio = document.getElementById('bgMusic');
    const btn = document.getElementById('audioBtn');
    const icon = document.getElementById('audioIcon');
    
    // Play audio safely within user interaction context
    let playPromise = audio.play();
    if (playPromise !== undefined) {
      playPromise.then(_ => {
        btn.classList.add('playing');
        icon.textContent = '⏸️';
      }).catch(e => {
        console.log('Audio autoplay prevented:', e);
      });
    }

    // Trigger opening animation
    envelope.classList.add('open');
    
    // Hide overlay entirely after animation finishes
    setTimeout(() => {
      envelope.style.display = 'none';
      document.body.style.overflow = 'auto'; // allow scrolling again
    }, 1500);
  }

  // Background Audio Toggle
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

  // Gift Box Logic
  function openGift() {
    const box = document.getElementById('giftBox');
    const hint = document.getElementById('giftHint');
    const vControls = document.getElementById('voiceControls');
    const voiceAudio = document.getElementById('voiceMsg');
    const bgAudio = document.getElementById('bgMusic');
    const bgBtn = document.getElementById('audioBtn');
    const bgIcon = document.getElementById('audioIcon');

    if (!box) return;
    if (box.classList.contains('opened')) return; // Already opened

    box.classList.add('opened');
    if(hint) hint.style.display = 'none';

    // Pause Background music
    if (bgAudio && !bgAudio.paused) {
      bgAudio.pause();
      if(bgBtn) bgBtn.classList.remove('playing');
      if(bgIcon) bgIcon.textContent = '▶️';
    }

    // Play Voice Message
    setTimeout(() => {
      if(vControls) vControls.classList.add('show');
      if(voiceAudio) {
          document.getElementById('vIcon').textContent = '⏸️';
          let playPromise = voiceAudio.play();
          if (playPromise !== undefined) {
              playPromise.then(_ => {
                  console.log("Audio playing successfully");
              })
              .catch(error => {
                  console.log("Autoplay prevented or audio load error:", error);
                  document.getElementById('vIcon').textContent = '▶️';
              });
          }
          
          voiceAudio.onended = () => {
            document.getElementById('vIcon').textContent = '▶️';
          };
      }
      
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
  }

  // Voice Controls Toggle
  function toggleVoice() {
    const voiceAudio = document.getElementById('voiceMsg');
    const vIcon = document.getElementById('vIcon');
    const bgAudio = document.getElementById('bgMusic');
    
    if (voiceAudio && voiceAudio.paused) {
        if(bgAudio && !bgAudio.paused) toggleAudio();
        voiceAudio.play();
        if(vIcon) vIcon.textContent = '⏸️';
    } else if(voiceAudio) {
        voiceAudio.pause();
        if(vIcon) vIcon.textContent = '▶️';
    }
  }

  // Floating petals background
  const petalEmojis = ['🌸','🌺','✿','❀','🌼'];
  const container = document.getElementById('petals');
  for (let i = 0; i < 15; i++) {
    const p = document.createElement('div');
    p.className = 'petal';
    p.textContent = petalEmojis[Math.floor(Math.random() * petalEmojis.length)];
    p.style.left = Math.random() * 100 + 'vw';
    p.style.animationDuration = (8 + Math.random() * 12) + 's';
    p.style.animationDelay = (Math.random() * 10) + 's';
    p.style.fontSize = (0.8 + Math.random() * 1) + 'rem';
    container.appendChild(p);
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

  // Countdown to March 30, 2026 (Uruguay time = UTC-3)
  function updateCountdown() {
    const target = new Date('2026-03-30T00:00:00-03:00');
    const now = new Date();
    const diff = target - now;
    if (diff <= 0) {
      document.getElementById('countdown').innerHTML = '<p style="font-family:Cormorant Garamond,serif;font-size:2rem;color:var(--gold-light);font-style:italic">¡Ya llegó el día! 🎉</p>';
      
      // Start fireworks if not running
      if(canvas.style.display !== 'block') {
         canvas.style.display = 'block';
         fireworkLoop();
      }
      return;
    }
    const days = Math.floor(diff / 86400000);
    const hours = Math.floor((diff % 86400000) / 3600000);
    const mins = Math.floor((diff % 3600000) / 60000);
    const secs = Math.floor((diff % 60000) / 1000);
    document.getElementById('cd-days').textContent = String(days).padStart(2,'0');
    document.getElementById('cd-hours').textContent = String(hours).padStart(2,'0');
    document.getElementById('cd-mins').textContent = String(mins).padStart(2,'0');
    document.getElementById('cd-secs').textContent = String(secs).padStart(2,'0');
  }
  updateCountdown();
  setInterval(updateCountdown, 1000);

  // Interactive Cake Logic
  function makeWish() {
    const btn = document.getElementById('wishBtn');
    const msg = document.getElementById('wishMsg');
    const candles = document.querySelectorAll('.candle');

    // Disable button to prevent spamming
    btn.disabled = true;
    btn.textContent = "Soplando...";

    // Blow out candles with a slight stagger
    candles.forEach((candle, index) => {
      setTimeout(() => {
        candle.classList.add('blown-out');
      }, index * 200 + 100);
    });

    // Show granted message after candles are out
    setTimeout(() => {
      btn.style.display = 'none';
      msg.classList.add('show');
      
      // Optional: Add a burst of petals here if desired
      for (let i = 0; i < 20; i++) {
        const p = document.createElement('div');
        p.className = 'petal';
        p.textContent = '✨';
        p.style.left = Math.random() * 100 + 'vw';
        p.style.top = (window.scrollY + window.innerHeight / 2) + 'px';
        p.style.animationDuration = (3 + Math.random() * 5) + 's';
        p.style.fontSize = (1 + Math.random() * 1) + 'rem';
        p.style.opacity = Math.random();
        document.getElementById('petals').appendChild(p);
      }
    }, 1000);
  }
</script>"""

    if re.search(script_pattern, content):
        content = re.sub(script_pattern, clean_script, content, count=1)
        print("Script block successfully replaced and syntax fixed")
    else:
        print("Script block not found")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    main()
