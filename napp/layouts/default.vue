<template>

  <div class="">
    <HeaderView />
  
    <transition name="fade" mode="out-in">
      <Nuxt id="page" />
    </transition>

    <FooterView />
  </div>

</template>
    
<script>
  import HeaderView from '~/components/HeaderView.vue';
  import FooterView from '~/components/FooterView.vue';
  
  export default {
    components: {
      HeaderView,
      FooterView,
    },
    data() {
      return {
        dataset: true,
        showWriteUs: true,
        latitude: null,
        longitude: null,
      }
    },
    methods: {
      // ...mapMutations({
      //   toggle: 'todos/toggle'
      // }),
      // ...mapActions({
      //   displayForm: 'displayForm',
      //   sendCoordinates: 'sendCoordinates',
      // }),
    },
  };
</script>