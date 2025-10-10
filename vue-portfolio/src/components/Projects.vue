<template>
  <section id="projects" ref="sectionRef" class="py-20">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div 
        class="text-center mb-16"
        v-motion
        :initial="{ opacity: 0, y: 30 }"
        :visible="{ opacity: 1, y: 0 }"
        :transition="{ duration: 800 }"
      >
        <h2 class="section-title">Projects</h2>
        <div class="w-24 h-1 bg-accent mx-auto mb-8"></div>
        <p class="text-lg text-lightSlate max-w-3xl mx-auto">
          Selected projects showcasing my work in AI, robotics, and multi-agent systems.
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
          v-if="projects.length > 0"
        >
          <div
            v-for="(project, index) in projects"
            :key="index"
            class="card group cursor-pointer"
            v-motion
            :initial="{ opacity: 0, y: 20 }"
            :visible="{ opacity: 1, y: 0 }"
            :transition="{ duration: 600, delay: index * 100 }"
            :hover="{ 
              scale: 1.05, 
              y: -5,
              transition: { duration: 200 }
            }"
          >
            <div class="h-full flex flex-col">
              <h3 class="text-xl font-semibold text-white mb-3 group-hover:text-accent transition-colors duration-200">
                {{ project.title }}
              </h3>
              
              <p v-if="project.content" class="text-lightSlate group-hover:text-lightestSlate transition-colors duration-200 flex-1">
                {{ project.content }}
              </p>

              <a
                v-if="project.link"
                :href="project.link"
                target="_blank"
                rel="noopener noreferrer"
                class="inline-flex items-center text-accent hover:text-white mt-4 transition-colors duration-200"
                v-motion
                :hover="{ scale: 1.05 }"
                :tap="{ scale: 0.95 }"
              >
                <span class="mr-2">View Project</span>
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                </svg>
              </a>
            </div>
          </div>
        </div>
        <div v-else class="col-span-full text-center py-12">
          <div class="text-lightSlate text-lg">
            No projects available at the moment.
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { ref, onMounted } from 'vue'
import { getAllContent } from '../utils/markdown'

export default {
  name: 'Projects',
  setup() {
    const sectionRef = ref(null)
    const projects = ref([])

    onMounted(() => {
      projects.value = getAllContent('projects')
    })

    return {
      sectionRef,
      projects
    }
  }
}
</script>
