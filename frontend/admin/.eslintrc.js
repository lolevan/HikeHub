module.exports = {
  root: true,
  env: {
    browser: true,
    node: true
  },
  parserOptions: {
    parser: 'babel-eslint'
  },
  extends: [
    '@nuxtjs',
    'plugin:nuxt/recommended'
  ],
  // add your custom rules here
  rules: {
    "vue/comment-directive": "off",
    "space-before-function-paren": "off"
    // можно отключить и другие правила, которые вызывают ошибки
  }
}
