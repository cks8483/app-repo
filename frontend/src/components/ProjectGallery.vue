<script setup>
// 프로젝트 갤러리 컴포넌트
// - 반응형 그리드 (모바일 1열, 데스크탑 3열)
// - 카드마다 이미지, 제목, 설명, 기술 태그 표시
// - 호버 시 살짝 확대(scale) 애니메이션 적용

defineProps({
  projects: {
    type: Array,
    required: true
  },
  // 관리자 모드 여부
  adminMode: {
    type: Boolean,
    default: false
  }
})
</script>

<template>
  <section id="projects" class="space-y-4">
    <!-- 섹션 타이틀 -->
    <div class="flex items-baseline justify-between gap-3">
      <div>
        <h2
          class="inline-flex items-center gap-2 text-xl sm:text-2xl font-semibold text-slate-50 tracking-tight"
        >
          <span
            class="inline-block h-5 w-1 rounded-full bg-gradient-to-b from-teal-400 to-indigo-500"
          />
          Featured Projects
        </h2>
        <p class="mt-1 text-xs sm:text-sm text-slate-400">
          CI/CD 파이프라인과 인프라 자동화를 중심으로 구성된 주요 프로젝트들입니다.
        </p>
      </div>

      <!-- 관리자 모드 시, 간단한 안내 배지 -->
      <span
        v-if="adminMode"
        class="hidden sm:inline-flex items-center rounded-full border border-teal-500/40 bg-teal-500/10 px-2.5 py-1 text-[10px] font-medium uppercase tracking-[0.16em] text-teal-300"
      >
        Admin Editing Enabled
      </span>
    </div>

    <!-- 프로젝트 카드 그리드 -->
    <div
      class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-5 sm:gap-6 mt-4"
    >
      <article
        v-for="project in projects"
        :key="project.id ?? project.title"
        class="group relative overflow-hidden rounded-2xl border border-slate-800 bg-slate-900/70 backdrop-blur-xl shadow-sm hover:shadow-xl hover:border-teal-500/60 transition-all duration-300 will-change-transform"
      >
        <!-- 카드 전체 영역에 scale 효과 -->
        <div
          class="flex flex-col h-full transform transition-transform duration-300 group-hover:-translate-y-1 group-hover:scale-[1.01]"
        >
          <!-- 상단 이미지 영역 -->
          <div class="relative h-40 sm:h-44 overflow-hidden">
            <img
              :src="project.image"
              alt=""
              class="h-full w-full object-cover transition-transform duration-500 group-hover:scale-110"
            />
            <!-- 그라데이션 오버레이 -->
            <div
              class="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-slate-950/20 to-transparent"
            />
          </div>

          <!-- 본문 영역 -->
          <div class="flex-1 flex flex-col px-4 sm:px-5 pt-3 pb-4 sm:pb-5 gap-3">
            <div class="space-y-1">
              <h3
                class="text-sm sm:text-base font-semibold text-slate-50 group-hover:text-teal-300 transition-colors"
              >
                {{ project.title }}
              </h3>
              <p class="text-xs sm:text-sm text-slate-400 leading-relaxed line-clamp-3">
                {{ project.description }}
              </p>
            </div>

            <!-- 기술 스택 태그 -->
            <div class="mt-1 flex flex-wrap gap-1.5">
              <span
                v-for="tag in project.techStack"
                :key="tag"
                class="inline-flex items-center rounded-full bg-slate-800/80 border border-slate-700/80 px-2.5 py-0.5 text-[10px] font-medium text-slate-200"
              >
                {{ tag }}
              </span>
            </div>
          </div>
        </div>
      </article>
    </div>
  </section>
</template>
