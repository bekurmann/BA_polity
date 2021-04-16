<template>
    <v-card>
        <v-card-title>
            Commissions (incomplete)
        </v-card-title>
        <v-card-text>
            <v-card 
                class="ma-3" 
                v-for="commission in commissions" :key="commission.id"
                >

                    <v-card-title>{{commission.title}} ({{commission.abbreviation}})</v-card-title>
                    <v-card-subtitle>{{commission.description}}</v-card-subtitle>

                </v-card>
            
        </v-card-text>
        
    </v-card>
</template>
<script>
export default {
    props: {
        commissions: {
            type: Object
        },
    },
}
</script>