<template>
  <div class="work absolute top-20 w-full mt-12">
    <div class="pl-10 w-full absolute pr-10">
      <div class="swiper">
        <div class="swiper-wrapper">
          <div class="swiper-slide">
            <div
              class="rounded border border-slate-500 shadow-2xl shadow-black m-auto w-1/2 p-10"
            >
              <div class="text-center m-auto w-1/2 pl-16">
                <img
                  src="@/assets/sammyb-review.jpg"
                  alt="Image"
                  class="rounded-full object-cover"
                  style="width: 150px; height: 150px"
                />
              </div>
              <div class="review-text mt-4 text-center">
                <h2 class="text-xl font-bold">SammyB</h2>
                <h3 class="text-lg">Software engineer</h3>
                <p class="mt-4 italic">
                  " Samuel is a great co-worker and a go getter. He works well under
                  pressure and always seeks to achieve his targets "
                </p>
              </div>
            </div>
          </div>
          <div class="swiper-slide">
            <div
              class="rounded border border-slate-500 shadow-2xl shadow-black m-auto w-1/2 p-10"
            >
              <div class="text-center m-auto w-1/2 pl-16">
                <img
                  src="@/assets/mary-review.jpg"
                  alt="Image"
                  class="rounded-full object-cover"
                  style="width: 150px; height: 150px"
                />
              </div>
              <div class="review-text mt-4 text-center">
                <h2 class="text-xl font-bold">Mary</h2>
                <h3 class="text-lg">Financial Analyst</h3>
                <p class="mt-4 italic">
                  " Samuel displays exemplary professionalism and is able to take on
                  challenges. He learns quickly and is an asset to any team. "
                </p>
              </div>
            </div>
          </div>
          <div class="swiper-slide">
            <div
              class="rounded border border-slate-500 shadow-2xl shadow-black m-auto w-1/2 p-10"
            >
              <div class="text-center m-auto w-1/2 pl-16">
                <img
                  src="@/assets/mike-review.jpg"
                  alt="Image"
                  class="rounded-full object-cover"
                  style="width: 150px; height: 150px"
                />
              </div>
              <div class="review-text mt-4 text-center">
                <h2 class="text-xl font-bold">Mike</h2>
                <h3 class="text-lg">C.E.O - Ezen Partners</h3>
                <p class="mt-4 italic">
                  " Samuel is a great employee and problem solver. He is quick to extend
                  his helping hand and makes a good team player "
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { Swiper, Autoplay, Pagination } from "swiper";
import "swiper/scss";
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
