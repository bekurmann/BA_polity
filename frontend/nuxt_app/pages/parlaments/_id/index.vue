<template>

        <v-card class="mt-3">
            <v-card-title primary-title>
                {{parlament.title}}
                <v-avatar
                    size="50"
                >
                <v-img :src="parlament.jurisdiction_canton.emblem" max-height="30" contain alt="canton emblem"></v-img>
                </v-avatar>
            </v-card-title>
        </v-card>

</template>
<script>
import ParlamentDetailGeneralInformation from '~/components/parlaments/ParlamentDetailGeneralInformation.vue'

export default {
    async asyncData({params, $axios}) {
        const parlament = await $axios.$get(`/parlaments/${params.id}`)
        return { 
            parlament: parlament,
        }
    },
    components: {
        ParlamentDetailGeneralInformation,
    },
    middleware: ['auth'],
    layout: 'parlaments',
}
</script>