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
      <v-container>
        <nuxt />
      </v-container>
    </v-main>

    <!-- global Snackbar -->
    <Snackbar></Snackbar>

  </v-app>
</template>

<script>
import Snackbar from '~/components/Snackbar.vue'

export default { 
  name: "default",
  components: {
    Snackbar
  },
  data () {
    return {
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
  }
}
</script>