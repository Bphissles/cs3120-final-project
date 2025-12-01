<script setup>
import { ref, onMounted } from 'vue'

const isLoading = ref(true)
const statusMessage = ref('Connecting to server...')
const config = useRuntimeConfig()
const API_URL = config.public.apiBase

const checkBackendHealth = async () => {
  try {
    const response = await fetch(`${API_URL}/health`)
    if (response.ok) {
      const data = await response.json()
      if (data.status === 'healthy' && data.model_loaded) {
        isLoading.value = false
        return
      }
    }
    // If not healthy yet (or model loading), wait and retry
    statusMessage.value = 'Waking up backend service... (This may take ~30s)'
    setTimeout(checkBackendHealth, 2000)
  } catch (error) {
    // Network error (backend likely down/sleeping), wait and retry
    statusMessage.value = 'Waking up backend service... (This may take ~30s)'
    setTimeout(checkBackendHealth, 2000)
  }
}

onMounted(() => {
  checkBackendHealth()
  import('bootstrap/dist/js/bootstrap.bundle.min.js')
})
</script>

<template>
  <div v-if="isLoading" class="d-flex flex-column justify-content-center align-items-center vh-100 bg-light">
    <div class="spinner-border text-primary mb-3" style="width: 3rem; height: 3rem;" role="status">
      <span class="visually-hidden">Loading...</span>
    </div>
    <h2 class="h5 text-dark">{{ statusMessage }}</h2>
    <p class="text-muted small mt-2">The API is hosted on a free tier and spins down after inactivity.</p>
  </div>

  <div v-else>
    <Navigation />
    <div class="container">
      <NuxtPage />
    </div>
  </div>
</template>
