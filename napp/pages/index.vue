<template>

  <div class="">
    <div class="relative">
      <div class="container mx-auto py-2 px-4">
        <div id="create-project" class="absolute z-10">
          <div class="bg-sky-900 w-[1000px] px-4 py-4 rounded-lg">
            <div class="">
              <label for="message" class="block mt-2 mb-1 text-xs font-medium text-gray-100">Название проекта: {{ name }}</label>
                <input id="text" v-model="name" type="text" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-sm focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-300 dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="МТВ-8000 ExpSuperVOC">
            </div>
            <div class="my-4">
              <label for="message" class="block mt-2 mb-1 text-xs font-medium text-gray-100">Описание проекта</label>
              <textarea id="message" v-model="description" rows="4" class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-sm border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Опишите проект..."></textarea>
            </div>


            <form  class="flex items-center space-x-6" @submit.prevent="uploadFile">
              <label class="block">
                <input
                  id="file" type="file"
                  class="block w-full text-sm text-slate-500
                  file:mr-4 file:py-2 file:px-4
                  file:rounded-full file:border-0
                  file:text-sm file:font-semibold
                  file:bg-white file:text-sky-700
                  hover:file:bg-white
                " @change="onFileChange"/>
              </label>

              <div v-if="uploadProgress !== null">
                <span class="text-white">Upload Progress: {{ uploadProgress }}% </span>
                <progress class="h-4 text-green-400 border border-white rounded-sm" :value="uploadProgress" max="100">{{ uploadProgress }}%</progress>
              </div>
              
              <button class="" type="submit">Загрузить файл</button>

            </form>

            <!-- <div class="flex items-center justify-between">
              <div>
                <form @submit.prevent="uploadFile">
                  <div>
                    <label for="file">File:</label>
                    <input id="file" type="file" @change="onFileChange" />
                  </div>
                  


                </form>
              </div>
            </div> -->
          </div>
        </div>
      </div>
    </div>
    <FilesList />
  </div>
</template>

<script>

export default {
  name: 'IndexPage',
  async asyncData({ $axios }) {
    const projects = await $axios.$get('s/projects/')
    return { projects }
  },
  data() {
    return {
      name: 'МТВ-8002',
      description: "Не большое описание",
      filename: null,

      file: null,
      uploadProgress: null,
    }
  },
  methods: {
    onFileChange(event) {
      this.file = event.target.files[0];
    },
    async uploadFile() {
      const formData = new FormData();
      formData.append('name', this.name);
      formData.append('description', this.description);
      formData.append('file', this.file);

      try {
        const response = await this.$axios.post('s/projects/', formData, {
          onUploadProgress: (progressEvent) => {
            this.uploadProgress = Math.round(
              (progressEvent.loaded * 100) / progressEvent.total
            );
          },
        });

        console.log(response.data);
      } catch (error) {
        console.log(error);
      }
    },

  },
}
</script>
