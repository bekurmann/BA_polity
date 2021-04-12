<template>
    <v-card>
        <v-card-title primary-title>
            Members
        </v-card-title>
        <v-card-text>

            <v-data-iterator
                :items="memberships"
                item-key="id"
                :items-per-page="5"
                :search="search"
                :sort-by="sortBy.toLowerCase()"
                :sort-desc="sortDesc"
            >
                <template v-slot:header>
                    <v-toolbar color="primary" dark>
                        <v-text-field
                            v-model="search"
                            clearable
                            flat
                            solo-inverted
                            hide-details
                            prepend-inner-icon="mdi-magnify"
                            label="Search"
                        ></v-text-field>
                        <template v-if="$vuetify.breakpoint.mdAndUp">
                            <v-spacer></v-spacer>
                            <v-select
                            v-model="sortBy"
                            flat
                            solo-inverted
                            hide-details
                            :items="keys"
                            label="Sort by"
                            ></v-select>
                            <v-spacer></v-spacer>
                            <v-btn-toggle
                            v-model="sortDesc"
                            mandatory
                            >
                            <v-btn
                                large
                                depressed
                                color="blue"
                                :value="false"
                            >
                                <v-icon>mdi-arrow-up</v-icon>
                            </v-btn>
                            <v-btn
                                large
                                depressed
                                color="blue"
                                :value="true"
                            >
                                <v-icon>mdi-arrow-down</v-icon>
                            </v-btn>
                            </v-btn-toggle>
                        </template>
                    </v-toolbar>
                </template>

                <template v-slot:default="{ items }">

                    <v-list three-line>

                        <template v-for="(membership, index) in items">
                            <v-list-item :key="membership.id">
                                <v-list-item-avatar>
                                    <v-img :src="membership.politican.avatar"></v-img>
                                </v-list-item-avatar>

                                <v-list-item-content>
                                    <v-list-item-title >
                        
                                        <NuxtLink :to="'/politicans/' + membership.politican.id">{{membership.politican.first_name}} {{membership.politican.last_name}}</NuxtLink> 
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
            search: '',
            sortBy: 'id',
            sortDesc: false,
            keys: [
                'id',
                'first_name',
                'last_name',
                'city',
            ],
        }
    },
    props: {
        memberships: {
            type: Array
        },
    },
    computed: {
    }
}
</script>