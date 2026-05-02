import re

with open('c:\\Users\\athul\\Documents\\Projects\\ddlc-main\\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# CHANGE 1 — DEPLOYED PRODUCT LANGUAGE
html = html.replace(
    'Identify microscopic cosmetic defects and texture anomalies',
    'Identifies microscopic cosmetic defects and texture anomalies'
)
html = html.replace(
    'Verify individual sub-components during assembly to ensure zero-defect\\n                        integrity before final integration. Catch errors before they become costly failures.',
    'Verifies individual sub-components during assembly to ensure zero-defect\\n                        integrity before final integration. Catches errors before they become costly failures.'
)
html = html.replace(
    'Verify individual sub-components during assembly to ensure zero-defect\\n                        integrity before final integration. Catch errors before they become costly failures.',
    'Verifies individual sub-components during assembly to ensure zero-defect\\n                        integrity before final integration. Catches errors before they become costly failures.'
)
# Using regex to handle possible whitespace differences for Change 1 replacements
html = re.sub(r'Verify individual sub-components during assembly to ensure zero-defect\s*integrity before final integration\.\s*Catch errors before they become costly failures\.',
              'Verifies individual sub-components during assembly to ensure zero-defect integrity before final integration. Catches errors before they become costly failures.', html)

html = re.sub(r'Measure geometric tolerances with sub-millimeter precision at the edge\.',
              'Measures geometric tolerances with sub-millimeter precision at the edge.', html)

html = re.sub(r'Extract raw pipeline data straight from existing floor sensors',
              'Extracts raw pipeline data straight from existing floor sensors', html)

html = re.sub(r'Upload high-frequency data to the DDLC cloud ecosystem utilizing military-grade\s*encrypted pipelines\.',
              'Uploads high-frequency data to the DDLC cloud ecosystem utilizing military-grade encrypted pipelines.', html)

html = re.sub(r'Define specific mechanical use cases and let our forge automatically map and instruct\s*the neural weights\.',
              'Defines specific mechanical use cases and automatically maps and instructs the neural weights.', html)

html = re.sub(r'Test computational accuracy in sandboxed twins using historical failure data prior to\s*live deployment\.',
              'Tests computational accuracy in sandboxed twins using historical failure data prior to live deployment.', html)

html = re.sub(r'Flash the confirmed intelligence model natively onto physical DDLC chassis attached\s*to your line\.',
              'Flashes the confirmed intelligence model natively onto physical DDLC chassis attached to your line.', html)

html = re.sub(r'Automate cosmetic inspections, predict tool degradation, and optimize assembly\s*pipelines using visual and acoustic signatures\.',
              'Automates cosmetic inspections, predicts tool degradation, and optimizes assembly pipelines using visual and acoustic signatures.', html)


# CHANGE 2 — VISUAL EFFECTS
html = html.replace(
    'background-color: rgba(255, 255, 255, 0.9);',
    'background-color: rgba(255, 255, 255, 0.75);'
)
html = html.replace(
    'border-bottom: 1px solid rgba(226, 232, 240, 0.8);',
    'border-bottom: 1px solid rgba(255, 255, 255, 0.3);'
)
html = html.replace(
    'background: rgba(255, 255, 255, 0.85);',
    'background: rgba(255, 255, 255, 0.75);'
)
html = html.replace(
    'backdrop-filter: blur(20px);\\n            box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.05);',
    'backdrop-filter: blur(20px);\\n            border-bottom: 1px solid rgba(255, 255, 255, 0.3);\\n            box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.05);'
)
# Make sure to also replace the unescaped version if the literal match above fails
html = re.sub(r'backdrop-filter: blur\(20px\);\s*box-shadow: 0 10px 30px -10px rgba\(0, 0, 0, 0\.05\);',
              'backdrop-filter: blur(20px);\\n            border-bottom: 1px solid rgba(255, 255, 255, 0.3);\\n            box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.05);', html)

hero_visual_right_css = """        .hero-visual-right {
            display: flex;
            justify-content: flex-end;
            align-items: center;
            position: relative;
        }

        .hero-visual-right::before {
            content: '';
            position: absolute;
            width: 150%;
            height: 150%;
            top: -25%;
            left: -25%;
            background: radial-gradient(circle, rgba(34,197,94,0.08) 0%, transparent 65%);
            z-index: -1;
            pointer-events: none;
        }"""
html = re.sub(r'\s*\.hero-visual-right\s*\{\s*display:\s*flex;\s*justify-content:\s*flex-end;\s*align-items:\s*center;\s*\}',
              '\\n' + hero_visual_right_css, html)

html = re.sub(r'\s*\.section\s*\{\s*padding:\s*8rem\s*0;\s*position:\s*relative;\s*\}',
              '\\n        .section {\\n            padding: 8rem 0;\\n            position: relative;\\n            border-bottom: 1px solid rgba(34,197,94,0.12);\\n        }\\n\\n        .section:nth-of-type(odd) {\\n            background: linear-gradient(135deg, #f7fdf9 0%, #ffffff 100%);\\n        }', html)

html = re.sub(r'\s*\.module-card:hover\s*\{\s*border-color:\s*var\(--primary-green\);\s*transform:\s*translateY\(-3px\);\s*box-shadow:\s*var\(--card-shadow-hover\);\s*\}',
              '\\n        .module-card:hover {\\n            border-color: #22c55e;\\n            transform: translateY(-4px);\\n            box-shadow: 0 20px 40px rgba(34,197,94,0.08);\\n            transition: all 0.25s ease;\\n        }', html)

html = html.replace('transition: all 0.2s ease;', 'transition: all 0.25s ease;')
html = html.replace('transform: scale(1.03);', 'transform: scale(1.04);')

# Replace Vanilla JS Scroll Reveal with Anime.js
html = re.sub(r'\s*\.reveal-element\s*\{[^}]*\}\s*', '\\n', html)
html = re.sub(r'\s*\.reveal-element\.visible\s*\{[^}]*\}\s*', '\\n', html)
html = re.sub(r'\s*body\.loaded\s*\.reveal-element\s*\{[^}]*\}\s*', '\\n', html)

# CHANGE 3 — ADD STATS BAR SECTION
stats_html = """    <section class="stats-bar" style="width: 100%; background-color: #f7f9f7; padding: 3rem 2rem; border-bottom: 1px solid rgba(34,197,94,0.12);">
        <div class="container">
            <div style="display: flex; justify-content: space-between; align-items: center; text-align: center; flex-wrap: wrap; gap: 2rem;">
                <div style="flex: 1; min-width: 150px;">
                    <div class="stat-number anime-stat" data-target="500" style="font-family: var(--font-display); font-size: clamp(2.5rem, 4vw, 3.5rem); font-weight: 700; color: #22c55e; line-height: 1;">0<span style="font-size: 2.5rem;">+</span></div>
                    <div style="font-family: var(--font-label); font-size: 0.8rem; color: var(--gray-text); text-transform: uppercase; letter-spacing: 0.1em; margin-top: 0.5rem;">Units Deployed</div>
                </div>
                <div style="width: 1px; height: 50px; background-color: rgba(34,197,94,0.12); display: none;" class="stat-divider"></div>
                <div style="flex: 1; min-width: 150px;">
                    <div class="stat-number anime-stat" data-target="12" style="font-family: var(--font-display); font-size: clamp(2.5rem, 4vw, 3.5rem); font-weight: 700; color: #22c55e; line-height: 1;">0<span style="font-size: 2.5rem;">ms</span></div>
                    <div style="font-family: var(--font-label); font-size: 0.8rem; color: var(--gray-text); text-transform: uppercase; letter-spacing: 0.1em; margin-top: 0.5rem;">Average Inference Time</div>
                </div>
                <div style="width: 1px; height: 50px; background-color: rgba(34,197,94,0.12); display: none;" class="stat-divider"></div>
                <div style="flex: 1; min-width: 150px;">
                    <div class="stat-number anime-stat" data-target="99" style="font-family: var(--font-display); font-size: clamp(2.5rem, 4vw, 3.5rem); font-weight: 700; color: #22c55e; line-height: 1;">0<span style="font-size: 2.5rem;">.7%</span></div>
                    <div style="font-family: var(--font-label); font-size: 0.8rem; color: var(--gray-text); text-transform: uppercase; letter-spacing: 0.1em; margin-top: 0.5rem;">Detection Accuracy</div>
                </div>
                <div style="width: 1px; height: 50px; background-color: rgba(34,197,94,0.12); display: none;" class="stat-divider"></div>
                <div style="flex: 1; min-width: 150px;">
                    <div class="stat-number-text" style="font-family: var(--font-display); font-size: clamp(2.5rem, 4vw, 3.5rem); font-weight: 700; color: #22c55e; line-height: 1;">24/7</div>
                    <div style="font-family: var(--font-label); font-size: 0.8rem; color: var(--gray-text); text-transform: uppercase; letter-spacing: 0.1em; margin-top: 0.5rem;">Active Operation</div>
                </div>
            </div>
            <style>
                @media (min-width: 768px) {
                    .stat-divider { display: block !important; }
                }
            </style>
        </div>
    </section>
"""
html = html.replace('</section>\\n\\n    <!-- Edge Inspection Modules -->', f'</section>\\n\\n{stats_html}\\n\\n    <!-- Edge Inspection Modules -->')
# In case the literal newline match fails:
html = re.sub(r'</section>\s*<!-- Edge Inspection Modules -->', f'</section>\\n\\n{stats_html}\\n\\n    <!-- Edge Inspection Modules -->', html)


# CHANGE 6 — FLOATING WHATSAPP BUTTON
whatsapp_btn = """    <!-- Floating WhatsApp Button -->
    <a href="https://wa.me/" target="_blank" class="floating-whatsapp" aria-label="Chat on WhatsApp">
        <svg viewBox="0 0 24 24" fill="currentColor">
            <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51a12.8 12.8 0 0 0-.57-.01c-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413Z"/>
        </svg>
    </a>
"""
css_whatsapp = """        .floating-whatsapp {
            position: fixed;
            bottom: 2rem;
            right: 2rem;
            z-index: 999;
            width: 60px;
            height: 60px;
            background-color: #25d366;
            color: #ffffff;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 4px 14px rgba(37,211,102,0.4);
            transition: all 0.2s ease;
            animation: whatsapp-pulse 2s infinite;
        }

        .floating-whatsapp:hover {
            transform: scale(1.08);
            box-shadow: 0 6px 20px rgba(37,211,102,0.6);
            animation: none;
        }

        .floating-whatsapp svg {
            width: 32px;
            height: 32px;
            fill: currentColor;
        }

        @keyframes whatsapp-pulse {
            0% {
                box-shadow: 0 0 0 0 rgba(37, 211, 102, 0.6);
            }
            70% {
                box-shadow: 0 0 0 15px rgba(37, 211, 102, 0);
            }
            100% {
                box-shadow: 0 0 0 0 rgba(37, 211, 102, 0);
            }
        }
"""
html = html.replace('</style>', f'{css_whatsapp}\\n    </style>')
html = html.replace('</body>', f'{whatsapp_btn}\\n</body>')


# CHANGE 7 — SMOOTH SCROLL PROGRESS BAR
scroll_progress_html = """    <!-- Smooth Scroll Progress Bar -->
    <div id="scrollProgressBar" style="position: fixed; top: 0; left: 0; height: 3px; background-color: #22c55e; width: 0%; z-index: 9999; transition: width 0.1s ease-out;"></div>
"""
html = html.replace('<body>', f'<body>\\n{scroll_progress_html}')

scroll_script = """
        // Scroll Progress Bar
        window.addEventListener("scroll", () => {
            const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
            const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
            const scrolled = (winScroll / height) * 100;
            document.getElementById("scrollProgressBar").style.width = scrolled + "%";
        });
"""
html = html.replace('</script>', f'{scroll_script}\\n    </script>')


# CHANGE 4 — ANIME.JS ANIMATIONS
anime_script = '<script src="https://cdnjs.cloudflare.com/ajax/libs/animejs/3.2.1/anime.min.js"></script>\\n    <!-- Interactive Scripts -->'
html = html.replace('<!-- Interactive Scripts -->', anime_script)

hero_cursor = """
    <div id="heroCursorGlow" style="position: absolute; width: 200px; height: 200px; background: rgba(34,197,94,0.06); border-radius: 50%; filter: blur(60px); pointer-events: none; transform: translate(-50%, -50%); z-index: 1; opacity: 0; transition: opacity 0.3s ease;"></div>
"""
html = html.replace('<div class="container hero-content">', f'{hero_cursor}\\n        <div class="container hero-content">')


old_js = """        document.addEventListener("DOMContentLoaded", () => {
            document.body.classList.add('loaded');
            const observer = new IntersectionObserver((entries) => {
                entries.forEach((entry, index) => {
                    if (entry.isIntersecting) {
                        setTimeout(() => {
                            entry.target.classList.add('visible');
                        }, index * 100);
                    }
                });
            }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

            document.querySelectorAll('.reveal-element, .section, .module-card, .feat-slide, .timeline-item').forEach((el) => {
                if (!el.classList.contains('reveal-element')) {
                    el.classList.add('reveal-element');
                }
                observer.observe(el);
            });

            // Count observer for step numbers
            const countObserver = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const target = entry.target;
                        if (!target.hasAttribute('data-counted')) {
                            target.setAttribute('data-counted', 'true');
                            const targetValue = parseInt(target.innerText) || parseInt(target.getAttribute('data-target') || '1');
                            target.innerText = "0";
                            let count = 0;
                            const interval = setInterval(() => {
                                if (count < targetValue) {
                                    count++;
                                    target.innerText = count.toString();
                                } else {
                                    clearInterval(interval);
                                }
                            }, 50);
                        }
                    }
                });
            }, { threshold: 0.5 });

            document.querySelectorAll('.tl-number').forEach(el => countObserver.observe(el));
        });"""

new_js = """        document.addEventListener("DOMContentLoaded", () => {
            document.body.classList.add('loaded');

            // Hero Page Load Animations (Anime.js)
            document.querySelectorAll('.ddlc-letter-container').forEach(el => { el.style.opacity = '0'; el.style.transform = 'translateY(50px)'; });
            const heroSubtitle = document.querySelector('.hero-interactive-subtitle');
            const heroFullForm = document.querySelector('.hero-full-form');
            if (heroSubtitle) { heroSubtitle.style.opacity = '0'; heroSubtitle.style.transform = 'translateY(20px)'; }
            if (heroFullForm) { heroFullForm.style.opacity = '0'; heroFullForm.style.transform = 'translateY(20px)'; }
            const heroImg = document.querySelector('.hero-product-img');
            if (heroImg) { heroImg.style.opacity = '0'; heroImg.style.transform = 'translateX(80px)'; }
            
            setTimeout(() => {
                anime({
                    targets: '.ddlc-letter-container',
                    translateY: [50, 0],
                    opacity: [0, 1],
                    delay: anime.stagger(80),
                    easing: 'easeOutExpo',
                    duration: 1000
                });

                anime({
                    targets: ['.hero-interactive-subtitle', '.hero-full-form'],
                    opacity: [0, 1],
                    translateY: [20, 0],
                    delay: 500,
                    duration: 1000,
                    easing: 'easeOutExpo'
                });

                if (heroImg) {
                    anime({
                        targets: heroImg,
                        translateX: [80, 0],
                        opacity: [0, 1],
                        delay: 250,
                        duration: 1200,
                        easing: 'easeOutExpo'
                    });
                }
            }, 100);

            // Section Headings
            const headingObserver = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        anime({
                            targets: entry.target,
                            opacity: [0, 1],
                            translateY: [25, 0],
                            duration: 550,
                            easing: 'easeOutQuart'
                        });
                        observer.unobserve(entry.target);
                    }
                });
            }, { threshold: 0.2 });
            document.querySelectorAll('.large-heading').forEach(el => {
                if (!el.classList.contains('hero-title')) {
                    el.style.opacity = '0';
                    headingObserver.observe(el);
                }
            });

            // Section Labels (Text reveal on scroll)
            const labelObserver = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.style.opacity = '1';
                        anime({
                            targets: entry.target,
                            clipPath: ['inset(0 100% 0 0)', 'inset(0 0% 0 0)'],
                            duration: 600,
                            easing: 'easeOutQuad'
                        });
                        observer.unobserve(entry.target);
                    }
                });
            }, { threshold: 0.2 });
            document.querySelectorAll('.section-label').forEach(el => {
                el.style.opacity = '0';
                labelObserver.observe(el);
            });

            // Card Grids (Module Cards)
            const gridObserver = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const cards = entry.target.querySelectorAll('.module-card, .sub-card');
                        anime({
                            targets: cards,
                            translateY: [35, 0],
                            opacity: [0, 1],
                            delay: anime.stagger(130),
                            duration: 800,
                            easing: 'easeOutQuart'
                        });
                        observer.unobserve(entry.target);
                    }
                });
            }, { threshold: 0.1 });
            document.querySelectorAll('.grid-3, .sub-cards-grid').forEach(el => {
                el.querySelectorAll('.module-card, .sub-card').forEach(c => { c.style.opacity = '0'; c.style.transform = 'translateY(35px)'; });
                gridObserver.observe(el);
            });

            // Deploy steps on scroll
            const timelineObserver = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const items = entry.target.querySelectorAll('.timeline-item');
                        anime({
                            targets: items,
                            translateX: [-25, 0],
                            opacity: [0, 1],
                            delay: anime.stagger(180),
                            duration: 800,
                            easing: 'easeOutQuart'
                        });

                        const numbers = entry.target.querySelectorAll('.tl-number');
                        numbers.forEach((num, idx) => {
                            const val = parseInt(num.innerText) || (idx + 1);
                            num.innerText = '0';
                            anime({
                                targets: num,
                                innerHTML: [0, val],
                                round: 1,
                                delay: 180 * idx,
                                duration: 1000,
                                easing: 'easeOutQuad'
                            });
                        });
                        observer.unobserve(entry.target);
                    }
                });
            }, { threshold: 0.1 });
            const timelineWrapper = document.querySelector('.timeline-wrapper');
            if (timelineWrapper) {
                timelineWrapper.querySelectorAll('.timeline-item').forEach(c => { c.style.opacity = '0'; });
                timelineObserver.observe(timelineWrapper);
            }

            // All images on scroll
            const imgObserver = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        anime({
                            targets: entry.target,
                            opacity: [0, 1],
                            translateY: [40, 0],
                            duration: 600,
                            easing: 'easeOutQuart'
                        });
                        observer.unobserve(entry.target);
                    }
                });
            }, { threshold: 0.1 });
            document.querySelectorAll('.tl-img, .visual-card img').forEach(el => {
                el.style.opacity = '0';
                imgObserver.observe(el);
            });

            // Stats numbers count up
            const statsObserver = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const stats = entry.target.querySelectorAll('.anime-stat');
                        stats.forEach((stat, idx) => {
                            const targetVal = parseFloat(stat.getAttribute('data-target'));
                            const suffix = stat.innerText.replace(/[0-9.]/g, ''); 
                            const dec = targetVal % 1 !== 0 ? 1 : 0;
                            
                            const obj = { val: 0 };
                            
                            anime({
                                targets: obj,
                                val: targetVal,
                                round: dec === 0 ? 1 : 10,
                                delay: idx * 150,
                                duration: 1500,
                                easing: 'easeOutQuad',
                                update: function() {
                                    let displayVal = obj.val;
                                    if(dec > 0) {
                                        displayVal = (displayVal / 10).toFixed(1);
                                    }
                                    if (stat.getAttribute('data-target') == '99') {
                                        displayVal = obj.val.toFixed(1);
                                    }
                                    stat.innerHTML = displayVal + '<span style="font-size: 2.5rem;">' + suffix + '</span>';
                                }
                            });
                        });
                        observer.unobserve(entry.target);
                    }
                });
            }, { threshold: 0.5 });
            const statsBar = document.querySelector('.stats-bar');
            if (statsBar) {
                statsObserver.observe(statsBar);
            }

            // Hero cursor follow effect
            const hero = document.querySelector('.hero');
            const heroCursorGlow = document.getElementById('heroCursorGlow');
            if (hero && heroCursorGlow) {
                hero.addEventListener('mousemove', (e) => {
                    const rect = hero.getBoundingClientRect();
                    const x = e.clientX - rect.left;
                    const y = e.clientY - rect.top;
                    heroCursorGlow.style.left = x + 'px';
                    heroCursorGlow.style.top = y + 'px';
                    heroCursorGlow.style.opacity = '1';
                });
                hero.addEventListener('mouseleave', () => {
                    heroCursorGlow.style.opacity = '0';
                });
            }
        });"""

# Because regex with multi-line can be tricky, let's just do an exact replace if possible.
# Actually, it's safer to use a regex that matches from document.addEventListener to the closing `});`
html = re.sub(r'\s*document\.addEventListener\("DOMContentLoaded", \(\) => \{.*?(?=// Navbar Scroll Effect)', '\\n' + new_js + '\\n\\n        ', html, flags=re.DOTALL)

with open('c:\\Users\\athul\\Documents\\Projects\\ddlc-main\\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Modifications successfully written!")
