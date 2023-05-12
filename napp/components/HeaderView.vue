<template>
  <div class="">
    
    <div class="bg-sky-800">
      <div class="container mx-auto py-8">

        <div class="px-4">
          <img src="logo.webp" class="h-[35px]" />
        </div>

      </div>
    </div>

    <div class="bg-sky-700">
      <div class="container mx-auto py-4">

        <div class="flex gap-4 px-4">
          <p class="text-white font-semibold text-sm border-b border-white cursor-pointer"> Модели</p>
          <p class="text-gray-300 font-semibold text-sm border-b border-gray-300 cursor-pointer"> Обнажёнка</p>
          <p class="text-gray-300 font-semibold text-sm border-b border-gray-300 cursor-pointer"> Документы</p>
        </div>

      </div>
    </div>


    <!-- <div class="bg-sky-500">
      <div class="container mx-auto py-2">

        <div class="flex gap-4 px-4">
          <p class="text-gray-100 font-semibold text-sm mdi mdi-view-grid-plus cursor-pointer"> Создать проект</p>
        </div>

      </div>
    </div> -->


  </div>

</template>

<script>

export default {
  name: 'HeaderView',
  props: {
    // filess: {
    //   type: Array,
    //   default: Array,
    // },
  },
  data() {
    return {

    }
  },
}
</script>
