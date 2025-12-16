<script setup>
defineProps({
  skills: {
    type: Array,
    required: true
  }
})
</script>

<template>
  <section>
    <h2 class="text-2xl font-bold text-white mb-6 border-l-4 border-emerald-500 pl-4">Technical Skills</h2>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <div v-for="skill in skills" :key="skill.name" class="bg-slate-800 p-4 rounded-lg shadow-lg">
        <div class="flex justify-between items-end mb-2">
          <span class="font-medium text-slate-200">{{ skill.name }}</span>
          <span class="text-sm text-emerald-400 font-mono">{{ skill.proficiency }}%</span>
        </div>
        <div class="w-full bg-slate-700 rounded-full h-2.5">
          <div 
            class="bg-gradient-to-r from-emerald-500 to-cyan-500 h-2.5 rounded-full transition-all duration-1000 ease-out" 
            :style="{ width: `${skill.proficiency}%` }"
          ></div>
        </div>
      </div>
    </div>
  </section>
</template>