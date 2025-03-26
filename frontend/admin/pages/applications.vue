<template>
  <section class="section">
    <h2 class="title">Заявки</h2>
    <b-table :data="applications">
      <b-table-column field="id" label="ID">
        {{ props.row.id }}
      </b-table-column>
      <b-table-column field="created_at" label="Дата создания">
        {{ props.row.created_at }}
      </b-table-column>
      <b-table-column field="name" label="Имя">
        {{ props.row.name }}
      </b-table-column>
      <b-table-column field="phone" label="Телефон">
        {{ props.row.phone }}
      </b-table-column>
      <b-table-column field="hike_name" label="Поход">
        {{ props.row.hike_name }}
      </b-table-column>
      <b-table-column field="cancelled" label="Отменена?">
        <b-checkbox
          :checked="props.row.cancelled"
          @input="toggleCancelled(props.row)"
        />
      </b-table-column>
    </b-table>
  </section>
</template>

<script>
export default {
  data() {
    return {
      applications: []
    }
  },
  async mounted() {
    this.applications = await this.$axios.$get('/api/v1/private/applications/')
  },
  methods: {
    async toggleCancelled(application) {
      application.cancelled = !application.cancelled
      await this.$axios.$patch(`/api/v1/private/applications/${application.id}/`, {
        cancelled: application.cancelled
      })
    }
  }
}
</script>
