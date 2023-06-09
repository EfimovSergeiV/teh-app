<template>

  <div class="bg-gradient-to-r from-gray-100 to-gray-50">
    <div id="background" class="bg-fixed bg-no-repeat bg-right-bottom bg-cover bg- contain bg-[url('/images/bg.webp')]">

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



      <div class="">

        <transition name="top-emergence">
          <div v-if="showSearchForm" class="fixed z-30 top-0 w-full">
            <div class="">
              <div class="container mx-auto py-2 px-12 bg-gray-100 h-[600px] border-t border-sky-500 rounded-br-xl rounded-bl-xl shadow-lg shadow-gray-900/50">
                <div class="flex justify-between my-2">
                  <div class=""><p class="font-semibold text-sky-800 text-sm">Поиск</p></div>
                  <div class=""><button class="text-sm mdi mdi-close text-sky-800" @click="searchModal = false"> Закрыть</button></div>
                </div>
                <div class="flex items-center justify-between gap-2">
                  <div class="w-32"><p class="text-sky-900 font-semibold text-sm mdi mdi-file cursor-pointer"> Проектов: <span class="mx-1">0</span></p></div>
                  <div v-if="false" class="grid grid-cols-1 gap-y-4">
                    <div class="flex gap-2 w-full">
                      <input id="history-file-name" v-model="newArchiveName" class="shadow text-xs appearance-none font-semibold rounded w-full py-1 px-3 text-gray-700 leading-tight placeholder-gray-700/80 focus:ring-white/0 focus:ring-offset-0 focus:outline-none" type="text" placeholder="Название">
                      <input id="author" v-model="authorFileHistory" class="shadow text-xs appearance-none font-semibold rounded w-full py-1 px-3 text-gray-700 leading-tight placeholder-gray-700/80 focus:ring-white/0 focus:ring-offset-0 focus:outline-none" type="text" placeholder="Иван Иванов">
                      <input id="date-time" v-model="dateFileHistory" class="shadow text-xs appearance-none font-semibold rounded w-full py-1 px-3 text-gray-700 leading-tight placeholder-gray-700/80 focus:ring-white/0 focus:ring-offset-0 focus:outline-none" type="datetime-local">
                    </div>

                    <div class="flex gap-2 items-center justify-between">
                      <form class="flex items-center space-x-6">
                        <label class="block">
                          <input
                              id="historyfile" type="file" multiple class="block w-full text-sm text-slate-500
                              file:rounded-full file:border-0
                              file:text-sm file:font-semibold
                              file:bg-gray-100 file:text-sky-700
                              hover:file:bg-gray-100
                            " @change="uploadDirChange"/>
                        </label>
                      </form>
                      <span class="flex items-center mdi mdi-upload cursor-pointer text-sky-700 font-semibold text-sm">
                        <button :disabled="loadingNow" class="" @click="sendHistoryFile">Загрузить в историю</button>
                      </span>
                    </div>
                  </div>
                </div>
                

                <div class="my-2">
                  <div class="overflow-y-auto h-[460px] py-1 border-b border-t border-sky-500/50">
                    <div class="">
                      <transition-group tag="div" name="fade" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-4 py-4">
                        <div v-for="historical_file in historical_files" :key="historical_file.id" class="">
                          <div class="border-b border-gray-300">
                            <div class="">
                              <p class="text-xs text-gray-600">{{ historical_file.name }}</p>
                            </div>
                            <div class="flex items-center justify-start gap-2 my-1">
                              <div>
                                <label class="flex items-center gap-2">
                                  <input :id="historical_file.id" v-model="сustomBuilderArchive" :value="historical_file.id" type="checkbox" class="rounded text-sky-700 focus:ring-0">
                                </label>
                              </div>
                              <a :href="historical_file.file" class=" text-sm text-sky-900">Скачать</a>
                            </div>
                            <div class="my-2">
                              <p class="text-xs font-semibold text-gray-600 mdi mdi-account"> {{ historical_file.author }}</p>
                              <p class="text-xs font-semibold text-gray-600 mdi mdi-calendar-clock"> {{ historical_file.created_date }}</p>
                            </div>
                          </div>
                        </div>
                      </transition-group>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </transition>

      </div>


      <transition name="top-emergence">
        <div v-if="showSearchForm" class="fixed z-30 top-0 w-full">
          <div class="">

            <div class="container mx-auto py-2 px-12 bg-gray-100 h-[600px] border-t border-sky-500 rounded-br-xl rounded-bl-xl shadow-lg shadow-gray-900/50">

              <div class="flex justify-between my-2">
                <div class=""><p class="font-semibold text-gray-700 text-sm">Поиск</p></div>
                <div class=""><button class="text-sm mdi mdi-close-thick font-semibold text-gray-700" @click="searchForm"> Закрыть</button></div>
              </div>
              
              <div class="flex gap-4">
                <div class="w-32"><p class="text-gray-600 font-semibold text-sm mdi mdi-file cursor-pointer"> Найдено: <span class="mx-1">0</span></p></div>
                <!-- <button class="text-gray-600 font-semibold text-sm mdi mdi-upload cursor-pointer">Загрузить в историю</button> -->
              </div>
              

              <div class="my-2">
                <div class="overflow-y-auto h-[500px] py-1 border-b border-t border-sky-500/50">
                  <div class="">

                    <!-- <transition-group tag="div" name="fade" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-4 py-4">
                      <div v-for="historical_file in historical_files" :key="historical_file.id" class="">
                        <div class="border-b border-gray-300">

                          <div class="">
                            <p class="text-sm text-gray-700">{{ historical_file.id }}. {{ historical_file.name }}</p>
                          </div>

                          <div class="flex items-center justify-start my-1">
                            <div>
                              <label class="flex items-center gap-2">
                                <input type="checkbox" class="rounded text-sky-700 focus:ring-0">
                                <p class="text-gray-700 text-sm font-semibold"></p>
                              </label>
                            </div>
                            <a :href="historical_file.file" class=" text-sm text-gray-900">Скачать</a>
                          </div>

                          <div class="my-1">
                            <p class="text-xs font-semibold text-gray-800 mdi mdi-account"> {{ historical_file.author }}</p>
                            <p class="text-xs font-semibold text-gray-800 mdi mdi-calendar-clock"> {{ historical_file.created_date }}</p>
                          </div>

                          <div class="">
                            <p class="text-xs text-gray-900">{{ historical_file.md5 }}</p>
                          </div>

                        </div>

                      </div>
                    </transition-group> -->

                  </div>
                </div>
              </div>


            </div>
          </div>
        </div>
      </transition>

      <HeaderView />

      <transition name="fade" mode="out-in">
        <Nuxt id="page" class="" />
      </transition>

      <FooterView />

    </div>
  </div>

</template>
    
<script>
  import { mapState, mapActions } from 'vuex'
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
        scrollPosition: 0,
      }
    },
    computed: {
      ...mapState({
        toasts: (state) => state.toasts,
        showSearchForm: (state) => state.showSearchForm,
      }),
    },
    beforeMount () {
      window.addEventListener('scroll', this.handleScroll)
    },
    beforeDestroy () {
      window.removeEventListener('scroll', this.handleScroll)
    },

    methods: {
      ...mapActions({
        searchForm: 'searchForm',
    }),
      // ...mapMutations({
      //   toggle: 'todos/toggle'
      // }),
      // ...mapActions({
      //   displayForm: 'displayForm',
      //   sendCoordinates: 'sendCoordinates',
      // }),
      // handleScroll() {
      //   const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
      //   console.log('Вертикальная прокрутка:', scrollTop);

      //   this.scrollPosition = scrollTop
      // }
    },
  };
</script>