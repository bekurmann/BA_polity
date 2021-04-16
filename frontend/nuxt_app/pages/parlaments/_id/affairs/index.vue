<template>
    <v-card class="mt-3">
        <Affairs :affairs="affairs"></Affairs>
    </v-card>
</template>
<script>
import Affairs from '~/components/parlaments/Affairs.vue'

export default {
    async asyncData({params, $axios}) {
        const affairs = await $axios.$get(`/parlaments/${params.id}/affairs/`)
        return { 
            affairs: affairs,
        }
    },
    components: {
        Affairs
    },
    middleware: ['auth'],
    layout: 'ParlamentDetail',
}
</script>