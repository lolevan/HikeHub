<template>
  <section class="section">
    <h2 class="title">Управление походами</h2>
    <b-button @click="$router.push('/hikes/create')" type="is-primary">Создать поход</b-button>
    <b-table :data="hikes">
      <b-table-column field="id" label="ID">
        {{ props.row.id }}
      </b-table-column>
      <b-table-column field="name" label="Название">
        {{ props.row.name }}
      </b-table-column>
      <b-table-column field="photo" label="Фото">
        <b-image :src="props.row.photo" size="48x48"></b-image>
      </b-table-column>
      <b-table-column field="actions" label="Действия">
        <b-button @click="editHike(props.row)" size="is-small">Редактировать</b-button>
        <b-button @click="deleteHike(props.row)" size="is-small" type="is-danger">Удалить</b-button>
      </b-table-column>
    </b-table>
  </section>
</template>

<script>
export default {
  data() {
    return {
      hikes: []
    }
  },
  async mounted() {
    this.hikes = await this.$axios.$get('/api/v1/private/hikes/')
  },
  methods: {
    editHike(hike) {
      this.$router.push(`/hikes/edit/${hike.id}`)
    },
    async deleteHike(hike) {
      if (confirm('Удалить поход?')) {
        await this.$axios.$delete(`/api/v1/private/hikes/${hike.id}/`)
        this.hikes = this.hikes.filter(h => h.id !== hike.id)
      }
    }
  }
}
</script>
