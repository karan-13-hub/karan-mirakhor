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
        
        <div class="space-y-6 text-lg text-lightSlate leading-relaxed">
          <p>
            I am a Graduate Research Assistant at the Robotics Institute, Carnegie Mellon University, 
            advised by Prof. Katia Sycara.
          </p>
          <p>
            My research explores multi-agent reinforcement learning (MARL) in cooperative and competitive 
            environments, emphasizing belief modeling, opponent adaptation, and decision-making under uncertainty.
          </p>
          <p>
            Previously, I was a Pre-doctoral Research Fellow at TCS Research, India, working on task planning 
            for indoor object rearrangement under partial observability.
          </p>
          <p>
            I hold a B.Tech (Honors) in Electronics and Communication Engineering from IIIT Hyderabad, 
            where I received the Program Gold Medal for highest GPA.
          </p>
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
            <div class="text-3xl font-bold text-accent mb-2">3+</div>
            <div class="text-lightSlate">Years Research Experience</div>
          </div>
          <div class="text-center">
            <div class="text-3xl font-bold text-accent mb-2">5+</div>
            <div class="text-lightSlate">Publications</div>
          </div>
          <div class="text-center">
            <div class="text-3xl font-bold text-accent mb-2">10+</div>
            <div class="text-lightSlate">Projects</div>
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
