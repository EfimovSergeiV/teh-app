<template>
  <div class="">

    <div class="bg-white">
      <div class="container mx-auto py-2 px-4">
        <div class="flex gap-4 items-center ">
          <nuxt-link :to="{ name: 'index' }" class="text-gray-600 font-semibold text-sm mdi mdi-home"> Вернуться на главную</nuxt-link>
          <button class="text-gray-600 font-semibold text-sm mdi mdi-update cursor-pointer" @click="updateProject($route.params.id)"> Обновить</button>
          <button class="text-gray-600 font-semibold text-sm mdi mdi-help-circle-outline"> Помощь</button>
        </div>
      </div>
    </div>


    <div class="relative pt-1 pb-4">
      <div class="container mx-auto px-4">

        <transition name="fade">
          <div v-if="changeProjectForm" class="bg-white">
            <div class="absolute">
              <div class="flex gap-4 items-center ">
                <button class="text-green-600 font-semibold text-sm mdi mdi-check-bold" @click="changeProjectForm = false"> Обновить проект</button>
                <button class="text-red-600 font-semibold text-sm mdi mdi-close-thick"> Отменить изменения</button>
              </div>
            </div>
          </div>
        </transition>

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




      <div>
        <div class=" h-full flex items-center justify-center">

          <transition name="fade" mode="out-in">
            <div v-if="uploadform" class=" w-full">
              <div class="flex items-center justify-end">
                <button class="mdi mdi-close text-sm" @click="uploadform = !uploadform"></button>
              </div>
              <div class="my-2">
                <label for="archiveName" class="block mt-2 mb-1 text-xs font-medium text-gray-700">Название архива: <span class="font-semibold">{{ name }}</span></label>
                <input id="archiveName" v-model="archiveName" type="text" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-sm focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-300 dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Конструкторская документация">
              </div>
            
              <div class="relative">
                <div class="flex items-center justify-center">
                  <form class="flex items-center space-x-6">
                    <label class="block">
                      <input
                        id="newfile" type="file" class="block w-full text-sm text-slate-500
                        file:mr-4 file:py-2 file:px-4
                        file:rounded-full file:border-0
                        file:text-sm file:font-semibold
                        file:bg-white file:text-sky-700
                        hover:file:bg-white
                      " @change="onFileChange"/>
                    </label>
                  </form>
                </div>
                <div class="flex items-center justify-center my-2">
                  <button :disabled="loadingNow" class="w-40 text-center text-sm font-semibold cursor-pointer mdi mdi-upload text-gray-700 disabled:text-gray-400" @click="uploadFile('newfile')"> Загрузить</button>
                </div>

                <div v-if="loadingID === 'newfile'" class="absolute top-0 w-full h-full">
                  <div class="w-full h-full flex items-center justify-center bg-white ">
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


            <button class="w-40 text-center text-sm font-semibold cursor-pointer mdi mdi-plus-thick text-gray-700 disabled:text-gray-400 my-2" @click="uploadform = !uploadform"> Добавить архив</button>

          </transition>
        </div>


        <div class="my-6 border-b border-gray-400">
          <p>Файлы проекта:</p>
        </div>


        <transition-group tag="div" name="absolute-left-emergence" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 py-4">

          <div v-for="project_file in files" :key="project_file.id" class="">

            <div class="border-b border-gray-200 bg-white rounded-sm p-4">
              <p class="">{{ project_file.name }}</p>
              
              <div class="flex items-center justify-start my-1">
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
                        :id="project_file.id" type="file" class="block w-full text-sm text-slate-500
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
                  <button :disabled="loadingNow" class="w-40 text-center text-sm font-semibold cursor-pointer mdi mdi-upload text-gray-700 disabled:text-gray-400" @click="uploadFile(project_file.id)"> Обновить</button>
                </div>

                <div v-if="loadingID === String(project_file.id)" class="absolute top-0 w-full h-full">
                  <div class="w-full h-full flex items-center justify-center bg-white">
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
        </transition-group>

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
      
      btnStatus: false,
      uploadform: false,

      uploadFiles: [],
      uploadProgress: 0,
      loadingNow: false,
      loadingID: 0,
      changeProjectForm: true,
    }
  },

  computed: {
    ...mapState({
      projects: (state) => state.projects,
      files: (state) => state.files,
    }),

  },
  mounted() {
    this.addFiles(this.project.project_files)
  },
  methods: {
    ...mapActions({
      addToast: 'addToast',
      createProject: 'createProject',
      updateProject: 'updateProject',
      addFiles: 'addFiles',
    }),
    onFileChange(event) {
      const EventData = event
      const EventID = EventData.target.id
      const IndexFile = this.uploadFiles.findIndex((item) => item.file_id === String(EventID))

      if (IndexFile === -1) {
        this.uploadFiles.push({
          "project_id": this.project.id,
          "file_id": EventID,
          "file": EventData.target.files[0]
        })
      } else {

        this.uploadFiles[IndexFile].file = EventData.target.files[0]
      }
    },
    async uploadFile(id) {
      const IndexUploadFile = this.uploadFiles.findIndex((item) => item.file_id === String(id))

      if (IndexUploadFile !== -1) {
        const formData = new FormData()
        const fileData = this.uploadFiles.pop(IndexUploadFile)

        formData.append("project_id", fileData.project_id)
        formData.append("file_id", fileData.file_id)
        formData.append("file", fileData.file)

        try {
          this.loadingNow = true
          this.loadingID = fileData.file_id

          const response = await this.$axios.post('s/files/create-or-update/', formData, {
            onUploadProgress: (progressEvent) => {
              this.uploadProgress = Math.round(
                (progressEvent.loaded * 100) / progressEvent.total
              );
            },
          })
          this.addToast(response.data)

          if (response.data.type === 'success') {
            this.uploadform = false
            setTimeout(() => {
              this.updateProject(fileData.project_id)
            }, "1500");
          }



        } catch (error) {
          this.addToast({ "id": 1, "msg": "Что то пошло не так!", "type": "error" })
        }
      } else {
        this.addToast({ "id": 1, "msg": "Нечего загружать", "type": "error" })
      }

      this.loadingNow = false
      this.loadingID = 0
      
    },

  },
}
</script>
