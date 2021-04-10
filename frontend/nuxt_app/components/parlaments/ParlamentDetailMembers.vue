<template>
    <v-card>
        <v-card-title primary-title>
            Members
        </v-card-title>
        <v-card-text>

            <v-data-iterator
                :items="memberships"
                item-key="id"
                :items-per-page.sync="itemsPerPage"
            >

                <template v-slot:default="memberships">
                    <v-list three-line>

                        <template v-for="(membership, index) in memberships">
                            <v-list-item :key="membership.politican.id">
                                <v-list-item-avatar>
                                    <v-img :src="politican.avatar"></v-img>
                                </v-list-item-avatar>

                                <v-list-item-content>
                                    <v-list-item-title >
                        
                                        <NuxtLink :to="'/politicans/' + membership.politican.id">{{politican.first_name}} {{politican.last_name}}</NuxtLink> 
                                        (<NuxtLink :to="'/fractions/' + fraction.id" 
                                                    v-for="fraction in membership.politican.fractions"
                                                    :key="fraction.id">{{fraction.name}}</NuxtLink>)
                                        
                                    </v-list-item-title>
                                    <v-list-item-subtitle>{{membership.politican.city.name}}</v-list-item-subtitle>
                                </v-list-item-content>
                            </v-list-item>
                            <v-divider :key="index"></v-divider>
                        </template>

                    </v-list>
                </template>
                
            </v-data-iterator>
            


        </v-card-text>
    </v-card>
</template>
<script>
export default {
    data() {
        return {
            itemsPerPage: 5,
        }
    },
    props: {
        memberships: {
            type: Array
        },
    },
    computed: {
        previewMemberships: function() {
            let previewMemberships = this.filteredMemberships
            // limit v-for to 5
            return previewMemberships.slice(0,5)
        },
        filteredMemberships: function() {
            // only active memberships
            let noInactiveMemberships = this.memberships.filter(el => el.politican.active !== true)
            return noInactiveMemberships;    
        }
    }
}
</script>