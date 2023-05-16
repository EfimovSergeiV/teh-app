<template>

  <div class="">
    <div class="relative">
      <div class="container mx-auto px-4">
        <transition name="fade">
          <div v-if="showCreateProject" id="create-project" class="fixed z-10 my-2">
            <div class="bg-sky-900 w-[600px] px-4 py-4 rounded-lg shadow-lg shadow-gray-900">
              <div class="flex items-center justify-end">
                <p class="text-white text-sm mdi mdi-close cursor-pointer" @click="createProject"> Закрыть</p>
              </div>
              <div class="">
                <label for="message" class="block mt-2 mb-1 text-xs font-medium text-gray-100">Название проекта: <span class="font-semibold">{{ name }}</span></label>
                  <input id="text" v-model="name" type="text" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-sm focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-300 dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="МТВ-8000 ExpSuperVOC">
              </div>
              <div class="my-4">
                <label for="message" class="block mt-2 mb-1 text-xs font-medium text-gray-100">Описание проекта (необязательно)</label>
                <textarea id="message" v-model="description" rows="4" class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-sm border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Опишите проект..."></textarea>
              </div>

              <div class="flex items-start justify-between">
                <div class="">
                  <form  class="" @submit.prevent="uploadFile">
                    <input
                      id="file" type="file"
                      class="block w-full text-sm text-gray-100
                      file:mr-4 file:py-2 file:px-4 cursor-pointer
                      file:rounded-full file:border-0
                      file:text-sm file:font-semibold
                      file:bg-white file:text-sky-800
                      hover:file:bg-white
                    " @change="onFileChange"/>

                    <div class="mt-4">
                      <button id="file" :disabled="btnStatus" class="px-6 py-2 bg-white disabled:bg-gray-400 rounded-full text-sm font-semibold text-sky-900 transition-all duration-700" type="submit">Создать</button>
                    </div>

                  </form>
                </div>
                <div class="">
                  <div class="text-center">
                    <span class="text-white text-xs font-semibold w-full text-center"> {{ uploadProgress }}% </span>
                  </div>                
                  <div class="">
                    <progress class="h-4 text-green-400 border border-white rounded-sm" :value="uploadProgress" max="100">{{ uploadProgress }}%</progress>
                  </div>
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
    const projects = await $axios.$get('s/projects/getall/')
    return { projects }
  },
  data() {
    return {
      name: null,
      description: null,
      file: null,
      uploadProgress: 0,
      btnStatus: false,

    }
  },
  computed: {
      ...mapState({
        showCreateProject: (state) => state.showCreateProject,
      }),
    },
  methods: {
    ...mapActions({
      addToast: 'addToast',
      createProject: 'createProject'
    }),
    onFileChange(event) {
      this.file = event.target.files[0];
    },
    async uploadFile() {
      const formData = new FormData();
      formData.append('name', this.name);
      formData.append('description', this.description);
      formData.append('file', this.file);

      if (this.name && this.file ) {
        try {
          this.btnStatus = true;
          const response = await this.$axios.post('s/projects/create/', formData, {
            onUploadProgress: (progressEvent) => {
              this.uploadProgress = Math.round(
                (progressEvent.loaded * 100) / progressEvent.total
              );
            },
          });

          if (response.data.type === 'error') {
            this.addToast(response.data)
            this.btnStatus = false
          } else {
            this.name = null
            this.description = null

            this.createProject()
            this.addToast(response.data)
          }

        } catch (error) {
          this.addToast({'id': 1, 'msg': "Что то пошло не так!", 'type': 'error'})
          this.btnStatus = false
        }        
      } else {
        this.addToast({'id': 1, 'msg': "Нет данных для отправки", 'type': 'error'},)
      }
        this.file = null
        this.btnStatus = false
        this.uploadProgress = 0

    },

  },
}
</script>
