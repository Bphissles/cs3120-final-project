<script setup>
import { onMounted } from 'vue'

onMounted(() => {
  import('bootstrap/dist/js/bootstrap.bundle.min.js')
})
</script>
<template>
  <Navigation />
  <div class="container">
    <NuxtPage />
  </div>
</template>
