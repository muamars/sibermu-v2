<script setup lang="ts">
import { usePrefersReducedMotion } from '@/composables/usePrefersReducedMotion'
import AppFooter from '@/components/layout/AppFooter.vue'
import AppNavbar from '@/components/layout/AppNavbar.vue'
import ChatbotWidget from '@/components/common/ChatbotWidget.vue'
import ScrollProgressBar from '@/components/layout/ScrollProgressBar.vue'
import AchievementSection from '@/components/sections/AchievementSection.vue'
import AikSection from '@/components/sections/AikSection.vue'
import AikValuesSection from '@/components/sections/AikValuesSection.vue'
import FaqSection from '@/components/sections/FaqSection.vue'
import HeroSectionBaru from '@/components/sections/HeroSectionBaru.vue'
import FinalCtaSection from '@/components/sections/FinalCtaSection.vue'
import HeroSection from '@/components/sections/HeroSection.vue'
import HighlightBanner from '@/components/sections/HighlightBanner.vue'
import KemahasiswaanSection from '@/components/sections/KemahasiswaanSection.vue'
import KemahasiswaanDetailSection from '@/components/sections/KemahasiswaanDetailSection.vue'
import KampusVirtualSection from '@/components/sections/KampusVirtualSection.vue'
import ProdiSection from '@/components/sections/ProdiSection.vue'
import ServicesSection from '@/components/sections/ServicesSection.vue'
import StudentStories from '@/components/sections/StudentStories.vue'

const prefersReducedMotion = usePrefersReducedMotion()
</script>

<template>
  <ScrollProgressBar />
  <AppNavbar />

  <main>
    <HeroSectionBaru v-if="!prefersReducedMotion" />
    <HeroSection v-else />

    <HighlightBanner />
    <!-- <AboutSection /> -->
    <ProdiSection />
    <KemahasiswaanSection />
    <KemahasiswaanDetailSection />
    <AikSection />
    <AikValuesSection />
    <!-- <StudentPathSection /> -->
    <AchievementSection />
    <!-- <BridgeSection /> -->
    <ServicesSection />
    <StudentStories />
    <FaqSection />
    <FinalCtaSection />
  </main>

  <KampusVirtualSection />
  <AppFooter />
  <ChatbotWidget />
</template>
