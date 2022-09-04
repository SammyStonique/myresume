<template>
  <div class="absolute top-0 w-full">
    <nav class="flex flex-row text-black py-3 px-5 w-full">
      <div class="basis-1/2">
        <p class="text-xl font-bold"><router-link to="/">OTIENO SAMUEL</router-link></p>
      </div>
      <div class="flex basis-1/2">
        <router-link
          to="/"
          class="mr-5 hover:border hover:border-x-0 hover:border-t-0 hover:border-b-2 hover:border-black hover:opacity-75 focus:border focus:border-x-0 focus:border-t-0 focus:border-b-2 focus:border-black"
          >Home</router-link
        >
        <router-link
          to="/about"
          class="mr-5 hover:border hover:border-x-0 hover:border-t-0 hover:border-b-2 hover:border-black hover:opacity-75 focus:border focus:border-x-0 focus:border-t-0 focus:border-b-2 focus:border-black"
          >About Me</router-link
        >
        <router-link
          to="/services"
          class="mr-5 hover:border hover:border-x-0 hover:border-t-0 hover:border-b-2 hover:border-black hover:opacity-75 focus:border focus:border-x-0 focus:border-t-0 focus:border-b-2 focus:border-black"
          >Services</router-link
        >
        <router-link
          to="/skills"
          class="mr-5 hover:border hover:border-x-0 hover:border-t-0 hover:border-b-2 hover:border-black hover:opacity-75 focus:border focus:border-x-0 focus:border-t-0 focus:border-b-2 focus:border-black"
          >My Skills</router-link
        >
        <router-link
          to="/work"
          class="mr-5 hover:border hover:border-x-0 hover:border-t-0 hover:border-b-2 hover:border-black hover:opacity-75 focus:border focus:border-x-0 focus:border-t-0 focus:border-b-2 focus:border-black"
          >My Work</router-link
        >
        <router-link
          to="/testimonials"
          class="mr-5 hover:border hover:border-x-0 hover:border-t-0 hover:border-b-2 hover:border-black hover:opacity-75 focus:border focus:border-x-0 focus:border-t-0 focus:border-b-2 focus:border-black"
          >Testimonials</router-link
        >
        <router-link
          to="/contacts"
          class="mr-5 hover:border hover:border-x-0 hover:border-t-0 hover:border-b-2 hover:border-black hover:opacity-75 focus:border focus:border-x-0 focus:border-t-0 focus:border-b-2 focus:border-black"
          >Contact Me</router-link
        >
      </div>
    </nav>
  </div>
</template>

<script>
export default {};
</script>

<style></style>
