import { reactive, ref, watch } from 'vue'
import type { Ref } from 'vue'
import axios from 'axios'
import { authenticated } from '@/assets/script/utils'


export const isAuthenticated = ref(await authenticated(localStorage.getItem("auth") || ""));
export const collapse: Ref<string[]> = ref(['chat', 'ai']);
export const settings = reactive({
  password: localStorage.getItem("auth") || "",
  background: "https://s1.ax1x.com/2023/05/22/p9okyfs.jpg",
})

axios.defaults.headers.common['auth'] = settings.password;

watch(settings, () => {
  axios.defaults.headers.common['auth'] = settings.password;
})
