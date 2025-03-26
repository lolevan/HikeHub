<template>
  <section class="section">
    <b-image :src="hike.photo"></b-image>
    <h1 class="title">{{ hike.name }}</h1>
    <p>{{ hike.short_description }}</p>

    <ValidationObserver v-slot="{ invalid, handleSubmit }">
      <form @submit.prevent="handleSubmit(onSubmit)">
        <ValidationProvider name="Имя" rules="required" v-slot="{ errors }">
          <b-field label="Имя">
            <b-input v-model="form.name"></b-input>
            <p class="help is-danger" v-if="errors.length">{{ errors[0] }}</p>
          </b-field>
        </ValidationProvider>

        <ValidationProvider name="Email" rules="required|email" v-slot="{ errors }">
          <b-field label="Email">
            <b-input v-model="form.email"></b-input>
            <p class="help is-danger" v-if="errors.length">{{ errors[0] }}</p>
          </b-field>
        </ValidationProvider>

        <ValidationProvider name="Телефон" rules="required|regex:/^\\+?[0-9\\-\\s]{7,15}$/" v-slot="{ errors }">
          <b-field label="Телефон">
            <b-input v-model="form.phone"></b-input>
            <p class="help is-danger" v-if="errors.length">{{ errors[0] }}</p>
          </b-field>
        </ValidationProvider>

        <b-button :disabled="invalid" type="is-primary">Отправить заявку</b-button>
      </form>
    </ValidationObserver>

    <b-modal :active.sync="modalActive" has-modal-card>
      <div class="modal-card">
        <header class="modal-card-head">
          <p class="modal-card-title">Спасибо!</p>
        </header>
        <section class="modal-card-body">
          <p>Ваша заявка принята.</p>
        </section>
        <footer class="modal-card-foot">
          <b-button @click="modalActive = false">Закрыть</b-button>
        </footer>
      </div>
    </b-modal>
  </section>
</template>

<script>
import { ValidationObserver, ValidationProvider } from 'vee-validate'

export default {
  components: { ValidationObserver, ValidationProvider },
  data() {
    return {
      hike: {},
      form: {
        name: '',
        email: '',
        phone: ''
      },
      modalActive: false
    }
  },
  async fetch() {
    const id = this.$route.params.id
    this.hike = await this.$axios.$get(`/api/v1/public/hikes/${id}/`)
  },
  methods: {
    async onSubmit() {
      await this.$axios.$post(`/api/v1/public/hikes/${this.hike.id}/applications/`, this.form)
      // Очистка формы и показ модалки
      this.form = { name: '', email: '', phone: '' }
      this.modalActive = true
    }
  }
}
</script>
