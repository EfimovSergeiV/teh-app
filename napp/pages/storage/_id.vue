<template>
  <div class="relative">
    
    <!-- <p class="text-xs text-gray-900">
      {{ project }}
    </p> -->


    <div class="bg-sky-700">
      <div class="py-1 container mx-auto">

        <div class="flex items-center gap-4 py-2 px-4">

          <p v-if="getNowCategoryName" class="text-white font-semibold text-sm border-white">{{ getNowCategoryName.name }}</p>

          <!-- <div v-for="ct in cts" :key="ct.id" class="">
            
            <div v-if="ct.id === selectedCategory" class="border-b border-white">
              <nuxt-link :to="{name: 'index'}" class="text-white font-semibold text-sm border-white">{{ ct.name }}</nuxt-link>
            </div>
            
          </div> -->
        </div>


      </div>
    </div>

    <div class="bg-gray-100">
      <div class="container mx-auto py-2 px-4">
        <div class="flex gap-4 items-center ">
          <nuxt-link :to="{ name: 'index' }" class="text-sky-900 font-semibold text-sm mdi mdi-home"> Главная</nuxt-link>
          <button class="text-sky-900 font-semibold text-sm mdi mdi-update cursor-pointer" @click="updateProject($route.params.id)"> Обновить</button>
          <button class="text-sky-900 font-semibold text-sm mdi mdi-help-circle-outline"> Помощь</button>
        </div>
      </div>
    </div>


    <div class="relative pt-1 pb-4">
      <!-- <div class="container mx-auto px-4">

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

      </div> -->
    </div>


    <div class="container min-h-screen mx-auto px-4">

      <div class="my-4">

        <div class="flex items-center justify-end">
          <span class="text-base mdi mdi-pencil-outline cursor-pointer mx-1 text-gray-600 hover:text-gray-800 transition-all" @click="editProjectDataForm = true"></span>
        </div>


        <div class="relative">
          <p class="text-lg font-semibold text-sky-900">{{ project.name }} </p>
          
          <!-- <div class="my-2">
            <p class="text-sky-800 text-sm font-semibold mdi mdi-download cursor-pointer"> Собрать проект</p>
          </div> -->
          
        
          <transition name="fade">
            <div v-if="editProjectDataForm" class="absolute top-0 w-full z-20">
              <div class="bg-sky-800 min-h-[220px] w-full p-4  rounded-lg shadow-lg shadow-gray-900">
                <div class="my-2">
                  <div class="flex items-center justify-end">
                    <p class="text-white text-sm mdi mdi-close cursor-pointer" @click="editProjectDataForm = false"> Закрыть</p>
                  </div>

                  <div class="">
                    <label for="message" class="block mt-2 mb-1 text-xs font-medium text-gray-100">Название проекта: <span class="font-semibold">{{ name }}</span></label>
                      <input id="text" v-model="name" type="text" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-sm focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-300 dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="МТВ-8000 ExpSuperVOC">
                  </div>

                  <label for="message" class="block mt-2 mb-1 text-xs font-medium text-gray-100">Описание:</label>
                  <textarea id="message" v-model="description" rows="4" class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-sm border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Опишите проект..."></textarea>


                  <div class="flex items-center justify-end">
                    <div class="mt-4">
                      <button id="file" :disabled="btnStatus" class="px-6 py-2 bg-white disabled:bg-gray-400 rounded-full text-sm font-semibold text-sky-900 transition-all duration-700" @click="editProject">Отправить</button>
                    </div>
                  </div>
                </div>
              </div>

            </div>            
          </transition>
        </div>
        
        
        <div class="my-2 relative">
          <p class="text-base text-gray-800">{{ project.description }}</p>
        </div>

        <div class="flex items-center justify-end gap-4 py-4">
          <div class="grid gap-1 grid-cols-1">
            <div class="flex justify-between gap-4">
              <p class="text-right text-xs text-gray-500 font-semibold">Создан: </p>
              <p class="text-right text-xs text-gray-600 font-semibold">{{ project.created_date }}</p>
            </div>
            <div class="flex justify-between gap-4">
              <p class="text-right text-xs text-gray-500 font-semibold">Обновлён: </p>
              <p class="text-right text-xs text-gray-600 font-semibold">{{ project.updated_date }}</p>
            </div>
          </div>
        </div>        
      </div>


      <div>

        <div class="my-6">
          <div class="my-2 border-b border-sky-400">


            <!-- <div class="flex items-center justify-between">
              <p class="text-sky-800">Узлы пректа:</p>
              <div class="flex my-2 gap-2 w-[320px]">
                <div class="w-full">
                  <input id="username" class="shadow text-xs appearance-none font-semibold rounded w-full py-1 px-3 text-gray-700 leading-tight placeholder-gray-700/80 focus:ring-white/0 focus:ring-offset-0 focus:outline-none" type="text" placeholder="Название узла">
                </div>
                <div class="w-full">
                  <button class="text-center text-sm font-semibold cursor-pointer mdi mdi-plus-thick text-sky-900 disabled:text-gray-400" @click="uploadform = !uploadform"> Добавить узел</button>
                </div>
              </div>
            </div> -->

            <div class="flex items-end justify-between my-2">
              <div class="">
                <p class="text-sky-800">Узлы/сборки пректа:</p>
              </div>
              <div class="grid grid-cols-1 gap-2">
                <div class="flex items-center justify-end">
                  <p class="text-xs text-gray-700 mdi mdi-plus">Добавить новый узел/сборку</p>
                </div>
                <div class="flex gap-2">

                  <div class="">
                    <input id="username" v-model="assemblyName" class="shadow text-xs appearance-none font-semibold rounded w-[200px] py-1 px-3 text-gray-700 leading-tight placeholder-gray-700/80 focus:ring-white/0 focus:ring-offset-0 focus:outline-none" type="text" placeholder="Название узла/сборки"/>
                  </div>
                  <div class="">
                    <button class="text-center text-sm cursor-pointer text-white disabled:text-gray-400 bg-sky-900 px-2 py-0.5 rounded" @click="addNewAssembly"> Добавить</button>

                  </div>
                </div>                
              </div>

            </div>


          </div>

          <div v-if="project.project_assembly.length > 0" class=" min-h-[12rem]">
            
            <transition-group tag="div" name="left-emergence"  class="grid grid-cols-4 my-4 gap-4">

              <div v-for="assembly in project_assembly" :key="assembly.id" class="">
                <button class="border-b border-gray-300 w-full" @click="selectAssembly(assembly);addFiles(assembly.assembly_files)">
                  <p class="text-xs text-left font-semibold text-gray-600 hover:text-gray-800 transition-all">{{ assembly.name }}</p>
                </button>
              </div>

            </transition-group>

          </div>
          <div v-else class="py-28">
            <div class="flex items-center justify-center h-full">
              <p class="mdi mdi-folder-remove text-gray-700 font-semibold"> Нет сборок</p>
            </div>
          </div>

        </div>


        <div class="my-2 border-b border-sky-400">
          <p class="text-sky-800">Архивы сборки: 
            <transition name="fade">
              <span v-if="selectedAssembly">{{ selectedAssembly.name }}</span>
            </transition>
          </p>
        </div>


        <div class=" h-full flex items-center justify-center">

          <transition name="fade" mode="out-in">
            <div v-if="uploadform" class=" w-full">
              <div class="flex items-center justify-end">
                <button class="mdi mdi-close text-sm" @click="uploadform = !uploadform"></button>
              </div>

              <div class="flex items-center justify-center">
                <div class="min-w-[400px] md:min-w-[560px] my-2">
                  <label for="archiveName" class="block mt-2 mb-1 text-xs font-medium text-gray-700">Название архива: <span class="font-semibold">{{ newArchiveName }}</span></label>
                  <input id="archiveName" v-model="newArchiveName" type="text" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-sm focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-300 dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Конструкторская документация">
                </div>
              </div>
            
              <div class="relative">
                <div class="flex items-center justify-center">
                  <form class="flex items-center space-x-6">
                    <label class="block">
                      <input
                        id="newfile" type="file" webkitdirectory class="block w-full text-sm text-slate-500
                        file:mr-4 file:py-2 file:px-4
                        file:rounded-full file:border-0
                        file:text-sm file:font-semibold
                        file:bg-white file:text-sky-700
                        hover:file:bg-white
                      " @change="onFileChange"/>
                    </label>
                  </form>
                </div>
                <div class="flex items-center justify-center my-2 gap-2">

                  <div>
                    <label class="flex items-center gap-2">
                      <input type="checkbox" class="rounded text-sky-700 focus:ring-0">
                      <p class="text-gray-700 text-sm font-semibold">Добавить ко всем проектам</p>
                    </label>
                  </div>

                  <button :disabled="loadingNow" class="w-40 text-center text-sm font-semibold cursor-pointer mdi mdi-upload text-sky-700 disabled:text-sky-400" @click="uploadFile('newfile')"> Загрузить</button>

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


            <button class="w-40 text-center text-sm font-semibold cursor-pointer mdi mdi-package-variant-plus text-sky-900 disabled:text-gray-400 my-2" @click="uploadform = !uploadform"> Добавить архив</button>

          </transition>
        </div>



        <div v-if="files.length > 0" class="min-h-[300px]">
          <transition-group tag="div" name="left-emergence" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 py-4">

            <div v-for="project_file in files" :key="project_file.id" class="">

              <div class="border-b text-gray-900 border-gray-200 bg-white rounded-sm py-2">
                <p class="border-b text-gray-900 border-gray-200">{{ project_file.name }}</p>
                
                <div class="flex items-center justify-start my-2 gap-2">
                  <div>
                    <label class="flex items-center">
                      <input type="checkbox" class="rounded text-sky-700 focus:ring-0">
                      <p class="text-gray-700 text-sm font-semibold"></p>
                    </label>
                  </div>
                  <a :href="project_file.file" class="font-semibold text-sky-800 hover:text-sky-900 text-sm">Скачать</a>
                  <div class="">
                    <button class="text-sm text-sky-800 font-semibold" @click="historyFilesModal = true && addHistoryFiles(project_file.historical_files)">История версий</button>
                  </div>                
                
                </div>

                <div class="my-2">
                  <div class="grid grid-cols-1 gap-0.5">
                    <p class="text-xs mdi mdi-account font-semibold text-gray-600"> {{ project_file.author }}</p>
                    <p class="text-xs mdi mdi-update font-semibold text-gray-600"> {{ project_file.created_date }}</p>
                    <p class="text-xs text-gray-900">md5: {{ project_file.md5 }}</p>                               
                  </div>
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
                    <button :disabled="loadingNow" class="w-40 text-center text-sm font-semibold cursor-pointer mdi mdi-upload text-sky-700 disabled:text-gray-400" @click="uploadFile(project_file.id)"> Обновить</button>
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
        <div v-else class="">
          <div class="flex items-center justify-center min-h-[300px]">
            <p class="mdi mdi-package-variant-remove text-gray-700 font-semibold"> Нет архивов</p>
          </div>
        </div>
        <div class="flex items-center justify-end my-4">
          <p class="text-sky-800 text-base font-semibold mdi mdi-download cursor-pointer"> Собрать проект</p>
        </div>
      </div>

    </div>

    <transition name="top-emergence">
      <div v-if="historyFilesModal" class="fixed z-30 top-0 w-full">
        <div class="">

          <div class="container mx-auto py-2 px-4 bg-gray-100 h-[600px] border-t border-sky-500 rounded-br-xl rounded-bl-xl shadow-lg shadow-gray-900/50">

            <div class="flex justify-between my-2">
              <div class=""><p class="font-semibold text-sky-800 text-sm">История версий</p></div>
              <div class=""><button class="text-sm mdi mdi-close text-sky-800" @click="historyFilesModal = false"> Закрыть</button></div>
            </div>
            
            <div class="flex items-center justify-between gap-2">
              <div class="w-32"><p class="text-sky-900 font-semibold text-sm mdi mdi-file cursor-pointer"> Проектов: <span class="mx-1">{{ historical_files.length }}</span></p></div>
              
              <div v-if="historical_files.length > 0" class="grid grid-cols-1 gap-y-4">
                <div class="flex gap-2 w-full">

                  <input id="username" v-model="authorFileHistory" class="shadow text-xs appearance-none font-semibold rounded w-full py-1 px-3 text-gray-700 leading-tight placeholder-gray-700/80 focus:ring-white/0 focus:ring-offset-0 focus:outline-none" type="text" placeholder="Иван Иванов">
                  <input id="username" v-model="dateFileHistory" class="shadow text-xs appearance-none font-semibold rounded w-full py-1 px-3 text-gray-700 leading-tight placeholder-gray-700/80 focus:ring-white/0 focus:ring-offset-0 focus:outline-none" type="datetime-local">

                </div>

                <div class="flex items-center">
                  <form class="flex items-center space-x-6">
                    <label class="block">
                      <input
                          :id="historical_files[0].latest" type="file" class="block w-full text-sm text-slate-500
                          file:rounded-full file:border-0
                          file:text-sm file:font-semibold
                          file:bg-white file:text-sky-700
                          hover:file:bg-white
                        " @change="onFileChange"/>
                    </label>
                  </form>
                  <span class="flex items-center mdi mdi-upload cursor-pointer text-sky-700 font-semibold text-sm">
                    <button :disabled="loadingNow" class="" @click="uploadFile(historical_files[0].latest);historyFilesModal = false">Загрузить в историю</button>
                  </span>

                </div>
              </div>
              
            </div>
            

            <div class="my-2">
              <div class="overflow-y-auto h-[500px] py-1 border-b border-t border-sky-500/50">
                <div class="">

                  <transition-group tag="div" name="fade" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-4 py-4">
                    <div v-for="historical_file in historical_files" :key="historical_file.id" class="">
                      <div class="border-b border-gray-300">

                        <div class="">
                          <p class="text-xs text-sky-700">{{ historical_file.name }}</p>
                        </div>

                        <div class="flex items-center justify-start gap-2 my-1">
                          <div>
                            <label class="flex items-center gap-2">
                              <input type="checkbox" class="rounded text-sky-700 focus:ring-0">
                            </label>
                          </div>
                          <a :href="historical_file.file" class=" text-sm text-sky-900">Скачать</a>
                        </div>

                        <div class="my-2">
                          <p class="text-xs font-semibold text-sky-800 mdi mdi-account"> {{ historical_file.author }}</p>
                          <p class="text-xs font-semibold text-sky-800 mdi mdi-calendar-clock"> {{ historical_file.created_date }}</p>
                        </div>

                        <div class="">
                          <p class="text-xs text-sky-900">{{ historical_file.md5 }}</p>
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
</template>

<script>
import { mapActions, mapState } from 'vuex';

export default {
  name: 'ProjectPage',
  middleware: ['auth'],
  async asyncData({ params, $axios }) {
    const cts = await $axios.$get(`s/cts/`)
    const project = await $axios.$get(`s/projects/getone/${params.id}/`)
    return { cts, project }
  },
  data() {
    return {
      name: null,
      description: null,
      file: null,
      
      updated: null,

      btnStatus: false,
      uploadform: false,

      newArchiveName: null,
      uploadFiles: [],
      uploadProgress: 0,
      loadingNow: false,
      loadingID: 0,
      changeProjectForm: true,
      editProjectDataForm: false,
      historyFilesModal: false,
      authorFileHistory: null,
      dateFileHistory: null,

      assemblyName: null,
    }
  },

  computed: {
    ...mapState({
      projects: (state) => state.projects,
      project_assembly: (state) => state.project_assembly,
      files: (state) => state.files,
      selectedCategory: (state) => state.selectedCategory,
      historical_files: (state) => state.historical_files,
      selectedAssembly: (state) => state.selectedAssembly,
    }),
    getNowCategoryName() {
      const id = this.cts.findIndex((item) => item.id === this.selectedCategory)
      return this.cts[id]
    },
  },
  mounted() {
    this.name = this.project.name
    this.description = this.project.description
    this.addCategory(this.cts)
    this.selectCategory(this.project.category)
    // this.addFiles(this.project.project_files)
    this.addAssembly(this.project.project_assembly)
  },
  methods: {
    ...mapActions({
      addCategory: 'addCategory',
      selectCategory: 'selectCategory',
      addToast: 'addToast',
      createProject: 'createProject',
      updateProject: 'updateProject',
      updateProjects: 'updateProjects',
      addAssembly: 'addAssembly',
      updateAssembly: 'updateAssembly',
      selectAssembly: 'selectAssembly',
      addFiles: 'addFiles',
      addHistoryFiles: 'addHistoryFiles',
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

    async editProject() {

      if (this.name) {
        try {
          const response = await this.$axios.post(`s/projects/create-or-update/`, {
            category: this.project.category,
            project: this.project.id,
            name: this.name,
            description: this.description,
          })

          this.addToast(response.data)
          this.editProjectDataForm = false

          await this.$axios.get(`s/projects/getone/${this.project.id}/`).then((resp) => {
            this.project = resp.data
          })
          

        } catch (error) {
          this.addToast({ "id": 1, "msg": "Что то пошло не так!", "type": "error" })
        }          
      } else {
        this.addToast({ "id": 1, "msg": "Нада обозвать проект!", "type": "error" })
      }
      this.loadingNow = false
      this.loadingID = 0
    },

    async addNewAssembly() {
      try {
        const response = await this.$axios.post('s/assembly/create/',{
          project: this.project.id,
          name: this.assemblyName
        })
        if (response.data.type === 'success') {
          this.assemblyName = null
          this.updateAssembly(this.project.id)          
        }
        this.addToast(response.data)
        // if (response.data.type === 'success') {
        //   this.uploadform = false
        //   setTimeout(() => {
        //     this.updateProject(fileData.project_id)
        //   }, "1500");
        // }

      } catch (error) {
        this.addToast({ "id": 1, "msg": "Что то пошло не так!", "type": "error" })
      }
    },

    // AssemblyFilesView(id) {
    //   this.addFiles(this.project.project_files)
    // },

    async uploadFile(id, latestId) {
      const IndexUploadFile = this.uploadFiles.findIndex((item) => item.file_id === String(id))

      if (IndexUploadFile !== -1) {
        const formData = new FormData()
        const fileData = this.uploadFiles.pop(IndexUploadFile)

        formData.append("project_id", fileData.project_id)
        formData.append("file_id", fileData.file_id)
        formData.append("file", fileData.file)

        if (this.newArchiveName) {
          formData.append("name", this.newArchiveName)
        }
        if (this.authorFileHistory) {
          formData.append("author_history", this.authorFileHistory)
        }
        if (this.dateFileHistory) {
          formData.append("date_history", this.dateFileHistory)
        }
        if (latestId) {
          formData.append("latest_id", latestId)
        }


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

      this.newArchiveName = null
      this.loadingNow = false
      this.loadingID = 0
      
    },

  },
}
</script>
