<template>
  <div class="home absolute top-20 pl-10 mt-36">
    <div>
      <p class="text-4xl font-bold opacity-100 mb-8">Hello!</p>
      <p class="text-2xl font-bold opacity-100 mb-4">I'm Otieno Samuel</p>
      <p class="text-2xl font-bold opacity-100 mb-4 capitalize">
        A passionate and enthusiastic Full Stack Web Developer
      </p>
      <button
        class="rounded bg-slate-600 p-3 mr-5 text-white font-bold hover:bg-white/50 hover:text-slate-600"
      >
        <a :href="`${publicPath}Curriculum_Vitae.pdf`" download="Curriculum_Vitae">
          Download CV</a
        >
      </button>

      <router-link
        to="/contacts"
        class="rounded bg-slate-600 p-3 text-white font-bold hover:bg-white/50 hover:text-slate-600"
        >Hire Me</router-link
      >

      <div class="flex mt-5">
        <a
          href="https://www.facebook.com/profile.php?id=100070767246388"
          target="blank"
          class="mr-5 bg-slate-400 px-2 rounded transition ease-in-out delay-150 hover:translate-x-1 hover:scale-110 duration-300 hover:text-white"
          ><i class="fa fa-facebook text-2xl" aria-hidden="true"></i
        ></a>
        <a
          href="https://twitter.com/SammyB06774908"
          target="blank"
          class="mr-5 bg-slate-400 px-2 rounded transition ease-in-out delay-150 hover:translate-x-1 hover:scale-110 duration-300 hover:text-white"
          ><i class="fa fa-twitter text-2xl" aria-hidden="true"></i
        ></a>
        <a
          href="https://www.linkedin.com/in/samuel-otieno-a41a36198/"
          target="blank"
          class="mr-5 bg-slate-400 px-2 rounded transition ease-in-out delay-150 hover:translate-x-1 hover:scale-110 duration-300 hover:text-white"
          ><i class="fa fa-linkedin-square text-2xl" aria-hidden="true"></i
        ></a>
        <a
          href="https://github.com/SammyStonique"
          target="blank"
          class="mr-5 bg-slate-400 px-2 rounded transition ease-in-out delay-150 hover:translate-x-1 hover:scale-110 duration-300 hover:text-white"
          ><i class="fa fa-github text-2xl" aria-hidden="true"></i
        ></a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HomeView",
  data() {
    return {
      publicPath: process.env.BASE_URL,
    };
  },
};
</script>
