<template>
  <div class="">

    <p class="">
      THIS UPLOAD WIDGET
    </p>

    <!-- <dropzone id="foo" ref="el" :options="options" :destroy-dropzone="true" placeholder="">Перетащите файлы для загрузки</dropzone> -->

    <div class="">
      <div class="flex items-start justify-center gap-4">

        <form class="flex items-center space-x-4">
          <label for="newfile" class="block">
            <!-- <div class="flex items-center gap-4">
              <p class="py-2 px-6 text-sm text-white font-semibold bg-sky-900 hover:bg-sky-800 transition-all cursor-pointer rounded">Выберите папку с файлами</p>
              <p class="text-sm text-gray-600 md:w-32">Файлов: <span class="">{{ uploadDirFiles.length }}</span></p>
            </div> -->
            <!-- 
              INPUT CLASS

            -->
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
    </div>

  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex';
// import Dropzone from 'nuxt-dropzone'
// import 'nuxt-dropzone/dropzone.css'

export default {
  name: 'UploadWidget',
  // props: {
  //   projectsResponse: {
  //     type: Array,
  //     default: Array,
  //   },
  //   filesResponse: {
  //     type: Array,
  //     default: Array,
  //   },
  // },
  // components: {
  //   Dropzone
  // },
  data() {
    return {
      uploadProgress: 0,
    }
  },
  computed: {
    ...mapState({
      selectedCategory: (state) => state.selectedCategory,
      projects: (state) => state.projects,
      files: (state) => state.files,
    }),

  },
  mounted() {
    // const instance = this.$refs.el.dropzone
    // return instance
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
    s3UploadError(errorMessage){
      console.log("Error")
    },
    s3UploadSuccess(s3ObjectLocation){
      console.log("Success")
    }
  },
}
</script>
