<template>
  <div class="skills absolute top-20 pl-10 mt-12 w-full">
    <h1 class="text-4xl mb-6 text-center">Professional Skills</h1>
    <div
      class="flex w-5/6 m-auto border border-slate-500 shadow-2xl shadow-black p-10 backdrop-blur-md"
    >
      <div class="basis-1/2">
        <div class="basis-1/2 mb-4">
          <p class="">HTML</p>
          <div class="rounded h-5 bg-gray-200 w-3/4">
            <div class="rounded w-5/6 h-full bg-blue-400 text-center">
              <small class="text-xs pb-2">EXPERT</small>
            </div>
          </div>
        </div>
        <div class="basis-1/2 mb-4">
          <p class="">CSS</p>
          <div class="rounded h-5 bg-gray-200 w-3/4">
            <div class="rounded w-4/6 h-full bg-blue-400 text-center">
              <small class="text-xs pb-2">VERY GOOD</small>
            </div>
          </div>
        </div>

        <div class="basis-1/2 mb-4">
          <p class="">VUE JS</p>
          <div class="rounded h-5 bg-gray-200 w-3/4">
            <div class="rounded w-4/6 h-full bg-blue-400 text-center">
              <small class="text-xs pb-2">VERY GOOD</small>
            </div>
          </div>
        </div>
        <div class="basis-1/2 mb-4">
          <p class="">TAILWIND CSS</p>
          <div class="rounded h-5 bg-gray-200 w-3/4">
            <div class="rounded w-5/6 h-full bg-blue-400 text-center">
              <small class="text-xs pb-2">EXPERT</small>
            </div>
          </div>
        </div>

        <div class="basis-1/2 mb-4">
          <p class="">NUXT JS</p>
          <div class="rounded h-5 bg-gray-200 w-3/4">
            <div class="rounded w-3/6 h-full bg-blue-400 text-center">
              <small class="text-xs pb-2">GOOD</small>
            </div>
          </div>
        </div>
      </div>
      <div class="basis-1/2">
        <div class="basis-1/2 mb-4">
          <p class="">PYTHON DJANGO</p>
          <div class="rounded h-5 bg-gray-200 w-3/4">
            <div class="rounded w-5/6 h-full bg-blue-400 text-center">
              <small class="text-xs pb-2">EXPERT</small>
            </div>
          </div>
        </div>

        <div class="basis-1/2 mb-4">
          <p class="">LEADERSHIP</p>
          <div class="rounded h-5 bg-gray-200 w-3/4">
            <div class="rounded w-4/6 h-full bg-blue-400 text-center">
              <small class="text-xs pb-2">VERY GOOD</small>
            </div>
          </div>
        </div>
        <div class="basis-1/2 mb-4">
          <p class="">COMMUNICATION</p>
          <div class="rounded h-5 bg-gray-200 w-3/4">
            <div class="rounded w-full h-full bg-blue-400 text-center">
              <small class="text-xs pb-2">EXCELLENT</small>
            </div>
          </div>
        </div>
        <div class="basis-1/2 mb-4">
          <p class="">FIRST AID</p>
          <div class="rounded h-5 bg-gray-200 w-3/4">
            <div class="rounded w-3/6 h-full bg-blue-400 text-center">
              <small class="text-xs pb-2">GOOD</small>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      pStyle: null,
      currStatus: false,
      progBar: false,
    };
  },
  mounted() {
    // this.pStyle = "hooray";
    // this.progBar = true;
    // document.getElementById("myDiv").focus();
    // this.currStatus = true;
  },
};
</script>

<style>
/* .progress {
  width: 50%;
  transition: width 2s ease;
}
.progress:focus {
  transform: translateZ(0) scale(1);
  width: 100%;
  height: 100%;
}
.hooray .progress {
  transform: translateZ(0) scale(1);
  width: 100%;
  height: 100%;
}
.test-prog {
  transition: opacity 1s ease;
} */
</style>
