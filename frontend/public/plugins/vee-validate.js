import { defineRule } from 'vee-validate'
import { required } from '@vee-validate/rules'

// Регистрируем правило "required"
defineRule('required', required)
