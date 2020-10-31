<template>
  <v-card style="background: #e5a708;" class="pa-4">
    <v-card-text class="py-2 black--text text-center">
      CrossFit® is a registered trademark of CrossFit, Inc. This website is not
      endorsed, sponsored, or affiliated with CrossFit, Inc.
    </v-card-text>
    <v-row justify="center" no-gutters>
      <v-btn
        v-for="(link, btnName) in links"
        :key="btnName"
        color="black"
        text
        flat
        class="my-2"
      >
        {{ btnName }}
      </v-btn>
    </v-row>
    <!-- <v-card-text> -->
    <v-row justify="center" no-gutters>
      <v-btn
        v-for="(link, icon) in socialMediaInfo"
        :key="icon"
        class="mx-4 white--text"
        icon
      >
        <a :href="link" style="text-decoration: none;">
          <v-icon size="24px">
            {{ icon }}
          </v-icon>
        </a>
      </v-btn>
    </v-row>
    <!-- </v-card-text> -->
  </v-card>
</template>

<script>
export default {
  name: "GymFooter",
  data() {
    return {
      links: {
        "About Us": "javascript:;",
        "Terms of Service": "javascript:;",
        "Privacy Policy": "javascript:;",
      },
      socialMediaInfo: {
        "mdi-facebook": "javascript:;",
        "mdi-twitter": "javascript:;",
        "mdi-linkedin": "javascript:;",
        "mdi-instagram": "javascript:;",
      },
    }
  },
}
</script>
