<template>
    <v-card>
        <v-card-title>
            Debate Statements from {{politicanDetails.first_name}} {{politicanDetails.last_name}}
        </v-card-title>
        <v-card-text>

            <v-expansion-panels>
                <v-expansion-panel
                v-for="(statement) in politicanDetails.debate_statements" 
                :key="statement.id"
                >
                    <v-expansion-panel-header>
                        <b>{{statement.affair.title}}</b> {{ statement.affair.identifier }}
                    </v-expansion-panel-header>
                    <v-expansion-panel-content>
                        {{statement.content}}
                    </v-expansion-panel-content>
                    <v-expansion-panel-content>
                        <v-btn 
                        color="primary"
                        :to="'/affairs/'+statement.affair.id"
                        >
                            See affair details
                        </v-btn>
                    </v-expansion-panel-content>
                </v-expansion-panel>
            </v-expansion-panels>

        </v-card-text>
    </v-card>  
</template>
<script>
export default {
    props: {
        politicanDetails: {
            type: Object
        }
    }
}
</script>