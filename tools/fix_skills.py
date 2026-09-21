import os

css = """
/* ==========================================================================
   SKILLS PAGE OVERHAUL
   ========================================================================== */
.skills-master-grid {
    display: grid;
    grid-template-columns: 1fr 1.55fr;
    gap: clamp(40px, 6vw, 80px);
    align-items: start;
}
@media (max-width: 1024px) {
    .skills-master-grid {
        grid-template-columns: 1fr;
    }
}
.skills-hero-img {
    width: 100%;
    aspect-ratio: 4/5;
    object-fit: cover;
    object-position: center;
    border-radius: 4px;
    filter: contrast(1.15) grayscale(20%);
    border: 1px solid rgba(222, 27, 28, 0.2);
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5), 0 0 20px rgba(222, 27, 28, 0.1);
    margin-bottom: 40px;
    transition: filter 0.5s;
}
.skills-hero-img:hover {
    filter: contrast(1.25) grayscale(0%);
    border-color: rgba(222, 27, 28, 0.5);
}
.skills-icon-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 16px;
}
.skills-icon {
    width: clamp(40px, 4vw, 48px);
    height: clamp(40px, 4vw, 48px);
    border-radius: 8px;
    background: rgba(15, 15, 15, 0.6);
    border: 1px solid rgba(255,255,255,0.1);
    padding: 8px;
    object-fit: contain;
    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}
.skills-icon:hover {
    background: rgba(222, 27, 28, 0.2);
    border-color: rgba(222, 27, 28, 0.6);
    transform: translateY(-4px) scale(1.05);
    box-shadow: 0 8px 20px rgba(222, 27, 28, 0.3);
}
"""

with open('src/styles/secondary.css', 'a', encoding='utf-8') as f:
    f.write(css)

html_new_grid = """        <div class="skills-master-grid">
            <div class="skills-left-col">
                <img class="skills-hero-img" src="public/projects/iclonis_tech.png" alt="Premium Developer Dashboard">
                
                <div class="tools-section" style="margin-top: 0;">
                    <p class="skill-group__title">Creative & AI Stack</p>
                    <div class="skills-icon-grid">
                        <img class="skills-icon" src="public/tools/figma.png" alt="Figma">
                        <img class="skills-icon" src="public/tools/photoshop.png" alt="Photoshop">
                        <img class="skills-icon" src="public/tools/premiere.png" alt="Premiere">
                        <img class="skills-icon" src="public/tools/aftereffects.png" alt="After Effects">
                        <img class="skills-icon" src="public/tools/notion.png" alt="Notion">
                        <img class="skills-icon" src="public/tools/chatgpt.png" alt="ChatGPT">
                        <img class="skills-icon" src="public/tools/claude.png" alt="Claude">
                        <img class="skills-icon" src="public/tools/midjourney.png" alt="Midjourney">
                        <img class="skills-icon" src="public/tools/spline.png" alt="Spline">
                        <img class="skills-icon" src="public/tools/webflow.png" alt="Webflow">
                        <img class="skills-icon" src="public/tools/framer.png" alt="Framer">
                    </div>
                </div>

                <div class="tools-section" style="margin-top: 48px;">
                    <p class="skill-group__title">Core Technologies</p>
                    <div class="tools-grid" style="margin-top: 16px;">
                        <span class="tool-chip">React</span><span class="tool-chip">Python</span>
                        <span class="tool-chip">FastAPI</span><span class="tool-chip">ASP.NET</span>
                        <span class="tool-chip">C#</span><span class="tool-chip">MySQL</span>
                        <span class="tool-chip">Git</span><span class="tool-chip">REST APIs</span>
                    </div>
                </div>
            </div>

            <div class="skills-layout-grid" style="grid-template-columns: 1fr; gap: 40px; margin-top: 0; z-index: 2;">
                <!-- Frontend -->
                <div class="skill-card">
                    <p class="skill-group__title">Frontend</p>
                    <div class="skill-bar">
                        <div class="skill-bar__name"><span>React / JSX</span><span class="skill-bar__pct">88%</span></div>
                        <div class="skill-bar__track">
                            <div class="skill-bar__fill" style="width:88%"></div>
                        </div>
                    </div>
                    <div class="skill-bar">
                        <div class="skill-bar__name"><span>HTML5 / CSS3</span><span class="skill-bar__pct">93%</span></div>
                        <div class="skill-bar__track">
                            <div class="skill-bar__fill" style="width:93%"></div>
                        </div>
                    </div>
                    <div class="skill-bar">
                        <div class="skill-bar__name"><span>JavaScript (ES6+)</span><span class="skill-bar__pct">87%</span></div>
                        <div class="skill-bar__track">
                            <div class="skill-bar__fill" style="width:87%"></div>
                        </div>
                    </div>
                    <div class="skill-bar">
                        <div class="skill-bar__name"><span>Vite / Next.js</span><span class="skill-bar__pct">78%</span></div>
                        <div class="skill-bar__track">
                            <div class="skill-bar__fill" style="width:78%"></div>
                        </div>
                    </div>
                </div>

                <!-- Backend -->
                <div class="skill-card">
                    <p class="skill-group__title">Backend</p>
                    <div class="skill-bar">
                        <div class="skill-bar__name"><span>Python / FastAPI</span><span class="skill-bar__pct">87%</span></div>
                        <div class="skill-bar__track">
                            <div class="skill-bar__fill" style="width:87%"></div>
                        </div>
                    </div>
                    <div class="skill-bar">
                        <div class="skill-bar__name"><span>ASP.NET Core / C#</span><span class="skill-bar__pct">81%</span></div>
                        <div class="skill-bar__track">
                            <div class="skill-bar__fill" style="width:81%"></div>
                        </div>
                    </div>
                    <div class="skill-bar">
                        <div class="skill-bar__name"><span>REST APIs</span><span class="skill-bar__pct">89%</span></div>
                        <div class="skill-bar__track">
                            <div class="skill-bar__fill" style="width:89%"></div>
                        </div>
                    </div>
                </div>

                <!-- Database & Tools -->
                <div class="skill-card">
                    <p class="skill-group__title">Database</p>
                    <div class="skill-bar">
                        <div class="skill-bar__name"><span>MySQL</span><span class="skill-bar__pct">86%</span></div>
                        <div class="skill-bar__track">
                            <div class="skill-bar__fill" style="width:86%"></div>
                        </div>
                    </div>
                    <div class="skill-bar">
                        <div class="skill-bar__name"><span>SQL Server</span><span class="skill-bar__pct">79%</span></div>
                        <div class="skill-bar__track">
                            <div class="skill-bar__fill" style="width:79%"></div>
                        </div>
                    </div>
                    <div class="skill-bar">
                        <div class="skill-bar__name"><span>Database Design</span><span class="skill-bar__pct">82%</span></div>
                        <div class="skill-bar__track">
                            <div class="skill-bar__fill" style="width:82%"></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>"""

with open('skills.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx1 = text.find('        <div class="skills-layout-grid">')
idx2 = text.find('    <footer class="sp-footer">')

# keep the closing '</div>' of pg
idx_pg_end = text.rfind('</div>', 0, idx2)
if idx_pg_end != -1:
    out_text = text[:idx1] + html_new_grid + '\n    </div>\n\n' + text[idx2:]
    with open('skills.html', 'w', encoding='utf-8') as f:
        f.write(out_text)
    print("skills.html successfully rebuilt")
else:
    print("Could not find div.pg end marker properly")
