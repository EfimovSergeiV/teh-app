<template>
  <div class="">

    <div class="bg-gray-100">
      <div class="container mx-auto py-2 px-4">
        <div class="flex gap-4 items-center ">
          <nuxt-link :to="{ name: 'index' }" class="text-gray-600 font-semibold text-sm mdi mdi-home"> Вернуться на главную</nuxt-link>
          <button class="text-gray-600 font-semibold text-sm mdi mdi-update cursor-pointer" @click="updateData"> Обновить</button>
          <button class="text-gray-600 font-semibold text-sm mdi mdi-help-circle-outline"> Помощь</button>

          <button class="text-green-600 font-semibold text-sm mdi mdi-check-bold"> Обновить проект</button>
          <button class="text-red-600 font-semibold text-sm mdi mdi-close-thick"> Отменить и вернуться на главную</button>
        </div>
      </div>
    </div>

    <div class="container min-h-screen mx-auto px-4">

      <div class="my-4">
        <p class="font-semibold text-gray-700">{{ project.name }}</p>
        
        <div class="my-6">
          <p class="text-sm my-1">Описание:</p>
          <p class="text-sm font-semibold text-gray-700">{{ project.description }}</p>
        </div>

        <p class="text-right text-sm">Создан: {{ project.created_date }}</p>        
      </div>


      <div class="my-6 border-b border-gray-400">
        <p>Файлы проекта:</p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 py-4">
        <div v-for="project_file in project.project_files" :key="project_file.id" class="">

          <div class="border-b border-gray-300">
            <p class="">{{ project_file.name }}</p>
            <div class="">
              <a :href="project_file.file" class="font-semibold text-gray-900 text-sm">Скачать</a>
            </div>
            <div class="my-2">
              <p class="text-sm">Обновлён: {{ project_file.created_date }}</p>
              <p class="text-xs">md5: {{ project_file.md5 }}</p>              
            </div>



            <div class="relative">
              <div class="flex items-center justify-center">
                <form class="flex items-center space-x-6">
                  <label class="block">
                    <input
                      id="1" type="file" class="block w-full text-sm text-slate-500
                      file:mr-4 file:py-2 file:px-4
                      file:rounded-full file:border-0
                      file:text-sm file:font-semibold
                      file:bg-white file:text-sky-700
                      hover:file:bg-white
                    " @change="onFileChange"/>
                  </label>
                </form>
              </div>
              <div class="flex items-center justify-center">
                <button :disabled="dissableBtns" class="w-40 text-center text-sm font-semibold cursor-pointer mdi mdi-upload text-gray-700 disabled:text-gray-400"> Обновить</button>
              </div>

              <div v-if="false" class="absolute top-0 w-full h-full">
                <div class="w-full h-full flex items-center justify-center bg-gradient-to-b from-gray-900/10 to-gray-900/30 backdrop-blur-sm ">
                  <div class="">
                    <div class="text-center">
                      <span class="text-gray-800 text-xs font-semibold w-full text-center"> {{ uploadProgress }}% </span>
                    </div>                
                    <div class=" flex items-center justify-center">
                      <progress class="h-4 text-green-400 border border-white rounded-sm" :value="uploadProgress" max="100">{{ uploadProgress }}%</progress>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        
        <div class="border-b border-gray-300 h-full flex items-center justify-center">

          <transition name="fade" mode="out-in">
            <div v-if="uploadform" class=" w-full">
              <div class="flex items-center justify-end">
                <button class="mdi mdi-close text-sm" @click="uploadform = !uploadform"></button>
              </div>
              <div class="my-2">
                <label for="message" class="block mt-2 mb-1 text-xs font-medium text-gray-700">Название архива: <span class="font-semibold">{{ name }}</span></label>
                <input id="text" v-model="name" type="text" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-sm focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-300 dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Конструкторская документация">
              </div>
            
              <div class="relative">
                <div class="flex items-center justify-center">
                  <form class="flex items-center space-x-6">
                    <label class="block">
                      <input
                        id="1" type="file" class="block w-full text-sm text-slate-500
                        file:mr-4 file:py-2 file:px-4
                        file:rounded-full file:border-0
                        file:text-sm file:font-semibold
                        file:bg-white file:text-sky-700
                        hover:file:bg-white
                      " @change="onFileChange"/>
                    </label>
                  </form>
                </div>
                <div class="flex items-center justify-center">
                  <button :disabled="dissableBtns" class="w-40 text-center text-sm font-semibold cursor-pointer mdi mdi-upload text-gray-700 disabled:text-gray-400"> Загрузить</button>
                </div>

                <div v-if="false" class="absolute top-0 w-full h-full">
                  <div class="w-full h-full flex items-center justify-center bg-gradient-to-b from-gray-900/10 to-gray-900/30 backdrop-blur-sm ">
                    <div class="">
                      <div class="text-center">
                        <span class="text-gray-800 text-xs font-semibold w-full text-center"> {{ uploadProgress }}% </span>
                      </div>                
                      <div class=" flex items-center justify-center">
                        <progress class="h-4 text-green-400 border border-white rounded-sm" :value="uploadProgress" max="100">{{ uploadProgress }}%</progress>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>


            <button class="w-40 text-center text-sm font-semibold cursor-pointer mdi mdi-upload text-gray-700 disabled:text-gray-400" @click="uploadform = !uploadform"> Загрузить</button>

          </transition>


        </div>




      </div>

    </div>

  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex';

export default {
  name: 'ProjectPage',
  async asyncData({ params, $axios }) {
    const project = await $axios.$get(`s/projects/getone/${params.id}/`)
    return { project }
  },
  data() {
    return {
      name: null,
      description: null,
      file: null,
      uploadProgress: 0,
      btnStatus: false,
      uploadform: false
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
      createProject: 'createProject',
      updateData: 'updateData',
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
            this.btnStatus = false
          } else {
            this.name = null
            this.description = null
            this.updateData()
            this.createProject()
          }
          
          this.addToast(response.data)

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
