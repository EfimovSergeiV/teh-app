<template>
  <div class="">

    <p class="">
      THIS UPLOAD WIDGET
    </p>

    <!-- <dropzone id="foo" ref="el" :options="options" :destroy-dropzone="true" placeholder="">Перетащите файлы для загрузки</dropzone> -->

    <dropzone
      id="my-dropzone"
      :options="dropzoneOptions"
      @vdropzone-s3-upload-error="s3UploadError"
      @vdropzone-s3-upload-success="s3UploadSuccess"
    >
      <div class="dz-message">Перетащите файлы сюда или щелкните для загрузки.</div>
    </dropzone>

  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex';
// import Dropzone from 'nuxt-dropzone'
// import 'nuxt-dropzone/dropzone.css'

export default {
  name: 'FilesList',
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
      // See https://rowanwins.github.io/vue-dropzone/docs/dist/index.html#/props
      // options: {
      //   url: "http://127.0.0.1:8000/s/upload-wiget/"
      //   // url: "http://httpbin.org/anything"
      // }
      dropzoneOptions: {
        url: 'http://127.0.0.1:8000/s/files/upload-latest-file/', // Замените URL на адрес вашего DRF API для загрузки файлов
        // url: 'https://httpbin.org/post',
        // paramName: 'file',
        // maxFilesize: 10, // Максимальный размер файла (в МБ)
        // acceptedFiles: 'image/*', // Типы принимаемых файлов
        headers: {
          'Authorization': 'Bearer e224ef33ffa49005bdc3c3c7a26915a62f25bf2d' // Замените 'your-token' на ваш токен авторизации для доступа к DRF API
        }
      }

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
