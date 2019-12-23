<template>
    <v-container>
        <br>
        <h1 class="font-weight-thin display-3 text-center animated bounceInDown">Portfolio</h1>
        <br><br><br>
        <v-layout
                v-if="!api_error"
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
                                v-bind:src="project.img === null ? '../assets/no_image_available.jpg' : project.img"
                                v-on:error="projects[index].img = '../assets/no_image_available.jpg'"
                                v-bind:alt="project.title"
                                aspect-ratio="2"
                        >
                            <template v-slot:placeholder>
                                <v-row
                                        class="fill-height ma-0"
                                        align="center"
                                        justify="center"
                                >
                                    <v-progress-circular indeterminate color="teal"></v-progress-circular>
                                </v-row>
                            </template>
                        </v-img>
                        <v-divider></v-divider>
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
                                    class="white--text subtitle-1 font-weight-light"
                                    v-bind:href="project.link.url"
                                    target="_blank"
                            >{{ project.link.type }}
                                <v-icon right size="24px">{{ get_icon(project.link.type) }}</v-icon>&nbsp;
                            </v-btn>
                            <v-spacer></v-spacer>
                            <v-btn
                                    v-if="project.description"
                                    color="teal"
                                    class="white--text"
                                    @click.stop="show_dialog(project)"
                                    fab
                            >
                                <v-icon size="24px">fas fa-search</v-icon>
                            </v-btn>
                        </v-card-actions>
                    </v-card>
                </v-hover>
            </v-flex>
            <v-dialog
                    v-model="dialog.visible"
                    width="900"
            >
                <v-card>
                    <v-card-title
                            class="white--text display-1 teal"
                            primary-title
                    >
                        {{ dialog.title }}
                    </v-card-title>
                    <v-layout class="pa-2">
                        <v-img
                                v-bind:src="dialog.img === null ? '../assets/no_image_available.jpg' : dialog.img"
                                v-bind:alt="dialog.title"
                                aspect-ratio="2"
                        >
                            <template v-slot:placeholder>
                                <v-row
                                        class="fill-height ma-0"
                                        align="center"
                                        justify="center"
                                >
                                    <v-progress-circular indeterminate color="teal"></v-progress-circular>
                                </v-row>
                            </template>
                        </v-img>
                    </v-layout>

                    <v-card-text class="headline black--text">
                        {{ dialog.description }}
                    </v-card-text>

                    <v-card-actions>
                        <v-btn
                                v-bind:color="dialog.button.color"
                                class="white--text subtitle-1 font-weight-light"
                                v-bind:href="dialog.button.url"
                                target="_blank"
                        >{{ dialog.button.type }}
                            <v-icon right size="24px">{{ dialog.button.icon }}</v-icon>&nbsp;
                        </v-btn>
                        <v-spacer></v-spacer>
                        <v-btn
                                class="white--text subtitle-1"
                                color="teal"
                                @click="dialog.visible = false"
                        >
                            Close
                            <v-icon right size="24px">fas fa-times-circle</v-icon>&nbsp;
                        </v-btn>
                    </v-card-actions>
                </v-card>
            </v-dialog>
        </v-layout>

        <v-layout
                v-else
                row
                wrap
        >
            <v-flex xs12>
                <v-alert
                        type="error"
                        icon="fas fa-exclamation-triangle"
                        class="title animated fadeInLeftBig"
                >
                    Despite sleeping on the couch most of the day, I will try to finds time to fix this.
                </v-alert>
            </v-flex>
        </v-layout>
        <br>
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
                title: '',
                img: '',
                description: '',
                button: {
                    color : '',
                    type : '',
                    icon : '',
                    url: ''
                },
                visible: false
            }
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
                return Graphics.getIcon(type);
            },
            get_iconBackground: function(type)
            {
                return Graphics.getIconBackground(type);
            },
            show_dialog: function(project)
            {
                this.dialog.button.type = project.link.type;
                this.dialog.button.icon = this.get_icon(project.link.type);
                this.dialog.button.url = project.link.url;
                this.dialog.button.color = this.get_iconBackground(project.link.type);
                this.dialog.title = project.title;
                this.dialog.img = project.img;
                this.dialog.description = project.description;
                this.dialog.visible = true;
            }
        }
    }
</script>
