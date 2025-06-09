<script setup lang="ts">
import { ref, onMounted } from 'vue'

const backendMessage = ref('Chargement...')

onMounted(async () => {
  try {
    const res = await fetch('/api/')
    const data = await res.json()
    backendMessage.value = data.message
  } catch (e) {
    backendMessage.value = 'Erreur connexion backend'
  }
})

</script>

<template>
  <div>
    <h1>Mon Portfolio Vue + FastAPI</h1>
    <p>Message backend : {{ backendMessage }}</p>
  </div>
</template>

<style scoped>
h1 {
  color: #42b983;
}
</style>
