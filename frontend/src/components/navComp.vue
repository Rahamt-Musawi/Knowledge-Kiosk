<template>
    <div>
      <nav class="flex items-center justify-between flex-wrap bg-slate-800 p-5 pt-10 text-sky-50">
        <div class="flex items-center flex-shrink-0 ">
          <img
            class="fill-current h-8 w-8 ml-6 "
            width="54"
            height="54"
            viewBox="0 0 54 54"
            src="../assets/logo.png"
          />
          <span class=" mr-2 ml-2 text-2xl font-bold font-outline-4 text-red-600 drop-shadow-md">Knowledge-Kiosk</span><span class="font-serif pt-1">Ask me <span class="text-blue-200">anything</span>, <span class="text-green-200">anytime</span>, <span class="text-red-200">anywhere</span> - give your response the way you wish :)</span>
        </div>
  
        <div class="float-right mr-6">
          <div class="text-sm border-solid flex-grow lg:flex float-right ">
            <a
              href="http://localhost:8080/"
              class="text-l font-semibold block mt-4 lg:inline-block lg:mt-0  hover:underline mr-4"
            >
              Home
            </a>
            <a
              href="https://github.com/Rahamt-Musawi?tab=repositories"
              class="text-l font-semibold block mt-4 lg:inline-block lg:mt-0  hover:underline mr-4"
            >
              Github Page
            </a>
            <a
              @click="about"
              class="cursor-pointer text-l font-semibold block mt-4 lg:inline-block lg:mt-0 hover:underline"
            >
              About
            </a>
          </div>
        </div>
      </nav>
    </div>
  </template>
  
  <script>
  export default {
    name: "navComp",
    methods: {
      about() {
        this.$emit("about");
      },
    },
  };
  </script>
  