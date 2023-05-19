<template>
  <div class="">
    
    <div class="bg-sky-800">
      <div class=" container mx-auto py-8 px-4">
        <div class="flex items-center justify-between">
          <nuxt-link :to="{ name: 'index' }" class="">
            <img src="/logo.webp" class="h-[35px]" />
          </nuxt-link>
          <div class="flex gap-4">
            <div class=""><p class="mdi mdi-account text-white text-sm flex items-center font-semibold">Пользователь</p></div>
            <!-- <div class="mdi mdi-star text-white text-sm flex items-center font-semibold"><p>Рейтинг 150</p></div> -->
          </div>
        </div>


      </div>
    </div>

    <div class="bg-sky-700">
      <div class=" container mx-auto">

        <div class="flex gap-4 py-2 px-4">
          <div v-for="category in categories" :key="category.id" class="">
            <p class="text-white font-semibold text-sm border-white cursor-pointer">{{ category.name }}</p>
          </div>
        </div>

        <div class="flex gap-4 py-2 px-4">
          <div v-for="inserted in inserteds" :key="inserted.id" class="">
            <p class="text-white font-semibold text-xs border-b border-white cursor-pointer">{{ inserted.name }}</p>
          </div>
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
      categories: [
        { "id": 1, "name": "Сварочные машины и установки", "inserted": [ { "id": 2, "name": "Точечная переменным током" }, { "id": 3, "name": "Точечная постоянным током"}, { "id": 3, "name": "Точечная конденсаторная"}, { "id": 3, "name": "Шовная постоянным током"}, { "id": 3, "name": "Рельефная переменным током"}, { "id": 3, "name": "Стыковая"}, ] },
        { "id": 2, "name": "Оборудование для сварки рельсов", "inserted": [ { "id": 2, "name": "Точечная переменным током" }, { "id": 3, "name": "Точечная постоянным током"}, { "id": 3, "name": "Точечная конденсаторная"}, { "id": 3, "name": "Шовная постоянным током"}, { "id": 3, "name": "Рельефная переменным током"}, { "id": 3, "name": "Стыковая"}, ] },
        { "id": 3, "name": "Трансформаторы", "inserted": [ { "id": 2, "name": "Точечная переменным током" }, { "id": 3, "name": "Точечная постоянным током"}, { "id": 3, "name": "Точечная конденсаторная"}, { "id": 3, "name": "Шовная постоянным током"}, { "id": 3, "name": "Рельефная переменным током"}, { "id": 3, "name": "Стыковая"}, ] },
        { "id": 4, "name": "Источники", "inserted": [ { "id": 2, "name": "Точечная переменным током" }, { "id": 3, "name": "Точечная постоянным током"}, { "id": 3, "name": "Точечная конденсаторная"}, { "id": 3, "name": "Шовная постоянным током"}, { "id": 3, "name": "Рельефная переменным током"}, { "id": 3, "name": "Стыковая"}, ] },
      ],
      inserteds: [
        { "id": 2, "name": "Контактная сваарка" },
        { "id": 2, "name": "Дуговая сваарка" },
        { "id": 2, "name": "Диффузионная сваарка" },
        { "id": 2, "name": "Микросварка сваарка" },
        { "id": 2, "name": "Контактная пайка" },
        { "id": 2, "name": "Специального назначения" },
      ]
    }
  },
}
</script>
