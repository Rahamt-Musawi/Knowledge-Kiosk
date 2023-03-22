<template>
  <div class="h-screen bg-txt-bg">
    <div>
      <NavComp @about="showAbout"/>

      <form @submit.prevent="send_question" class="bg-txt-bg border-b-2">
        <div class="font-sans m-10 flex items-center justify-center">
          <input
            v-model="question"
            type="text"
            class="transition delay-150 duration-300 ease-in-out p-3 rounded-l-lg h-13 flex-1 focus:outline-none border-2 border-slate-400 border-r-0 focus:border-blue-800"
            placeholder="Type your question here..."
          />
          <button
            type="submit"
            class="flex rounded-r-lg items-center justify-center px-4 bg-blue-700 border-2 border-blue-900"
          >
            <img src="./assets/search.png" class="h-12 w-12 p-2" />
          </button>
        </div>
        <div class="h-12">
          <loadingComp v-if="loading" />
        </div>
      </form>

      <div>
        <div class="bg-txt-bg p-11 h-full">
          <mottoComp v-if="motto" />

          <section class="answer pb-5">
            <span class="fade-in font-bold text-xl text-red-900 opacity-80">{{
              asked
            }}</span>
            <p v-if="response" class="fade-in delayed whitespace-pre-wrap">
              {{ response }}
            </p>
            <AboutApp v-if="about" />
          </section>
        </div>
      </div>
    </div>
    <FooterComp />
  </div>
</template>
<script>

import loadingComp from "./components/loadingComp.vue";
import footerComp from "./components/footerComp.vue";
import mottoComp from "./components/mottoComp.vue";
import aboutApp from "./components/aboutApp.vue"
import navComp from "./components/navComp.vue";

import io from "socket.io-client";

export default {
  components: { navComp, loadingComp, footerComp, mottoComp, aboutApp },
  data() {
    return {
      question: "",
      motto: true,
      asked: "",
      response: "",
      loading: false,
      about: false
    };
  },

  created() {
    this.socket = io("http://localhost:5000");
    this.socket.on("connect", () => {
      console.log("Connected to Socket.io server");
    });
    this.socket.on("response", (data) => {
      this.response = data.data;
      console.log(this.response)
      this.loading = false;
      this.question = "";
      this.about=false
    });
  },
  methods: {
    send_question() {
      console.log("Sending your question:", this.question);
      this.socket.emit("question", this.question);
      this.asked = this.question;
      this.response = "";
      this.motto = false;
      this.loading = true;
      this.about=false;
    },
    showAbout() {
      this.about=true
      this.response = ""
      this.motto=true
      this.asked=""
    }
  },
};
</script>

<style>
.answer {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

/* make keyframes that tell the start state and the end state of our object */

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

.fade-in {
  opacity: 0; /* make things invisible upon start */
  animation: fadeIn ease-in 1;
  animation-fill-mode: forwards;
  animation-duration: 0.5s;
}

.fade-in.delayed {
  animation-delay: 0.3s;
}
</style>
