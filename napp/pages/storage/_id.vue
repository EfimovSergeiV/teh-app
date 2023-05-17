<template>
  <div class="">

    <div class="bg-gray-100">
      <div class="container mx-auto py-2 px-4">
        <div class="flex gap-4 items-center ">
          <nuxt-link :to="{ name: 'index' }" class="text-gray-600 font-semibold text-sm mdi mdi-home"> Вернуться на главную</nuxt-link>
          <button class="text-gray-600 font-semibold text-sm mdi mdi-help-circle-outline"> Помощь</button>
          <button class="text-green-600 font-semibold text-sm mdi mdi-check-bold"> Обновить проект</button>
          <button class="text-red-600 font-semibold text-sm mdi mdi-close-thick"> Отменить и вернуться на главную</button>
        </div>
      </div>
    </div>


    <div class="container min-h-screen mx-auto px-4">

      <div class="my-4">
        <p class="font-semibold text-gray-700">{{ project.name }}</p>
        <p class="text-sm">Описание:</p>
        <p class="text-sm font-semibold text-gray-700">{{ project.description }}</p>
        <p class="text-sm">Создан: {{ project.created_date }}</p>        
      </div>


      <div class="my-4 border-b border-gray-400">
        <p>Файлы проекта:</p>
      </div>

      <div class="">
        <div v-for="project_file in project.project_files" :key="project_file.id" class="">

          <div class="my-2 border-b border-gray-300">
            <p class="">{{ project_file.name }}</p>
            <p class="text-sm">Обновлён: {{ project_file.created_date }}</p>
            <p class="text-xs">md5: {{ project_file.md5 }}</p>
            <div class="flex">
              <div class="">
                <div class="text-center">
                  <span class="text-gray-800 text-xs font-semibold w-full text-center"> {{ uploadProgress }}% </span>
                </div>                
                <div class=" flex items-center justify-center">
                  <progress class="h-4 text-green-400 border border-white rounded-sm" :value="uploadProgress" max="100">{{ uploadProgress }}%</progress>
                </div>
              </div>
            </div>
            <div class="flex gap-2">
              <div class="">
                <a :href="project_file.file" class="font-semibold text-gray-900 text-sm">Скачать</a>
              </div>
              <div class="">
                <button class="font-semibold text-gray-900 text-sm">Обновить</button>
              </div>
            </div>
          </div>

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
