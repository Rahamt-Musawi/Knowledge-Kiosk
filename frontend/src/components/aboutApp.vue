<template>
  <div class="p-6 sm:p-12 dark:bg-gray-900 dark:text-gray-100">
    <div class="flex flex-col space-y-4 md:space-y-0 md:space-x-6 md:flex-row">
      <div class="flex flex-col">
        <h4 class="text-lg font-semibold text-center md:text-left">
          KNOWLEDGE-KIOSK
        </h4>
        <p class="dark:text-gray-400">
          This application is developed using Python on the backend and
          Javascript on the frontend. It is empowered by OpenAI API that can
          answer any question you ask. The Interface is designed to be simple,
          user friendly, responsive and effiecient. Thanks to the nice
          combination of Python and Vue 3, the application can be customized and
          scaled easily in the future.
        </p>
        <br />
        <details>
          <summary class="bg-sky-900 text-stone-100 cursor-pointer p-2">
            Get in touch with me
          </summary>
          <div class="flex bg-sky-50 p-5 fade-in duration-300">
            <img
              src="../assets/profile.jpeg"
              alt=""
              class="self-center flex w-24 h-24 border rounded-full md:justify-self-start dark:bg-gray-500 dark:border-gray-700"
            />

            <ul class="flex-none list-disc mr-5 ml-5">
              <p class="pt-3 font-bold text-blue-900">RAHMATULLAH MUSAWI</p>
              <li class="mr-5 ml-5">musawi.rahmat@gmail.com</li>
              <li class="mr-5 ml-5">+49 15733303451</li>
            </ul>
          </div>
        </details>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AboutApp",
};
</script>
