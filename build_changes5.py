import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove countdown section
html = re.sub(r'<!-- Countdown Section -->\s*<section id="countdown".*?</section>', '', html, flags=re.DOTALL)

# 2. Replace Hero HTML
hero_html = """
        <div class="container hero-content">
            <div style="display:flex; flex-direction:column; align-items:flex-start;" class="reveal-element">
                <div class="hero-interactive-ddlc">
                    <div class="ddlc-letters">
                        <div class="ddlc-letter-container">
                            <span class="ddlc-letter">D</span>
                            <span class="ddlc-tooltip">Data</span>
                        </div>
                        <div class="ddlc-letter-container">
                            <span class="ddlc-letter">D</span>
                            <span class="ddlc-tooltip">Driven</span>
                        </div>
                        <div class="ddlc-letter-container">
                            <span class="ddlc-letter">L</span>
                            <span class="ddlc-tooltip">Logic</span>
                        </div>
                        <div class="ddlc-letter-container">
                            <span class="ddlc-letter">C</span>
                            <span class="ddlc-tooltip">Controllers</span>
                        </div>
                    </div>
                    <div class="hero-full-form" style="opacity: 1; margin-top: 0.5rem; margin-bottom: 0.5rem;">
                        Data Driven Logic Controllers
                    </div>
                    <div class="hero-interactive-subtitle" style="opacity: 1;">
                        The intelligent edge for modern automation.
                    </div>
                </div>
            </div>

            <div class="hero-visual-right reveal-element">
                <img src="https://ddlc-website-ecru.vercel.app/ddlc__1_.png" alt="DDLC Hardware" class="hero-product-img" style="animation: heroFloat 6s ease-in-out infinite; filter: drop-shadow(0 20px 40px rgba(0,0,0,0.15));">
            </div>
        </div>
"""
html = re.sub(r'<div class="container hero-content">.*?</div>\s*</section>', hero_html + '\n    </section>', html, flags=re.DOTALL)

# 3. Clean up JS: Remove Typewriter, Countdown, Particles
js_start = html.find('// 1. Particles')
js_end = html.find('// 3D Card Tilt Effect')
if js_start != -1 and js_end != -1:
    new_js = """
            const heroImg = document.querySelector('.hero-product-img');
            if(heroImg) {
                anime({
                    targets: heroImg,
                    translateX: [80, 0],
                    opacity: [0, 1],
                    delay: 250,
                    duration: 1000,
                    easing: 'easeOutExpo'
                });
            }

            """
    html = html[:js_start] + new_js + html[js_end:]

# 4. Remove hero-particles div and cursor glow div from HTML
html = re.sub(r'<div class="hero-particles"></div>', '', html)
html = re.sub(r'<div id="heroCursorGlow".*?</div>', '', html)

# 5. Add float keyframes if not exists
float_css = """
        @keyframes heroFloat {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-15px); }
            100% { transform: translateY(0px); }
        }
"""
if "@keyframes heroFloat" not in html:
    html = html.replace("/* Utilities */", float_css + "\n        /* Utilities */")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
