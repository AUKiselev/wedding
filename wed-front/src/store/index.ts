import { defineStore } from "pinia";
import api from '@/api';

export const useStore = defineStore({
  id: "store",
  state: () => ({
    userForm: {
      slug: '',
      will_come: null,
      solo: null,
      have_car: false,
      transfer_to: undefined as undefined | boolean,
      transfer_from: undefined as undefined | boolean
    },
    isShowModal: false
  }),
  actions: {
    async sendForm() {
      try {
        const response = await api.post('/claims/', this.userForm);

        this.showModal();
        
        return response;
      } catch(e) {
        console.error(e);

        return e;
      }
    },
    showModal() {
      this.isShowModal = true,
      setTimeout(() => {
        this.isShowModal = false;
      }, 2000)
    }
  },
});