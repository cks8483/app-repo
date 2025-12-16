<script setup>
defineProps({
  name: {
    type: String,
    required: true
  },
  bio: {
    type: String,
    required: true
  }
})
</script>

<template>
  <section class="text-center space-y-4">
    <div class="inline-block p-1 rounded-full bg-gradient-to-tr from-emerald-500 to-cyan-500 mb-4">
        <!-- Placeholder for Avatar -->
        <div class="h-24 w-24 rounded-full bg-slate-800 flex items-center justify-center text-2xl font-bold text-slate-400">
            {{ name.charAt(0) }}
        </div>
    </div>
    <h1 class="text-4xl md:text-6xl font-extrabold tracking-tight text-white">
      Hi, I'm <span class="text-transparent bg-clip-text bg-gradient-to-r from-emerald-400 to-cyan-400">{{ name }}</span>
    </h1>
    <p class="text-lg md:text-xl text-slate-400 max-w-2xl mx-auto leading-relaxed">
      {{ bio }}
    </p>
  </section>
</template>