<template>
    <v-card>
        <v-card-title>{{affair.title}}</v-card-title>
        <v-card-text>
            <v-row>
                <v-col cols="12" xs="12" sm="12" md="12" lg="12" xl="12">

                    <v-card class="ma-1" color="primary" dark>
                        <v-card-title>General Information</v-card-title>
                        <v-card-text>
                            <v-row>
                                <v-col>
                                    <v-chip outlined>{{affair.affair_type}}</v-chip>
                                    <v-chip outlined>{{affair.identifier}}</v-chip>
                                    <v-chip outlined>{{affair.date_received}}</v-chip>
                                    <v-chip v-if="affair.recommendation" color="green">Recommendation Executive</v-chip>
                                    <v-chip v-else color="red">Recommendation Executive</v-chip>

                                    <v-chip v-if="affair.urgent" color="red" light>urgent</v-chip>
                                    <v-chip v-else color="yellow" light>not urgent</v-chip>
                                </v-col>
                            </v-row>
                            <v-row>
                                <v-col cols="12" xs="12" sm="12" md="6" lg="6" xl="6" class="d-flex child-flex align-stretch">

                                    <v-card class="ma-1" light>
                                        <v-card-title>Signatory</v-card-title>
                                        <v-card-text>
                                            <v-row>
                                                <v-col cols="12" xs="12" sm="4" md="4" lg="4" xl="4">
                                                    <v-avatar
                                                        size="100"
                                                    >
                                                        <v-img :src="politican.avatar"></v-img>
                                                    </v-avatar>
                                                </v-col>
                                                <v-col cols="12" xs="12" sm="8" md="8" lg="8" xl="8">
                                                    <NuxtLink :to="'/politicans/'+politican.id">
                                                        <span class="text-h6">{{politican.first_name}} {{politican.last_name}}</span>
                                                    </NuxtLink>
                                                    <br>
                                                    on {{affair.date_received}}
                                                    <br>
                                                    with <b>{{affair.joint_signatories_count}}</b> other councillors
                                                </v-col>
                                            </v-row>
                                        </v-card-text>
                                    </v-card>

                                </v-col>

                                <v-col cols="12" xs="12" sm="12" md="6" lg="6" xl="6" class="d-flex child-flex align-stretch">
                                    <v-card class="ma-1" v-if="affairResult(affair) =='no_vote'" color="yellow">
                                        <v-card-title>Vote</v-card-title>
                                        <v-card-text>no vote</v-card-text>
                                    </v-card>
                                    <v-card class="ma-1" v-else-if="affairResult(affair) =='accepted'" color="green" dark>
                                        <v-card-title>Vote</v-card-title>
                                        <v-card-subtitle class="text-h4">
                                            accepted <v-icon>mdi-check-outline</v-icon>
                                        </v-card-subtitle>
                                        <v-card-text>Yes: {{affair.anon_yes}} / No: {{affair.anon_no}} / Abstinent: {{affair.anon_abstinence}}</v-card-text>
                                    </v-card>
                                    <v-card class="ma-1" v-else-if="affairResult(affair) =='declined'" color="red" dark>
                                        <v-card-title>Vote</v-card-title>
                                        <v-card-subtitle class="text-h4">
                                            declined <v-icon>mdi-cancel</v-icon>
                                        </v-card-subtitle>
                                        <v-card-text>Yes: {{affair.anon_yes}} / No: {{affair.anon_no}} / Abstinent: {{affair.anon_abstinence}}</v-card-text>
                                    </v-card>
                                </v-col>
                            </v-row>

                        </v-card-text>
                    </v-card>

                </v-col>

            </v-row>

        </v-card-text>
    </v-card>
</template>
<script>
export default {
    props: {
        affair: {
            type: Object
        },
        politican: {
            type: Object
        }
    },
    methods: {
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
    }
}
</script>