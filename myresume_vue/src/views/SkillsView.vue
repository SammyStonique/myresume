<template>
  <div class="skills absolute top-20 pl-10 mt-36 w-full">
    <h1 class="text-4xl mb-6">Professional Skills</h1>
    <div class="flex w-full">
      <div class="basis-1/2">
        <div class="basis-1/2 mb-4">
          <p class="">HTML</p>
          <div
            :class="
              progBar
                ? 'rounded h-5 bg-gray-200 w-3/4 mr-4 '
                : 'rounded h-5 bg-gray-200 w-3/4 mr-4 py-1'
            "
          >
            <div
              :class="
                currStatus ? `${pStyle} rounded` : 'progress rounded h-3 bg-blue-400'
              "
              id="myDiv"
              tabindex="0"
            ></div>
          </div>
        </div>
        <div class="basis-1/2 mb-4">
          <p class="">CSS</p>
          <div
            :class="
              progBar
                ? 'rounded h-5 bg-gray-200 w-3/4 mr-4 '
                : 'rounded h-5 bg-gray-200 w-3/4 mr-4 py-1'
            "
          >
            <div
              :class="
                currStatus ? `${pStyle} rounded` : 'progress rounded h-3 bg-blue-400'
              "
            ></div>
          </div>
        </div>

        <div class="basis-1/2 mb-4">
          <p class="">VUE JS</p>
          <div class="rounded h-5 bg-gray-200 w-3/4 py-1">
            <div class="progress rounded h-3 w-3/4 bg-blue-400"></div>
          </div>
        </div>
        <div class="basis-1/2 mb-4">
          <p class="">TAILWIND CSS</p>
          <div class="rounded h-5 bg-gray-200 w-3/4 py-1">
            <div class="progress rounded h-3 w-3/4 bg-blue-400"></div>
          </div>
        </div>

        <div class="basis-1/2 mb-4">
          <p class="">NUXT JS</p>
          <div class="rounded h-5 bg-gray-200 w-3/4 py-1">
            <div class="progress rounded h-3 w-3/4 bg-blue-400"></div>
          </div>
        </div>
      </div>
      <div class="basis-1/2">
        <div class="basis-1/2 mb-4">
          <p class="">PYTHON DJANGO</p>
          <div class="rounded h-5 bg-gray-200 w-3/4 py-1">
            <div class="progress rounded h-3 w-3/4 bg-blue-400"></div>
          </div>
        </div>

        <div class="basis-1/2 mb-4">
          <p class="">LEADERSHIP</p>
          <div class="rounded h-5 bg-gray-200 w-3/4 py-1">
            <div class="progress rounded h-3 w-3/4 bg-blue-400"></div>
          </div>
        </div>
        <div class="basis-1/2 mb-4">
          <p class="">COMMUNICATION</p>
          <div class="rounded h-5 bg-gray-200 w-3/4 py-1">
            <div class="progress rounded h-3 w-3/4 bg-blue-400"></div>
          </div>
        </div>
        <div class="basis-1/2 mb-4">
          <p class="">FIRST AID</p>
          <div class="rounded h-5 bg-gray-200 w-3/4">
            <div class="rounded w-3/4 h-full bg-blue-400 text-center">
              <small class="text-xs">INTERMEDIATE</small>
            </div>
          </div>
        </div>
        <div class="test-prog basis-1/2 mb-4">
          <p class="">TEST</p>
          <div class="rounded h-5 bg-gray-200 w-3/4">
            <div class="rounded w-3/4 h-full bg-blue-400 text-center">
              <!-- <small class="text-xs">INTERMEDIATE</small> -->
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
    this.pStyle = "hooray";
    this.progBar = true;
    document.getElementById("myDiv").focus();
    // this.currStatus = true;
  },
};
</script>

<style>
.progress {
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
}
</style>
