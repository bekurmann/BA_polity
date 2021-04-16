<template>
    <v-card>
        <v-card-title>
            Fractions
        </v-card-title>
        <v-card-text>

            <v-card class="ma-3" v-for="fraction in fractions" :key="fraction.id">
                <v-card-title>{{fraction.name}} ({{fraction.abbreviation}})</v-card-title>
                <v-card-subtitle>{{fraction.description}}</v-card-subtitle>
                <v-card-text>
                    <v-avatar size="70" color="primary">
                        <v-img :src="fraction.avatar"></v-img>
                    </v-avatar>
                </v-card-text>
            </v-card>

        </v-card-text>
    </v-card>
</template>
<script>
export default {
    props: {
        fractions: {
            type: Object
        },
    },
}
</script>