<template>
    <v-card>
        <v-card-title>
            Memberships of {{politicanDetails.first_name}} {{politicanDetails.last_name}}
        </v-card-title>
        <v-card-text>

            <v-simple-table>
                <thead>
                    <tr>
                        <th>Title</th>
                        <th>Type</th>
                        <th>Function</th>
                        <th>start_date</th>
                        <th>end_date</th>
                        <th>active</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(membership) in memberships" :key="membership.id">
                        <td v-if="membership.membership_type=='Parlament'">
                            {{membership.parlament.title}}
                        </td>
                        <td v-else-if="membership.membership_type=='Fraction'">
                            {{membership.politican.fractions[0].name}}
                        </td>
                        <td v-else>Unknown Type</td>

                        <td>{{membership.membership_type}}</td>
                        <td>{{membership.membership_function}}</td>
                        <td>{{membership.start_date}}</td>
                        <td>{{membership.end_date}}</td>
                        <td>
                            <v-chip v-if="membership.active" color="green" dark>active</v-chip>
                            <v-chip v-else color="red" dark>inactive</v-chip>
                        </td>
                    </tr>
                </tbody>
            </v-simple-table>

        </v-card-text>
    </v-card>  
</template>
<script>
export default {
    data() {
        return {
            memberships: {}
        }
    },
    async fetch() {
        try {
            const membershipsData = await this.$axios.$get(`/politicans/${this.$route.params.id}/memberships`)
            this.memberships = membershipsData
        } catch(error) {
            throw new Error(`Failed to fetch membershipsData from /politicans/${this.$route.params.id}/memberships`)
        }
    },
    props: {
        politicanDetails: {
            type: Object
        }
    },
}
</script>