<template>
    <v-container>
        <br>
        <v-layout v-if="!api_error">
            <v-flex lg8 offset-lg2 sm10 offset-sm1 xs12 v-if="person">
                <div class="text-xs-center">
                    <div v-if="person.name" class="display-2 animated bounceInDown">&nbsp;{{ person.name }}</div>
                    <br>
                    <div v-if="person.nationality" class="title font-weight-light animated rollIn">&nbsp;&nbsp;Nationality : {{ person.nationality }}</div>
                    <div v-if="person.birthdate" class="title font-weight-light animated rollIn">&nbsp;&nbsp;Age : {{ render_ageFromBirthay(person.birthdate) }}</div>
                    <div v-if="person.city_residence" class="title font-weight-light animated rollIn">&nbsp;&nbsp;City : {{ person.city_residence }}</div>
                </div>
                <br>
                <div class="text-xs-center">
                    <v-avatar
                            color="grey lighten-4"
                            size="200"
                    >
                        <img v-if="person.photo" class="animated zoomIn" v-bind:src="person.photo" alt="photo">
                    </v-avatar>
                </div>
                <br>
                <div v-if="person.actual_position" class="text-xs-center">
                    <div><v-btn flat small class="title font-weight-light text-capitalize animated rollIn" v-bind:href="person.actual_position.url" target="_blank">{{ person.actual_position.title }}</v-btn></div>
                </div>
                <br>
                <div>
                    <span v-if="person.presentation">
                        <div class="display-1 font-weight-light">Presentation</div>
                        <br>
                        <div class="title font-weight-light animated bounceInLeft">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{ person.presentation }}</div>
                        <br>
                    </span>
                    <span v-if="experiences">
                        <div class="display-1 font-weight-light">Work experience</div>
                        <div
                                v-for="work in render_experience('work')"
                                v-bind:key="work.id"
                        >
                            <v-btn flat small class="title font-weight-light text-capitalize animated bounceInLeft" v-bind:href="work.url" target="_blank">- {{ work.title }}</v-btn>
                        </div>
                        <br>
                        <div class="display-1 font-weight-light">Volonteer experience</div>
                        <div
                                v-for="volunteer in render_experience('volunteer')"
                                v-bind:key="volunteer.id"
                        >
                            <v-btn flat small class="title font-weight-light text-capitalize animated bounceInLeft" v-bind:href="volunteer.url" target="_blank">- {{ volunteer.title }}</v-btn>
                        </div>
                        <br>
                    </span>
                    <span v-if="languages">
                        <div class="display-1 font-weight-light">Language</div>
                        <div
                                v-for="language in languages"
                                v-bind:key="language.id"
                        >
                            <v-btn flat small class="title font-weight-light text-capitalize animated bounceInLeft">- {{ language.name }} {{ render_optionnalField('(', language.level, ')') }}</v-btn>
                        </div>
                        <br>
                    </span>
                    <span v-if="educations">
                        <div class="display-1 font-weight-light">Education</div>
                        <div
                                v-for="education in educations"
                                v-bind:key="education.id"
                        >
                            <v-btn flat small class="title font-weight-light text-capitalize animated bounceInLeft" v-bind:href="education.url" target="_blank">- {{ education.title }} {{ render_optionnalField('(', education.subtitle, ')') }}</v-btn>
                        </div>
                        <br>
                    </span>
                    <br>
                    <v-tabs
                            v-if="skills"
                            centered
                            color="teal"
                            icons-and-text
                            dark
                    >
                        <v-tabs-slider color="yellow"></v-tabs-slider>

                        <v-tab
                                v-for="skill in skills"
                                v-bind:key="'tab_' + skill.id"
                                class="title font-weight-light"
                        >
                            {{ skill.title }}
                            <v-icon>{{ get_icon(skill.title) }}</v-icon>
                        </v-tab>

                        <v-tab-item
                                v-for="(skill, indexSkill) in skills"
                                v-bind:key="'tabitem_' + indexSkill"
                                v-bind:value="indexSkill"
                        >
                            <v-card flat>
                                <v-card-text>
                                    <span
                                            v-for="(skillTheme, indexTheme) in skill.skillThemes"
                                            v-bind:key="indexTheme"
                                    >
                                        <v-chip
                                                v-for="(item, indexItem) in skillTheme.skillItems"
                                                v-bind:key="indexItem"
                                                color="teal"
                                                text-color="white"
                                        >
                                            <div class="title font-weight-light">{{ item.title }}</div>
                                            <v-rating
                                                    v-bind:length="item.stars"
                                                    v-bind:value="item.stars"
                                                    v-bind:full-icon="get_icon(skill.title)"
                                                    v-bind:half-icon="get_icon(skill.title)"
                                                    v-bind:empty-icon="get_icon(skill.title)"
                                                    small
                                                    color="yellow"
                                                    readonly
                                            >
                                            </v-rating>
                                        </v-chip>
                                    </span>
                                </v-card-text>
                            </v-card>
                        </v-tab-item>
                    </v-tabs>
                    <br>
                    <div
                            v-if="person.cv_url"
                            class="text-xs-center animated bounceInUp"
                    >
                        <v-btn
                                class="white--text display-1 font-weight-light text-capitalize"
                                color="teal"
                                v-bind:href="person.cv_url"
                                target="_blank"
                                v-bind:download="render_cvFilename(person.name)"
                        >Download CV
                            <v-icon
                                    right
                                    medium>
                                fas fa-file-download
                            </v-icon>
                        </v-btn>
                    </div>
                </div>
            </v-flex>
        </v-layout>
        <v-layout
                v-else
                row
                wrap
        >
            <v-flex xs12>
                <h1 class="font-weight-thin display-3 text-xs-center animated bounceInDown">About</h1>
                <br><br><br>
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
    </v-container>
</template>

<script>
    import ApiService from '@/store/ApiService'
    import Graphics from '@/store/graphics'
    export default {
        name: "About",
        data: () => ({
            person_id: '1',
            person: null,
            experiences: null,
            educations: null,
            languages: null,
            skills: null,
            animation_about: true,
            api_error: false,
            actualPosition: {title: 'Student in Networks & Telecoms', url: 'https://www.iut-valence.fr/nos-formations/dut/dut-reseaux-et-telecoms-247966.kjsp'},
            workExperiences: [
                {title: 'Esports Micro entrepreneur', url: 'https://www.societe.com/societe/ludovic-ortega-832968283.html'},
                {title: 'Order picker Burger King', url: 'https://www.burgerking.fr/'}
            ],
            volonteerExperiences: [
                {title: 'Tech sys & networks Lyon e-Sport', url: 'https://www.lyon-esport.fr/'},
                {title: 'Head-Admin VaKarM', url: 'https://www.vakarm.net/'},
                {title: 'Tech support Faceit', url: 'https://www.faceit.com/'},
                {title: 'Head-Admin FDJ eSport', url: 'https://www.fdjesport.fr/'}
            ],
            technical_skills: {
                networks: {
                    icon: 'fas fa-ethernet',
                    technologies: [
                        {name: 'TCP/IP', stars: 5},
                        {name: 'LAN Routing', stars: 5},
                        {name: 'NAT', stars: 5},
                        {name: 'VLAN', stars: 5},
                        {name: 'ACL / Firewall', stars: 3},
                        {name: 'Wi-Fi', stars: 3},
                        {name: 'IPBX', stars: 3},
                        {name: 'VPN', stars: 2},
                        {name: 'SDN', stars: 1},
                        {name: 'MPLS', stars: 1}
                    ]
                },
                programming: {
                    icon: 'fas fa-code',
                    language: [
                        {name: 'PHP', stars: 5},
                        {name: 'Python', stars: 5},
                        {name: 'Html', stars: 5},
                        {name: 'JavaScript', stars: 3},
                        {name: 'Bash', stars: 3},
                        {name: 'CSS', stars: 2},
                        {name: 'C', stars: 2},
                        {name: 'Pascal', stars: 2},
                        {name: 'SQL', stars: 2},
                        {name: 'PowerShell', stars: 2},
                        {name: 'Java & Android', stars: 2}
                    ],
                    framework: [
                        {name: 'BootStrap', language: ['CSS', 'JavaScript'], stars: 5},
                        {name: 'Bulma', language: ['CSS'], stars: 5},
                        {name: 'Flask', language: ['Python'], stars: 3},
                        {name: 'JQuery', language: ['JavaScript'], stars: 2},
                        {name: 'Django', language: ['Python'], stars: 2},
                        {name: 'VueJS', language: ['JavaScript'], stars: 2},
                        {name: 'Vuetify', language: ['CSS', 'JavaScript'], stars: 2}
                    ]
                },
                systems: {
                    icon: 'fas fa-server',
                    technologies: [
                        {name: 'Linux', stars: 5},
                        {name: 'DHCP / DNS', stars: 5},
                        {name: 'Apache/Nginx', stars: 4},
                        {name: 'ESXI', stars: 3},
                        {name: 'Windows / Windows servers', stars: 3},
                        {name: 'Dockers', stars: 3},
                        {name: 'Grafana / Centreon', stars: 3},
                        {name: 'Ansible', stars: 1}
                    ]
                },
            }
        }),
        mounted () {
            this.getPerson(this.person_id);
            this.getExperiences(this.person_id);
            this.getEducations(this.person_id);
            this.getLanguages(this.person_id);
            this.getSkills(this.person_id);
        },
        methods: {
            async getPerson(id) {
                try {
                    const response = await ApiService.getPerson(id);
                    this.person = response.data;
                }
                catch (e) {
                    this.api_error = true;
                }
            },
            async getExperiences(id) {
                try {
                    const response = await ApiService.getExperiences(id);
                    this.experiences = response.data;
                }
                catch (e) {
                    this.api_error = true;
                }
            },
            async getEducations(id) {
                try {
                    const response = await ApiService.getEducations(id);
                    this.educations = response.data;
                }
                catch (e) {
                    this.api_error = true;
                }
            },
            async getLanguages(id) {
                try {
                    const response = await ApiService.getLanguages(id);
                    this.languages = response.data;
                }
                catch (e) {
                    this.api_error = true;
                }
            },
            async getSkills(id) {
                try {
                    const response = await ApiService.getSkills(id);
                    this.skills = response.data;
                }
                catch (e) {
                    this.api_error = true;
                }
            },
            render_ageFromBirthay: function(birthday) {
                return ~~((Date.now() - Date.parse(birthday)) / (31557600000));
            },
            get_icon: function(type)
            {
                return Graphics.get_icon(type);
            },
            render_experience: function(type)
            {
                return this.experiences.filter(experience => experience.type === type);
            },
            render_cvFilename: function(name)
            {
                return name.replace(" ", "-") + "_CV";
            },
            render_optionnalField: function(prefix, field, suffix)
            {
                return field.length > 0 ? prefix + field + suffix : '';
            }
        }
    }
</script>