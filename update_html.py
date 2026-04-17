import os

html_file = "/home/km13/Documents/mirakhor_karan_portfolio/index.html"
with open(html_file, 'r') as f:
    text = f.read()

# 1. Navbar changes
text = text.replace('<li><a href="#about">About</a></li>\n                <li><a href="#research">Research</a></li>', '<li><a href="#about">About</a></li>\n                <li><a href="#experience">Experience</a></li>\n                <li><a href="#research">Research</a></li>')
text = text.replace('<li><a href="#about">About</a></li>\n                    <li><a href="#research">Research</a></li>', '<li><a href="#about">About</a></li>\n                    <li><a href="#experience">Experience</a></li>\n                    <li><a href="#research">Research</a></li>')

# We need to replace the entire section from <!-- About Section --> to <!-- Publications Section -->
start_idx = text.find('    <!-- About Section -->')
end_idx = text.find('    <!-- Publications Section -->')

if start_idx != -1 and end_idx != -1:
    new_html = """    <!-- About Section -->
    <section id="about" class="py-20 section">
        <div class="container mx-auto px-6 max-w-6xl">
            <!-- Section Header -->
            <div class="text-center mb-16">
                <h2 class="text-4xl font-bold mb-4 tracking-wide" style="color: var(--text-primary);">About Me</h2>
                <div class="w-24 h-1 mx-auto rounded-full" style="background: var(--accent-primary);"></div>
            </div>

            <!-- Main Content Container -->
            <div class="prose prose-lg max-w-none">
                <!-- Introduction Card -->
                <div class="backdrop-blur-sm rounded-2xl p-8 mb-12 border transition-all duration-300 hover:shadow-xl hover:transform hover:-translate-y-2" style="background: var(--bg-card); border-color: var(--border-color); box-shadow: 0 4px 12px -2px var(--shadow-color), 0 2px 6px -1px var(--shadow-color);" onmouseover="this.style.borderColor='var(--accent-primary)'; this.style.boxShadow='0 8px 25px -5px var(--particle-glow), 0 4px 12px -2px var(--shadow-color)'" onmouseout="this.style.borderColor='var(--border-color)'; this.style.boxShadow='0 4px 12px -2px var(--shadow-color), 0 2px 6px -1px var(--shadow-color)'">
                    <div class="text-center">
                        <p class="text-lg leading-relaxed" style="color: var(--text-primary);">
                            I am a Master of Science (Research) in Robotics student at <a href="https://www.cmu.edu/" target="_blank" class="transition-colors duration-300 font-semibold" style="color: var(--accent-primary);" onmouseover="this.style.color='var(--text-primary)'" onmouseout="this.style.color='var(--accent-primary)'">Carnegie Mellon University</a>, working as a Graduate Research Assistant at the <a href="https://www.ri.cmu.edu/" target="_blank" class="transition-colors duration-300 font-semibold" style="color: var(--accent-primary);" onmouseover="this.style.color='var(--text-primary)'" onmouseout="this.style.color='var(--accent-primary)'">Robotics Institute</a> under the advisement of <a href="https://www.ri.cmu.edu/ri-people/katia-sycara/" target="_blank" class="transition-colors duration-300 font-medium" style="color: var(--accent-primary);" onmouseover="this.style.color='var(--text-primary)'" onmouseout="this.style.color='var(--accent-primary)'">Prof. Katia Sycara</a>. Prior to this, I spent two years as a Research Fellow at <a href="https://www.tcs.com/what-we-do/research" target="_blank" class="transition-colors duration-300 font-medium" style="color: var(--accent-primary);" onmouseover="this.style.color='var(--text-primary)'" onmouseout="this.style.color='var(--accent-primary)'">TCS Research</a>, working under the guidance of <a href="https://scholar.google.co.in/citations?user=Eqf8NrEAAAAJ&hl=en" target="_blank" class="transition-colors duration-300 font-medium" style="color: var(--accent-primary);" onmouseover="this.style.color='var(--text-primary)'" onmouseout="this.style.color='var(--accent-primary)'">Dr. Brojeshwar Bhowmick</a>. Before my fellowship, I earned my B.Tech (Honors) in Electronics and Communication Engineering from the <a href="https://www.iiit.ac.in/" target="_blank" class="transition-colors duration-300 font-medium" style="color: var(--accent-primary);" onmouseover="this.style.color='var(--text-primary)'" onmouseout="this.style.color='var(--accent-primary)'">International Institute of Information Technology Hyderabad</a>, where I was awarded the Program Gold Medal. During my undergraduate studies, I also worked as a Research Assistant at the <a href="https://robotics.iiit.ac.in/" target="_blank" class="transition-colors duration-300 font-medium" style="color: var(--accent-primary);" onmouseover="this.style.color='var(--text-primary)'" onmouseout="this.style.color='var(--accent-primary)'">Robotics Research Centre</a> under the guidance of <a href="https://faculty.iiit.ac.in/~mkrishna/" target="_blank" class="transition-colors duration-300 font-medium" style="color: var(--accent-primary);" onmouseover="this.style.color='var(--text-primary)'" onmouseout="this.style.color='var(--accent-primary)'">Prof. Madhav Krishna</a> and <a href="https://scholar.google.co.in/citations?user=5i1t_QgAAAAJ&hl=en" target="_blank" class="transition-colors duration-300 font-medium" style="color: var(--accent-primary);" onmouseover="this.style.color='var(--text-primary)'" onmouseout="this.style.color='var(--accent-primary)'">Dr. Harikumar Kandath</a>.
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Experience Section -->
    <section id="experience" class="py-20 section">
        <div class="container mx-auto px-6 max-w-6xl">
            <h2 class="section-title">Experience</h2>
            <div class="section-content max-w-none">
                <div class="space-y-8">
                    <!-- CMU Research -->
                    <div class="backdrop-blur-sm rounded-xl p-6 border transition-all duration-300 hover:shadow-xl hover:transform hover:-translate-y-2" style="background: var(--bg-card); border-color: var(--border-color); box-shadow: 0 4px 12px -2px var(--shadow-color), 0 2px 6px -1px var(--shadow-color);" onmouseover="this.style.borderColor='var(--accent-primary)'; this.style.boxShadow='0 8px 25px -5px var(--particle-glow), 0 4px 12px -2px var(--shadow-color)'" onmouseout="this.style.borderColor='var(--border-color)'; this.style.boxShadow='0 4px 12px -2px var(--shadow-color), 0 2px 6px -1px var(--shadow-color)'">
                        <div class="flex flex-col md:flex-row md:items-center md:justify-between mb-4">
                            <h4 class="text-xl font-bold mb-2 md:mb-0" style="color: var(--text-primary);">
                                Graduate Research Assistant
                            </h4>
                            <a href="https://www.ri.cmu.edu/" target="_blank" class="transition-colors duration-300 font-semibold text-lg" style="color: var(--accent-primary);" onmouseover="this.style.color='var(--text-primary)'" onmouseout="this.style.color='var(--accent-primary)'">
                                Carnegie Mellon University
                            </a>
                        </div>
                        <p class="mb-5" style="color: var(--text-secondary);">
                            <span class="font-bold" style="color: var(--text-secondary);">Advisor:</span> 
                            <a href="https://www.ri.cmu.edu/ri-people/katia-sycara/" target="_blank" class="transition-colors duration-300 font-medium" style="color: var(--accent-primary);" onmouseover="this.style.color='var(--text-primary)'" onmouseout="this.style.color='var(--accent-primary)'">Prof. Katia Sycara</a>
                        </p>
                        <!-- CMU Current Works -->
                        <div class="grid md:grid-cols-2 gap-4 mt-4">
                            <!-- Bullet 1 -->
                            <div class="p-4 rounded-xl border border-gray-200 dark:border-gray-700" style="background: rgba(15, 23, 42, 0.05);">
                                <h5 class="font-bold mb-2 flex items-center" style="color: var(--text-primary);">
                                    <span class="text-xl mr-2">🧠</span> Zero-shot Coordination in Cooperative MARL
                                </h5>
                                <p class="text-sm leading-relaxed" style="color: var(--text-secondary);">
                                    Developing agents that can seamlessly collaborate with previously unseen partners without additional training. Specifically, I focus on offline-to-online training frameworks that leverage behavioral diversity in offline datasets and enable efficient online adaptation.
                                </p>
                            </div>
                            <!-- Bullet 2 -->
                            <div class="p-4 rounded-xl border border-gray-200 dark:border-gray-700" style="background: rgba(15, 23, 42, 0.05);">
                                <h5 class="font-bold mb-2 flex items-center" style="color: var(--text-primary);">
                                    <span class="text-xl mr-2">🎭</span> Targeted Deception in Competitive MARL
                                </h5>
                                <p class="text-sm leading-relaxed" style="color: var(--text-secondary);">
                                    Developing targeted deception strategies by leveraging higher-order opponent belief models and analyzing historical response patterns to identify and exploit individual vulnerabilities.
                                </p>
                            </div>
                        </div>
                    </div>

                    <!-- TCS Research -->
                    <div class="backdrop-blur-sm rounded-xl p-6 border transition-all duration-300 hover:shadow-xl hover:transform hover:-translate-y-2" style="background: var(--bg-card); border-color: var(--border-color); box-shadow: 0 4px 12px -2px var(--shadow-color), 0 2px 6px -1px var(--shadow-color);" onmouseover="this.style.borderColor='var(--accent-primary)'; this.style.boxShadow='0 8px 25px -5px var(--particle-glow), 0 4px 12px -2px var(--shadow-color)'" onmouseout="this.style.borderColor='var(--border-color)'; this.style.boxShadow='0 4px 12px -2px var(--shadow-color), 0 2px 6px -1px var(--shadow-color)'">
                        <div class="flex flex-col md:flex-row md:items-center md:justify-between mb-4">
                            <h4 class="text-xl font-bold mb-2 md:mb-0" style="color: var(--text-primary);">
                                Pre-doctoral Research Fellow
                            </h4>
                            <a href="https://www.tcs.com/what-we-do/research" target="_blank" class="transition-colors duration-300 font-semibold text-lg" style="color: var(--accent-primary);" onmouseover="this.style.color='var(--text-primary)'" onmouseout="this.style.color='var(--accent-primary)'">
                                TCS Research
                            </a>
                        </div>
                        <p class="mb-3" style="color: var(--text-secondary);">
                            <span class="font-bold" style="color: var(--text-secondary);">Advisor:</span> 
                            <a href="https://scholar.google.co.in/citations?user=Eqf8NrEAAAAJ&hl=en" target="_blank" class="transition-colors duration-300 font-medium" style="color: var(--accent-primary);" onmouseover="this.style.color='var(--text-primary)'" onmouseout="this.style.color='var(--accent-primary)'">Dr. Brojeshwar Bhowmick</a>
                        </p>
                        <p class="leading-relaxed" style="color: var(--text-secondary);">
                            Explored <span class="font-bold" style="color: var(--text-secondary);">Task Planning</span> for Indoor Object Rearrangement under 
                            <span class="font-bold" style="color: var(--text-secondary);">partial observability (POMDP)</span>. Developed scalable graph-based scene representations, utilized <span class="font-bold" style="color: var(--text-secondary);">Large Language Models (LLMs)</span> for semantic object search, and applied <span class="font-bold" style="color: var(--text-secondary);">Deep RL</span> for efficient single and multi-room planning.
                        </p>
                    </div>

                    <!-- IIIT Hyderabad -->
                    <div class="backdrop-blur-sm rounded-xl p-6 border transition-all duration-300 hover:shadow-xl hover:transform hover:-translate-y-2" style="background: var(--bg-card); border-color: var(--border-color); box-shadow: 0 4px 12px -2px var(--shadow-color), 0 2px 6px -1px var(--shadow-color);" onmouseover="this.style.borderColor='var(--accent-primary)'; this.style.boxShadow='0 8px 25px -5px var(--particle-glow), 0 4px 12px -2px var(--shadow-color)'" onmouseout="this.style.borderColor='var(--border-color)'; this.style.boxShadow='0 4px 12px -2px var(--shadow-color), 0 2px 6px -1px var(--shadow-color)'">
                        <div class="flex flex-col md:flex-row md:items-center md:justify-between mb-4">
                            <h4 class="text-xl font-bold mb-2 md:mb-0" style="color: var(--text-primary);">
                                Research Assistant
                            </h4>
                            <span class="text-lg">
                                <a href="https://robotics.iiit.ac.in/" target="_blank" class="transition-colors duration-300 font-semibold" style="color: var(--accent-primary);" onmouseover="this.style.color='var(--text-primary)'" onmouseout="this.style.color='var(--accent-primary)'">Robotics Research Center</a>, 
                                <a href="https://www.iiit.ac.in/" target="_blank" class="transition-colors duration-300 font-semibold" style="color: var(--accent-primary);" onmouseover="this.style.color='var(--text-primary)'" onmouseout="this.style.color='var(--accent-primary)'">IIIT Hyderabad</a>
                            </span>
                        </div>
                        <div class="space-y-2 mb-4">
                            <p style="color: var(--text-secondary);">
                                <span class="font-bold" style="color: var(--text-secondary);">Advisor:</span> 
                                <a href="https://scholar.google.co.in/citations?user=5i1t_QgAAAAJ&hl=en" target="_blank" class="transition-colors duration-300 font-medium" style="color: var(--accent-primary);" onmouseover="this.style.color='var(--text-primary)'" onmouseout="this.style.color='var(--accent-primary)'">Dr. Harikumar Kandath</a>
                            </p>
                        </div>
                        <p class="leading-relaxed" style="color: var(--text-secondary);">
                            Worked on Aerial Manipulator Control using 
                            <span class="font-bold" style="color: var(--text-secondary);">Control Barrier Lyapunov</span> constraints within a 
                            <span class="font-bold" style="color: var(--text-secondary);">Model Predictive Controller</span> for safe operation of the aerial manipulator in constrained environments.
                        </p>
                    </div>
                </div>
                
                <!-- Stats Section moved to after Previous Experience -->
                <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mt-16">
                    <div class="backdrop-blur-sm rounded-xl p-6 border text-center transition-all duration-300 hover:shadow-xl hover:transform hover:-translate-y-2" style="background: var(--bg-card); border-color: var(--border-color); box-shadow: 0 4px 12px -2px var(--shadow-color), 0 2px 6px -1px var(--shadow-color);" onmouseover="this.style.borderColor='var(--accent-primary)'; this.style.boxShadow='0 8px 25px -5px var(--particle-glow), 0 4px 12px -2px var(--shadow-color)'" onmouseout="this.style.borderColor='var(--border-color)'; this.style.boxShadow='0 4px 12px -2px var(--shadow-color), 0 2px 6px -1px var(--shadow-color)'">
                        <div class="text-4xl font-bold mb-2" style="color: var(--accent-primary);">5+</div>
                        <div class="font-medium" style="color: var(--text-secondary);">Years Research Experience</div>
                    </div>
                    <div class="backdrop-blur-sm rounded-xl p-6 border text-center transition-all duration-300 hover:shadow-xl hover:transform hover:-translate-y-2" style="background: var(--bg-card); border-color: var(--border-color); box-shadow: 0 4px 12px -2px var(--shadow-color), 0 2px 6px -1px var(--shadow-color);" onmouseover="this.style.borderColor='var(--accent-primary)'; this.style.boxShadow='0 8px 25px -5px var(--particle-glow), 0 4px 12px -2px var(--shadow-color)'" onmouseout="this.style.borderColor='var(--border-color)'; this.style.boxShadow='0 4px 12px -2px var(--shadow-color), 0 2px 6px -1px var(--shadow-color)'">
                        <div class="text-4xl font-bold mb-2" style="color: var(--accent-primary);">2+</div>
                        <div class="font-medium" style="color: var(--text-secondary);">Years Job Experience</div>
                    </div>
                    <div class="backdrop-blur-sm rounded-xl p-6 border text-center transition-all duration-300 hover:shadow-xl hover:transform hover:-translate-y-2" style="background: var(--bg-card); border-color: var(--border-color); box-shadow: 0 4px 12px -2px var(--shadow-color), 0 2px 6px -1px var(--shadow-color);" onmouseover="this.style.borderColor='var(--accent-primary)'; this.style.boxShadow='0 8px 25px -5px var(--particle-glow), 0 4px 12px -2px var(--shadow-color)'" onmouseout="this.style.borderColor='var(--border-color)'; this.style.boxShadow='0 4px 12px -2px var(--shadow-color), 0 2px 6px -1px var(--shadow-color)'">
                        <div class="text-4xl font-bold mb-2" style="color: var(--accent-primary);">3+</div>
                        <div class="font-medium" style="color: var(--text-secondary);">Publications & Patents</div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Research Section -->
    <section id="research" class="py-20 section">
        <div class="max-w-6xl mx-auto px-6">
            <h2 class="section-title">Research Focus</h2>
            <div class="text-center mb-12">
                <p class="text-lg max-w-5xl mx-auto leading-relaxed" style="color: var(--text-secondary); font-size: 1.25rem;">
                    My research focuses on advancing artificial intelligence through <span class="font-bold" style="color: var(--text-primary);">Long-Horizon Planning, Sequential Decision-Making under uncertainty, Reinforcement Learning, Multi-agent systems, and Human-AI Collaboration</span>. My objective is to engineer autonomous systems capable of exhibiting strategic planning, adaptive behavior, and robust decision-making.
                </p>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 mb-16">
                <!-- RL Tile -->
                <div class="backdrop-blur-sm rounded-2xl shadow-lg text-center transition-all duration-300 hover:shadow-xl hover:transform hover:-translate-y-2" style="background: var(--bg-card); padding: 2rem; border: 2px solid var(--border-color); box-shadow: 0 4px 12px -2px var(--shadow-color), 0 2px 6px -1px var(--shadow-color);" onmouseover="this.style.borderColor='var(--accent-primary)'; this.style.boxShadow='0 8px 25px -5px var(--particle-glow), 0 4px 12px -2px var(--shadow-color)'" onmouseout="this.style.borderColor='var(--border-color)'; this.style.boxShadow='0 4px 12px -2px var(--shadow-color), 0 2px 6px -1px var(--shadow-color)'">
                    <div class="w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-6">
                        <span class="text-3xl">🤖</span>
                    </div>
                    <h3 class="text-2xl font-semibold mb-4" style="color: var(--text-primary); font-size: 1.5rem;">Reinforcement Learning</h3>
                    <p class="leading-relaxed" style="color: var(--text-secondary); font-size: 1.125rem;">
                        Develop algorithms that enable agents to learn close-to-optimal planning and control strategies in robotics, leveraging human demonstrations, fixed datasets, or interactions with dynamic environments.
                    </p>
                </div>
                
                <!-- MARL Tile -->
                <div class="backdrop-blur-sm rounded-2xl shadow-lg text-center transition-all duration-300 hover:shadow-xl hover:transform hover:-translate-y-2" style="background: var(--bg-card); padding: 2rem; border: 2px solid var(--border-color); box-shadow: 0 4px 12px -2px var(--shadow-color), 0 2px 6px -1px var(--shadow-color);" onmouseover="this.style.borderColor='var(--accent-primary)'; this.style.boxShadow='0 8px 25px -5px var(--particle-glow), 0 4px 12px -2px var(--shadow-color)'" onmouseout="this.style.borderColor='var(--border-color)'; this.style.boxShadow='0 4px 12px -2px var(--shadow-color), 0 2px 6px -1px var(--shadow-color)'">
                    <div class="w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-6">
                        <span class="text-3xl">👫</span>
                    </div>
                    <h3 class="text-2xl font-semibold mb-4" style="color: var(--text-primary); font-size: 1.5rem;">Multi-Agent Reinforcement Learning (MARL)</h3>
                    <p class="leading-relaxed" style="color: var(--text-secondary); font-size: 1.125rem;">
                        Study interactions of multiple agents learning together, including cooperation, competition, and strategic reasoning.
                    </p>
                </div>
                
                <!-- Decision Making under Uncertainty Tile -->
                <div class="backdrop-blur-sm rounded-2xl shadow-lg text-center transition-all duration-300 hover:shadow-xl hover:transform hover:-translate-y-2" style="background: var(--bg-card); padding: 2rem; border: 2px solid var(--border-color); box-shadow: 0 4px 12px -2px var(--shadow-color), 0 2px 6px -1px var(--shadow-color);" onmouseover="this.style.borderColor='var(--accent-primary)'; this.style.boxShadow='0 8px 25px -5px var(--particle-glow), 0 4px 12px -2px var(--shadow-color)'" onmouseout="this.style.borderColor='var(--border-color)'; this.style.boxShadow='0 4px 12px -2px var(--shadow-color), 0 2px 6px -1px var(--shadow-color)'">
                    <div class="w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-6">
                        <span class="text-3xl">🎯</span>
                    </div>
                    <h3 class="text-2xl font-semibold mb-4" style="color: var(--text-primary); font-size: 1.5rem;">Decision Making under Uncertainty</h3>
                    <p class="leading-relaxed" style="color: var(--text-secondary); font-size: 1.125rem;">
                        Develop methods for robust and adaptive decision-making in partially observable or stochastic environments, ensuring systems can safely navigate strict constraints and unpredictable scenarios.
                    </p>
                </div>

                <!-- World Models Tile -->
                <div class="backdrop-blur-sm rounded-2xl shadow-lg text-center transition-all duration-300 hover:shadow-xl hover:transform hover:-translate-y-2" style="background: var(--bg-card); padding: 2rem; border: 2px solid var(--border-color); box-shadow: 0 4px 12px -2px var(--shadow-color), 0 2px 6px -1px var(--shadow-color);" onmouseover="this.style.borderColor='var(--accent-primary)'; this.style.boxShadow='0 8px 25px -5px var(--particle-glow), 0 4px 12px -2px var(--shadow-color)'" onmouseout="this.style.borderColor='var(--border-color)'; this.style.boxShadow='0 4px 12px -2px var(--shadow-color), 0 2px 6px -1px var(--shadow-color)'">
                    <div class="w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-6">
                        <span class="text-3xl">🌍</span>
                    </div>
                    <h3 class="text-2xl font-semibold mb-4" style="color: var(--text-primary); font-size: 1.5rem;">World Models</h3>
                    <p class="leading-relaxed" style="color: var(--text-secondary); font-size: 1.125rem;">
                        Develop predictive models of environment dynamics that enable agents to simulate future states and visual observations. This facilitates robust look-ahead planning and adaptive execution for long-horizon robotic tasks.
                    </p>
                </div>

                <!-- Foundational Models Tile -->
                <div class="backdrop-blur-sm rounded-2xl shadow-lg text-center transition-all duration-300 hover:shadow-xl hover:transform hover:-translate-y-2" style="background: var(--bg-card); padding: 2rem; border: 2px solid var(--border-color); box-shadow: 0 4px 12px -2px var(--shadow-color), 0 2px 6px -1px var(--shadow-color);" onmouseover="this.style.borderColor='var(--accent-primary)'; this.style.boxShadow='0 8px 25px -5px var(--particle-glow), 0 4px 12px -2px var(--shadow-color)'" onmouseout="this.style.borderColor='var(--border-color)'; this.style.boxShadow='0 4px 12px -2px var(--shadow-color), 0 2px 6px -1px var(--shadow-color)'">
                    <div class="w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-6">
                        <span class="text-3xl">🧠</span>
                    </div>
                    <h3 class="text-2xl font-semibold mb-4" style="color: var(--text-primary); font-size: 1.5rem;">Foundational Models (VLAs)</h3>
                    <p class="leading-relaxed" style="color: var(--text-secondary); font-size: 1.125rem;">
                        Integrate and fine-tune Vision-Language-Action (VLA) pipelines to bridge high-level semantic reasoning with low-level physical control, enabling scalable and generalizable robot learning.
                    </p>
                </div>

                <!-- LLM Tile -->
                <div class="backdrop-blur-sm rounded-2xl shadow-lg text-center transition-all duration-300 hover:shadow-xl hover:transform hover:-translate-y-2" style="background: var(--bg-card); padding: 2rem; border: 2px solid var(--border-color); box-shadow: 0 4px 12px -2px var(--shadow-color), 0 2px 6px -1px var(--shadow-color);" onmouseover="this.style.borderColor='var(--accent-primary)'; this.style.boxShadow='0 8px 25px -5px var(--particle-glow), 0 4px 12px -2px var(--shadow-color)'" onmouseout="this.style.borderColor='var(--border-color)'; this.style.boxShadow='0 4px 12px -2px var(--shadow-color), 0 2px 6px -1px var(--shadow-color)'">
                    <div class="w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-6">
                        <span class="text-3xl">💬</span>
                    </div>
                    <h3 class="text-2xl font-semibold mb-4" style="color: var(--text-primary); font-size: 1.5rem;">Large Language Models (LLMs)</h3>
                    <p class="leading-relaxed" style="color: var(--text-secondary); font-size: 1.125rem;">
                        Post-train LLMs for advanced reasoning, semantic task planning, and strategic belief manipulation using reinforcement learning paradigms.
                    </p>
                </div>
            </div>

            <!-- Future Vision -->
            <div class="mb-16">
                <h3 class="text-xl font-bold mb-6 flex items-center" style="color: var(--text-primary);">
                    <span class="text-3xl mr-3">🔭</span>
                    Future Vision
                </h3>
                <div class="backdrop-blur-sm rounded-xl p-6 border transition-all duration-300 hover:shadow-xl hover:transform hover:-translate-y-2" style="background: var(--bg-card); border-color: var(--border-color); box-shadow: 0 4px 12px -2px var(--shadow-color), 0 2px 6px -1px var(--shadow-color);" onmouseover="this.style.borderColor='var(--accent-primary)'; this.style.boxShadow='0 8px 25px -5px var(--particle-glow), 0 4px 12px -2px var(--shadow-color)'" onmouseout="this.style.borderColor='var(--border-color)'; this.style.boxShadow='0 4px 12px -2px var(--shadow-color), 0 2px 6px -1px var(--shadow-color)'">
                    <p class="leading-relaxed" style="color: var(--text-secondary);">
                        I am fascinated by how intelligent agents can learn structured, transferable policies that generalize across tasks embodiments, and environments, moving toward autonomous systems capable of learning and reasoning like humans. My long-term goal is to develop generalist robot policies that unify learning, reasoning, and control, advancing adaptable embodied agents for diverse real-world tasks.
                    </p>
                </div>
            </div>

            <!-- Beyond Research -->
            <div>
                <h3 class="text-xl font-bold mb-6 flex items-center" style="color: var(--text-primary);">
                    <span class="text-3xl mr-3">☕</span>
                    Beyond Research
                </h3>
                <div class="backdrop-blur-sm rounded-xl p-6 border transition-all duration-300 hover:shadow-xl hover:transform hover:-translate-y-2" style="background: var(--bg-card); border-color: var(--border-color); box-shadow: 0 4px 12px -2px var(--shadow-color), 0 2px 6px -1px var(--shadow-color);" onmouseover="this.style.borderColor='var(--accent-primary)'; this.style.boxShadow='0 8px 25px -5px var(--particle-glow), 0 4px 12px -2px var(--shadow-color)'" onmouseout="this.style.borderColor='var(--border-color)'; this.style.boxShadow='0 4px 12px -2px var(--shadow-color), 0 2px 6px -1px var(--shadow-color)'">
                    <p class="leading-relaxed" style="color: var(--text-secondary);">
                        Outside the lab, I enjoy 
                        <span class="inline-flex items-center mx-1"><span class="text-2xl mr-1">♟️</span>Chess</span>, 
                        <span class="inline-flex items-center mx-1"><span class="text-2xl mr-1">🏸</span>Squash</span>, and 
                        <span class="inline-flex items-center mx-1"><span class="text-2xl mr-1">🏓</span>Table Tennis</span>. 
                        I'm a dedicated <span class="inline-flex items-center mx-1"><span class="text-2xl mr-1">☕</span>coffee enthusiast</span> who enjoys strategy both on and off the board. I also enjoy reading books, watching sci-fi movies and TV shows.
                    </p>
                </div>
            </div>
        </div>
    </section>
"""

    text = text[:start_idx] + new_html + text[end_idx:]

with open(html_file, 'w') as f:
    f.write(text)

print("Updates applied successfully.")
