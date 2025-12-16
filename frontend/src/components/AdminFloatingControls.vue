<script setup>
// 관리자 전용 플로팅 컨트롤 컴포넌트
// - 화면 우측 하단에 고정된 FAB 형태
// - 실제 동작은 아직 없고, 우선 console.log 로만 처리

import { Plus, FileText, Wrench } from 'lucide-vue-next'

// 버튼 클릭 시 공통 핸들러
const handleClick = (type) => {
  // TODO: 실제 모달/페이지 연동 시 이 부분을 교체
  // 한글 로그로 어떤 버튼이 눌렸는지 표시
  console.log(`[ADMIN] ${type} 버튼 클릭 - Open Modal`)
}
</script>

<template>
  <!-- 우측 하단 고정 플로팅 영역 -->
  <div class="fixed bottom-6 right-6 z-30">
    <!-- 글래스모피즘 카드 -->
    <div
      class="rounded-2xl border border-teal-500/40 bg-slate-900/80 backdrop-blur-2xl shadow-2xl shadow-teal-500/20 px-4 py-3 w-64 space-y-3"
    >
      <div class="flex items-center justify-between gap-2">
        <span class="text-[11px] font-semibold uppercase tracking-[0.18em] text-teal-300">
          Admin Panel
        </span>
        <span class="rounded-full bg-teal-500/10 px-2 py-0.5 text-[10px] text-teal-200">
          작성 모드
        </span>
      </div>

      <p class="text-[11px] leading-relaxed text-slate-400">
        프로젝트/이력서/기술 스택을 <span class="text-teal-300">실시간으로 수정</span>할 수 있는
        관리자 전용 컨트롤입니다.
      </p>

      <!-- 액션 버튼 그룹 -->
      <div class="space-y-1.5">
        <!-- 새 프로젝트 추가 -->
        <button
          type="button"
          @click="handleClick('새 프로젝트 추가')"
          class="flex w-full items-center gap-2 rounded-xl bg-gradient-to-r from-teal-500 to-indigo-500 px-2.5 py-1.5 text-xs font-semibold text-slate-950 shadow-md shadow-teal-500/40 hover:shadow-lg hover:shadow-teal-500/50 transition-transform duration-150 hover:-translate-y-0.5"
        >
          <span
            class="inline-flex h-5 w-5 items-center justify-center rounded-lg bg-slate-950/20 text-slate-950"
          >
            <Plus class="h-3.5 w-3.5" />
          </span>
          <span class="truncate">새 프로젝트 추가</span>
        </button>

        <!-- 이력서 내용 수정 -->
        <button
          type="button"
          @click="handleClick('이력서 내용 수정')"
          class="flex w-full items-center gap-2 rounded-xl border border-slate-700/80 bg-slate-900/80 px-2.5 py-1.5 text-xs font-medium text-slate-200 hover:border-indigo-400/80 hover:bg-slate-900/95 hover:text-indigo-100 transition-colors"
        >
          <span
            class="inline-flex h-5 w-5 items-center justify-center rounded-lg bg-slate-800/80 text-indigo-300"
          >
            <FileText class="h-3.5 w-3.5" />
          </span>
          <span class="truncate">이력서 내용 수정</span>
        </button>

        <!-- 기술 스택 관리 -->
        <button
          type="button"
          @click="handleClick('기술 스택 관리')"
          class="flex w-full items-center gap-2 rounded-xl border border-slate-700/80 bg-slate-900/80 px-2.5 py-1.5 text-xs font-medium text-slate-200 hover:border-teal-400/80 hover:bg-slate-900/95 hover:text-teal-100 transition-colors"
        >
          <span
            class="inline-flex h-5 w-5 items-center justify-center rounded-lg bg-slate-800/80 text-teal-300"
          >
            <Wrench class="h-3.5 w-3.5" />
          </span>
          <span class="truncate">기술 스택 관리</span>
        </button>
      </div>
    </div>
  </div>
</template>


