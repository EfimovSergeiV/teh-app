<template>
  <div class="">

    <div class="bg-gray-100">
      <div class="container mx-auto py-2 px-4">
        <div class="flex gap-4 items-center ">
          <div class="w-28"><p class="text-gray-600 font-semibold text-sm mdi mdi-file cursor-pointer"> Проектов: {{ files.length }}</p></div> 
          <p class="text-gray-600 font-semibold text-sm mdi mdi-help-circle-outline"> Помощь</p>
          <p class="text-gray-600 font-semibold text-sm mdi mdi-plus-thick"> Создать категорию</p>
          <p class="text-gray-600 font-semibold text-sm mdi mdi-view-grid-plus cursor-pointer" @click="createProject"> Создать проект</p>
          <p class="text-gray-600 font-semibold text-sm mdi mdi-cloud-search cursor-pointer"> Найти проект</p>
        </div>      
      </div>      
    </div>


    <div class="container mx-auto min-h-screen py-2 px-4">
      
      <div class="">

        <p class="  my-4"></p>

        <div class="my-2 flex gap-4 items-center text-gray-700 hover:text-gray-900 transition-all duration-700">
          <div class="w-80 text-xs"><p class="">Название проекта</p></div>
          <div class="w-[640px] text-center text-xs"><p class=""> Действия</p></div>
        </div>

        <transition-group name="fade">
          <div v-for="file in files" :key="file.id">
            <div class="flex gap-4 items-center justify-between text-gray-700 hover:text-gray-900 transition-all duration-700">

              <div class="">
                <div class="w-80"><p class="">{{ file.name }}</p></div>
              </div>

              <div class="flex justify-end">
                <div class="w-40"><p class="text-center cursor-pointer mdi mdi-download"> Скачать</p></div>
                <form class="flex items-center space-x-6">
                  <label class="block">
                    <input
                      type="file" class="block w-full text-sm text-slate-500
                      file:mr-4 file:py-2 file:px-4
                      file:rounded-full file:border-0
                      file:text-sm file:font-semibold
                      file:bg-white file:text-sky-700
                      hover:file:bg-white
                    "/>
                  </label>
                </form>
                <div class="w-40"><p class="text-center cursor-pointer mdi mdi-upload"> Загрузить</p></div>
                <div class="w-40"><p class="text-right cursor-pointer mdi mdi-information"> Подробнее</p></div>              
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
  name: 'FilesList',
  props: {
    filess: {
      type: Array,
      default: Array,
    },
  },
  data() {
    return {
      resp: [
        {'id': 1, 'name': 'МТВ-8000'}, {'id': 2, 'name': 'МТВ-8001'}, {'id': 3, 'name': 'МТВ-8002'},
        {'id': 4, 'name': 'МТВ-8003'}, {'id': 5, 'name': 'МТВ-8004'}, {'id': 6, 'name': 'МТВ-8005'},
        {'id': 7, 'name': 'МТВ-8006'}, {'id': 8, 'name': 'МТВ-8007'}, {'id': 9, 'name': 'МТВ-8008'},
        {'id': 10, 'name': 'МТВ-8009'}, {'id': 11, 'name': 'МТВ-8010'}, {'id': 12, 'name': 'МТВ-8011'},
        {'id': 13, 'name': 'МТВ-8012'}, {'id': 14, 'name': 'МТВ-8013'}, {'id': 15, 'name': 'МТВ-8014'},
        {'id': 16, 'name': 'МТВ-8015'}, {'id': 17, 'name': 'МТВ-8015'}, {'id': 18, 'name': 'МТВ-8017'},
      ],
    }
  },
  computed: {
    
    ...mapState({
      files: (state) => state.files,
      
    }),

  },
  mounted() {
    this.addFiles(this.resp)
  },
  methods: {
    ...mapActions({
      addFiles: 'addFiles',
      createProject: 'createProject'
    }),
  },
}
</script>
