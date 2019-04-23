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
                        <v-card>
                            <v-card-title>
                                <div class="title font-weight-light animated bounceInLeft">{{ person.presentation }}</div>
                            </v-card-title>
                        </v-card>
                        <br>
                    </span>
                    <span v-if="experiences">
                        <div class="display-1 font-weight-light">Work experience</div>
                        <br>
                        <v-expansion-panel>
                            <v-expansion-panel-content
                                    v-for="work in render_experience('work')"
                                    v-bind:key="work.id"
                                    class="animated bounceInLeft"
                            >
                                <template v-slot:actions>
                                    <v-icon color="teal">fas fa-chevron-down</v-icon>
                                </template>
                                <template v-slot:header>
                                    <div class="title font-weight-light">
                                        {{ work.title }}
                                        <v-spacer></v-spacer>
                                        <span class="subheading font-weight-light font-italic">{{ work.start_date }}{{ work.end_date ? ' - ' + work.end_date : ' - Present '}} ({{ render_duration_between_date(work.start_date, work.end_date) }})</span>
                                    </div>
                                </template>
                                <v-card>
                                    <v-card-text class="grey lighten-3">{{ work.description }}</v-card-text>
                                    <v-card-text v-if="work.url" class="grey lighten-3 text-xs-center"><v-btn flat class="title font-weight-light text-capitalize teal white--text" v-bind:href="work.url" target="_blank">Website</v-btn></v-card-text>
                                </v-card>
                            </v-expansion-panel-content>
                        </v-expansion-panel>
                        <br>
                        <div class="display-1 font-weight-light">Volonteer experience</div>
                        <br>
                        <v-expansion-panel>
                            <v-expansion-panel-content
                                    v-for="volunteer in render_experience('volunteer')"
                                    v-bind:key="volunteer.id"
                                    class="animated bounceInLeft"
                            >
                                <template v-slot:actions>
                                    <v-icon color="teal">fas fa-chevron-down</v-icon>
                                </template>
                                <template v-slot:header>
                                    <div class="title font-weight-light">
                                        {{ volunteer.title }}
                                        <v-spacer></v-spacer>
                                        <span class="subheading font-weight-light font-italic">{{ volunteer.start_date }}{{ volunteer.end_date ? ' - ' + volunteer.end_date : ' - Present '}} ({{ render_duration_between_date(volunteer.start_date, volunteer.end_date) }})</span>
                                    </div>
                                </template>
                                <v-card>
                                    <v-card-text class="grey lighten-3">{{ volunteer.description }}</v-card-text>
                                    <v-card-text v-if="volunteer.url" class="grey lighten-3 text-xs-center"><v-btn flat class="title font-weight-light text-capitalize teal white--text" v-bind:href="volunteer.url" target="_blank">Website</v-btn></v-card-text>
                                </v-card>
                            </v-expansion-panel-content>
                        </v-expansion-panel>
                        <br>
                    </span>
                    <span v-if="languages">
                        <div class="display-1 font-weight-light">Language</div>
                        <br>
                        <v-card>
                            <v-card-title
                                    v-for="language in languages"
                                    v-bind:key="language.id"
                            >
                                <div class="title font-weight-light text-capitalize animated bounceInLeft">{{ language.name }} {{ render_optionnalField('(', language.level, ')') }}</div>
                            </v-card-title>
                        </v-card>
                        <br>
                    </span>
                    <span v-if="educations">
                        <div class="display-1 font-weight-light">Education</div>
                        <br>
                        <v-expansion-panel>
                            <v-expansion-panel-content
                                    v-for="education in educations"
                                    v-bind:key="education.id"
                                    class="animated bounceInLeft"
                            >
                                <template v-slot:actions>
                                    <v-icon color="teal">fas fa-chevron-down</v-icon>
                                </template>
                                <template v-slot:header>
                                    <div class="title font-weight-light">{{ render_year(education.date) }} - {{ education.title }}</div>
                                </template>
                                <v-card>
                                    <v-card-text v-if="education.url" class="grey lighten-3 text-xs-center"><v-btn flat class="title font-weight-light text-capitalize teal white--text" v-bind:href="education.url" target="_blank">Website</v-btn></v-card-text>
                                </v-card>
                            </v-expansion-panel-content>
                        </v-expansion-panel>
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
                                        <v-spacer></v-spacer>
                                        <div class="headline font-weight-light text-xs-center">{{ skillTheme.title }}</div>
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
                        >View my CV
                            <v-icon
                                    right
                                    medium>
                                fas fa-eye
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
            api_error: false
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
            render_optionnalField: function(prefix, field, suffix)
            {
                return field.length > 0 ? prefix + field + suffix : '';
            },
            render_duration_between_date: function (begin, end)
            {
                begin = new Date(begin);
                end = end ? new Date(end) : new Date();

                let duration = '';

                let yy = end.getFullYear() - begin.getFullYear();
                let mm = end.getMonth() - begin.getMonth();

                yy = Math.sign(mm) === -1 ? yy -1 : yy;
                mm = Math.abs(mm);

                if(yy > 0)
                {
                    duration = yy === 1 ? yy + ' year' : yy + ' years';
                }

                if(mm > 0)
                {
                    duration = duration.length > 0 ? duration + ' ' : '';
                    duration = duration + (mm === 1 ? mm + ' month' : mm + ' months');
                }

                if(!duration)
                {
                    const dd = end.getDate() - begin.getDate() === 0 ? 1 : end.getDate() - begin.getDate();
                    duration = dd === 1 ? dd + ' day' : dd + ' days';
                }

                return duration;
            },
            render_year: function(date)
            {
                return date.getFullYear();
            }
        }
    }
</script>