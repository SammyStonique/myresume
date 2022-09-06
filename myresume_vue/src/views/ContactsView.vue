<template>
  <div class="contacts absolute top-20 w-full">
    <h1 class="text-4xl mb-6 pl-20">Contact</h1>
    <div class="flex flex-row backdrop-blur-md">
      <div class="basis-1/3 px-10">
        <p class="mb-3">
          <i class="fa fa-phone mr-2 text-black/75" aria-hidden="true"></i>
          <small class="text-lg font-semibold text-black/75">+254-717-423-651</small>
        </p>
        <p class="mb-9">
          <i class="fa fa-envelope-o mr-2 text-black/75" aria-hidden="true"></i
          ><small class="text-lg font-semibold text-black/75"
            >otisamueloti@gmail.com</small
          >
        </p>
        <form action="" @submit.prevent="giveFeedback">
          <input
            type="text"
            placeholder="Name"
            class="rounded w-full h-10 mb-4 focus:outline-0 pl-4"
            v-model="name"
          />
          <input
            type="text"
            placeholder="Email"
            class="rounded w-full h-10 mb-4 focus:outline-0 pl-4"
            v-model="email"
          />
          <textarea
            placeholder="Message"
            cols="40"
            rows="5"
            class="rounded w-full mb-6 focus:outline-0 pl-4"
            v-model="message"
          ></textarea>
          <div class="" v-if="errors.length">
            <p style="color: red" v-for="error in errors" v-bind:key="error">
              {{ error }}
            </p>
          </div>
          <button
            class="rounded w-full h-10 bg-slate-600 text-white font-bold hover:bg-white/50 hover:text-slate-600"
            type="submit"
          >
            SEND
          </button>
        </form>
      </div>
      <div class="basis-2/3 pl-10">
        <iframe
          src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3258.698786404983!2d36.819033504790234!3d-1.2806192853698508!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x182f10d4bf65dc8f%3A0xe534a1f3b7f619!2sTwiga%20Towers%2C%20Nairobi!5e0!3m2!1sen!2ske!4v1662305788805!5m2!1sen!2ske"
          width="800"
          height="450"
          style="border: 0"
          allowfullscreen=""
          loading="lazy"
          referrerpolicy="no-referrer-when-downgrade"
        ></iframe>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      name: "",
      email: "",
      message: "",
      errors: [],
    };
  },
  methods: {
    giveFeedback() {
      this.errors = [];
      if (this.email === "" && this.name === "" && this.message === "") {
        this.errors.push("Please fill in the details");
        this.$toast.error("Please Enter Your Details", {
          duration: 5000,
          position: "top",
        });
      } else {
        if (this.email === "") {
          this.errors.push("Please enter your email");
        }
        if (this.name === "") {
          this.errors.push("Please enter your name");
        }
        if (this.message === "") {
          this.errors.push("Please give your feedback");
        }
      }
      if (!this.errors.length) {
        let formData = {
          name: this.name,
          email: this.email,
          message: this.message,
        };
        this.axios
          .post("/api/v1/employer-feedback/", formData)
          .then((response) => {
            console.log(response);
            this.$toast.success("Message Sent", {
              duration: 5000,
              position: "top",
            });
            this.name = "";
            this.email = "";
            this.message = "";
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
  },
};
</script>
