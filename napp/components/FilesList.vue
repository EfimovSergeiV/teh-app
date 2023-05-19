<template>
  <div class="">

    <div class="bg-gray-100">
      <div class="container mx-auto py-2 px-4">
        <div class="flex gap-4 items-center ">
          <div class="w-32"><p class="text-gray-600 font-semibold text-sm mdi mdi-file cursor-pointer"> Проектов: <span class="mx-1">{{ projects.length }}</span></p></div> 
          <button class="text-gray-600 font-semibold text-sm mdi mdi-help-circle-outline"> Помощь</button>
          <button class="text-gray-600 font-semibold text-sm mdi mdi-plus-thick"> Создать категорию</button>
          <button class="text-gray-600 font-semibold text-sm mdi mdi-view-grid-plus cursor-pointer" @click="createProjectForm"> Создать проект</button>
          <button class="text-gray-600 font-semibold text-sm mdi mdi-update cursor-pointer" @click="updateProjects"> Обновить</button>
          <button class="text-gray-600 font-semibold text-sm mdi mdi-cloud-search cursor-pointer"> Найти проект</button>
        </div>      
      </div>      
    </div>


    <div class="container mx-auto min-h-screen py-6 px-4">
      
      <div>

        <!-- <div class="my-2 grid grid-cols-2 gap-4 text-gray-700 hover:text-gray-900 transition-all duration-700">
          <div class="text-center text-xs"><p class="">Название проекта</p></div>
          <div class="text-center text-xs"><p class=""> Действия</p></div>
        </div> -->

        <transition-group v-if="projects.length > 0" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4" name="left-emergence">
          <div v-for="fileResp in projects" :key="fileResp.id">
            <div class=" border-b border-gray-300 my-2 grid gap-1 xl:flex xl:gap-4 items-center justify-start text-gray-700 hover:text-gray-900 transition-all duration-700">

              <nuxt-link :to="{ name: 'storage-id', params: { id: fileResp.id }}" class="w-full">
                <div class="">
                  <div class=""><p class="text-sm font-semibold">{{ fileResp.name }}</p></div>
                  <div class="grid grid-cols-1">
                    <p class="text-xs">Обновлён: {{ fileResp.created_date }}</p>
                    <!-- <p class="text-xs">MD5: {{ fileResp.project_files.slice(-1)[0].md5 }}</p> -->
                  </div>
                </div>
              </nuxt-link>

              <!-- <div class="flex items-center justify-end">
                <div class="w-24"><a href="#" class="text-center text-sm cursor-pointer mdi mdi-download font-semibold"> Скачать всё</a></div>
                <form class="flex items-center space-x-6">
                  <label class="block">
                    <input
                      :id="fileResp.id" type="file" class="block w-full text-sm text-slate-500
                      file:mr-4 file:py-2 file:px-4
                      file:rounded-full file:border-0
                      file:text-sm file:font-semibold
                      file:bg-white file:text-sky-700
                      hover:file:bg-white
                    " @change="onFileChange"/>
                  </label>
                </form>
                <transition name="fade" mode="out-in">

                  <button v-if="uploadedId !== fileResp.id" :disabled="dissableBtns" class="w-40 text-center text-sm font-semibold cursor-pointer mdi mdi-upload text-gray-700 disabled:text-gray-400" @click="uploadFile(fileResp.id)"> Загрузить</button>
                  <div v-else class="">
                    <div class="text-center">
                      <span class="text-gray-800 text-xs font-semibold w-full text-center"> {{ uploadProgress }}% </span>
                    </div>                
                    <div class="">
                      <progress class="h-4 text-green-400 border border-white rounded-sm" :value="uploadProgress" max="100">{{ uploadProgress }}%</progress>
                    </div>
                  </div>

                </transition>

                <div class="w-28"><p class="text-right cursor-pointer mdi mdi-information text-sm font-semibold"> Подробнее</p></div>              
              </div> -->

            </div>

          </div>      
        </transition-group>

        <div v-else class=" flex justify-center items-center py-12">
          <p class="mdi mdi-close"> Нет файлов </p>
        </div>

      </div>


    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex';

export default {
  name: 'FilesList',
  props: {
    projectsResponse: {
      type: Array,
      default: Array,
    },
    filesResponse: {
      type: Array,
      default: Array,
    },
  },
  data() {
    return {
      // resp: [
      //   {'id': 1, 'name': 'МТВ-8000'}, {'id': 2, 'name': 'МТВ-8001'}, {'id': 3, 'name': 'МТВ-8002'},
      //   {'id': 4, 'name': 'МТВ-8003'}, {'id': 5, 'name': 'МТВ-8004'}, {'id': 6, 'name': 'МТВ-8005'},
      //   {'id': 7, 'name': 'МТВ-8006'}, {'id': 8, 'name': 'МТВ-8007'}, {'id': 9, 'name': 'МТВ-8008'},
      //   {'id': 10, 'name': 'МТВ-8009'}, {'id': 11, 'name': 'МТВ-8010'}, {'id': 12, 'name': 'МТВ-8011'},
      //   {'id': 13, 'name': 'МТВ-8012'}, {'id': 14, 'name': 'МТВ-8013'}, {'id': 15, 'name': 'МТВ-8014'},
      //   {'id': 16, 'name': 'МТВ-8015'}, {'id': 17, 'name': 'МТВ-8015'}, {'id': 18, 'name': 'МТВ-8017'},
      // ],
      name: null,
      description: null,
      file: null,
      uploadProgress: 0,
      uploadFiles: [],
      uploadedId: null,
      dissableBtns: false,
    }
  },
  computed: {
    ...mapState({
      projects: (state) => state.projects,
      files: (state) => state.files,
    }),

  },
  mounted() {
    this.addProjects(this.projectsResponse)
  },
  methods: {
    ...mapActions({
      addProjects: 'addProjects',
      // addFiles: 'addFiles',
      addNewUploadFile: 'addNewUploadFile',
      createProjectForm: 'createProjectForm',
      addToast: 'addToast',
      updateProjects: 'updateProjects',
    }),


  },
}
</script>
