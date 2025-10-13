<template>
  <section id="about" ref="sectionRef" class="py-20 bg-lightNavy/30">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div 
        class="max-w-5xl mx-auto"
        v-motion
        :initial="{ opacity: 0, y: 30 }"
        :visible="{ opacity: 1, y: 0 }"
        :transition="{ duration: 800 }"
      >
        <h2 class="section-title text-center text-4xl font-bold text-white mb-8">About Me</h2>
        <div class="w-24 h-1 bg-teal-500 mx-auto mb-12"></div>
        
        <div class="about-content text-lg text-gray-100 leading-relaxed">
          <!-- Intro Section -->
          <div class="about-intro mb-12">
            <p class="intro-text text-xl leading-relaxed mb-6 text-gray-100">
              Hello! I'm <strong class="name-highlight text-white font-bold">Karan Mirakhor</strong>, a <strong>second-year Master of Science (Research) student in Robotics (MSR) at the <a href="https://www.ri.cmu.edu/" target="_blank" class="link-accent text-teal-400 hover:text-teal-300 transition-colors duration-300">Robotics Institute</a>, <a href="https://www.cmu.edu/" target="_blank" class="link-accent text-teal-400 hover:text-teal-300 transition-colors duration-300">Carnegie Mellon University</a></strong>.
            </p>
            
            <div class="position-info bg-slate-900/40 p-6 rounded-lg border-l-4 border-teal-500 mb-6">
              <p class="position-title text-teal-400 text-lg font-semibold mb-2">
                <strong>Graduate Research Assistant</strong> - <a href="https://www.ri.cmu.edu/robotics-groups/advanced-agent-robotics-technology-lab/" target="_blank" class="link-accent text-teal-400 hover:text-teal-300 transition-colors duration-300">Advanced Agent Robotics Technology Lab</a>
              </p>
              <p class="advisor-info text-gray-400">
                <strong>Advisor:</strong> <a href="https://www.cs.cmu.edu/~sycara/" target="_blank" class="link-accent text-teal-400 hover:text-teal-300 transition-colors duration-300">Prof. Katia Sycara</a>
              </p>
            </div>
            
            <p class="research-focus text-lg text-gray-100">
              My research primarily focuses on <strong class="highlight-text text-teal-400 font-semibold">Multi-Agent Reinforcement Learning (MARL)</strong>. Specifically, my work is on:
            </p>
          </div>
          
          <!-- Research Areas -->
          <div class="research-areas mb-12">
            <div class="research-area bg-slate-900/30 p-8 rounded-xl mb-6 border border-teal-500/20 hover:border-teal-500/40 transition-all duration-300 hover:-translate-y-1 hover:shadow-lg hover:shadow-teal-500/10">
              <h3 class="area-title text-teal-400 text-xl font-semibold mb-4 flex items-center gap-3">
                <span class="area-icon text-lg">🧠</span>
                Zero-shot Coordination in Cooperative MARL
              </h3>
              <p class="area-description text-gray-100 leading-relaxed">
                Developing agents that can seamlessly collaborate with previously unseen partners without additional training. Specifically, I focus on <strong>offline-to-online training frameworks</strong> that leverage behavioral diversity in offline datasets and enable efficient online adaptation using belief models.
              </p>
            </div>
            
            <div class="research-area bg-slate-900/30 p-8 rounded-xl mb-6 border border-teal-500/20 hover:border-teal-500/40 transition-all duration-300 hover:-translate-y-1 hover:shadow-lg hover:shadow-teal-500/10">
              <h3 class="area-title text-teal-400 text-xl font-semibold mb-4 flex items-center gap-3">
                <span class="area-icon text-lg">🎭</span>
                Competitive MARL and Targeted Deception
              </h3>
              <p class="area-description text-gray-100 leading-relaxed">
                Developing <strong>targeted deception strategies</strong> by leveraging <strong>higher-order opponent belief models</strong> and analyzing <strong>historical response patterns</strong> to identify and exploit individual behavioral vulnerabilities.
              </p>
            </div>
          </div>
          
          <!-- Experience Section -->
          <div class="experience-section mb-12">
            <h3 class="section-subtitle text-teal-400 text-2xl font-semibold mb-8 flex items-center gap-3">
              <span class="section-icon text-xl">📚</span>
              Previous Research Experience
            </h3>
            
            <div class="experience-item bg-slate-900/20 p-8 rounded-lg mb-6 border-l-4 border-teal-500">
              <p class="experience-title text-white text-lg font-semibold mb-2">
                <strong>Pre-doctoral Research Fellow</strong> — <a href="https://www.tcs.com/research-and-innovation" target="_blank" class="link-accent text-teal-400 hover:text-teal-300 transition-colors duration-300"><strong>TCS Research</strong></a>
              </p>
              <p class="experience-advisor text-gray-400 mb-4 italic">
                <em>Advisor: <a href="https://scholar.google.co.in/citations?user=Eqf8NrEAAAAJ&hl=en" target="_blank" class="link-accent text-teal-400 hover:text-teal-300 transition-colors duration-300">Dr. Brojeshwar Bhowmick</a></em>
              </p>
              <p class="experience-description text-gray-100 leading-relaxed">
                Explored <strong>Task Planning for Indoor Object Rearrangement</strong> under <strong>partial observability (POMDP)</strong>. Developed scalable <strong>graph-based scene representations</strong>, utilized <strong>Large Language Models (LLMs)</strong> for semantic object search, and applied <strong>Deep RL</strong> for efficient single and multi-room planning.
              </p>
            </div>
            
            <div class="experience-item bg-slate-900/20 p-8 rounded-lg mb-6 border-l-4 border-teal-500">
              <h3 class="section-subtitle text-teal-400 text-xl font-semibold mb-4 flex items-center gap-3">
                <span class="section-icon text-lg">🎓</span>
                B.Tech (Honors) in Electronics and Communication Engineering (ECE)
              </h3>
              <p class="experience-title text-white text-lg font-semibold mb-2">
                <strong>IIIT Hyderabad</strong> — <a href="https://www.iiit.ac.in/" target="_blank" class="link-accent text-teal-400 hover:text-teal-300 transition-colors duration-300">IIIT Hyderabad</a>
              </p>
              <p class="experience-advisor text-gray-400 mb-2 italic">
                <em>Research Assistant, <a href="https://robotics.iiit.ac.in/" target="_blank" class="link-accent text-teal-400 hover:text-teal-300 transition-colors duration-300">Robotics Research Center</a></em>
              </p>
              <p class="experience-advisor text-gray-400 mb-4 italic">
                <em>Advisor: <a href="https://scholar.google.co.in/citations?user=5i1t_QgAAAAJ&hl=en" target="_blank" class="link-accent text-teal-400 hover:text-teal-300 transition-colors duration-300">Dr. Harikumar Kandath</a></em>
              </p>
              <p class="experience-description text-gray-100 leading-relaxed">
                Worked on <strong>aerial manipulator control</strong> using <strong>Control Barrier Lyapunov constraints</strong> within a <strong>Model Predictive Controller</strong> for safe and stable operation.
              </p>
            </div>
          </div>
          
          <!-- Vision Section -->
          <div class="vision-section bg-slate-900/30 p-8 rounded-xl mb-6 border border-teal-500/20">
            <h3 class="section-subtitle text-teal-400 text-2xl font-semibold mb-6 flex items-center gap-3">
              <span class="section-icon text-xl">🔭</span>
              Future Vision
            </h3>
            <p class="vision-text text-gray-100 leading-relaxed mb-4">
              I am fascinated by how <strong>intelligent agents</strong> can learn <strong>structured, transferable policies</strong> that generalize across <strong>tasks, embodiments, and environments</strong>, moving toward autonomous systems capable of <strong>learning and reasoning like humans</strong>.
            </p>
            <p class="vision-text text-gray-100 leading-relaxed">
              My long-term goal is to develop <strong>generalist robot policies</strong> that <strong>unify learning, reasoning, and control</strong>, advancing adaptable embodied agents for diverse real-world tasks.
            </p>
          </div>
          
          <!-- Personal Section -->
          <div class="personal-section bg-slate-900/30 p-8 rounded-xl mb-6 border border-teal-500/20">
            <h3 class="section-subtitle text-teal-400 text-2xl font-semibold mb-4 flex items-center gap-3">
              <span class="section-icon text-xl">☕</span>
              Beyond Research
            </h3>
            <p class="personal-text text-gray-100 leading-relaxed">
              Outside the lab, I enjoy ♟️ <strong>Chess</strong>, 🏸 <strong>Squash</strong>, and 🏓 <strong>Table Tennis</strong>. I'm a dedicated ☕ <strong>coffee enthusiast</strong> who enjoys strategy both on and off the board.
            </p>
          </div>
        </div>

        <!-- Research Stats -->
        <div 
          class="grid grid-cols-1 md:grid-cols-3 gap-8 mt-16"
          v-motion
          :initial="{ opacity: 0, y: 20 }"
          :visible="{ opacity: 1, y: 0 }"
          :transition="{ duration: 800, delay: 300 }"
        >
          <div class="text-center">
            <div class="text-3xl font-bold text-accent mb-2">5+</div>
            <div class="text-lightSlate">Years Research Experience</div>
          </div>
          <div class="text-center">
            <div class="text-3xl font-bold text-accent mb-2">2+</div>
            <div class="text-lightSlate">Years Job Experience</div>
          </div>
          <div class="text-center">
            <div class="text-3xl font-bold text-accent mb-2">3+</div>
            <div class="text-lightSlate">Publications & Patents</div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { ref } from 'vue'

export default {
  name: 'AboutSection',
  setup() {
    const sectionRef = ref(null)

    return {
      sectionRef
    }
  }
}
</script>
