<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { Icon } from "@iconify/vue";

const error = ref<string | null>(null)

interface Repo {
  name: string
  url: string
  description: string | null
  language: string | null
  stars: number
  updated: string
  commits: number
}

const repos = ref<Repo[] | null>(null)

onMounted(async () => {
  try {
    const res = await fetch('/api/repos')
    const data: Repo[] = await res.json()
    repos.value = data
  } catch (e) {
    error.value = 'Erreur connexion backend'
  }
})

</script>

<template>
  <div>
    <h1>Mon Portfolio Vue + FastAPI</h1>

    <ul v-if="repos">
      <li v-for="repo in repos" :key="repo.name">
        <a :href="repo.url" target="_blank"><strong>{{ repo.name }}</strong></a>
        <p>{{ repo.description }}</p>
        <Icon icon="mdi:github" width="32" height="32"/>
        <p>Commits : {{ repo.commits }}</p>
        <p><small>⭐ {{ repo.stars }} - {{ repo.language }} - Mis à jour : {{ new Date(repo.updated).toLocaleDateString()
        }}</small></p>
      </li>
    </ul>

  </div>
</template>

<style scoped>
h1 {
  color: #42b983;
}
</style>
