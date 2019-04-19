<template>
    <v-container>
        <h1 class="font-weight-thin display-3 text-xs-center animated bounceInDown">Contact</h1>
        <br><br><br>
        <v-layout>
            <v-flex offset-lg2 lg8 offset-md1 md10 xs12>
                <v-alert
                        value="true"
                        icon="fas fa-exclamation-triangle"
                        color="red"
                        class="title animated fadeInLeftBig"
                >
                    Under construction.
                </v-alert>
                <form method="post">
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
                                v-bind:name="field.name"
                                v-bind:label="field.label"
                                required
                        ></component>
                    </v-layout>
                    <v-layout row justify-center>
                        <v-btn
                                type="submit"
                                color="teal"
                                class="font-weight-light title white--text animated bounceInUp"
                                disabled
                        >
                            Submit
                            <v-icon right>fas fa-paper-plane</v-icon>
                        </v-btn>
                    </v-layout>
                </form>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
    import { VTextField, VTextarea } from 'vuetify/lib'

    export default {
        name: "Contact",
        components: { VTextField, VTextarea },
        data: () => ({
            fields: [
                {icon: 'fas fa-user', name: 'name', label: 'Name', type: 'v-text-field', animation: 'animated bounceInLeft'},
                {icon: 'fas fa-at', name: 'email', label: 'Email', type: 'v-text-field', animation: 'animated bounceInRight'},
                {icon: 'fas fa-heading', name: 'subject', label: 'Subject', type: 'v-text-field', animation: 'animated bounceInLeft'},
                {icon: 'far fa-comment-dots', name: 'message', label: 'Message', type: 'v-textarea', animation: 'animated bounceInRight'},
            ],
            animation_contact: true
        })
    }
</script>