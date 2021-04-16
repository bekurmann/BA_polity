<template>
    <v-card>
        <v-card-title>
            Affairs
        </v-card-title>
        <v-card-text>

            <v-data-iterator
                :items="affairs"
                item-key="id"
                :items-per-page="15"
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

                    <v-simple-table>
                            <tbody>
                                <tr v-for="(affair) in items" :key="affair.id">
                                    
                                    <td>
                                        <NuxtLink :to="$route.path + affair.id">
                                            {{affair.title}}
                                        </NuxtLink>
                                    </td>

                                    <td>
                                        {{affair.date_received}}
                                    </td>
                                    <td>
                                        {{affair.identifier}}
                                    </td>
                                    <td>
                                        <v-chip v-if="affair.accepted" color="green" dark>accepted</v-chip>
                                        <v-chip v-else color="red" dark>declined</v-chip>
                                    </td>
                                </tr>
                            </tbody>
                    </v-simple-table>

                </template>
                
            </v-data-iterator>

        </v-card-text>
    </v-card>
</template>
<script>
export default {
    data() {
        return {
            itemsPerPage: 15,
            search: '',
            sortBy: 'id',
            sortDesc: false,
            keys: [
                'id',
                'title',
                'date_received',
            ],
        }
    },
    props: {
        affairs: {
            type: Object
        },
    },
    computed: {
    }
}
</script>