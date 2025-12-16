<script setup>
defineProps({
  projects: {
    type: Array,
    required: true
  }
})
</script>

<template>
  <section>
    <h2 class="text-2xl font-bold text-white mb-6 border-l-4 border-cyan-500 pl-4">Featured Projects</h2>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <article 
        v-for="project in projects" 
        :key="project.title" 
        class="group bg-slate-800 rounded-xl p-6 hover:bg-slate-750 transition-all duration-300 hover:-translate-y-1 hover:shadow-xl border border-slate-700"
      >
        <h3 class="text-xl font-bold text-white mb-2 group-hover:text-cyan-400 transition-colors">
          {{ project.title }}
        </h3>
        <p class="text-slate-400 mb-6 h-20 overflow-hidden text-ellipsis">
          {{ project.description }}
        </p>
        <a 
          :href="project.link" 
          target="_blank" 
          rel="noopener noreferrer"
          class="inline-flex items-center text-sm font-semibold text-emerald-400 hover:text-emerald-300 transition-colors"
        >
          View Project 
          <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 ml-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3" />
          </svg>
        </a>
      </article>
    </div>
  </section>
</template>