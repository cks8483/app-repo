<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import HeroSection from './components/HeroSection.vue'
import SkillList from './components/SkillList.vue'
import ProjectGallery from './components/ProjectGallery.vue'

// Reactive State
const profile = ref(null)
const loading = ref(true)
const error = ref(null)

// Environment variable for API URL (defaults to localhost for dev)
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api/profile'

const fetchProfile = async () => {
  try {
    const response = await axios.get(API_URL)
    profile.value = response.data
  } catch (err) {
    console.error('Failed to fetch profile:', err)
    error.value = "Failed to load profile data. Please ensure the backend is running."
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  fetchProfile()
})
</script>

<template>
  <div class="min-h-screen bg-slate-900 text-slate-200 font-sans selection:bg-emerald-500 selection:text-white">
    <!-- Loading State -->
    <div v-if="loading" class="flex items-center justify-center h-screen">
      <div class="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-emerald-500"></div>
    </div>

    <!-- Error State -->
    <div v-else-if="error" class="flex flex-col items-center justify-center h-screen text-red-400">
      <p class="text-xl font-semibold">{{ error }}</p>
      <button @click="fetchProfile" class="mt-4 px-4 py-2 bg-slate-800 rounded hover:bg-slate-700 transition">
        Retry
      </button>
    </div>

    <!-- Main Content -->
    <main v-else class="container mx-auto px-6 py-12 max-w-4xl space-y-16">
      <HeroSection :name="profile.name" :bio="profile.bio" />
      <SkillList :skills="profile.skills" />
      <ProjectGallery :projects="profile.projects" />
      
      <footer class="text-center text-slate-500 text-sm pt-12 border-t border-slate-800">
        &copy; {{ new Date().getFullYear() }} {{ profile.name }}. All rights reserved.
      </footer>
    </main>
  </div>
</template>