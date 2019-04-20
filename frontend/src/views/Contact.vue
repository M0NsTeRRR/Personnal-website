<template>
    <v-container>
        <h1 class="font-weight-thin display-3 text-xs-center animated bounceInDown">Contact</h1>
        <br><br><br>
        <v-layout>
            <v-flex offset-lg2 lg8 offset-md1 md10 xs12>
                <v-form
                        ref="form"
                        v-model="valid"
                        lazy-validation
                >
                    <v-layout
                            row
                            v-for="(field, index) in fields"
                            v-bind:key="index"
                    >
                        <component
                                v-bind:is="field.type"
                                class="title animated fadeIn slow"
                                outline
                                clearable
                                clear-icon="fas fa-times-circle"
                                v-bind:append-outer-icon="field.icon"
                                background-color="teal"
                                color="teal"
                                v-model="$data[field.name]"
                                v-bind:label="field.label"
                                v-bind:rules="$data[field.rules]"
                                required
                        ></component>
                    </v-layout>
                    <v-layout row justify-center>
                        <v-btn
                                color="teal"
                                class="font-weight-light title white--text animated bounceInUp"
                                v-bind:disabled="!valid"
                                @click="validate"
                        >
                            Submit
                            <v-icon right>fas fa-paper-plane</v-icon>
                        </v-btn>
                    </v-layout>
                </v-form>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
    import { VTextField, VTextarea } from 'vuetify/lib'
    import ApiService from '@/store/ApiService'

    export default {
        name: "Contact",
        components: { VTextField, VTextarea },
        data: () => ({
            animation_contact: true,
            valid : true,
            name: '',
            nameRules: [
                v => !!v || 'Name is required',
                v => /^.{1,50}$/.test(v) || 'Name must be valid (1-50 characters)'
            ],
            subject: '',
            subjectRules: [
                v => !!v || 'Subject is required',
                v => /^.{1,50}$/.test(v) || 'Subject must be valid (1-50 character)'
            ],
            email: '',
            emailRules: [
                v => !!v || 'Email is required',
                v => /^([a-zA-Z0-9_.\-+])+@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/.test(v) || 'Email must be valid'
            ],
            message: '',
            messageRules: [
                v => !!v || 'Message is required',
                v => /^.{1,2000}$/.test(v) || 'Message must be valid (1-2000 characters)'
            ],
            fields: [
                {icon: 'fas fa-user', name: 'name', label: 'Name', type: 'v-text-field', animation: 'animated bounceInLeft', rules: 'nameRules'},
                {icon: 'fas fa-at', name: 'email', label: 'Email', type: 'v-text-field', animation: 'animated bounceInRight', rules: 'emailRules'},
                {icon: 'fas fa-heading', name: 'subject', label: 'Subject', type: 'v-text-field', animation: 'animated bounceInLeft', rules: 'subjectRules'},
                {icon: 'far fa-comment-dots', name: 'message', label: 'Message', type: 'v-textarea', animation: 'animated bounceInRight', rules: 'messageRules'},
            ]
        }),
        methods: {
            validate () {
                if (this.$refs.form.validate()) {
                    this.snackbar = true;
                    this.postMail(this.name, this.email, this.subject, this.message);
                }
            },
            async postMail(name, email, subject, message) {
                try {
                    const response = await ApiService.postMail(name, email, subject, message);
                    this.mail_response = response.data;
                }
                catch (e) {
                    this.mail_response = "ERROR";
                }
            }
        }
    }
</script>