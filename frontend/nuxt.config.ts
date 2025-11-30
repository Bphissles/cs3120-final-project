// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },
  
  runtimeConfig: {
    public: {
      apiBase: process.env.API_URL || 'https://cs3120-final-project.onrender.com/'
    }
  },

  css: ['~/assets/scss/theme.scss']
})
