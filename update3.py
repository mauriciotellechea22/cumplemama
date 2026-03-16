import sys
import re

def main():
    file_path = 'C:\\Users\\elfac\\Documents\\Cumple Mamá\\cumpleanos_mama.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Target 1: CSS insertion before </style>
    css_pattern = r"(</style>)"
    
    css_replacement = r"""  /* ===== ENVELOPE OVERLAY ===== */
  #envelopeOverlay {
    position: fixed;
    top: 0; left: 0; width: 100vw; height: 100vh;
    background: linear-gradient(135deg, #fdfbf7 0%, #f4e8d1 100%);
    z-index: 9999;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    transition: transform 1.5s cubic-bezier(0.77, 0, 0.175, 1), opacity 1.5s ease;
  }
  
  #envelopeOverlay.open {
    transform: translateY(-100vh);
    opacity: 0;
    pointer-events: none;
  }

  .envelope-container {
    position: relative;
    text-align: center;
    animation: pulseEnv 2s infinite alternate ease-in-out;
  }

  @keyframes pulseEnv {
    from { transform: scale(1); }
    to { transform: scale(1.03); }
  }

  .envelope-text {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(2.5rem, 8vw, 4rem);
    color: var(--dark);
    margin-bottom: 50px;
    letter-spacing: 0.1em;
    text-shadow: 2px 4px 12px rgba(139,98,57,0.15);
  }

  .envelope-seal {
    width: 90px;
    height: 90px;
    background: radial-gradient(circle, #b32400 0%, #801a00 100%);
    border-radius: 50%;
    margin: 0 auto;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    box-shadow: 0 6px 20px rgba(128,26,0,0.5), inset 0 2px 5px rgba(255,255,255,0.3);
    color: #f9e596;
    font-family: 'Montserrat', sans-serif;
    font-weight: 600;
    font-size: 1rem;
    text-transform: uppercase;
    letter-spacing: 0.15em;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    border: 2px solid #591200;
  }

  .envelope-seal:hover {
    transform: scale(1.15) rotate(5deg);
    box-shadow: 0 8px 25px rgba(128,26,0,0.7), inset 0 2px 5px rgba(255,255,255,0.5);
  }
\1"""
    
    if re.search(css_pattern, content):
        content = re.sub(css_pattern, css_replacement, content, count=1)
        print("CSS applied")
    else:
        print("CSS Target not found.")

    # Target 2: HTML insertion
    html_pattern = r"(<body>\s*<div class=\"page\">)"
    html_replacement = r"""<body>
<!-- ENVELOPE OVERLAY -->
<div id="envelopeOverlay">
  <div class="envelope-container">
    <h2 class="envelope-text">¡Feliz cumple Má!</h2>
    <div class="envelope-seal" onclick="openEnvelope()" title="Abrir y reproducir música">
      <span>Abrir</span>
    </div>
  </div>
</div>

<div class="page">"""
    
    if re.search(html_pattern, content):
        content = re.sub(html_pattern, html_replacement, content, count=1)
        print("HTML applied")
    else:
        print("HTML Target not found.")


    # Target 3: JS insertion
    js_pattern = r"(<script>\s*function toggleAudio\(\)\s*\{)"
    js_replacement = r"""<script>
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

  function toggleAudio() {"""
    
    if re.search(js_pattern, content):
        content = re.sub(js_pattern, js_replacement, content, count=1)
        print("JS applied")
    else:
        print("JS Target not found.")

    # Hide overflow on body initially
    body_pattern = r"(body \{[^}]*?)(overflow-x: hidden;)"
    body_replacement = r"\1overflow: hidden;"
    if re.search(body_pattern, content):
        content = re.sub(body_pattern, body_replacement, content, count=1)
        print("Body overflow hidden applied")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    main()
