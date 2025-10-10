<template>
  <section id="research" ref="sectionRef" class="py-20">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div 
        class="text-center mb-16"
        v-motion
        :initial="{ opacity: 0, y: 30 }"
        :visible="{ opacity: 1, y: 0 }"
        :transition="{ duration: 800 }"
      >
        <h2 class="section-title">Research Interests</h2>
        <div class="w-24 h-1 bg-accent mx-auto mb-8"></div>
        <p class="text-lg text-lightSlate max-w-3xl mx-auto">
          My research focuses on advancing artificial intelligence through multi-agent systems, 
          with particular emphasis on learning, adaptation, and strategic decision-making.
        </p>
      </div>

      <div 
        class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8"
        v-motion
        :initial="{ opacity: 0, y: 30 }"
        :visible="{ opacity: 1, y: 0 }"
        :transition="{ duration: 800, delay: 200 }"
      >
        <div
          v-for="(interest, index) in interests"
          :key="index"
          class="card group cursor-pointer"
          v-motion
          :hover="{ 
            scale: 1.05, 
            y: -5,
            transition: { duration: 200 }
          }"
          :tap="{ scale: 0.95 }"
        >
          <div class="text-center">
            <div class="text-4xl mb-4 group-hover:scale-110 transition-transform duration-200">
              {{ interest.icon }}
            </div>
            <h3 class="text-xl font-semibold text-white mb-3 group-hover:text-accent transition-colors duration-200">
              {{ interest.title }}
            </h3>
            <p class="text-lightSlate group-hover:text-lightestSlate transition-colors duration-200">
              {{ interest.description }}
            </p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { ref } from 'vue'

export default {
  name: 'Interests',
  setup() {
    const sectionRef = ref(null)

    const interests = [
      {
        title: "Multi-Agent Reinforcement Learning",
        description: "Cooperative and competitive learning in multi-agent systems",
        icon: "🤖"
      },
      {
        title: "Robotics",
        description: "Autonomous systems and robotic manipulation",
        icon: "🦾"
      },
      {
        title: "Imitation Learning",
        description: "Learning from human demonstrations and expert behavior",
        icon: "👥"
      },
      {
        title: "Decision Making under Uncertainty",
        description: "Robust decision-making in partially observable environments",
        icon: "🎯"
      },
      {
        title: "Deception in AI",
        description: "Strategic deception and adversarial behavior in AI systems",
        icon: "🎭"
      }
    ]

    return {
      sectionRef,
      interests
    }
  }
}
</script>
