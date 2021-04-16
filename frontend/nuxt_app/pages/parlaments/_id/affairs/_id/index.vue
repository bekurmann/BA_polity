<template>
    <v-card class="mt-3">
        <v-card-title>{{affair.title}}</v-card-title>
        <v-card-text>
            <v-row>
                <v-col cols="12" xs="12" sm="12" md="12" lg="12" xl="12">
                    <AffairInfo :affair="affair" :politican="politican"></AffairInfo>
                </v-col>
            </v-row>
            <v-row>
                <v-col>
                    <AffairFiles></AffairFiles>
                </v-col>
            </v-row>
        </v-card-text>
    </v-card>
</template>
<script>
import AffairInfo from '~/components/affairs/Info.vue'
import AffairFiles from '~/components/affairs/Files.vue'

export default {
    data() {

    },
    async asyncData({params, $axios}) {
        const affair = await $axios.$get(`/affairs/${params.id}`);
        const politican = await $axios.$get(`/politicans/${affair.signatory}`);
        return { 
            affair: affair,
            politican: politican
        }
    },
    components: {
        AffairInfo,
        AffairFiles,
    },
    middleware: ['auth'],
    layout: 'ParlamentDetail',
}
</script>