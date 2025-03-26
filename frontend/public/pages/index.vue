<template>
  <section class="section">
    <b-field>
      <b-input v-model="search" placeholder="Поиск по названию"></b-input>
    </b-field>
    <div class="columns is-multiline">
      <div v-for="hike in filteredHikes" :key="hike.id" class="column is-one-third">
        <b-card>
          <b-image :src="hike.photo" lazy></b-image>
          <div class="card-content">
            <p class="title">{{ hike.name }}</p>
            <nuxt-link :to="`/hike/${hike.id}`" class="button is-link">Перейти</nuxt-link>
          </div>
        </b-card>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  data() {
    return {
      hikes: [],
      search: ''
    }
  },
  computed: {
    filteredHikes() {
      return this.hikes.filter(hike =>
        hike.name.toLowerCase().includes(this.search.toLowerCase())
      )
    }
  },
  async fetch() {
    this.hikes = await this.$axios.$get('/api/v1/public/hikes/')
  }
}
</script>
