<template>
    <v-container>
        <br>
        <h1 class="font-weight-thin display-3 text-center animated bounceInDown">Homelab</h1>
        <br><br><br>
        <v-layout
                v-if="!api_error && homelab"
                row
                wrap
        >
            <v-tabs
                    v-model="tab"
                    background-color="teal"
                    grow
                    dark
                    icons-and-text
            >
                <v-tabs-slider color="yellow"></v-tabs-slider>

                <v-tab key="tab_homelab-rack">
                    Homelab rack
                    <v-icon>fas fa-server</v-icon>
                </v-tab>

                <v-tab key="tab_homelab-hardware-architecture">
                    Homelab hardware architecture
                    <v-icon>fas fa-sitemap</v-icon>
                </v-tab>

                <v-tab key="tab_homelab-application-architecture">
                    Homelab application architecture
                    <v-icon>fas fa-desktop</v-icon>
                </v-tab>
            </v-tabs>

            <v-container class="pa-0">
                <v-tabs-items v-model="tab">
                    <v-tab-item key="tab-homelab-rack">
                        <v-img
                                v-bind:src="homelab.rack === null ? '../assets/no_image_available.jpg' : homelab.rack"
                                v-on:error="homelab.rack = '../assets/no_image_available.jpg'"
                                alt="Homelab rack"
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
                    </v-tab-item>
                    <v-tab-item key="tab-homelab-hardware-architecture">
                        <v-img
                                v-bind:src="homelab.hardware_architecture === null ? '../assets/no_image_available.jpg' : homelab.hardware_architecture"
                                v-on:error="homelab.hardware_architecture = '../assets/no_image_available.jpg'"
                                alt="Homelab hardware architecture"
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
                    </v-tab-item>
                    <v-tab-item key="tab-homelab-application-architecture">
                        <v-img
                                v-bind:src="homelab.application_architecture === null ? '../assets/no_image_available.jpg' : homelab.application_architecture"
                                v-on:error="homelab.application_architecture = '../assets/no_image_available.jpg'"
                                alt="Homelab application architecture"
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
                    </v-tab-item>
                </v-tabs-items>
            </v-container>
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
    export default {
        name: "Portfolio",
        data: () => ({
            tab: null,
            person_id: '1',
            api_error: false,
            homelab: null
        }),
        mounted () {
            this.getHomelab(this.person_id);
        },
        methods: {
            async getHomelab(id) {
                try {
                    const response = await ApiService.getHomelab(id);
                    this.homelab = response.data;
                }
                catch (e) {
                    this.api_error = true;
                }
            }
        }
    }
</script>