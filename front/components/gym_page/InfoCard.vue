<template>
  <v-card class="pa-2" tile>
    <v-container>
      <v-row>
        <v-col md6 class="d-flex justify-center align-center">
          <v-avatar v-show="$store.state.gym_object.photo" size="200">
            <!--eslint-disable-next-line vue/html-self-closing-->
            <img
              itemprop="image"
              :src="$store.state.gym_object.photo"
              :alt="$store.state.gym_object.name"
            />
          </v-avatar>
        </v-col>
        <v-col md6 class="d-flex flex-column justify-center">
          <h1 itemprop="name">
            {{ $store.state.gym_object.name }}
          </h1>

          <v-rating
            v-if="gymRating && gymRating != -1"
            v-model="gymRating"
            readonly
            class="mt-2"
            background-color="yellow"
            color="yellow accent-4"
          />
          <v-progress-circular
            v-if="gymRating === undefined && gymRating != -1"
            indeterminate
            color="amber"
          />
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script>
export default {
  name: "InfoCard",
  computed: {
    gymRating: function () {
      return this.$store.state.place_details.rating || -1
    },
  },
}
</script>
