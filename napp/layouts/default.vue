<template>

  <div class="">

    <div class="">
      <div class="relative">
        
        <div class="fixed right-4 z-20 my-2">

          <transition-group tag="div" name="right-emergence">
            <div v-for="toast in toasts" :key="toast.id" class="my-2">
            
              <div class=" bg-gray-100 border border-gray-200 shadow-lg shadow-gray-900 rounded-md">
                
                <div v-if="toast.type == 'success'" class="flex gap-2 items-center">
                  <div class="">
                    <img src="/cat-two.webp" class="w-28 rounded-l-md"/>
                  </div>
                  <div class="h-full w-60 flex items-center justify-center">
                    <p class="text-xs font-semibold text-gray-700">{{ toast.msg }}</p>
                  </div>
                </div>

                <div v-else class="flex gap-2 items-center">
                  <div class="">
                    <img src="/cat-third.webp" class="w-28 rounded-l-md"/>
                  </div>
                  <div class="h-full w-60 flex items-center justify-center">
                    <div class="text-center">
                      <p class="text-base font-semibold text-gray-700">Ошибка!</p>
                      <p class="text-xs text-gray-800">{{ toast.msg }}</p>
                    </div>
                  </div>
                </div>
                
                
              </div>            
            
            </div>
          </transition-group>





           
        </div>
      </div>
    </div>

    <HeaderView />


  
    <transition name="fade" mode="out-in">
      <Nuxt id="page" />
    </transition>

    <FooterView />
  </div>

</template>
    
<script>
  import { mapState } from 'vuex'
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
    computed: {
      ...mapState({
        toasts: (state) => state.toasts,
      }),
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