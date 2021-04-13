<template>
    <v-container v-if="$fetchState.pending">
        <v-row>
            <v-col>
                <v-skeleton-loader
                class="mx-auto"
                type="article@2"
                ></v-skeleton-loader>
            </v-col>
        </v-row>
    </v-container>
    <v-container v-else>
        <v-row>
            <v-col cols="12">
                <v-card align="center" >
                    <v-card-title primary-title class="justify-center">
                        {{details.first_name}} {{details.last_name}}
                    </v-card-title>
                    <v-card-subtitle>{{details.city.name}}</v-card-subtitle>
                    <v-card-text>
                        <v-avatar
                            size="150"
                        >
                        <v-img :src="details.avatar" max-height="150" contain alt="canton emblem"></v-img>
                        </v-avatar>
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>
<script>

export default {
    data() {
        return {
            details: {}
        }
    },
    async fetch() {
        try {
            const politicanDetails = await this.$axios.$get(`/politicans/${this.$route.params.id}`)
            this.details = politicanDetails
        } catch(error) {
            throw new Error(`Failed to fetch politicanDetails from /politicans/${this.$route.params.id}`)
        }
    },
    middleware: ['auth'],
}
</script>