<script setup>
// 상단 네비게이션 바 컴포넌트
// - 로고, 기본 메뉴, 관리자 모드 토글 스위치 포함

import { computed } from 'vue'
import { Menu, Shield } from 'lucide-vue-next'

// 부모(App)로부터 전달받는 props
const props = defineProps({
  // 관리자 모드 여부 (양방향 바인딩용)
  adminMode: {
    type: Boolean,
    default: false
  }
})

// 부모로 상태 변경을 알리기 위한 emit
const emit = defineEmits(['update:admin-mode'])

// 토글 클릭 시 호출되는 핸들러
const toggleAdmin = () => {
  emit('update:admin-mode', !props.adminMode)
}

// 관리자 모드 텍스트
const adminLabel = computed(() => (props.adminMode ? '관리자 모드 ON' : '관리자 모드 OFF'))
</script>

<template>
  <!-- 글래스모피즘 스타일의 상단 고정 네비게이션 -->
  <header
    class="fixed top-0 inset-x-0 z-40 border-b border-slate-800/70 bg-slate-950/70 backdrop-blur-xl"
  >
    <nav
      class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between gap-4"
    >
      <!-- 좌측 로고/타이틀 -->
      <div class="flex items-center gap-2">
        <div
          class="h-8 w-8 rounded-xl bg-gradient-to-tr from-teal-500 to-indigo-500 flex items-center justify-center text-xs font-bold shadow-lg shadow-teal-500/40"
        >
          CCH
        </div>
        <div class="flex flex-col leading-tight">
          <span class="text-sm font-semibold text-slate-50">CI/CD Portfolio</span>
          <span class="text-[11px] text-slate-400">Developer · Platform Engineer</span>
        </div>
      </div>

      <!-- 우측 메뉴 + 관리자 토글 -->
      <div class="flex items-center gap-4">
        <!-- 데스크탑 메뉴 -->
        <div class="hidden sm:flex items-center gap-6 text-xs font-medium">
          <a href="#projects" class="text-slate-300 hover:text-teal-300 transition-colors">
            프로젝트
          </a>
          <a href="#about" class="text-slate-400 hover:text-teal-300 transition-colors">
            소개
          </a>
          <a href="#contact" class="text-slate-400 hover:text-teal-300 transition-colors">
            연락
          </a>
        </div>

        <!-- 관리자 모드 토글 스위치 -->
        <button
          type="button"
          @click="toggleAdmin"
          class="group relative inline-flex items-center gap-2 rounded-full border border-slate-700/80 bg-slate-900/70 px-2.5 py-1.5 text-[11px] font-medium text-slate-300 shadow-sm hover:border-teal-400/80 hover:text-teal-200 hover:bg-slate-900/90 transition-colors"
        >
          <div
            class="relative flex items-center gap-1.5 pr-1.5 border-r border-slate-700/60 text-[10px] uppercase tracking-[0.12em]"
          >
            <Shield
              class="h-3.5 w-3.5 text-slate-400 group-hover:text-teal-400 transition-colors"
            />
            <span class="text-slate-400 group-hover:text-teal-300">
              Admin
            </span>
          </div>
          <div class="flex items-center gap-1">
            <!-- 스위치 배경 -->
            <span
              class="relative inline-flex items-center h-4 w-7 rounded-full bg-slate-700/80 transition-colors"
              :class="props.adminMode ? 'bg-teal-500/80' : 'bg-slate-700/80'"
            >
              <!-- 스위치 핸들 -->
              <span
                class="inline-block h-3 w-3 rounded-full bg-white shadow transform transition-transform duration-200"
                :class="props.adminMode ? 'translate-x-3' : 'translate-x-0.5'"
              />
            </span>
            <span
              class="hidden sm:inline text-[11px]"
              :class="props.adminMode ? 'text-teal-300' : 'text-slate-400'"
            >
              {{ adminLabel }}
            </span>
          </div>
        </button>

        <!-- 모바일 메뉴 아이콘 (실제 드로어는 추후 구현 가능) -->
        <button
          type="button"
          class="sm:hidden inline-flex items-center justify-center rounded-full border border-slate-700/80 bg-slate-900/70 p-1.5 text-slate-300 hover:bg-slate-800 hover:text-white transition-colors"
          aria-label="메뉴 열기"
        >
          <Menu class="h-4 w-4" />
        </button>
      </div>
    </nav>
  </header>
</template>


