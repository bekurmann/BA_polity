<template>
<v-container>

        <v-row class="px-3" justify="center">
            
            <v-col cols="12" xs="12" sm="12" md="6" lg="6" xl="6">
                <v-card>

                    <v-card-title>
                    SignUp
                    </v-card-title>

                    <v-card-text>
                        <v-form v-model="formValid" @submit.prevent="registerUser"> 
                            <v-text-field label="Username" placeholder="Your Username" outline required v-model="username"></v-text-field>

                            <v-text-field label="Firstname" placeholder="Your Firstname" outline required v-model="firstname"></v-text-field>

                            <v-text-field label="Lastname" placeholder="Your Lastname" outline required v-model="lastname"></v-text-field>
                            

                            <v-text-field label="eMail" placeholder="Your eMail" required v-model="email" :rules="[formRules.required, formRules.validEmail]"></v-text-field>

                            <v-text-field
                            v-model="password1"
                            :append-icon="pwShow ? 'mdi-eye' : 'mdi-eye-off'"
                            :rules="[formRules.required, formRules.min]"
                            :type="pwShow ? 'text' : 'password'"
                            name="input-10-1"
                            label="Your Password"
                            hint="At least 8 characters"
                            counter
                            @click:append="pwShow = !pwShow"
                            ></v-text-field>

                            <v-text-field
                            v-model="password2"
                            :append-icon="pwShow ? 'mdi-eye' : 'mdi-eye-off'"
                            :rules="[formRules.required, formRules.min, formRules.pwMatch]"
                            :type="pwShow ? 'text' : 'password'"
                            name="input-10-1"
                            label="Your Password"
                            hint="At least 8 characters"
                            counter
                            @click:append="pwShow = !pwShow"
                            ></v-text-field>

                            <v-checkbox label="Accept terms of service" required v-model="terms" :rules="[formRules.required]"></v-checkbox>
                            <v-btn block color="primary" type="submit" dark>SignUp</v-btn>
                        </v-form>
                        <v-spacer class="ma-10"></v-spacer>
                        <v-divider></v-divider>
                        <v-spacer class="ma-10"></v-spacer>
                        <p>Already have an account?</p>
                        <p><v-btn block color="primary" outlined to="/login" dark>Login</v-btn></p>
                    </v-card-text>

                </v-card>

            </v-col>

        </v-row>

</v-container>
</template>

<script>

export default {
    data () {
        return {
            formValid: false,

            username: '',
            firstname: '',
            lastname: '',
            email: '',
            password1: '',
            password2: '',
            terms: false,

            pwShow: false,
            formRules: {
                required: value => !!value || 'Required.',
                min: v => v.length >= 8 || 'Min 8 characters',
                //emailMatch: () => ('The email and password you entered don\'t match'),
                validEmail: v => /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) || 'E-mail must be valid',
                pwMatch: () => (this.password1 == this.password2) || 'Passwords must match',
            },
        }
    },
    methods: {
        async registerUser () {
            if(this.formValid) {
                try {
                    await this.$axios.$post('/auth/registration/', {
                        first_name: this.firstname,
                        last_name: this.lastname,
                        username: this.username,
                        email: this.email,
                        password1: this.password1,
                        password2: this.password2
                    })
                    this.$router.push('/')
                    this.$notifier.showSnackbar({content: 'Registration successful. Check your e-mail to confirm registration process.', color: 'success'})
                } catch(error) {
                    console.log(error)
                    this.$notifier.showSnackbar({content: 'Registration failed. 🤯<br><br>'+ error.response.data.username + '<br>' + error.response.data.email, color: 'error'})
                }
            } else {
                this.$notifier.showSnackbar({ content: 'Your inputs are not valid. Try again!', color: 'info' })
            }
        }
    }
}
</script>