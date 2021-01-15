<template>
<v-container>
    <v-card class="mx-auto" max-width="700">

        <v-img
        src="https://images.pexels.com/photos/167708/pexels-photo-167708.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260"
        height="200px"
        ></v-img>

        <v-card-title>
        Login
        </v-card-title>

        <v-card-subtitle>
        login & start!
        </v-card-subtitle>
          
        <v-card-text>
                <v-form v-model="formValid" @submit.prevent="loginUser"> 

                <v-text-field label="Username" placeholder="Your Username" outlined required v-model="username"></v-text-field>

                <v-text-field label="eMail" placeholder="Your eMail" outlined required v-model="email" :rules="[pwRules.required, pwRules.validEmail]"></v-text-field>

                <v-text-field label="Password" placeholder="Your Password" outlined required type="password" v-model="password"></v-text-field>
        
                <v-btn block color="info" type="submit">Login</v-btn>
            </v-form>
            <v-spacer class="ma-5"></v-spacer>
            <v-divider></v-divider>
            <v-spacer class="ma-5"></v-spacer>
            <p>Don't have a Login?</p>
            <p><v-btn block color="red" to="/login/registration" dark>Sign Up</v-btn></p>
        </v-card-text>
        
    </v-card>
</v-container>
</template>

<script>

export default {
    data () {
        return {
            formValid: false,

            username: '',
            email: '',
            password: '',
            pwRules: {
                required: value => !!value || 'Required.',
                //emailMatch: () => ('The email and password you entered don\'t match'),
                validEmail: v => /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) || 'E-mail must be valid',
            }
        }
    },
    methods: {
        async loginUser () {
            if(this.formValid) {
                try {
                    await this.$auth.loginWith('local', {
                        data: {
                            username: this.username,
                            password: this.password
                        }
                    })
                } catch(error) {
                    this.$notifier.showSnackbar({ content: 'Login Failed! Check your inputs.<br><br><b>Error Message:</b><br>' + error.response.data.non_field_errors, color: 'error' })
                }
            } else {
                this.$notifier.showSnackbar({ content: 'Your inputs are not valid. Try again!', color: 'info' })
            }
        }
    },
}
</script>