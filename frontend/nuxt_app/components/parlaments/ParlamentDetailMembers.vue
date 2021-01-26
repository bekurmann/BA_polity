<template>
    <v-card>
        <v-card-title primary-title>
            Members
        </v-card-title>
        <v-card-text>
            
            <v-list three-line>

                <template v-for="(membership, index) in previewMemberships">
                    <v-list-item :key="membership.politican.id">
                        <v-list-item-avatar>
                            <v-img :src="membership.politican.avatar"></v-img>
                        </v-list-item-avatar>

                        <v-list-item-content>
                            <v-list-item-title >
                                <NuxtLink :to="'/politican/' + membership.politican.id">
                                {{membership.politican.first_name}} {{membership.politican.last_name}}
                                </NuxtLink>
                            </v-list-item-title>
                            <v-list-item-subtitle>{{membership.politican.city.name}}</v-list-item-subtitle>
                        </v-list-item-content>
                    </v-list-item>
                    <v-divider :key="index"></v-divider>
                </template>

                <v-list-item>
                    <v-list-item-avatar>
                        <v-img src="/avatar.png"></v-img>
                    </v-list-item-avatar>

                    <v-list-item-content>
                        <v-list-item-title >
                            And + {{memberships.length -5}} more.
                        </v-list-item-title>
                    </v-list-item-content>
                </v-list-item>

            </v-list>

        </v-card-text>
    </v-card>
</template>
<script>
export default {
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
            let noInactiveMemberships = this.memberships.filter(el => el.politican.active !== true)
            return noInactiveMemberships;    
        }
    }
}
</script>