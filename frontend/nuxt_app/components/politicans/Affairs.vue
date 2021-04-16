<template>
    <v-card>
        <v-card-title>
            Affairs from {{politicanDetails.first_name}} {{politicanDetails.last_name}}
        </v-card-title>
        <v-card-text>

            <v-simple-table>
                <thead>
                    <tr>
                        <th>Title</th>
                        <th>Date received</th>
                        <th>Type</th>
                        <th>Accepted</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(affair) in politicanDetails.affairs" :key="affair.id" @click:row="routerNuxtLink">
                        <td>
                            <NuxtLink :to="'/parlaments/' + selectedParlament.id + '/affairs/' + affair.id">{{affair.title}}</NuxtLink>
                        </td>
                        <td>{{affair.date_received}}</td>
                        <td>{{affair.affair_type}}</td>
                        <td>
                            <!-- <v-chip v-if="affair.accepted" color="green" dark>accepted</v-chip>
                            <v-chip v-else color="red" dark>rejected</v-chip> -->
                            <v-chip v-if="affairResult(affair) =='no_vote'" color="yellow">no vote</v-chip>
                            <v-chip v-else-if="affairResult(affair) =='accepted'" color="green" dark>accepted</v-chip>
                            <v-chip v-else-if="affairResult(affair)=='declined'" color="red" dark>declined</v-chip>
                        </td>
                    </tr>
                </tbody>
            </v-simple-table>

        </v-card-text>
    </v-card>  
</template>
<script>
import {mapState} from 'vuex'

export default {
    props: {
        politicanDetails: {
            type: Object
        }
    },
    methods: {
        routerNuxtLink() {
            this.router.push('/affairs'+affair.id)
        },
        affairResult(affair) {
            let total_votes = affair.anon_no + affair.anon_yes + affair.anon_abstinence
            let no_share = affair.anon_no
            let yes_share = affair.anon_yes
            if(total_votes == 0) {
                return 'no_vote'
            }
            else if(yes_share > no_share) {
                return 'accepted'
            } else {
                return 'declined'
            }
        }
    },
    computed: {
        ...mapState({
            selectedParlament: state => state.parlaments.selectedParlament
        })
    }
}
</script>