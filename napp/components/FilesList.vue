<template>

  <div class="px-2 py-2">
    <p class=" text-gray-800 mdi mdi-file my-4">Files: {{ files.length }}</p>

    <!-- <button @click="addFiles()">Send</button> -->
    
    <div class="mx-8">

      <div class="my-2 flex gap-4 items-center text-gray-700 hover:text-gray-900 transition-all duration-700">
        <div class="w-80"><p class="">Название проекта</p></div>
        <div class="w-[640px]"><p class=""> Действия</p></div>
      </div>

      <transition-group name="fade">
        <div v-for="file in files" :key="file.id">
          <div class="flex gap-4 items-center text-gray-700 hover:text-gray-900 transition-all duration-700">

            <div class="w-80"><p class="">{{ file.name }}</p></div>
            <div class="w-40"><p class="text-center cursor-pointer mdi mdi-download"> Скачать</p></div>
            <div class="w-40"><p class="text-center cursor-pointer mdi mdi-upload"> Загрузить</p></div>
            <div class="w-40"><p class="text-center cursor-pointer mdi mdi-information"> Подробнее</p></div>
            
            

          </div>
          
        </div>      
      </transition-group>      
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
    }),
  },
}
</script>
