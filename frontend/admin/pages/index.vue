<template>
  <section class="section">
    <h1 class="title">Панель управления</h1>
    <b-menu>
      <b-menu-list>
        <nuxt-link to="/hikes" class="menu-item">Походы</nuxt-link>
        <nuxt-link to="/applications" class="menu-item">Заявки</nuxt-link>
        <b-button @click="logout" type="is-danger" size="is-small">Выйти</b-button>
      </b-menu-list>
    </b-menu>
  </section>
</template>

<script>
export default {
  methods: {
    logout() {
      this.$store.dispatch('logout')
      this.$router.push('/login')
    }
  }
}
</script>
