<script setup lang="ts">
import { usePrefersReducedMotion } from '@/composables/usePrefersReducedMotion'
import AppFooter from '@/components/layout/AppFooter.vue'
import AppNavbar from '@/components/layout/AppNavbar.vue'
import ChatbotWidget from '@/components/common/ChatbotWidget.vue'
import ScrollProgressBar from '@/components/layout/ScrollProgressBar.vue'
import AboutSection from '@/components/sections/AboutSection.vue'
import AchievementSection from '@/components/sections/AchievementSection.vue'
import AikSection from '@/components/sections/AikSection.vue'
import BridgeSection from '@/components/sections/BridgeSection.vue'
import FaqSection from '@/components/sections/FaqSection.vue'
import FilmHeroSection from '@/components/sections/FilmHeroSection.vue'
import FinalCtaSection from '@/components/sections/FinalCtaSection.vue'
import HeroSection from '@/components/sections/HeroSection.vue'
import HighlightBanner from '@/components/sections/HighlightBanner.vue'
import KemahasiswaanSection from '@/components/sections/KemahasiswaanSection.vue'
import ServicesSection from '@/components/sections/ServicesSection.vue'
import StudentPathSection from '@/components/sections/StudentPathSection.vue'
import StudentStories from '@/components/sections/StudentStories.vue'

const prefersReducedMotion = usePrefersReducedMotion()
</script>

<template>
  <ScrollProgressBar />
  <AppNavbar />

  <main>
    <FilmHeroSection v-if="!prefersReducedMotion" />
    <HeroSection v-else />

    <HighlightBanner />
    <AboutSection />
    <KemahasiswaanSection />
    <StudentPathSection />
    <AchievementSection />
    <AikSection />
    <BridgeSection />
    <ServicesSection />
    <StudentStories />
    <FaqSection />
    <FinalCtaSection />
  </main>

  <AppFooter />
  <ChatbotWidget />
</template>
