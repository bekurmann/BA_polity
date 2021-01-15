<template>
  <v-snackbar top right v-model="show" :color="color">
    <p v-html="message">
      {{ message }}
    </p>
    <v-btn text @click="show = false" outlined>Close</v-btn>
  </v-snackbar>
</template>

<script>
export default {
  data () {
    return {
      show: false,
      message: '',
      color: ''
    }
  },

  created () {
    this.$store.subscribe((mutation, state) => {
      if (mutation.type === 'snackbar/showSnackbar') {
        this.message = state.snackbar.content
        this.color = state.snackbar.color
        this.show = true
      }
    })
  }
}
</script>