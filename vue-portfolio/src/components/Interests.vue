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
        class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 max-w-6xl mx-auto"
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
        title: "Reinforcement Learning",
        description: "Develop algorithms that enable agents to learn close-to-optimal planning and control strategies in robotics, leveraging human demonstrations, fixed datasets, or interactions with dynamic environments.",
        icon: "🤖"
      },
      {
        title: "Sequence Modelling",
        description: "Design models that predict and understand sequential data, including temporal patterns, trajectories, and planning sequences.",
        icon: "📈"
      },
      {
        title: "Decision Making under Uncertainty",
        description: "Develop methods for robust and adaptive decision-making in partially observable or stochastic environments.",
        icon: "🎯"
      },
      {
        title: "Multi-Agent Reinforcement Learning (MARL)",
        description: "Study interactions of multiple agents learning together, including cooperation, competition, and strategic reasoning.",
        icon: "👥"
      },
      {
        title: "Safe and Robust Control",
        description: "Design control strategies for autonomous systems that ensure safety, reliability, and robustness under uncertainty.",
        icon: "🛡️"
      },
      {
        title: "Planning",
        description: "Develop algorithms for efficient and adaptive planning in robotics and AI systems, including long-horizon decision-making.",
        icon: "🗺️"
      }
    ]

    return {
      sectionRef,
      interests
    }
  }
}
</script>
