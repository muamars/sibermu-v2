<script setup lang="ts">
import SectionHeading from '@/components/common/SectionHeading.vue'
import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from '@/components/ui/accordion'
import { faqItems } from '@/data/faq'
</script>

<template>
  <section id="faq" class="px-4 py-16 sm:px-6 sm:py-20 lg:px-10 lg:py-28">
    <div class="mx-auto max-w-3xl">
      <SectionHeading
        align="center"
        eyebrow="FAQ"
        title="Masih penasaran? Kami punya jawabannya."
        description="Beberapa hal yang mungkin ingin kamu ketahui tentang kehidupan mahasiswa di SiberMu."
      />

      <Accordion type="single" collapsible default-value="0" class="mt-8 rounded-2xl border border-border bg-white px-2 sm:px-4">
        <AccordionItem v-for="(item, index) in faqItems" :key="item.question" :value="String(index)">
          <AccordionTrigger class="py-5 text-base font-semibold">
            {{ item.question }}
          </AccordionTrigger>
          <AccordionContent class="pb-5 text-sm leading-relaxed text-muted-foreground">
            {{ item.answer }}
          </AccordionContent>
        </AccordionItem>
      </Accordion>
    </div>
  </section>
</template>
