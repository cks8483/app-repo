<script setup>
// 히어로 섹션
// - 중앙 정렬 레이아웃
// - 이름은 그라데이션 텍스트로 강조
// - "프로젝트 보기", "이력서 다운로드" 메인 버튼 배치

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

// 버튼 클릭은 현재 UI 데모 단계이므로 console.log 로 처리
const handleClick = (type) => {
  console.log(`[HERO] ${type} 버튼 클릭`)
}
</script>

<template>
  <section
    class="min-h-[60vh] flex flex-col items-center justify-center text-center gap-8"
    id="top"
  >
    <!-- 아바타 + 이름 -->
    <div class="flex flex-col items-center gap-4">
      <!-- 원형 아바타 (이니셜) -->
      <div
        class="relative inline-flex items-center justify-center h-24 w-24 rounded-full bg-gradient-to-tr from-slate-800 via-slate-900 to-slate-950 shadow-lg shadow-teal-500/30"
      >
        <div
          class="h-20 w-20 rounded-full bg-slate-900/80 border border-slate-700 flex items-center justify-center text-3xl font-bold text-slate-300"
        >
          {{ name.charAt(0) }}
        </div>
        <div
          class="absolute -bottom-1 -right-1 h-7 px-2 rounded-full bg-gradient-to-r from-teal-500 to-indigo-500 text-[10px] font-semibold text-slate-950 flex items-center shadow-lg shadow-teal-500/50"
        >
          ONLINE
        </div>
      </div>

      <!-- 이름 + 타이틀/소개 -->
      <div class="space-y-3 max-w-3xl">
        <h1
          class="text-4xl sm:text-5xl md:text-6xl font-extrabold tracking-tight text-slate-50 leading-tight"
        >
          <span class="block text-sm sm:text-base font-medium text-teal-300 mb-2">
            DevOps / Backend &amp; Platform Engineer
          </span>
          <span class="text-transparent bg-clip-text bg-gradient-to-r from-teal-400 via-cyan-400 to-indigo-400">
            {{ name }}
          </span>
        </h1>
        <p class="text-sm sm:text-base md:text-lg text-slate-300/90 leading-relaxed">
          {{ bio }}
        </p>
      </div>
    </div>

    <!-- 주요 CTA 버튼 영역 -->
    <div class="flex flex-wrap items-center justify-center gap-3 sm:gap-4">
      <!-- 프로젝트 보기 -->
      <button
        type="button"
        @click="handleClick('프로젝트 보기')"
        class="inline-flex items-center justify-center gap-2 rounded-full bg-gradient-to-r from-teal-500 via-cyan-500 to-indigo-500 px-6 sm:px-8 py-2.5 text-sm sm:text-base font-semibold text-slate-950 shadow-lg shadow-teal-500/40 hover:shadow-teal-500/60 hover:-translate-y-0.5 transition-all"
      >
        <span>프로젝트 보기</span>
      </button>

      <!-- 이력서 다운로드 -->
      <button
        type="button"
        @click="handleClick('이력서 다운로드')"
        class="inline-flex items-center justify-center gap-2 rounded-full border border-slate-700/80 bg-slate-900/80 px-6 sm:px-8 py-2.5 text-sm sm:text-base font-medium text-slate-100 hover:border-indigo-400/80 hover:bg-slate-900 hover:text-indigo-100 transition-colors"
      >
        <span>이력서 다운로드</span>
      </button>
    </div>
  </section>
</template>
