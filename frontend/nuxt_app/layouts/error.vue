<template>
    <v-card>
      <v-img src="/error.png" alt="error" max-height="400" contain></v-img>
      <v-card-title primary-title>
        <h1 v-if="error.statusCode === 404">
          {{ pageNotFound }}
        </h1>
        <h1 v-else>
          {{ otherError }}
        </h1>
      </v-card-title>
      <v-card-text>
        Something didn't work. <br>
        Go back to the
        <NuxtLink to="/">
          Homepage
        </NuxtLink> and try again.
      </v-card-text>
    </v-card>
</template>

<script>
export default {
  layout: 'empty',
  props: {
    error: {
      type: Object,
      default: null
    }
  },
  data () {
    return {
      pageNotFound: '404 Not Found',
      otherError: 'An error occurred'
    }
  },
  head () {
    const title =
      this.error.statusCode === 404 ? this.pageNotFound : this.otherError
    return {
      title
    }
  }
}
</script>

<style scoped>
h1 {
  font-size: 20px;
}
</style>
