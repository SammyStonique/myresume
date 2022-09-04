<template>
  <div class="relative">
    <div class="overflow-y-hidden h-screen w-full z-10">
      <img class="opacity-50" src="@/assets/profile.jpg" alt="My Pic" />
    </div>
    <Header />
    <router-view />
  </div>
</template>

<script>
import Header from "./components/Header.vue";
export default { components: { Header } };
</script>

<style></style>
