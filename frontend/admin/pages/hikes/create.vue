<template>
  <section class="section">
    <h2 class="title">Создать поход</h2>
    <form @submit.prevent="createHike">
      <b-field label="Название">
        <b-input v-model="hike.name"></b-input>
      </b-field>
      <b-field label="Описание">
        <b-input v-model="hike.description"></b-input>
      </b-field>
      <b-field label="Краткое описание">
        <b-input v-model="hike.short_description"></b-input>
      </b-field>
      <b-field label="Фото">
        <b-input type="file" @change="onFileChange"></b-input>
      </b-field>
      <b-button type="is-primary">Создать</b-button>
    </form>
  </section>
</template>

<script>
export default {
  data() {
    return {
      hike: {
        name: '',
        description: '',
        short_description: ''
      },
      photo: null
    }
  },
  methods: {
    onFileChange(e) {
      this.photo = e.target.files[0]
    },
    async createHike() {
      const formData = new FormData()
      formData.append('name', this.hike.name)
      formData.append('description', this.hike.description)
      formData.append('short_description', this.hike.short_description)
      if (this.photo) {
        formData.append('photo', this.photo)
      }
      await this.$axios.$post('/api/v1/private/hikes/', formData)
      this.$router.push('/hikes')
    }
  }
}
</script>
