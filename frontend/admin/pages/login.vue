<template>
  <section class="section">
    <h1 class="title">Вход</h1>
    <form @submit.prevent="login">
      <b-field label="Логин">
        <b-input v-model="username"></b-input>
      </b-field>
      <b-field label="Пароль">
        <b-input type="password" v-model="password"></b-input>
      </b-field>
      <b-button type="is-primary" native-type="submit">Войти</b-button>
    </form>
  </section>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    async login() {
      try {
        await this.$store.dispatch('login', {
          username: this.username,
          password: this.password
        })
        this.$router.push('/')
      } catch (error) {
        alert('Неверные учетные данные')
      }
    }
  }
}
</script>
