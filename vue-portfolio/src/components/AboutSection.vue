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
          <p>I am a <strong>Graduate Research Assistant</strong> at the <a href="https://www.ri.cmu.edu/" target="_blank" class="accent-link text-cyan-400 hover:text-cyan-300">Robotics Institute</a>, <a href="https://www.cmu.edu/" target="_blank" class="accent-link text-cyan-400 hover:text-cyan-300">Carnegie Mellon University</a>, and a <strong>second-year Master of Science (Research) student in Robotics (MSR)</strong>.</p>
          
          <p>I strive to build <strong>intelligent multi-agent systems</strong> that can <em>perceive, reason, and collaborate</em> with human-level efficiency, ultimately advancing the field of <strong>Multi-Agent Reinforcement Learning (MARL)</strong>. My work focuses on developing agents that can seamlessly coordinate with previously unseen partners and develop strategic behaviors through <em>belief modeling and opponent adaptation</em>.</p>
          
          <p>Previously, I was a <strong>Pre-doctoral Research Fellow</strong> at <a href="https://www.tcs.com/research-and-innovation" target="_blank" class="accent-link text-cyan-400 hover:text-cyan-300">TCS Research</a> with <a href="https://scholar.google.co.in/citations?user=Eqf8NrEAAAAJ&hl=en" target="_blank" class="accent-link text-cyan-400 hover:text-cyan-300">Dr. Brojeshwar Bhowmick</a>. I completed my B.Tech (Honors) at <a href="https://www.iiit.ac.in/" target="_blank" class="accent-link text-cyan-400 hover:text-cyan-300">IIIT Hyderabad</a> and <a href="https://robotics.iiit.ac.in/" target="_blank" class="accent-link text-cyan-400 hover:text-cyan-300">Robotics Research Center</a>, advised by <a href="https://scholar.google.co.in/citations?user=5i1t_QgAAAAJ&hl=en" target="_blank" class="accent-link text-cyan-400 hover:text-cyan-300">Dr. Harikumar Kandath</a>. My work has been recognized with the <strong>Program Gold Medal</strong> for highest GPA and research contributions in <strong>robotic task planning</strong> and <strong>aerial manipulation control</strong>.</p>
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
