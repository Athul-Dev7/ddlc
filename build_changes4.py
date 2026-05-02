import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Particles
particles_css = """
        /* Particles */
        .hero-particles {
            position: absolute;
            inset: 0;
            z-index: 0;
            pointer-events: none;
            overflow: hidden;
        }
        .particle {
            position: absolute;
            background: rgba(34,197,94,0.15);
            border-radius: 50%;
            animation: floatParticle linear infinite;
        }
        @keyframes floatParticle {
            0% { transform: translateY(100vh) scale(0); opacity: 0; }
            10% { opacity: 1; transform: translateY(50vh) scale(1); }
            90% { opacity: 1; transform: translateY(-50px) scale(1.5); }
            100% { transform: translateY(-100px) scale(2); opacity: 0; }
        }
"""
if "/* Particles */" not in html:
    html = html.replace('/* UNIQUE MODERN HERO SECTION */', particles_css + '\n        /* UNIQUE MODERN HERO SECTION */')

# Insert particles div
particles_html = '\n    <div class="hero-particles"></div>\n'
if '<div class="hero-particles">' not in html:
    html = html.replace('<section id="home" class="hero">', '<section id="home" class="hero">' + particles_html)

# 2. Typewriter Effect HTML & Cursor
typewriter_css = """
        .typewriter-cursor {
            font-weight: 800;
            color: #22c55e;
            animation: blinkCursor 0.7s step-end infinite;
        }
        @keyframes blinkCursor {
            0%, 100% { opacity: 1; }
            50% { opacity: 0; }
        }
"""
if ".typewriter-cursor" not in html:
    html = html.replace('/* Layout */', typewriter_css + '\n        /* Layout */')

# Waitlist HTML
waitlist_html = """
                    <div class="hero-waitlist" style="margin-top: 2rem; opacity: 0; transform: translateY(20px);">
                        <form onsubmit="event.preventDefault(); document.getElementById('waitlist-container').innerHTML='<div style=\\'color:#22c55e; font-weight:600; font-size: 1.1rem;\\'>Request received. We\\'ll be in touch shortly.</div>';">
                            <div id="waitlist-container">
                                <div style="display:flex; gap:1rem; flex-wrap: wrap;">
                                    <input type="email" placeholder="Enter your work email" required style="padding: 1.125rem 1.5rem; border: 1px solid var(--border-color); border-radius: 12px; font-family: var(--font-body); width: 100%; max-width: 300px; font-size: 1rem; background: rgba(255,255,255,0.9);">
                                    <button type="submit" class="btn" style="box-shadow: 0 8px 24px rgba(34,197,94,0.2);">Request Early Access &rarr;</button>
                                </div>
                                <div style="font-family: 'DM Mono', monospace; font-size: 0.85rem; color: var(--gray-text); margin-top: 0.75rem;">Limited to first 50 industrial partners.</div>
                            </div>
                        </form>
                    </div>
"""

# Re-write the hero interactive text structure
hero_interactive = """
                <div class="hero-interactive-ddlc" style="min-height: 250px;">
                    <div class="ddlc-letters" id="hero-title"></div>
                    <div class="hero-full-form" id="hero-fullform" style="opacity:0;">Data Driven Logic Controllers</div>
                    <div class="hero-interactive-subtitle" id="hero-subtitle" style="font-size:1.15rem; font-weight:600; margin-top:0.5rem;"></div>
                    <div class="hero-desc" id="hero-desc" style="opacity:0; margin-top:1.5rem; font-size:1.05rem; color:var(--gray-text); line-height:1.6;">
                        Lab-proven DDLC modules sit at the intersection of AI vision and hardcore mechanical control, engineered to deliver unparalleled inline inspection capabilities.
                    </div>
                    """ + waitlist_html + """
                </div>
"""

# Replace the current hero text
if 'hero-waitlist' not in html:
    html = re.sub(r'<div class="hero-interactive-ddlc">.*?</div>\s*</div>', hero_interactive + '</div>', html, flags=re.DOTALL)


# 3. Marquee
marquee_css = """
        .marquee-wrapper {
            width: 100%;
            overflow: hidden;
            background: var(--pure-white);
            border-top: 1px solid rgba(34,197,94,0.1);
            border-bottom: 1px solid rgba(34,197,94,0.1);
            padding: 1rem 0;
            white-space: nowrap;
            position: relative;
        }
        .marquee-content {
            display: inline-block;
            animation: marquee 20s linear infinite;
            font-family: 'DM Mono', monospace;
            font-size: 0.9rem;
            color: #22c55e;
            text-transform: uppercase;
            letter-spacing: 0.1em;
        }
        @keyframes marquee {
            0% { transform: translateX(0); }
            100% { transform: translateX(-50%); }
        }
"""
if ".marquee-wrapper" not in html:
    html = html.replace('/* Navigation */', marquee_css + '\n        /* Navigation */')

marquee_html = """
    <!-- Marquee -->
    <div class="marquee-wrapper">
        <div class="marquee-content">
            LAUNCH READY &middot; LAB PROVEN &middot; EARLY ACCESS OPEN &middot; 50 SLOTS AVAILABLE &middot; DDLC v2.0 &middot; INTELLIGENT EDGE &middot; ZERO LATENCY &middot; LAUNCH READY &middot; LAB PROVEN &middot; EARLY ACCESS OPEN &middot; 50 SLOTS AVAILABLE &middot; DDLC v2.0 &middot; INTELLIGENT EDGE &middot; ZERO LATENCY &middot; 
        </div>
    </div>
"""


# 4. Animated Underline for Section Headings
underline_css = """
        .large-heading {
            position: relative;
            display: inline-block;
            padding-bottom: 0.5rem;
        }
        .heading-underline {
            position: absolute;
            bottom: 0;
            left: 0;
            height: 3px;
            background: #22c55e;
            width: 0;
            border-radius: 2px;
        }
"""
if ".heading-underline" not in html:
    html = html.replace('.large-heading {', underline_css + '\n        .large-heading {')
    html = re.sub(r'(<h2 class="large-heading"[^>]*>)(.*?)(</h2>)', r'\1\2<span class="heading-underline"></span>\3', html)
    html = re.sub(r'(<h3 class="large-heading"[^>]*>)(.*?)(</h3>)', r'\1\2<span class="heading-underline"></span>\3', html)

# 5. Image Reveal Overlay
reveal_css = """
        .reveal-image-container {
            position: relative;
            overflow: hidden;
            display: inline-block;
        }
        .reveal-overlay {
            position: absolute;
            inset: 0;
            background: #22c55e;
            z-index: 2;
            clip-path: inset(0 0 0 0);
        }
"""
if ".reveal-image-container" not in html:
    html = html.replace('/* Utilities */', reveal_css + '\n        /* Utilities */')
    html = re.sub(r'(<img src="[^"]+" alt="[^"]+" class="rounded-24 branded-img"[^>]*>)', r'<div class="reveal-image-container">\1<div class="reveal-overlay"></div></div>', html)


# 6. Countdown HTML
countdown_html = """
    <!-- Countdown Section -->
    <section id="countdown" class="section reveal-section" style="background-color: #f7f9f7; padding: 4rem 2rem; text-align: center;">
        <div class="container">
            <span class="section-label" style="color: #22c55e;">COMMERCIAL LAUNCH</span>
            <h2 class="large-heading" style="margin-bottom: 3rem;">DDLC launches in<span class="heading-underline"></span></h2>
            
            <div style="display: flex; justify-content: center; gap: 2rem; flex-wrap: wrap;" class="countdown-grid">
                <div class="countdown-box" style="background: rgba(255,255,255,0.75); backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px); border: 1px solid rgba(34,197,94,0.15); border-radius: 16px; padding: 1.5rem; min-width: 140px; box-shadow: 0 10px 30px rgba(0,0,0,0.02);">
                    <div id="cd-days" style="font-family: var(--font-display); font-size: 3.5rem; font-weight: 700; color: #22c55e; line-height: 1;">00</div>
                    <div style="font-family: 'DM Mono', monospace; font-size: 0.9rem; color: var(--gray-text); margin-top: 0.5rem; text-transform: uppercase;">Days</div>
                </div>
                <div class="countdown-box" style="background: rgba(255,255,255,0.75); backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px); border: 1px solid rgba(34,197,94,0.15); border-radius: 16px; padding: 1.5rem; min-width: 140px; box-shadow: 0 10px 30px rgba(0,0,0,0.02);">
                    <div id="cd-hours" style="font-family: var(--font-display); font-size: 3.5rem; font-weight: 700; color: #22c55e; line-height: 1;">00</div>
                    <div style="font-family: 'DM Mono', monospace; font-size: 0.9rem; color: var(--gray-text); margin-top: 0.5rem; text-transform: uppercase;">Hours</div>
                </div>
                <div class="countdown-box" style="background: rgba(255,255,255,0.75); backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px); border: 1px solid rgba(34,197,94,0.15); border-radius: 16px; padding: 1.5rem; min-width: 140px; box-shadow: 0 10px 30px rgba(0,0,0,0.02);">
                    <div id="cd-minutes" style="font-family: var(--font-display); font-size: 3.5rem; font-weight: 700; color: #22c55e; line-height: 1;">00</div>
                    <div style="font-family: 'DM Mono', monospace; font-size: 0.9rem; color: var(--gray-text); margin-top: 0.5rem; text-transform: uppercase;">Minutes</div>
                </div>
                <div class="countdown-box" style="background: rgba(255,255,255,0.75); backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px); border: 1px solid rgba(34,197,94,0.15); border-radius: 16px; padding: 1.5rem; min-width: 140px; box-shadow: 0 10px 30px rgba(0,0,0,0.02);">
                    <div id="cd-seconds" style="font-family: var(--font-display); font-size: 3.5rem; font-weight: 700; color: #22c55e; line-height: 1;">00</div>
                    <div style="font-family: 'DM Mono', monospace; font-size: 0.9rem; color: var(--gray-text); margin-top: 0.5rem; text-transform: uppercase;">Seconds</div>
                </div>
            </div>
        </div>
    </section>
"""

# Replace stats bar with new structure
stats_html = """
    <!-- Stats Bar -->
    <section class="stats-bar reveal-section" style="width: 100%; background-color: #ffffff; padding: 4rem 2rem; border-bottom: 1px solid rgba(34,197,94,0.12);">
        <div class="container">
            <div class="stats-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 2rem;">
                <div class="stat-card" style="background: rgba(255,255,255,0.6); backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px); border: 1px solid rgba(255,255,255,0.5); border-radius: 16px; padding: 1.5rem 2rem; box-shadow: 0 8px 32px rgba(34,197,94,0.06); text-align: center; position: relative;">
                    <div class="anime-stat" data-target="50" style="font-family: var(--font-display); font-size: 3.5rem; font-weight: 700; color: #22c55e; line-height: 1;">0</div>
                    <div style="font-family: 'DM Mono', monospace; font-size: 0.8rem; color: var(--gray-text); text-transform: uppercase; letter-spacing: 0.1em; margin-top: 0.5rem;">Early Access Slots</div>
                    <div class="stat-divider" style="position: absolute; right: -1rem; top: 20%; bottom: 20%; width: 1px; background: rgba(34,197,94,0.2);"></div>
                </div>
                <div class="stat-card" style="background: rgba(255,255,255,0.6); backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px); border: 1px solid rgba(255,255,255,0.5); border-radius: 16px; padding: 1.5rem 2rem; box-shadow: 0 8px 32px rgba(34,197,94,0.06); text-align: center; position: relative;">
                    <div class="anime-stat" data-target="12" data-suffix="ms" style="font-family: var(--font-display); font-size: 3.5rem; font-weight: 700; color: #22c55e; line-height: 1;">0<span style="font-size: 2rem;">ms</span></div>
                    <div style="font-family: 'DM Mono', monospace; font-size: 0.8rem; color: var(--gray-text); text-transform: uppercase; letter-spacing: 0.1em; margin-top: 0.5rem;">Target Inference Speed</div>
                    <div class="stat-divider" style="position: absolute; right: -1rem; top: 20%; bottom: 20%; width: 1px; background: rgba(34,197,94,0.2);"></div>
                </div>
                <div class="stat-card" style="background: rgba(255,255,255,0.6); backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px); border: 1px solid rgba(255,255,255,0.5); border-radius: 16px; padding: 1.5rem 2rem; box-shadow: 0 8px 32px rgba(34,197,94,0.06); text-align: center; position: relative;">
                    <div class="anime-stat" data-target="99.7" data-suffix="%" style="font-family: var(--font-display); font-size: 3.5rem; font-weight: 700; color: #22c55e; line-height: 1;">0<span style="font-size: 2rem;">%</span></div>
                    <div style="font-family: 'DM Mono', monospace; font-size: 0.8rem; color: var(--gray-text); text-transform: uppercase; letter-spacing: 0.1em; margin-top: 0.5rem;">Lab Accuracy Rate</div>
                    <div class="stat-divider" style="position: absolute; right: -1rem; top: 20%; bottom: 20%; width: 1px; background: rgba(34,197,94,0.2);"></div>
                </div>
                <div class="stat-card" style="background: rgba(255,255,255,0.6); backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px); border: 1px solid rgba(255,255,255,0.5); border-radius: 16px; padding: 1.5rem 2rem; box-shadow: 0 8px 32px rgba(34,197,94,0.06); text-align: center;">
                    <div style="font-family: var(--font-display); font-size: 3.5rem; font-weight: 700; color: #22c55e; line-height: 1;" class="anime-text-reveal">Q3 2025</div>
                    <div style="font-family: 'DM Mono', monospace; font-size: 0.8rem; color: var(--gray-text); text-transform: uppercase; letter-spacing: 0.1em; margin-top: 0.5rem;">Commercial Launch</div>
                </div>
            </div>
            <style>
                @media (max-width: 768px) {
                    .stat-divider { display: none !important; }
                }
            </style>
        </div>
    </section>
"""

if 'id="countdown"' not in html:
    html = re.sub(r'<section class="stats-bar.*?</section>', countdown_html + '\n' + stats_html, html, flags=re.DOTALL)

# Insert Marquee
if "marquee-wrapper" not in html:
    html = html.replace('<!-- Platform Understanding -->', marquee_html + '\n    <!-- Platform Understanding -->')

# 7. Update JS
new_js = """
    <!-- Interactive Scripts -->
    <script>
        document.addEventListener("DOMContentLoaded", () => {
            document.body.classList.add('loaded');

            // 1. Particles
            const particlesContainer = document.querySelector('.hero-particles');
            for(let i=0; i<20; i++) {
                const p = document.createElement('div');
                p.classList.add('particle');
                const size = Math.random() * 8 + 4;
                p.style.width = size + 'px';
                p.style.height = size + 'px';
                p.style.left = Math.random() * 100 + '%';
                p.style.top = Math.random() * 100 + '%';
                p.style.animationDuration = (Math.random() * 10 + 10) + 's';
                p.style.animationDelay = (Math.random() * 5) + 's';
                if (particlesContainer) particlesContainer.appendChild(p);
            }

            // 2. Typewriter Effect
            const titleEl = document.getElementById('hero-title');
            const fullformEl = document.getElementById('hero-fullform');
            const subtitleEl = document.getElementById('hero-subtitle');
            const descEl = document.getElementById('hero-desc');
            const waitlistEl = document.querySelector('.hero-waitlist');
            const heroImg = document.querySelector('.hero-product-img');
            
            const titleText = "DDLC";
            const subtitleText = "The intelligent edge for modern automation.";
            
            let cursorHtml = '<span class="typewriter-cursor">|</span>';
            
            // Step 1
            let titleIdx = 0;
            function typeTitle() {
                if(!titleEl) return;
                if (titleIdx < titleText.length) {
                    titleEl.innerHTML = titleText.substring(0, titleIdx + 1) + cursorHtml;
                    titleIdx++;
                    setTimeout(typeTitle, 120);
                } else {
                    // Blinks 3 times (approx 2100ms)
                    setTimeout(() => {
                        titleEl.innerHTML = titleText; // remove cursor
                        // Step 2
                        if(fullformEl) {
                            anime({
                                targets: fullformEl,
                                opacity: [0, 1],
                                translateY: [10, 0],
                                duration: 400,
                                easing: 'easeOutQuad',
                                complete: () => {
                                    // Step 3
                                    let subIdx = 0;
                                    function typeSubtitle() {
                                        if(!subtitleEl) return;
                                        if (subIdx < subtitleText.length) {
                                            subtitleEl.innerHTML = subtitleText.substring(0, subIdx + 1) + cursorHtml;
                                            subIdx++;
                                            setTimeout(typeSubtitle, 35);
                                        } else {
                                            setTimeout(() => {
                                                subtitleEl.innerHTML = subtitleText;
                                                // Step 4
                                                if(descEl) {
                                                    anime({
                                                        targets: descEl,
                                                        opacity: [0, 1],
                                                        duration: 400,
                                                        easing: 'easeOutQuad'
                                                    });
                                                }
                                                if(waitlistEl) {
                                                    anime({
                                                        targets: waitlistEl,
                                                        opacity: [0, 1],
                                                        translateY: [20, 0],
                                                        delay: 400,
                                                        duration: 600,
                                                        easing: 'easeOutQuad'
                                                    });
                                                }
                                            }, 1000);
                                        }
                                    }
                                    typeSubtitle();
                                }
                            });
                        }
                    }, 2100);
                }
            }
            if(titleEl) {
                // initial cursor blink
                titleEl.innerHTML = cursorHtml;
                setTimeout(typeTitle, 500);
            }

            // Hero Image
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

            // Countdown Logic
            const cdDays = document.getElementById('cd-days');
            const cdHours = document.getElementById('cd-hours');
            const cdMins = document.getElementById('cd-minutes');
            const cdSecs = document.getElementById('cd-seconds');
            
            const targetDate = new Date(Date.now() + 90 * 24 * 60 * 60 * 1000);
            
            function updateCountdown() {
                const now = new Date();
                const diff = targetDate - now;
                if(diff <= 0) return;
                
                const d = Math.floor(diff / (1000 * 60 * 60 * 24));
                const h = Math.floor((diff / (1000 * 60 * 60)) % 24);
                const m = Math.floor((diff / 1000 / 60) % 60);
                const s = Math.floor((diff / 1000) % 60);
                
                if(cdDays) cdDays.textContent = d.toString().padStart(2, '0');
                if(cdHours) cdHours.textContent = h.toString().padStart(2, '0');
                if(cdMins) cdMins.textContent = m.toString().padStart(2, '0');
                if(cdSecs) cdSecs.textContent = s.toString().padStart(2, '0');
            }
            updateCountdown();
            setInterval(updateCountdown, 1000);

            // 3D Card Tilt Effect
            document.querySelectorAll('.module-card').forEach(card => {
                card.addEventListener('mousemove', e => {
                    const rect = card.getBoundingClientRect();
                    const x = e.clientX - rect.left;
                    const y = e.clientY - rect.top;
                    const centerX = rect.width / 2;
                    const centerY = rect.height / 2;
                    
                    const rotateX = ((y - centerY) / centerY) * -5;
                    const rotateY = ((x - centerX) / centerX) * 5;
                    
                    card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-4px)`;
                    card.style.transition = 'none';
                });
                card.addEventListener('mouseleave', () => {
                    card.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) translateY(0)';
                    card.style.transition = 'transform 0.3s ease';
                });
            });

            // Intersection Observer for scroll animations
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const el = entry.target;
                        
                        // Section Headings
                        if(el.classList.contains('large-heading') && !el.classList.contains('animated')) {
                            el.classList.add('animated');
                            anime({
                                targets: el,
                                opacity: [0, 1],
                                translateY: [25, 0],
                                duration: 550,
                                easing: 'easeOutQuad'
                            });
                            // Underline
                            const underline = el.querySelector('.heading-underline');
                            if(underline) {
                                anime({
                                    targets: underline,
                                    width: [0, 60],
                                    duration: 600,
                                    easing: 'easeOutQuad'
                                });
                            }
                        }

                        // Countdown boxes
                        if(el.classList.contains('countdown-grid') && !el.classList.contains('animated')) {
                            el.classList.add('animated');
                            anime({
                                targets: el.querySelectorAll('.countdown-box'),
                                translateY: [30, 0],
                                opacity: [0, 1],
                                delay: anime.stagger(120),
                                easing: 'easeOutQuad',
                                duration: 800
                            });
                        }

                        // Stats count up with slot machine effect
                        if(el.classList.contains('stats-grid') && !el.classList.contains('animated')) {
                            el.classList.add('animated');
                            const statEls = el.querySelectorAll('.anime-stat');
                            statEls.forEach((statEl, i) => {
                                const finalVal = parseFloat(statEl.getAttribute('data-target'));
                                const isFloat = finalVal % 1 !== 0;
                                const suffix = statEl.getAttribute('data-suffix') || '';
                                
                                // Slot machine effect
                                let obj = { val: 0 };
                                anime({
                                    targets: obj,
                                    val: finalVal,
                                    round: isFloat ? 10 : 1,
                                    duration: 2000,
                                    delay: i * 150,
                                    easing: 'easeOutExpo',
                                    update: function() {
                                        // add random noise while updating
                                        let displayVal = obj.val;
                                        if(obj.val < finalVal * 0.9) {
                                            displayVal = Math.random() * finalVal;
                                        }
                                        displayVal = isFloat ? displayVal.toFixed(1) : Math.floor(displayVal);
                                        statEl.innerHTML = displayVal + `<span style="font-size: 2rem;">${suffix}</span>`;
                                    },
                                    complete: function() {
                                        statEl.innerHTML = (isFloat ? finalVal.toFixed(1) : finalVal) + `<span style="font-size: 2rem;">${suffix}</span>`;
                                    }
                                });
                            });
                        }

                        // Card grids
                        if(el.classList.contains('grid-3') && !el.classList.contains('animated')) {
                            el.classList.add('animated');
                            anime({
                                targets: el.querySelectorAll('.module-card'),
                                translateY: [35, 0],
                                opacity: [0, 1],
                                delay: anime.stagger(130),
                                duration: 800,
                                easing: 'easeOutQuad'
                            });
                        }

                        // Image reveals
                        if(el.classList.contains('reveal-image-container') && !el.classList.contains('animated')) {
                            el.classList.add('animated');
                            const img = el.querySelector('img');
                            const overlay = el.querySelector('.reveal-overlay');
                            
                            anime({
                                targets: overlay,
                                clipPath: ['inset(0 0 0 0)', 'inset(0 100% 0 0)'],
                                duration: 800,
                                easing: 'easeInOutQuart'
                            });
                            
                            anime({
                                targets: img,
                                opacity: [0, 1],
                                scale: [1.1, 1],
                                duration: 1200,
                                easing: 'easeOutQuart'
                            });
                        }
                        
                        // Deploy steps
                        if(el.classList.contains('timeline-wrapper') && !el.classList.contains('animated')) {
                            el.classList.add('animated');
                            anime({
                                targets: el.querySelectorAll('.timeline-item'),
                                translateX: [-25, 0],
                                opacity: [0, 1],
                                delay: anime.stagger(180),
                                duration: 800,
                                easing: 'easeOutQuad'
                            });
                        }

                        // Section labels
                        if(el.classList.contains('section-label') && !el.classList.contains('animated')) {
                            el.classList.add('animated');
                            anime({
                                targets: el,
                                clipPath: ['inset(0 100% 0 0)', 'inset(0 0% 0 0)'],
                                duration: 600,
                                easing: 'easeOutQuad'
                            });
                        }

                        observer.unobserve(el);
                    }
                });
            }, { threshold: 0.2 });

            document.querySelectorAll('.large-heading, .countdown-grid, .stats-grid, .grid-3, .reveal-image-container, .timeline-wrapper, .section-label').forEach(el => {
                observer.observe(el);
                if(el.classList.contains('large-heading') || el.classList.contains('section-label')) {
                    el.style.opacity = '0';
                }
                if(el.classList.contains('countdown-grid')) {
                    el.querySelectorAll('.countdown-box').forEach(b => b.style.opacity = '0');
                }
                if(el.classList.contains('grid-3')) {
                    el.querySelectorAll('.module-card').forEach(b => b.style.opacity = '0');
                }
                if(el.classList.contains('timeline-wrapper')) {
                    el.querySelectorAll('.timeline-item').forEach(b => b.style.opacity = '0');
                }
            });

            // Hero Glow Follow
            const cursorGlow = document.getElementById('heroCursorGlow');
            const heroSection = document.getElementById('home');
            
            if(cursorGlow && heroSection) {
                heroSection.addEventListener('mousemove', (e) => {
                    cursorGlow.style.opacity = '1';
                    cursorGlow.style.left = e.pageX + 'px';
                    cursorGlow.style.top = e.pageY + 'px';
                });
                heroSection.addEventListener('mouseleave', () => {
                    cursorGlow.style.opacity = '0';
                });
            }
        });

        function showSubCards() {
            const sc = document.getElementById('sub-cards-surface');
            if (sc) sc.classList.add('expanded');
        }
        function hideSubCards() {
            const sc = document.getElementById('sub-cards-surface');
            if (sc) sc.classList.remove('expanded');
        }
    </script>
"""

html = re.sub(r'<!-- Interactive Scripts -->.*?</script>', new_js, html, flags=re.DOTALL)

# Floating Button Replace
whatsapp_html = """
    <div class="floating-request" onclick="document.querySelector('.hero-waitlist').scrollIntoView({behavior:'smooth'});" style="position:fixed; bottom:2rem; right:2rem; width:60px; height:60px; border-radius:50%; background:rgba(34,197,94,0.85); backdrop-filter:blur(12px); -webkit-backdrop-filter:blur(12px); border:1px solid rgba(34,197,94,0.4); box-shadow:0 8px 32px rgba(34,197,94,0.25); display:flex; align-items:center; justify-content:center; color:#fff; cursor:pointer; z-index:999; animation:green-pulse 2s infinite;">
        <svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
    </div>
    <style>
        @keyframes green-pulse {
            0% { box-shadow: 0 0 0 0 rgba(34,197,94,0.6); }
            70% { box-shadow: 0 0 0 15px rgba(34,197,94,0); }
            100% { box-shadow: 0 0 0 0 rgba(34,197,94,0); }
        }
    </style>
"""

if 'floating-request' not in html:
    html = re.sub(r'<div class="floating-whatsapp".*?</div>', whatsapp_html, html, flags=re.DOTALL)


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
