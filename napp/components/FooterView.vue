<template>
  <div class="bg-sky-900">
    <div class=" container mx-auto py-3 px-4 md:px-12">
      <div class=" relative">

        <div class="flex items-center justify-end h-full">
          <div class="grid grid-cols-1 justify-center items-center gap-1">
            <div class="text-xs font-semibold text-gray-100">Место на диске: {{ storageSpace.total_space }} / {{ storageSpace.used_space }} ( {{ Math.round(storageSpace.total_space - storageSpace.used_space) }} ) GB</div>
            <progress class="w-full text-green-400 border border-white rounded-sm" :value="storageSpace.used_space" :max="storageSpace.total_space" />
          </div>
        </div>

        <div class="absolute bottom-0 h-full w-full flex  items-center justify-start md:justify-center gap-4 px-4">
          <p class="text-gray-100 font-semibold text-xs mdi mdi-copyright"> 2023 | ООО Техносвар КС </p>
        </div> 

      </div>     

    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex';

export default {
  name: 'FooterView',
  props: {
    // filess: {
    //   type: Array,
    //   default: Array,
    // },
  },
  data() {
    return {
      storageResult: 100
    }
  },
  computed: {
    ...mapState({
      storageSpace: (state) => state.storageSpace,
    }),

  },
}
</script>

<style scoped>
progress {
    border: 0;
    height: 10px;
    border-radius: 20px;
}
progress::-webkit-progress-bar {
    border: 0;
    height: 10px;
    border-radius: 20px;
}
progress::-webkit-progress-value {
    border: 0;
    height: 10px;
    border-radius: 20px;
}
progress::-moz-progress-bar {
    border: 0;
    height: 10px;
    border-radius: 20px;
}
</style>
