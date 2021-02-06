<template>
<v-container>

    <v-card color="primary">

    <v-row class="px-3" align="center">

        <v-col cols="12" xs="12" sm="12" md="6" lg="6" xl="6">
            <v-card>
                <v-card-title>
                Login
                </v-card-title>
                
                <v-card-text>
                        <v-form v-model="formValid" @submit.prevent="loginUser"> 

                        <v-text-field label="Username" placeholder="Your Username" outlined required v-model="username"></v-text-field>

                        <v-text-field label="eMail" placeholder="Your eMail" outlined required v-model="email" :rules="[pwRules.required, pwRules.validEmail]"></v-text-field>

                        <v-text-field label="Password" placeholder="Your Password" outlined required type="password" v-model="password"></v-text-field>
                
                        <v-btn block color="primary" type="submit">Login</v-btn>
                    </v-form>
                    <v-spacer class="ma-5"></v-spacer>
                    <v-divider></v-divider>
                    <v-spacer class="ma-5"></v-spacer>
                    <p>Don't have a Login?</p>
                    <p><v-btn block color="primary" outlined to="/registration" dark>Sign Up</v-btn></p>
                </v-card-text>
            </v-card>

        </v-col>

        <v-col cols="12" xs="12" sm="12" md="6" lg="6" xl="6" align="center">
                <v-img src="/home/login.svg" max-width="80%"></v-img>
        </v-col>

    </v-row>  

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
                    this.$notifier.showSnackbar({ content: 'Login successful! <br>Welcome @ polity.ch 👋', color: 'success' })
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