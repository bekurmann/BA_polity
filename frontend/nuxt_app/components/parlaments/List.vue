<template>
<v-container>
    <p v-if="$fetchState.pending">
        <v-skeleton-loader
        class="mx-auto"
        type="article@2"
        ></v-skeleton-loader>
    </p>
    <p v-else-if="$fetchState.error">{{ $fetchState.error.message }}</p>
    <v-container v-else>
        <v-row class="mb-5" v-for="parlament in parlaments" :key="parlament.id">

            <v-col cols="12">

                <v-card
                dark
                style="background-image: radial-gradient(circle, rgba(0,91,173,1) 1%, rgba(68,142,208,1) 100%)"
                color="primary"
                :to="'/parlaments/' + parlament.id"
                >  
                    <v-card-title primary-title>
                        {{parlament.title}}
                    
                    <v-avatar
                        size="50"
                    >
                    <v-img :src="parlament.jurisdiction_canton.emblem" max-height="30" contain alt="canton emblem"></v-img>
                    </v-avatar>
                    </v-card-title>
                </v-card>

            </v-col>
        </v-row>
    </v-container>

</v-container>
</template>
<script>
export default {
    data() {
        return {
            parlaments:  {},
        }
    },
    async fetch() {
        try {
            const parlamentData = await this.$axios.$get('/parlaments/')
            this.parlaments = parlamentData
        } catch(error) {
            throw new Error('Failed to fetch parlamentData from /parlaments')
        }
    },
}
</script>
