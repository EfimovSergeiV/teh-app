<template>
  <div class="">
    
    <div class="bg-sky-800">
      <div class=" container mx-auto py-8 px-4">
        <div class="flex items-center justify-between">
          <nuxt-link :to="{ name: 'index' }" class="">
            <img src="/logo.webp" class="h-[35px]" />
          </nuxt-link>


          <!-- <div class="flex gap-4">
            <div class=""><p class="mdi mdi-account text-white text-sm flex items-center font-semibold"> Пользователь</p></div>
          </div> -->

          <div class="grid grid-cols-1 gap-2">
            <transition name="fade">
              <div v-if="isAuthenticated" id="isAuthenticated" class="flex items-center justify-end gap-2">
                <div class="flex gap-6">
                  <p class="text-white">{{ loggedInUser }}</p>
                  <button class="py-0.5 px-6 bg-white shadow rounded text-gray-700 text-sm" @click="logout">
                    выйти
                  </button>
                </div>
              </div>

              <div v-else id="notAuthenticated" class="flex items-center justify-end gap-2">
                <div class="">
                  <input id="username" v-model="login.username" class="shadow text-xs appearance-none font-semibold rounded w-full py-1 px-3 text-gray-700 leading-tight placeholder-gray-700/80 focus:ring-white/0 focus:ring-offset-0 focus:outline-none" type="text" placeholder="Логин">
                </div>
                <div class="">
                  <input id="username" v-model="login.password" class="shadow text-xs appearance-none font-semibold rounded w-full py-1 px-3 text-gray-700 leading-tight placeholder-gray-700/80 focus:ring-white/0 focus:ring-offset-0 focus:outline-none" type="password" placeholder="Пароль" @keyup.enter="userLogin">
                </div>
                <div class="">
                  <button class="py-0.5 px-6 bg-white text-gray-700 shadow rounded text-sm" @click="userLogin">
                    войти
                  </button>
                </div>
              </div>
            </transition>

          </div>
        </div>




      </div>
    </div>






    <!-- <div class="bg-sky-700">
      <div class="py-1 container mx-auto">

        <div class="flex items-center gap-4 py-2 px-4">
          <div v-for="ct in cts" :key="ct.id" class="">

            <div v-if="ct.id === selectedCategory" class="border-b border-white">
              <button class="text-white font-semibold text-sm border-white">{{ ct.name }}</button>
            </div>

            <button v-else class="text-white font-semibold text-sm border-white cursor-pointer" @click="selectCategory(ct); getCategoryProjects(ct.id)">{{ ct.name }}</button>              
            
          </div>
        </div>



      </div>
    </div> -->
        <!-- <div class="flex gap-4 py-2 px-4">
          <div v-for="inserted in inserteds" :key="inserted.id" class="">
            <p class="text-white font-semibold text-xs border-b border-white cursor-pointer">{{ inserted.name }}</p>
          </div>
        </div> -->

    <!-- <div class="bg-sky-500">
      <div class="container mx-auto py-2">

        <div class="flex gap-4 px-4">
          <p class="text-gray-100 font-semibold text-sm mdi mdi-view-grid-plus cursor-pointer"> Создать проект</p>
        </div>

      </div>
    </div> -->


  </div>

</template>

<script>
import { mapState, mapActions, mapGetters } from 'vuex'

export default {
  name: 'HeaderView',
  middleware: 'guest',
  props: {
    // filess: {
    //   type: Array,
    //   default: Array,
    // },
  },
  data() {
    return {
      categories: [
        { "id": 1, "name": "Сварочные машины и установки", "inserted": [ { "id": 2, "name": "Точечная переменным током" }, { "id": 3, "name": "Точечная постоянным током"}, { "id": 3, "name": "Точечная конденсаторная"}, { "id": 3, "name": "Шовная постоянным током"}, { "id": 3, "name": "Рельефная переменным током"}, { "id": 3, "name": "Стыковая"}, ] },
        { "id": 2, "name": "Оборудование для сварки рельсов", "inserted": [ { "id": 2, "name": "Точечная переменным током" }, { "id": 3, "name": "Точечная постоянным током"}, { "id": 3, "name": "Точечная конденсаторная"}, { "id": 3, "name": "Шовная постоянным током"}, { "id": 3, "name": "Рельефная переменным током"}, { "id": 3, "name": "Стыковая"}, ] },
        { "id": 3, "name": "Трансформаторы", "inserted": [ { "id": 2, "name": "Точечная переменным током" }, { "id": 3, "name": "Точечная постоянным током"}, { "id": 3, "name": "Точечная конденсаторная"}, { "id": 3, "name": "Шовная постоянным током"}, { "id": 3, "name": "Рельефная переменным током"}, { "id": 3, "name": "Стыковая"}, ] },
        { "id": 4, "name": "Источники", "inserted": [ { "id": 2, "name": "Точечная переменным током" }, { "id": 3, "name": "Точечная постоянным током"}, { "id": 3, "name": "Точечная конденсаторная"}, { "id": 3, "name": "Шовная постоянным током"}, { "id": 3, "name": "Рельефная переменным током"}, { "id": 3, "name": "Стыковая"}, ] },
      ],
      inserteds: [
        { "id": 2, "name": "Контактная сваарка" },
        { "id": 2, "name": "Дуговая сваарка" },
        { "id": 2, "name": "Диффузионная сваарка" },
        { "id": 2, "name": "Микросварка сваарка" },
        { "id": 2, "name": "Контактная пайка" },
        { "id": 2, "name": "Специального назначения" },
      ],
      login: {
        username: '',
        password: ''
      }
    }
  },
  computed: {
    ...mapState({
        selectedCategory: (state) => state.selectedCategory,
        cts: (state) => state.cts,
      }),
    ...mapGetters(['isAuthenticated', 'loggedInUser'])
  },  
  // watch: {
  //   selectedCategory() {
  //     this.getCategoryProjects(this.selectedCategory)
  //   },
  // },   

  methods: {
    ...mapActions({
      selectCategory: 'selectCategory',
      addProjects: 'addProjects',
      // addCategory: 'addCategory',
      // addToast: 'addToast',
      // createProjectForm: 'createProjectForm',
      // updateProjects: 'updateProjects',
    }),
    async userLogin() {
      try {
        await this.$auth.loginWith('local', { data: this.login })
      } catch (err) {
        console.log(err)
      }
    },
    async logout() {
      await this.$auth.logout();
    },
    async getCategoryProjects(id) {
      try {
        const projects = await this.$axios.get(`s/projects/${id}/`)
        this.addProjects(projects.data)
      } catch (err){
        console.log(err)
      }
    },
  }
}
</script>
