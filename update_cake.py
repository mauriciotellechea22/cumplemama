import re

def main():
    file_path = 'C:\\Users\\elfac\\Documents\\Cumple Mamá\\cumpleanos_mama.html'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Insert CSS before </style>
    css_pattern = r"(</style>)"
    css_insertion = r"""
  /* ===== INTERACTIVE CAKE ===== */
  .cake-section {
    padding: 80px 20px;
    text-align: center;
    background: linear-gradient(to top, rgba(252,249,242,0.9) 0%, transparent 100%);
    display: flex;
    flex-direction: column;
    align-items: center;
    position: relative;
  }

  .cake-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(2rem, 5vw, 3rem);
    color: var(--dark);
    margin-bottom: 50px;
  }

  .cake-container {
    position: relative;
    width: 250px;
    height: 200px;
    margin: 0 auto 40px;
    display: flex;
    justify-content: center;
    align-items: flex-end;
  }

  /* The Cake Body */
  .cake-tier {
    position: absolute;
    bottom: 0;
    width: 200px;
    height: 80px;
    background: var(--cream);
    border-radius: 10px 10px 0 0;
    box-shadow: inset 0 -10px 20px rgba(139,98,57,0.1), 0 5px 15px rgba(0,0,0,0.05);
    border: 2px solid var(--gold-light);
    border-bottom: none;
  }
  
  .cake-tier::after {
    content: '';
    position: absolute;
    top: -10px; left: -2px; right: -2px; height: 20px;
    background: radial-gradient(circle at 15px 10px, var(--rose) 10px, transparent 11px) repeat-x;
    background-size: 30px 20px;
  }

  /* The Candles */
  .candles {
    position: absolute;
    bottom: 80px;
    display: flex;
    gap: 30px;
    z-index: 2;
  }

  .candle {
    width: 12px;
    height: 45px;
    background: repeating-linear-gradient(45deg, #fff, #fff 5px, var(--gold) 5px, var(--gold) 10px);
    border-radius: 3px;
    position: relative;
    box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
  }

  /* The Flames */
  .flame {
    position: absolute;
    top: -20px;
    left: 50%;
    transform: translateX(-50%);
    width: 14px;
    height: 20px;
    background: #ffaa00;
    border-radius: 50% 50% 20% 20%;
    box-shadow: 0 0 15px 5px rgba(255, 170, 0, 0.6), 0 0 30px 10px rgba(255, 100, 0, 0.4);
    animation: flicker 0.5s infinite alternate;
    transform-origin: bottom center;
    opacity: 1;
    transition: opacity 0.5s ease-out, transform 0.5s ease-out;
  }

  @keyframes flicker {
    0% { transform: translateX(-50%) scale(1) rotate(-2deg); background: #ffaa00; box-shadow: 0 0 15px 5px rgba(255, 170, 0, 0.6); }
    100% { transform: translateX(-50%) scale(1.1) rotate(2deg); background: #ffcc00; box-shadow: 0 0 20px 8px rgba(255, 204, 0, 0.8); }
  }

  /* Blown out state */
  .candle.blown-out .flame {
    opacity: 0;
    transform: translateX(-50%) scale(0) translateY(-10px);
    animation: none;
  }

  .smoke {
    position: absolute;
    top: -20px;
    left: 50%;
    width: 10px;
    height: 10px;
    background: rgba(100, 100, 100, 0.6);
    border-radius: 50%;
    opacity: 0;
    pointer-events: none;
  }

  .candle.blown-out .smoke {
    animation: smokePuff 2s ease-out forwards;
  }

  @keyframes smokePuff {
    0% { transform: translateX(-50%) scale(1) translateY(0); opacity: 0.8; }
    100% { transform: translateX(-80%) scale(4) translateY(-30px); opacity: 0; }
  }

  /* Wish Button */
  .wish-btn {
    background: var(--gold);
    color: var(--cream);
    border: none;
    padding: 15px 40px;
    font-size: 1.1rem;
    font-family: 'Montserrat', sans-serif;
    font-weight: 600;
    letter-spacing: 0.1em;
    border-radius: 30px;
    cursor: pointer;
    box-shadow: 0 4px 15px rgba(197, 155, 39, 0.4);
    transition: all 0.3s ease;
    text-transform: uppercase;
  }

  .wish-btn:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 20px rgba(197, 155, 39, 0.6);
    background: #b58d1f;
  }
  
  .wish-btn:disabled {
    background: #ccc;
    box-shadow: none;
    cursor: not-allowed;
    transform: none;
  }

  /* Granted Message */
  .wish-granted {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(2rem, 6vw, 3.5rem);
    color: var(--rose);
    margin-top: 30px;
    opacity: 0;
    transform: translateY(20px);
    transition: all 1s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    text-shadow: 0 0 15px rgba(226, 133, 110, 0.3);
  }

  .wish-granted.show {
    opacity: 1;
    transform: translateY(0);
  }
\1"""

    # 2. Insert HTML before <!-- FOOTER -->
    html_pattern = r"(<!-- FOOTER -->)"
    html_insertion = r"""  <!-- INTERACTIVE CAKE SECTION -->
  <section class="cake-section">
    <h3 class="cake-title">Un último detalle...</h3>
    
    <div class="cake-container">
      <div class="candles">
        <div class="candle"><div class="flame"></div><div class="smoke"></div></div>
        <div class="candle"><div class="flame"></div><div class="smoke"></div></div>
        <div class="candle"><div class="flame"></div><div class="smoke"></div></div>
      </div>
      <div class="cake-tier"></div>
    </div>

    <button class="wish-btn" id="wishBtn" onclick="makeWish()">Pedir un deseo</button>
    <p class="wish-granted" id="wishMsg">✨ ¡Deseo concedido! ✨</p>
  </section>

  \1"""

    # 3. Insert JS before </script>
    js_pattern = r"(</script>\s*</body>)"
    js_insertion = r"""  // Interactive Cake Logic
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
\1"""

    if re.search(css_pattern, content):
        content = re.sub(css_pattern, css_insertion, content, count=1)
        print("CSS applied")
        
    if re.search(html_pattern, content):
        content = re.sub(html_pattern, html_insertion, content, count=1)
        print("HTML applied")
        
    if re.search(js_pattern, content):
        content = re.sub(js_pattern, js_insertion, content, count=1)
        print("JS applied")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    main()
