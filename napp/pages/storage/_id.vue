<template>
  <div class="">


    <div class="bg-sky-700">
      <div class="py-1 container mx-auto px-12">
        <div class="flex items-center gap-4 py-2 min-h-[49px]">
          <div v-if="getNowCategoryName">
            <p class="text-white font-semibold text-sm border-white">{{ getNowCategoryName.name }}</p>
          </div>
        </div>
      </div>
    </div>

    <div class="bg-gray-200">
      <div class="container mx-auto py-2 px-12">
        <div class="flex gap-4 items-center ">
          <nuxt-link :to="{ name: 'index' }" class="text-sky-900 font-semibold text-sm mdi mdi-home"> Главная</nuxt-link>
          <button class="text-sky-900 font-semibold text-sm mdi mdi-update cursor-pointer" @click="updateProject($route.params.id)"> Обновить</button>
          <button class="text-sky-900 font-semibold text-sm mdi mdi-help-circle-outline"> Помощь</button>
        </div>
      </div>
    </div>

    <div class="container min-h-screen mx-auto px-12">
      <div class="my-4">
        <div class="flex items-center justify-end">
          <span class="text-base mdi mdi-pencil-outline cursor-pointer mx-1 text-gray-600 hover:text-gray-800 transition-all" @click="editProjectDataForm = true"></span>
        </div>
        <div class="relative">
          <p class="text-lg font-semibold text-sky-900">{{ project.name }} </p>
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
            <div class="flex items-end justify-between my-2">
              <div class="">
                <p class="text-sky-800">Узлы/сборки пректа: {{ project_assembly.length }}</p>
              </div>
              <div class="grid grid-cols-1 gap-2">
                <div class="flex items-center justify-end">
                  <p class="text-xs text-gray-700 mdi mdi-plus">Добавить новый узел/сборку</p>
                </div>
                <div class="flex gap-2">
                  <div class="">
                    <input id="username" v-model="assemblyName" class="shadow text-xs appearance-none font-semibold rounded w-[200px] py-1 px-3 text-gray-700 leading-tight placeholder-gray-700/80 focus:ring-white/0 focus:ring-offset-0 focus:outline-none" type="text" placeholder="Название узла/сборки" @keyup.enter="addNewAssembly"/>
                  </div>
                  <div class="">
                    <button class="text-center text-sm cursor-pointer text-white disabled:text-gray-400 bg-sky-900 px-2 py-0.5 rounded" @click="addNewAssembly"> Добавить</button>
                  </div>
                </div>                
              </div>
            </div>
          </div>
          <div v-if="project_assembly.length > 0" class=" min-h-[12rem]">
            <transition-group tag="div" name="left-emergence"  class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 my-4 gap-4">
              <div v-for="assembly in project_assembly" :key="assembly.id" class="">
                <div v-if="selectedAssembly && selectedAssembly.id === assembly.id" disabled class="flex items-center gap-1">
                  <input type="checkbox" class="rounded text-sky-700 focus:ring-0" />
                  <button class="border-b border-gray-400 w-full h-full">
                    <p class="text-xs text-left font-semibold text-gray-800">{{ assembly.name }}</p>                                      
                  </button>
                </div>
                <div v-else class="flex items-center gap-1">
                  <input type="checkbox" class="rounded text-sky-700 focus:ring-0" />
                  <button class="border-b border-gray-300 w-full h-full" @click="selectAssembly(assembly);updateFiles(assembly.id)">                    
                    <p class="text-xs text-left font-semibold text-gray-600 hover:text-gray-800 transition-all">{{ assembly.name }}</p>
                  </button> 
                </div>              
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
              <span v-if="selectedAssembly" class="px-2 text-gray-600">{{ selectedAssembly.name }}</span>
            </transition>
          </p>
        </div>
        <div class=" h-full flex items-center justify-center">
          <transition name="fade" mode="out-in">
            <div v-if="uploadform" class=" w-full">
              <div class="flex items-center justify-end">
                <button class="mdi mdi-close text-sm" @click="uploadform = false"></button>
              </div>
              <div class="flex items-center justify-center">
                <div class="min-w-[400px] md:min-w-[560px] my-4">
                  <label for="archiveName" class="block mt-2 mb-1 text-xs font-medium text-gray-700">Название архива: <span class="font-semibold">{{ newArchiveName }}</span></label>
                  <input id="archiveName" v-model="newArchiveName" type="text" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-sm focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-300 dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Конструкторская документация">
                </div>
              </div>
              <div class="mb-4">
                <div class="flex items-start justify-center gap-4">
                  <form class="flex items-center space-x-4">
                    <label for="newfile" class="block">
                      <input
                        id="newfile" type="file" multiple
                        class="block w-full text-sm text-slate-500
                        file:mr-4 file:py-2 file:px-4
                        file:rounded-full file:border-0
                        file:text-sm file:font-semibold
                        file:bg-sky-700 file:text-white
                        hover:file:bg-sky-800 transition-all duration-700"
                        @change="uploadDirChange"/>
                    </label>
                  </form>
                  <div class="flex items-center justify-center">
                    <div class="">
                      <div class="text-center">
                        <span class="text-gray-800 text-xs font-semibold w-full text-center"> {{ uploadProgress }}% </span>
                      </div>                
                      <div class=" flex items-center justify-center my-2">
                        <progress class="h-4 text-green-400 border border-white rounded-sm" :value="uploadProgress" max="100">{{ uploadProgress }}%</progress>
                      </div>
                    </div>
                  </div>
                </div>

                <div class="flex items-center justify-center gap-2">
                  <button :disabled="loadingNow" class="w-40 text-center text-sm font-semibold cursor-pointer mdi mdi-upload text-sky-700 disabled:text-gray-600" @click="sendLatestFile"> Загрузить</button>
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

            <button v-if="selectedAssembly" class="w-40 text-center text-sm font-semibold cursor-pointer mdi mdi-package-variant-plus text-sky-900 disabled:text-gray-400 my-2" @click="uploadform = !uploadform"> Создать архив</button>

          </transition>
        </div>



        <div v-if="files.length > 0" class="min-h-[300px]">
          <transition-group tag="div" name="left-emergence" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 py-4">
            <div v-for="project_file in files" :key="project_file.id" class="bg-white/50 backdrop-blur-sm rounded-xl p-1">
              <div class="text-gray-900 rounded-sm py-2">
                <div class="flex items-center min-h-[50px] border-b border-sky-300">
                  <p class="text-sm text-gray-800">{{ project_file.name }}</p>
                </div>
                
                <div class="flex items-center justify-start my-2 gap-2">
                  <div>
                    <label class="flex items-center">
                      <input type="checkbox" class="rounded text-sky-700 focus:ring-0">
                      <p class="text-gray-700 text-sm font-semibold"></p>
                    </label>
                  </div>
                  <a :href="`http://192.168.60.201:8080/files/${project_file.file}`" class="text-sky-800 hover:text-sky-900 text-sm">Скачать</a>
                  <div class="">
                    <button class="text-sm text-sky-800" @click="historyFilesModal = true; updateHistoryFiles(project_file.id); historyFilesActived = project_file.id"> История версий</button>
                  </div>                
                </div>
                <div class="my-2">
                  <div class="grid grid-cols-1 gap-0.5">
                    <p class="text-xs mdi mdi-account font-semibold text-gray-600"> {{ project_file.author }}</p>
                    <p class="text-xs mdi mdi-update font-semibold text-gray-600"> {{ project_file.created_date }}</p>
                  </div>
                </div>
                <div class="relative">
                  <div class="flex items-center justify-center">
                    <form class="flex items-center space-x-4">
                      <label :for="project_file.id" class="block">                        
                        <input
                          :id="project_file.id" type="file" multiple
                          class="block w-full text-sm text-slate-500
                          file:mr-4 file:py-2 file:px-4
                          file:rounded-full file:border-0
                          file:text-sm
                          file:bg-white/0 file:text-sky-700
                          hover:file:bg-white
                        " @change="onFileChange"/>
                      </label>
                    </form>
                  </div>
                  <div class="flex items-center justify-center">
                    <button :disabled="loadingNow" class="w-40 text-center text-sm cursor-pointer mdi mdi-upload text-sky-700 disabled:text-gray-400" @click="uploadFile(project_file.id)"> Обновить</button>
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
        <!-- <div class="flex items-center justify-end my-4">
          <div v-if="latest_file" class="">
            <a :href="latest_file" class="text-center text-sm text-white disabled:text-gray-400 bg-sky-900 px-4 py-1 rounded cursor-pointer flex gap-1 items-start mdi mdi-download" target="_blank"> Скачать архив</a>
          </div>
          <button v-else :disabled="build_latest_file" class="transition-all text-center text-sm text-white disabled:text-white disabled:bg-sky-600  bg-sky-900 px-4 py-1 rounded cursor-pointer flex gap-1 items-start" @click="BuildProject"><span class="mdi mdi-package-variant"></span> Собрать проект</button>
        </div> -->
      </div>
    </div>

    <transition name="top-emergence">
      <div v-if="historyFilesModal" class="fixed z-30 top-0 w-full">
        <div class="">
          <div class="container mx-auto py-2 px-12 bg-gray-100 h-[600px] border-t border-sky-500 rounded-br-xl rounded-bl-xl shadow-lg shadow-gray-900/50">
            <div class="flex justify-between my-2">
              <div class=""><p class="font-semibold text-sky-800 text-sm">История версий</p></div>
              <div class=""><button class="text-sm mdi mdi-close text-sky-800" @click="historyFilesModal = false"> Закрыть</button></div>
            </div>
            <div class="flex items-center justify-between gap-2">
              <div class="w-32"><p class="text-sky-900 font-semibold text-sm mdi mdi-file cursor-pointer"> Проектов: <span class="mx-1">{{ historical_files.length }}</span></p></div>
              <div v-if="historical_files.length > 0" class="grid grid-cols-1 gap-y-4">
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
                              <input type="checkbox" class="rounded text-sky-700 focus:ring-0">
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


    <div class="">
      <div class="fixed bottom-56 left-0 w-0">
        <div class=" rotate-90">
          <div class="">

            <div class="">
              <div class=" w-[220px] h-16">
                <div v-if="latest_file" class="">
                  <a :href="latest_file" class="w-[190px] border border-green-500 text-center text-sm font-semibold text-gray-100 bg-green-600 px-8 py-2 rounded cursor-pointer flex gap-2 items-start mdi mdi-download" target="_blank"> Скачать архив</a>
                </div>  
                <button v-else :disabled="build_latest_file" class="w-[190px] px-8 py-2 transition-all text-center text-sm font-semibold text-gray-100 disabled:text-gray-100 disabled:bg-sky-600 bg-sky-800 border border-sky-700 disabled:border-sky-500 rounded-lg cursor-pointer flex gap-2 items-start" @click="BuildProject"><span class="mdi mdi-package-variant"></span> Собрать проект</button>
              </div>
            </div>
          
          </div>
        </div>
      </div>
    </div>

    <!-- <div class="py-1 container mx-auto hidden">
      <UploadWidget />
    </div> -->


  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
import JSZip from 'jszip';
// import UploadWidget from '~/components/UploadWidget.vue'

export default {
  name: 'ProjectPage',
  // components: {
  //   UploadWidget
  // },
  middleware: ['auth'],
  async asyncData({ params, $axios }) {
    const cts = await $axios.$get(`s/cts/`)
    const space = await $axios.$get(`s/getspace/`)
    const project = await $axios.$get(`s/projects/getone/${params.id}/`)
    return { cts, space, project }
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
      
      uploadProgress: 0,
      loadingNow: false,   /// Выключаем кнопки загрузки
      loadingID: 0,
      changeProjectForm: true,
      editProjectDataForm: false,
      historyFilesModal: false,
      authorFileHistory: this.$auth.user,
      dateFileHistory: '2000-01-12T12:00',

      assemblyName: null,
      uploadDirFiles: [], /// Сюда скидывает новый один
      uploadFiles: [],    /// Сюда скидывает обновлённый с id
      historyFilesActived: null, /// Идентификатор файлов версий, которые отображаются

      latest_file: null, /// Адрес архива
      build_latest_file: false /// Сборка проекта

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
    // this.selectCategory(this.project.category)
    // this.addFiles(this.project.project_files) /// REMOVE
    this.addAssembly(this.project.project_assembly)
    this.selectAssembly(null)
    this.updateStorageSpace(this.space)
  },
  methods: {
    ...mapActions({
      addCategory: 'addCategory',
      updateStorageSpace: 'updateStorageSpace',
      addToast: 'addToast',
      createProject: 'createProject',
      updateProject: 'updateProject',
      updateProjects: 'updateProjects',
      addAssembly: 'addAssembly',
      updateAssembly: 'updateAssembly', ///
      selectAssembly: 'selectAssembly',
      addFiles: 'addFiles',
      addHistoryFiles: 'addHistoryFiles',
      updateHistoryFiles: 'updateHistoryFiles',
      updateFiles: 'updateFiles'
    }),

    /// Без ключа х3 как сделать поэтому
    onFileChange(event) {
      const EventData = event
      const EventID = EventData.target.id
      const IndexFile = this.uploadFiles.findIndex((item) => item.file_id === String(EventID))

      if (IndexFile === -1) {
        this.uploadFiles.push({
          "project_id": this.project.id,
          "file_id": EventID,
          "files": Array.from(event.target.files)
        })
      } else {

        this.uploadFiles[IndexFile].files = Array.from(event.target.files)
      }
    },

    /// Выгрузка проекта одного
    uploadDirChange(event) {
      this.uploadDirFiles = Array.from(event.target.files)
    },
    

    /// Тут архивируются файлы
    readFileContent(file) {
      return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.onload = () => resolve(reader.result);
        reader.onerror = (error) => reject(error);
        reader.readAsArrayBuffer(file);
      })
    },

    async sendLatestFile() {

      this.loadingNow = true /// Выключаем кнопку закгрузки

      const formData = new FormData();
      
      if (this.uploadDirFiles.length > 0) {
        const zip = new JSZip()

        for (let i = 0; i < this.uploadDirFiles.length; i++) {
          const file = this.uploadDirFiles[i];
          const fileContent = await this.readFileContent(file);
          zip.file(file.name, fileContent);
        }

        const zipContent = await zip.generateAsync({ type: 'blob' });
        const archiveName = `${this.newArchiveName}.zip`
        formData.append("file", zipContent, archiveName)
      }


      formData.append("project_id", this.project.id)
      formData.append("assembly_id", this.selectedAssembly.id)
      if (this.newArchiveName) {
          formData.append("name", this.newArchiveName)
      }
      // if (this.authorFileHistory) {
      //   formData.append("author_history", this.authorFileHistory)
      // }
      // if (this.dateFileHistory) {
      //   formData.append("date_history", this.dateFileHistory)
      // }

      try {
        const response = await this.$axios.post('s/files/upload-latest-file/', formData, {
          onUploadProgress: (progressEvent) => {
            this.uploadProgress = Math.round(
              (progressEvent.loaded * 100) / progressEvent.total
            );
          },
        })

          if (response.data.type === 'success') {
            this.uploadform = false
            this.newArchiveName = null
            this.uploadProgress = 0
            this.addToast(response.data)
            setTimeout(() => {
              this.updateFiles(this.project.id)
              this.uploadDirFiles = []
            }, "1500");
          }

        } catch (error) {
          console.log(error)
        }

      this.loadingNow = false
    },


    async sendHistoryFile() {
      
      this.loadingNow = true /// Выключаем кнопку закгрузки
      const formData = new FormData();

      if (this.uploadDirFiles.length > 0) {
        const zip = new JSZip()
        for (let i = 0; i < this.uploadDirFiles.length; i++) {
          const file = this.uploadDirFiles[i];
          const fileContent = await this.readFileContent(file);
          zip.file(file.name, fileContent);
        }
        const zipContent = await zip.generateAsync({ type: 'blob' });
        const archiveName = `${this.newArchiveName}.zip`
        formData.append("file", zipContent, archiveName)        
      }
      
      formData.append("project_id", this.project.id)
      formData.append("assembly_id", this.selectedAssembly.id)
      if (this.newArchiveName) {
          formData.append("name", this.newArchiveName)
      }
      if (this.authorFileHistory) {
        formData.append("author_history", this.authorFileHistory)
      }
      if (this.dateFileHistory) {
        formData.append("date_history", this.dateFileHistory)
      }

      try {
        const response = await this.$axios.post(`s/files/create-history-file/${this.historical_files[0].latest}/`, formData, {
          onUploadProgress: (progressEvent) => {
            this.uploadProgress = Math.round(
              (progressEvent.loaded * 100) / progressEvent.total
            );
          },
        })

          if (response.data.type === 'success') {
            this.uploadform = false
            this.newArchiveName = null
            this.uploadProgress = 0
            this.updateHistoryFiles(this.historyFilesActived)
            // this.addToast(response.data)
            setTimeout(() => {
              // this.updateFiles(this.project.id)
              this.uploadDirFiles = []
            }, "1500");
          }

        } catch (error) {
          console.log(error)
        }

      this.loadingNow = false
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

        const zip = new JSZip()
        for (let i = 0; i < fileData.files.length; i++) {
          const file = fileData.files[i];
          const fileContent = await this.readFileContent(file);
          zip.file(file.name, fileContent);
        }
        const zipContent = await zip.generateAsync({ type: 'blob' });
        const archiveName = `archive.zip` // <= Сделать сюда название архива
        formData.append("file", zipContent, archiveName)



        // if (this.newArchiveName) {
        //   formData.append("name", this.newArchiveName)
        // }
        // if (this.authorFileHistory) {
        //   formData.append("author_history", this.authorFileHistory)
        // }
        // if (this.dateFileHistory) {
        //   formData.append("date_history", this.dateFileHistory)
        // }
        if (latestId) {
          formData.append("latest_id", latestId)
        }


        try {
          this.loadingNow = true
          this.loadingID = fileData.file_id

          const response = await this.$axios.post(`s/files/update-latest-file/${fileData.file_id}/`, formData, {
            onUploadProgress: (progressEvent) => {
              this.uploadProgress = Math.round(
                (progressEvent.loaded * 100) / progressEvent.total
              );
            },
          })

          if (response.data.type === 'success') {
            this.uploadform = false
            this.newArchiveName = null
            this.uploadFiles = []
            this.addToast(response.data)
            setTimeout(() => {
              this.updateFiles(fileData.file_id)
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

    async BuildProject() {
      this.build_latest_file = true
      try {
        const response = await this.$axios.post(`s/projects/builderproject/${this.project.id}/`) 
        this.latest_file = response.data.file
        this.build_latest_file = false
      } catch (err) {
        console.log(err)
      }

    },

  },
}
</script>
