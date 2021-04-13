<template>
  <v-app style="background-color: #eee;">
    <!-- navigation drawer ********************************** -->
    <v-navigation-drawer
      v-model="drawer"
      clipped
      fixed
      right
      app
      class="primary"
      dark
      disable-resize-watcher
    >
      <v-list rounded>
        <v-list-item
          v-for="(item, i) in drawerItems"
          :key="i"
          :to="item.to"
          router
          exact
        >
          <v-list-item-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title v-text="item.title" />
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <!-- app bar ********************************** -->
    <v-app-bar
      clipped-right
      fixed
      color="white"
      app
    >
      <client-only>

      <nuxt-link to="/">
        <v-img src="/polity.jpg" class="mx-2" max-width="100" max-height="50" contain />
      </nuxt-link>
      
      <v-spacer />
    
      <!-- desktop menu -->
      <div v-show="$vuetify.breakpoint.mdAndUp && $auth.loggedIn">
        <v-btn
          v-for="(item, i) in drawerItems"
          :key="i"
          :to="item.to"
          router
          text
          class="mx-2"
          rounded
        >
          <v-icon class="mx-1">{{ item.icon }}</v-icon>{{ item.title}}
        </v-btn>
      </div>

      <v-spacer />
     
      <!-- user menu -->
      <template v-if="$auth.loggedIn">

        <v-divider vertical class="mx-2"></v-divider>
        <v-icon>mdi-bell-outline</v-icon>
        
        <v-divider vertical class="mx-2"></v-divider>

        <v-menu offset-y>
          <template v-slot:activator="{on, attrs}">

            <v-avatar v-bind="attrs" v-on="on">
              <img :src="$auth.user.avatar" class="mx-2" max-height="40" max-width="40" contain v-if="$auth.user.avatar != null" />
              <img src="/avatar.png" class="mx-2" max-height="40" max-width="40" contain v-else />
            </v-avatar>
          </template>

          <v-list>
            <v-list-item v-for="(item, index) in userItems" :key="index" :to="item.to" link>
              <v-list-item-title>
                <v-icon class="mx-1">{{ item.icon }}</v-icon>
                {{ item.title }}
              </v-list-item-title>
            </v-list-item>
            <v-list-item @click="$auth.logout()">
              <v-icon class="mx-1">mdi-exit-to-app</v-icon>
              Logout
            </v-list-item>
          </v-list>

        </v-menu>
        
      </template>
      <template v-else>
        <v-btn color="primary" outlined to="/login">Login</v-btn>
      </template>


      <!-- mobile menu -->
      <template v-if="$vuetify.breakpoint.smAndDown">
        <v-divider vertical class="mx-2"></v-divider>
        <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      </template>

      </client-only>

    </v-app-bar>

    <!-- main ********************************** -->
    <v-main>
      <v-container v-if="$fetchState.pending">
        <v-card>
            <v-skeleton-loader
            class="mx-auto"
            type="article@2"
            light
            ></v-skeleton-loader>
        </v-card>
      </v-container>

      <v-container v-else>

        <!-- additional menu for parlaments -->
        <v-card dark color="primary">

          <v-card-text align="center">
              <v-row>
                <v-col>
                  <v-card-text align="center">
                    <v-img 
                      :src="selectedParlament.jurisdiction_canton.emblem" 
                      max-height="100" 
                      contain
                    ></v-img>
                    {{selectedParlament.title}}
                  </v-card-text>
                </v-col>
              </v-row>

              <v-row>
                <v-col>

                  <v-btn :to="'/parlaments/' + $route.params.id " router exact text rounded>
                      Overview
                      <v-icon top>mdi-view-comfy-outline</v-icon>
                  </v-btn>

                  <v-btn :to="'/parlaments/' + $route.params.id + '/members/'" router text rounded>
                          Members
                          <v-icon>mdi-account-multiple-outline</v-icon>
                  </v-btn>  

                  <v-btn :to="'/parlaments/' + $route.params.id + '/affairs/'" router text rounded>
                          Affairs
                          <v-icon>mdi-file-document-outline</v-icon>
                  </v-btn>  

                  <v-btn :to="'/parlaments/' + $route.params.id + '/sessions/'" router text rounded>
                          Sessions
                          <v-icon>mdi-seat-outline</v-icon>
                  </v-btn>  

                  <v-btn :to="'/parlaments/' + $route.params.id + '/commissions/'" router text rounded>
                          Commissions
                          <v-icon>mdi-domain</v-icon>
                  </v-btn>  

                  <v-btn :to="'/parlaments/' + $route.params.id + '/map/'" router text rounded>
                          Map
                          <v-icon>mdi-map-marker-outline</v-icon>
                  </v-btn> 

                  <v-btn :to="'/parlaments/' + $route.params.id + '/analysis/'" router text rounded>
                          Analysis
                          <v-icon>mdi-chart-line-variant</v-icon>
                  </v-btn> 

                  

                </v-col>
              </v-row>

            </v-card-text>

        </v-card> 


        <nuxt />
      </v-container>
    </v-main>

    <!-- global Snackbar -->
    <Snackbar></Snackbar>

  </v-app>
</template>

<script>
import Snackbar from '~/components/Snackbar.vue'
import {mapState} from 'vuex'

export default { 
  name: "parlaments",
  components: {
    Snackbar,
  },
  data () {
    return {
      //parlamentInformation: {},
      drawer: false,
      drawerItems: [
        {
          icon: 'mdi-chart-bubble',
          title: 'Start',
          to: '/start'
        },
        {
          icon: 'mdi-bank',
          title: 'Parlaments',
          to: '/parlaments'
        },
        {
          icon: 'mdi-account-multiple',
          title: 'Politicans',
          to: '/politicans',
        },
        {
          icon: 'mdi-file-document-outline',
          title: 'Affairs',
          to: '/affairs',
        },
      ],
      userItems: [
        { 
          icon: 'mdi-account',
          title: 'My Profile',
          to: '/user',
        }
      ]
    }
  },
  async fetch() {
      try {
          const parlamentData = await this.$axios.$get(`/parlaments/${this.$route.params.id}`);
          this.$store.dispatch("parlaments/setSelectedParlament", parlamentData);
      } catch(error) {
          throw new Error(`Failed to fetch parlamentData from /parlaments/${this.$route.params.id}`)
      }
  },
  computed: {
    ...mapState({
      selectedParlament: state => state.parlaments.selectedParlament
    })
  }
}
</script>