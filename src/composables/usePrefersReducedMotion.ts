import { onScopeDispose, ref } from 'vue'

export function usePrefersReducedMotion() {
  const query = '(prefers-reduced-motion: reduce)'
  const prefersReducedMotion = ref(false)

  if (typeof window !== 'undefined' && 'matchMedia' in window) {
    const mediaQuery = window.matchMedia(query)
    prefersReducedMotion.value = mediaQuery.matches

    const handleChange = (event: MediaQueryListEvent) => {
      prefersReducedMotion.value = event.matches
    }

    mediaQuery.addEventListener('change', handleChange)
    onScopeDispose(() => mediaQuery.removeEventListener('change', handleChange))
  }

  return prefersReducedMotion
}
