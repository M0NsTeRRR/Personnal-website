<template>
    <v-container>
        <h1 class="font-weight-thin display-3 text-xs-center animated bounceInDown">Portfolio</h1>
        <br><br><br>
        <v-layout
                v-if="!api_error && projects"
                row
                wrap
        >
            <v-flex
                    v-for="(project, index) in projects"
                    v-bind:key="index"
                    class="pa-2 animated fadeIn"
                    xs12
                    sm6
                    md4
            >
                <v-hover>
                    <v-card>
                        <v-img
                                v-bind:src="project.img"
                                v-bind:alt="project.title"
                                aspect-ratio="2"
                        ></v-img>
                        <v-divider></v-divider>
                        <v-card-title primary-title>
                            <div>
                                <div class="headline">{{ project.title }}</div>
                                <div>Start date : {{ project.start_date ? project.start_date : 'Unknown'}}</div>
                                <div>Publication date : {{ project.pub_date ? project.pub_date : 'Unknown'}}</div>
                            </div>
                        </v-card-title>

                        <v-card-actions>
                            <v-btn
                                    v-bind:color="get_iconBackground(project.link.type)"
                                    class="white--text title font-weight-light"
                                    v-bind:href="project.link.url"
                                    target="_blank"
                            >{{ project.link.title }}
                                <v-icon
                                        right
                                        medium
                                >
                                    {{ get_icon(project.link.type) }}
                                </v-icon>
                            </v-btn>
                            <v-spacer></v-spacer>
                            <v-btn
                                    v-if="project.description"
                                    color="teal"
                                    class="white--text"
                                    @click.stop="show_dialog(project.link.title, get_icon(project.link.type), project.link.url, get_iconBackground(project.link.type), project.description)"
                                    fab
                            >
                                <v-icon medium>fas fa-search</v-icon>
                            </v-btn>
                        </v-card-actions>
                    </v-card>
                </v-hover>
            </v-flex>
            <v-dialog
                    v-model="dialog.visible"
                    persistent
                    width="500"
            >
                <v-card>
                    <v-card-title
                            class="white--text headline teal"
                            primary-title
                    >
                        Description
                    </v-card-title>

                    <v-card-text class="subheading">
                        {{ dialog.description }}
                    </v-card-text>

                    <v-divider></v-divider>

                    <v-card-actions>
                        <v-btn
                                v-bind:color="dialog.button.color"
                                class="white--text title font-weight-light"
                                v-bind:href="dialog.button.url"
                                target="_blank"
                        >{{ dialog.button.title }}
                            <v-icon
                                    right
                                    medium
                            >
                                {{ dialog.button.icon }}
                            </v-icon>
                        </v-btn>
                        <v-spacer></v-spacer>
                        <v-btn
                                class="white--text"
                                color="teal"
                                @click="dialog.visible = false"
                        >
                            Close
                        </v-btn>
                    </v-card-actions>
                </v-card>
            </v-dialog>
        </v-layout>

        <v-layout
                v-else-if="api_error"
                row
                wrap
        >
            <v-flex xs12>
                <v-alert
                        value="true"
                        icon="fas fa-exclamation-triangle"
                        color="red"
                        class="title animated fadeInLeftBig"
                >
                    Despite sleeping on the couch most of the day, I will try to finds time to fix this.
                </v-alert>
            </v-flex>
        </v-layout>

        <v-layout
                v-else
                row
                wrap
        >
            <v-flex xs12>
                <v-alert
                        value="true"
                        icon="fas fa-exclamation-triangle"
                        color="red"
                        class="title animated fadeInLeftBig"
                >
                    Despite sleeping on the couch most of the day, I will try to work to fill this page.
                </v-alert>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
    import ApiService from '@/store/ApiService'
    import Graphics from '@/store/graphics'
    export default {
        name: "Portfolio",
        data: () => ({
            person_id: '1',
            projects: null,
            api_error: false,
            dialog: {
                description: '',
                button: {
                    color : '',
                    title : '',
                    icon : '',
                    url: ''
                },
                visible: false
            },
            test: [
                {
                    img: '',
                    title: 'Ludovic-website',
                    buttons: [
                        {id: 0, name: 'Github', href: 'https://github.com/lyon-esport/SwitchConfGenerator', icon: 'fab fa-github', color_btn_content: 'white--text', color_btn_background: 'black'}
                    ]
                },
                {
                    img: '',
                    title: 'SwitchConfGenerator',
                    buttons: [
                        {id: 0, name: 'Github', href: 'https://github.com/lyon-esport/SwitchConfGenerator', icon: 'fab fa-github', color_btn_content: 'white--text', color_btn_background: 'black'}
                    ]
                },
                {
                    img: '',
                    title: 'AdminAFK-registration',
                    buttons: [
                        {id: 0, name: 'Github', href: 'https://github.com/lyon-esport/AdminAFK-registration', icon: 'fab fa-github', color_btn_content: 'white--text', color_btn_background: 'black'}
                    ]
                },
                {
                    img: '',
                    title: 'Supervision',
                    buttons: [
                        {id: 0, name: 'Github', href: 'https://github.com/lyon-esport/Supervision', icon: 'fab fa-github', color_btn_content: 'white--text', color_btn_background: 'black'}
                    ]
                },
                {
                    img: '',
                    title: 'Monitor-VRRP',
                    buttons: [
                        {id: 0, name: 'Github', href: 'https://github.com/lyon-esport/Monitor-VRRP', icon: 'fab fa-github', color_btn_content: 'white--text', color_btn_background: 'black'}
                    ]
                },
                {
                    img: '',
                    title: 'Discord-BOT-AdminAFK',
                    buttons: [
                        {id: 0, name: 'Github', href: 'https://github.com/lyon-esport/Discord-BOT-AdminAFK', icon: 'fab fa-github', color_btn_content: 'white--text', color_btn_background: 'black'}
                    ]
                },
                {
                    img: '',
                    title: 'AdminAFK',
                    buttons: [
                        {id: 0, name: 'Github', href: 'https://github.com/lyon-esport/AdminAFK', icon: 'fab fa-github', color_btn_content: 'white--text', color_btn_background: 'black'}
                    ]
                }
            ]
        }),
        mounted () {
            this.getProjects(this.person_id)
        },
        methods: {
            async getProjects(id) {
                try {
                    const response = await ApiService.getProjects(id);
                    this.projects = response.data;
                }
                catch (e) {
                    this.api_error = true;
                }
            },
            get_icon: function(type)
            {
                return Graphics.get_icon(type);
            },
            get_iconBackground: function(type)
            {
                return Graphics.get_iconBackground(type);
            },
            show_dialog: function(title, icon, url, color, description)
            {
                this.dialog.button.title = title;
                this.dialog.button.icon = icon;
                this.dialog.button.url = url;
                this.dialog.button.color = color;
                this.dialog.description = description;
                this.dialog.visible = true;
            }
        }
    }
</script>