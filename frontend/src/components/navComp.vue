<template>
    <div>
      <nav class="flex items-center justify-between flex-wrap bg-slate-800 p-5 pt-10 text-sky-50">
        <div class="flex items-center ">
          <a
              href="http://localhost:8080/" class="flex">
          <img
            class="fill-current h-10 w-10 ml-6 "
            width="54"
            height="54"
            viewBox="0 0 54 54"
            src="../assets/logo.png"
          />

          <span class=" mr-6 ml-2 text-4xl font-dancing-script text-stone-300">KNOWLEDGE-KIOSK</span></a>  <span class="drop-shadow-md text-white ml-3 border-1 border-t-2 border-b-2 border-gray-400 p-1"> <span>Ask me <span class="text-blue-200 ">anything</span>, <span class="text-green-200">anytime</span>, <span class="text-red-200">anywhere</span> - I respond immediately as you wish</span></span>   
        </div>
  
        <div class="float-right mr-6 ml-7">
          <div class="text-sm border-solid flex-grow lg:flex float-right ">
            <a
              href="http://localhost:8080/"
              class="text-l font-semibold block mt-4 lg:inline-block lg:mt-0  hover:underline mr-4"
            >
              Home
            </a>
            <a
              href="https://github.com/Rahamt-Musawi/Knowledge-Kiosk"
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
  