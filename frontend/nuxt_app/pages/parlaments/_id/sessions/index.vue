<template>
    <v-card class="mt-3">
        <Sessions :sessions="sessions"></Sessions>
    </v-card>
</template>
<script>
import Sessions from '~/components/parlaments/Sessions.vue'

export default {
    async asyncData({params, $axios}) {
        const sessions = await $axios.$get(`/parlaments/${params.id}/sessions/`)
        return { 
            sessions: sessions,
        }
    },
    components: {
        Sessions,
    },
    middleware: ['auth'],
    layout: 'ParlamentDetail',
}
</script>