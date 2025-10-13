<template>
  <section id="about" ref="sectionRef" class="py-20 bg-lightNavy/30">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div 
        class="max-w-4xl mx-auto text-center"
        v-motion
        :initial="{ opacity: 0, y: 30 }"
        :visible="{ opacity: 1, y: 0 }"
        :transition="{ duration: 800 }"
      >
        <h2 class="section-title">About Me</h2>
        <div class="w-24 h-1 bg-accent mx-auto mb-8"></div>
        
        <div class="about-content text-lg text-gray-200 leading-relaxed">
          <p>Hello! I'm <strong>Karan Mirakhor</strong>, a <strong>second-year Master of Science (Research) student in Robotics (MSR) at the <a href="https://www.ri.cmu.edu/" target="_blank" class="accent-link text-cyan-400 hover:text-cyan-300">Robotics Institute</a>, <a href="https://www.cmu.edu/" target="_blank" class="accent-link text-cyan-400 hover:text-cyan-300">Carnegie Mellon University</a></strong>.</p>
          
          <p><strong>Graduate Research Assistant</strong> - <a href="https://www.ri.cmu.edu/robotics-groups/advanced-agent-robotics-technology-lab/" target="_blank" class="accent-link text-cyan-400 hover:text-cyan-300">Advanced Agent Robotics Technology Lab</a><br>
          <strong>Advisor:</strong> <a href="https://www.cs.cmu.edu/~sycara/" target="_blank" class="accent-link text-cyan-400 hover:text-cyan-300">Prof. Katia Sycara</a></p>
          
          <p>My research primarily focuses on <strong>Multi-Agent Reinforcement Learning (MARL)</strong>. Specifically, my work is on:</p>
          
          <div class="research-areas mt-6">
            <div class="research-area bg-slate-900/20 p-6 rounded-lg mb-4 border-l-4 border-cyan-400">
              <h3 class="area-title text-cyan-400 text-xl font-semibold mb-3 flex items-center gap-2">
                🧠 Zero-shot Coordination in Cooperative MARL
              </h3>
              <p>Developing agents that can seamlessly collaborate with previously unseen partners without additional training. Specifically, I focus on <strong>offline-to-online training frameworks</strong> that leverage behavioral diversity in offline datasets and enable efficient online adaptation using belief models.</p>
            </div>
            
            <div class="research-area bg-slate-900/20 p-6 rounded-lg mb-4 border-l-4 border-cyan-400">
              <h3 class="area-title text-cyan-400 text-xl font-semibold mb-3 flex items-center gap-2">
                🎭 Competitive MARL and Targeted Deception
              </h3>
              <p>Developing <strong>targeted deception strategies</strong> by leveraging <strong>higher-order opponent belief models</strong> and analyzing <strong>historical response patterns</strong> to identify and exploit individual behavioral vulnerabilities.</p>
            </div>
          </div>
          
          <div class="experience-section mt-8">
            <h3 class="section-subtitle text-cyan-400 text-2xl font-semibold mb-6 flex items-center gap-2">
              📚 Previous Research Experience
            </h3>
            
            <div class="experience-item bg-slate-900/10 p-6 rounded-lg mb-6 border-l-3 border-cyan-400">
              <p class="experience-title text-white text-lg font-semibold mb-2">
                <strong>Pre-doctoral Research Fellow</strong> — <a href="https://www.tcs.com/research-and-innovation" target="_blank" class="accent-link text-cyan-400 hover:text-cyan-300"><strong>TCS Research</strong></a>
              </p>
              <p class="experience-advisor text-gray-400 mb-4 italic">
                <em>Advisor: <a href="https://scholar.google.co.in/citations?user=Eqf8NrEAAAAJ&hl=en" target="_blank" class="accent-link text-cyan-400 hover:text-cyan-300">Dr. Brojeshwar Bhowmick</a></em>
              </p>
              <p class="experience-description text-gray-200 leading-relaxed">
                Explored <strong>Task Planning for Indoor Object Rearrangement</strong> under <strong>partial observability (POMDP)</strong>. Developed scalable <strong>graph-based scene representations</strong>, utilized <strong>Large Language Models (LLMs)</strong> for semantic object search, and applied <strong>Deep RL</strong> for efficient single and multi-room planning.
              </p>
            </div>
            
            <div class="experience-item bg-slate-900/10 p-6 rounded-lg mb-6 border-l-3 border-cyan-400">
              <h3 class="section-subtitle text-cyan-400 text-xl font-semibold mb-4 flex items-center gap-2">
                🎓 B.Tech (Honors) in Electronics and Communication Engineering (ECE)
              </h3>
              <p class="experience-title text-white text-lg font-semibold mb-2">
                <strong>IIIT Hyderabad</strong> — <a href="https://www.iiit.ac.in/" target="_blank" class="accent-link text-cyan-400 hover:text-cyan-300">IIIT Hyderabad</a>
              </p>
              <p class="experience-advisor text-gray-400 mb-2 italic">
                <em>Research Assistant, <a href="https://robotics.iiit.ac.in/" target="_blank" class="accent-link text-cyan-400 hover:text-cyan-300">Robotics Research Center</a></em>
              </p>
              <p class="experience-advisor text-gray-400 mb-4 italic">
                <em>Advisor: <a href="https://scholar.google.co.in/citations?user=5i1t_QgAAAAJ&hl=en" target="_blank" class="accent-link text-cyan-400 hover:text-cyan-300">Dr. Harikumar Kandath</a></em>
              </p>
              <p class="experience-description text-gray-200 leading-relaxed">
                Worked on <strong>aerial manipulator control</strong> using <strong>Control Barrier Lyapunov constraints</strong> within a <strong>Model Predictive Controller</strong> for safe and stable operation.
              </p>
            </div>
          </div>
          
          <div class="vision-section bg-slate-900/10 p-6 rounded-lg mb-6 border-l-3 border-cyan-400">
            <h3 class="section-subtitle text-cyan-400 text-2xl font-semibold mb-4 flex items-center gap-2">
              🔭 Future Vision
            </h3>
            <p class="text-gray-200 leading-relaxed mb-4">
              I am fascinated by how <strong>intelligent agents</strong> can learn <strong>structured, transferable policies</strong> that generalize across <strong>tasks, embodiments, and environments</strong>, moving toward autonomous systems capable of <strong>learning and reasoning like humans</strong>.
            </p>
            <p class="text-gray-200 leading-relaxed">
              My long-term goal is to develop <strong>generalist robot policies</strong> that <strong>unify learning, reasoning, and control</strong>, advancing adaptable embodied agents for diverse real-world tasks.
            </p>
          </div>
          
          <div class="personal-section bg-slate-900/10 p-6 rounded-lg mb-6 border-l-3 border-cyan-400">
            <h3 class="section-subtitle text-cyan-400 text-2xl font-semibold mb-4 flex items-center gap-2">
              ☕ Beyond Research
            </h3>
            <p class="text-gray-200 leading-relaxed">
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
