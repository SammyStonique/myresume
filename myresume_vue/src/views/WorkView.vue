<template>
  <div class="work absolute top-20 w-full mt-12">
    <div class="pl-10 w-full absolute pr-10">
      <div class="swiper">
        <div class="swiper-wrapper">
          <div class="swiper-slide">
            <h3 class="text-xl font-bold mb-2">Gee Collections</h3>
            <div class="flex flex-row shadow-2xl shadow-slate-800">
              <div class="basis-1/2 shadow-2xl shadow-slate-800">
                <img
                  src="@/assets/gee-collections.png"
                  alt="Slider Image"
                  style="width: 800px; height: 400px"
                />
              </div>
              <div class="basis-1/2 pl-2 pt-10 shadow-2xl shadow-slate-800">
                <p class="text-lg text-black/75 font-semibold mb-4">
                  Gee Collections is a fully functional e-commerce website that has been
                  intergrated with Lipa Na Mpesa, PayPal, Email and SMS. Users can create
                  an account, log in, search for products, add items to their wishlist or
                  cart.
                </p>
                <p class="text-lg text-black/75 font-semibold mb-4">
                  They can then proceed to checkout and either use M-Pesa or PayPal to
                  make payment after which they receive an email and SMS about their
                  order. They can also view their order history.
                </p>
                <p class="text-lg text-black/75 font-semibold">
                  The system was built using HTML, CSS, VueJS and Django.
                </p>
              </div>
            </div>
          </div>
          <div class="swiper-slide">
            <h3 class="text-xl font-bold mb-2">Ezen Events</h3>
            <div class="flex flex-row shadow-2xl shadow-slate-800">
              <div class="basis-1/2 pl-2 pt-10 shadow-2xl shadow-slate-800">
                <p class="text-lg text-black/75 font-semibold mb-4">
                  Ezen Events is an events management system that has been intergrated
                  with Email and SMS. Users can create an account, log in, create events,
                  create a guests list and invite guests to their events. Event organizers
                  can either approve or deny applications for private events.
                </p>
                <p class="text-lg text-black/75 font-semibold mb-4">
                  Individuals can also view all the available events and make
                  applications/reservations for invites only events.
                </p>
                <p class="text-lg text-black/75 font-semibold">
                  The system was built using HTML, CSS, NuxtJS and Django.
                </p>
              </div>
              <div class="basis-1/2 shadow-2xl shadow-slate-800">
                <img
                  src="@/assets/ezenevents.png"
                  alt="Slider Image"
                  style="width: 800px; height: 400px"
                />
              </div>
            </div>
          </div>
          <!-- <div class="swiper-slide">
            <img
              src="@/assets/blog.png"
              alt="Slider Image"
              style="width: 500px; height: 400px"
            />
          </div>
          <div class="swiper-slide">
            <img
              src="@/assets/music-player.png"
              alt="Slider Image"
              style="width: 500px; height: 400px"
            />
          </div> -->
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { Swiper, Autoplay, Pagination } from "swiper";
import "swiper/scss";
import "swiper/scss/navigation";
export default {
  components: {
    Swiper,
  },
  mounted() {
    Swiper.use(Autoplay, Pagination);
    const swiper = new Swiper(".swiper", {
      direction: "horizontal",
      loop: true,
      speed: 700,
      modules: [Autoplay, Pagination],
      autoplay: {
        delay: 5000,
        disableOnInteraction: false,
        pauseOnMouseEnter: true,
        el: ".swiper-slide",
      },
      on: {
        init() {
          this.el.addEventListener("mouseenter", () => {
            this.autoplay.stop();
          });
          this.el.addEventListener("mouseleave", () => {
            this.autoplay.start();
          });
        },
      },
    });
    swiper.autoplay.start();
  },
};
</script>

<style>
.swiper {
  margin-left: auto;
  margin-right: auto;
  position: relative;
  overflow: hidden;
  list-style: none;
  padding: 0;
  z-index: 1;
}
</style>
