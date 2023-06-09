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


      <transition name="top-emergence">
        <div v-if="showSearchForm" class="fixed z-30 top-0 w-full">
          <div class="">

            <div class="container mx-auto py-2 px-12 bg-gray-100 h-[600px] border-t border-sky-500 rounded-br-xl rounded-bl-xl shadow-lg shadow-gray-900/50">

              <div class="flex justify-between my-4">
                <div class=""><p class="font-semibold text-gray-700 text-sm">Поиск</p></div>
                <div class=""><button class="text-sm mdi mdi-close text-gray-700" @click="searchForm"> Закрыть</button></div>
              </div>
              
              <div class="flex items-center gap-4">
                <div class="flex gap-2 w-full">
                  <input id="history-file-name" v-model="searchName" class="shadow text-xs appearance-none font-semibold rounded w-full py-1 px-3 text-gray-700 leading-tight placeholder-gray-700/80 focus:ring-white/0 focus:ring-offset-0 focus:outline-none" type="text" placeholder="Что будем искать?">
                  <select id="countries" v-model="selectAuthor" placeholder="ds,th" class="shadow text-xs appearance-none font-semibold rounded w-full py-1 px-3 text-gray-700 leading-tight placeholder-gray-700/80 focus:ring-white/0 focus:ring-offset-0 focus:outline-none">
                    <option selected value="null">Выберите конструктора</option>
                    <option v-for="(author, pk) in projectAuthors.authors" :key="pk" :value="author" >{{ author }}</option>
                  </select>
                  
                  <div class="flex items-center gap-2">
                    <input id="date" v-model="startDateFile" class="shadow text-xs appearance-none font-semibold rounded w-full py-1 px-3 text-gray-700 leading-tight placeholder-gray-700/80 focus:ring-white/0 focus:ring-offset-0 focus:outline-none" type="datetime-local">
                    <p class="text-base font-semibold text-gray-700"> - </p>
                    <input id="date" v-model="endDateFile" class="shadow text-xs appearance-none font-semibold rounded w-full py-1 px-3 text-gray-700 leading-tight placeholder-gray-700/80 focus:ring-white/0 focus:ring-offset-0 focus:outline-none" type="datetime-local">
                  </div>

                </div>
                <div class="">
                  <button class=" w-28 text-gray-600 font-semibold text-sm mdi mdi-database-search-outline cursor-pointer" @click="searchSend()"> Искать</button>
                </div>
              </div>

              

              <div class="my-2">
                <div class="overflow-y-auto h-[500px] py-1 border-b border-t border-sky-500/50">
                  <div class="">

                    <div v-if="searchResult.length > 0" class="">
                      <transition-group tag="div" name="fade" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 py-4">
                        <div v-for="result in searchResult" :key="result.id" class="">
                          <div class="border-b border-gray-300">

                            <div class="">
                              <p class="text-sm text-gray-700">{{ result.name }}</p>
                            </div>

                            <div class="flex items-center justify-start my-1">
                              <div>
                                <label class="flex items-center gap-2">
                                  <input type="checkbox" class="rounded text-sky-700 focus:ring-0">
                                  <p class="text-gray-700 text-sm font-semibold"></p>
                                </label>
                              </div>
                              <a :href="result.file" class=" text-sm text-gray-900">Скачать</a>
                            </div>

                            <div class="my-1">
                              <p class="text-xs font-semibold text-gray-700 mdi mdi-account"> {{ result.author }}</p>
                              <p class="text-xs font-semibold text-gray-700 mdi mdi-calendar-clock"> {{ result.created_date }}</p>
                            </div>

                          </div>

                        </div>
                      </transition-group>
                    </div>
                    <div v-else class="">
                      <div class="my-4">
                        <p class="text-gray-700 text-sm">Нет результатов для отображения</p>
                      </div>
                    </div>



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
        selectAuthor: null,
        searchName: null,
        startDateFile: null,
        endDateFile: null,
      }
    },
    computed: {
      ...mapState({
        toasts: (state) => state.toasts,
        projectAuthors: (state) => state.projectAuthors,
        showSearchForm: (state) => state.showSearchForm,
        searchResult: (state) => state.searchResult
      }),
      
    },
    mounted() {
      this.addAllAuthors()
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
        addAllAuthors: 'addAllAuthors',
        searchAction: 'searchAction',
    }),
    searchSend() {
      this.searchAction({
        name: this.searchName,
        author: this.selectAuthor,
        start_date: this.startDateFile,
        end_date: this.endDateFile,
      })
    },
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