<template>
    <v-card>
        <v-card-title>Debate</v-card-title>
        <v-card-text>

            <v-expansion-panels>
                <v-expansion-panel
                class="ma-3" 
                :dark="getCardStyle(debate.order)" 
                :color="getCardColor(debate.order)" 
                v-for="debate in debates" 
                :key="debate.id"
                >
                    <v-expansion-panel-header>
                        #{{debate.order}} {{debate.politican_first_name}} {{debate.politican_last_name}}
                    </v-expansion-panel-header>
                    <v-expansion-panel-content>
                        {{debate.content}}
                    </v-expansion-panel-content>

                    <v-expansion-panel-content>
                        <v-btn 
                        color="primary"
                        :to="'/parlaments/'+affair.parlament+'/members/'+debate.politican"
                        >
                            Profile {{debate.politican_first_name}} {{debate.politican_last_name}}
                        </v-btn>
                    </v-expansion-panel-content>

                </v-expansion-panel>

            </v-expansion-panels>



        </v-card-text>

    </v-card>
</template>
<script>
export default {
    data() {
        return {
            debates: {},
        }
    },
    async fetch() {
        try {
            const affairDebates = await this.$axios.$get(this.$route.path +'/debate/')
            this.debates = affairDebates
        } catch(error) {
            throw new Error('Failed to fetch affairFiles from '+ this.$route.path +'/debate/')
        }
    },
    props: {
        affair: {
            type: Object
        }
    },
    methods: {
        getCardColor(order) {
            if(order % 2 == 0) {
                return "white"
            } else {
                return "primary"
            }
        },
        getCardStyle(order) {
            if(order % 2 == 0) {
                return false
            } else {
                return true
            }
        },
    }
}
</script>