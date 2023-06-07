<template>

  <div class="">
    <div class="relative">

      <div class="bg-sky-700">
        <div class="py-1 container mx-auto px-12">

          <div class="flex items-center gap-4 py-2">
            <div v-for="ct in cts" :key="ct.id" class="">

              <div v-if="ct.id === selectedCategory" class="border-b border-white">
                <button class="text-white font-semibold text-sm border-white">{{ ct.name }}</button>
              </div>

              <button v-else class="text-white font-semibold text-sm border-white cursor-pointer" @click="selectCategory(ct.id); updateProjects(ct.id)">{{ ct.name }}</button>              
              
            </div>
          </div>

          <!-- <div class="flex gap-4 py-2 px-4">
            <div v-for="inserted in inserteds" :key="inserted.id" class="">
              <p class="text-white font-semibold text-xs border-b border-white cursor-pointer">{{ inserted.name }}</p>
            </div>
          </div> -->

        </div>
      </div>

      <div class="container mx-auto px-12">
        <transition name="fade">
          <div v-if="showCreateProject" id="create-project" class="fixed z-10 my-2">
            <div class="bg-sky-900 w-[600px] px-4 py-4 rounded-lg shadow-lg shadow-gray-900">
              <div class="flex items-center justify-end">
                <p class="text-white text-sm mdi mdi-close cursor-pointer" @click="createProjectForm"> Закрыть</p>
              </div>
              <div class="">
                <label for="message" class="block mt-2 mb-1 text-xs font-medium text-gray-100">Название проекта: <span class="font-semibold">{{ name }}</span></label>
                  <input id="text" v-model="name" type="text" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-sm focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-300 dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="МТВ-8000 ExpSuperVOC">
              </div>
              <div class="my-4">
                <label for="message" class="block mt-2 mb-1 text-xs font-medium text-gray-100">Описание проекта (необязательно)</label>
                <textarea id="message" v-model="description" rows="4" class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-sm border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Опишите проект..."></textarea>
              </div>

              <div class="flex items-center justify-end">
                <div class="mt-4">
                  <button id="file" :disabled="btnStatus" class="px-6 py-2 bg-white disabled:bg-gray-400 rounded-full text-sm font-semibold text-sky-900 transition-all duration-700" @click="createProject">Создать</button>
                </div>
              </div>

            </div>
          </div>
        </transition>
      </div>
    </div>

    <FilesList />
    
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex';

export default {
  name: 'IndexPage',
  async asyncData({ $axios }) {
    const cts = await $axios.$get(`s/cts/`)
    return { cts }
  },
  data() {
    return {
      name: null,
      description: null,
    }
  },
  computed: {
      ...mapState({
        selectedCategory: (state) => state.selectedCategory,
        showCreateProject: (state) => state.showCreateProject,
        projects: (state) => state.projects,
      }),
    },
  mounted() {
    if (this.selectedCategory) {
      this.updateProjects(this.selectedCategory)
    } else {
      this.selectCategory(this.cts[0].id)
      this.updateProjects(this.cts[0].id)
    }
    
    // this.addCategory(this.cts)
    // this.getCategoryProjects(this.selectedCategory)
  },
  methods: {
    ...mapActions({
      selectCategory: 'selectCategory',
      addCategory: 'addCategory',
      addToast: 'addToast',
      addProjects: 'addProjects',
      createProjectForm: 'createProjectForm',
      updateProjects: 'updateProjects',
    }),
    // onFileChange(event) {
    //   this.file = event.target.files[0];
    // },
    // async getCategoryProjects(id) {
    //   // try {
    //   //   const projects = await this.$axios.get(`s/projects/${id}/`)
    //   //   this.addProjects(projects.data)          

    //   // } catch (err){
    //   //   console.log(err)
    //   // }
    // },
    async createProject() {

        if (this.name) {
          try {

            const response = await this.$axios.post('s/projects/create-or-update/', {
              category: this.selectedCategory,
              name: this.name,
              description: this.description,
            })

            this.addToast(response.data)
            this.updateProjects(this.selectedCategory)
            this.createProjectForm()

          } catch (error) {
            this.addToast({ "id": 1, "msg": "Что то пошло не так!", "type": "error" })
          }          
        } else {
          this.addToast({ "id": 1, "msg": "Нада обозвать проект!", "type": "error" })
        }



      this.loadingNow = false
      this.loadingID = 0
      
    },

  },
}
</script>
