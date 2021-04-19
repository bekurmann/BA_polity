<template>
    <v-card>
        <v-card-title>
            Fractions (incomplete)
        </v-card-title>
        <v-card-text>
            <v-card 
                class="ma-3" 
                v-for="fraction in fractions" :key="fraction.id"
                >
                <div class="d-flex flex-no-wrap justify-space-between">
                    <div>

                        <v-card-title>{{fraction.name}} ({{fraction.abbreviation}})</v-card-title>
                        <v-card-subtitle>{{fraction.description}}</v-card-subtitle>
                        <v-card-text>{{fraction.number_of_active_members}} Mitglieder</v-card-text>

                    </div>
                    <v-avatar size="60" class="ma-3" tile>
                        <v-img :src="fraction.avatar" contain></v-img>
                    </v-avatar>
                </div>
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