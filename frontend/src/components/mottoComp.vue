<template>
    <section>
    
      <p class=" text-2xl font-bold tracking-tighter">
      Ask me
        <span :class="actionClasses">{{ action }}</span>
      </p>
      <p class="text-2xl font-light ml-20 mb-3 pl-1">in any language</p>
      <p class="text-2xl font-light ml-20 pl-1">I can provide you usefull informations. Try it! It's free &#128522;</p>
    
    </section>
  </template>
  
  <script>
  import nextElementInList from "../utils/nextElementList";
  
  export default {
    name: "TheHeadline",
    data() {
      return {
        action: "anything",
        interval: null,
      };
    },
    computed: {
      actionClasses() {
        return {
          [this.action.toLowerCase()]: true,
        };
      },
    },
    created() {
      this.changeTitle();
    },
    beforeUnmount() {
      clearInterval(this.interval);
    },
    methods: {
      changeTitle() {
        this.interval = setInterval(() => {
          const actions = ["anything", "anytime", "anywhere"];
          this.action = nextElementInList(actions, this.action);
        }, 3000);
      },
    },
  };
  </script>
  
  <style scoped>
  .anything {
    color: #1a73e8;
  }
  
  .anytime {
    color: #34a853;
  }
  
  .anywhere {
    color: #d93025;
  }
  </style>
  