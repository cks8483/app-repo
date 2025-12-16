<script setup>
// 기본 Vue API
import { ref } from 'vue'

// 레이아웃/섹션 컴포넌트
import NavBar from './components/NavBar.vue'
import HeroSection from './components/HeroSection.vue'
import ProjectGallery from './components/ProjectGallery.vue'
import AdminFloatingControls from './components/AdminFloatingControls.vue'

// -------------------------------
// 상태 정의
// -------------------------------

// 관리자 모드 토글 상태
// - NavBar에서 토글
// - AdminFloatingControls, 작성 버튼 노출 제어에 사용
const adminMode = ref(false)

// 현재는 백엔드 연동 전이므로,
// 프론트엔드 UI 레이아웃 테스트용 더미 데이터 정의
const profile = ref({
  name: 'Ch. Choi',
  bio: 'CI/CD 기반의 개발자 포트폴리오 및 인프라 자동화를 설계·구현하는 백엔드/플랫폼 엔지니어입니다.',
  projects: [
    {
      id: 1,
      title: 'CI/CD 포트폴리오 플랫폼',
      description:
        'GitHub Actions, Argo CD, Kubernetes를 활용해 포트폴리오 변경 사항을 자동으로 배포하는 풀스택 플랫폼.',
      image:
        'https://images.pexels.com/photos/1181675/pexels-photo-1181675.jpeg?auto=compress&cs=tinysrgb&w=1200',
      techStack: ['Vue 3', 'FastAPI', 'PostgreSQL', 'Kubernetes', 'GitHub Actions']
    },
    {
      id: 2,
      title: '개발자 블로그/위키 플랫폼',
      description:
        '마크다운 기반의 기술 문서를 GitOps 방식으로 관리하고, 자동 빌드/배포되는 개인 위키 시스템.',
      image:
        'https://images.pexels.com/photos/3861964/pexels-photo-3861964.jpeg?auto=compress&cs=tinysrgb&w=1200',
      techStack: ['Vue 3', 'Tailwind CSS', 'Nginx', 'Docker', 'GitOps']
    },
    {
      id: 3,
      title: '모니터링 & 알림 대시보드',
      description:
        '애플리케이션/인프라 메트릭을 수집하고, 슬랙/이메일로 알림을 보내는 관제 대시보드.',
      image:
        'https://images.pexels.com/photos/1181315/pexels-photo-1181315.jpeg?auto=compress&cs=tinysrgb&w=1200',
      techStack: ['Prometheus', 'Grafana', 'Python', 'Webhooks']
    }
  ]
})

// NavBar에서 관리자 모드를 토글할 때 호출되는 핸들러
const handleToggleAdmin = (value) => {
  adminMode.value = value
}
</script>

<template>
  <!-- 전체 페이지 컨테이너: 다크 테마 + 글래스 느낌 배경 -->
  <div
    class="min-h-screen bg-slate-950 text-slate-50 font-sans selection:bg-teal-500 selection:text-white"
  >
    <!-- 상단 네비게이션 바 (고정) -->
    <NavBar :admin-mode="adminMode" @update:admin-mode="handleToggleAdmin" />

    <!-- 메인 콘텐츠 영역 -->
    <main class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 pt-28 pb-16 space-y-16">
      <!-- 히어로 섹션: 이름, 한 줄 소개, 주요 CTA 버튼 -->
      <HeroSection :name="profile.name" :bio="profile.bio" />

      <!-- 프로젝트 갤러리 (반응형 그리드) -->
      <ProjectGallery :projects="profile.projects" :admin-mode="adminMode" />

      <!-- 푸터 영역 -->
      <footer class="pt-12 border-t border-slate-800/70 text-xs sm:text-sm text-slate-500 flex justify-between flex-col sm:flex-row gap-2">
        <span>&copy; {{ new Date().getFullYear() }} {{ profile.name }}. All rights reserved.</span>
        <span class="text-slate-600">
          Built with
          <span class="text-teal-400">Vue 3</span>
          ·
          <span class="text-indigo-400">Tailwind CSS</span>
        </span>
      </footer>
    </main>

    <!-- 관리자 모드 전용 플로팅 컨트롤 -->
    <AdminFloatingControls v-if="adminMode" />
  </div>
</template>