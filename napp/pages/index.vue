<template>

  <div class="">
    <!-- {{ projects }} -->

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

            <div class="flex items-center justify-between">

              <form class="flex items-center space-x-6">
                <label class="block">
                  <input
                    type="file" class="block w-full text-sm text-gray-100
                    file:mr-4 file:py-2 file:px-4
                    file:rounded-full file:border-0
                    file:text-sm file:font-semibold
                    file:bg-white file:text-sky-700
                    hover:file:bg-white 
                  " @change="onFileChange" />
                </label>
              </form>

              <button class="text-white " @click="createProject">Создать проект</button>

            </div>


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
      name: null,
      description: null,
      filename: null,
    }
  },
  methods: {
    onFileChange(e) {
      const files = e.target.files || e.dataTransfer.files;
      if (!files.length)
        return;
      this.createImage(files[0]);
    },
    createImage(file) {
      // const image = new Image();
      const reader = new FileReader();
      const vm = this;

      reader.onload = (e) => {
        vm.image = e.target.result;
      };
      reader.readAsDataURL(file);
    },


    createProject(filename) {

      const data = {
        name: this.name,
        description: this.description,
        filename: this.filename
      }
      console.log(filename)

      this.$axios.$post('s/projects/', data, { headers: { 'Content-Type': 'multipart/form-data' } }).then((resp) => {
        // this.saveOrder(resp)

        console.log("TRY")
      }).catch(() => {
        console.log('CATCH')
      })
     

    },
  },
}
</script>
