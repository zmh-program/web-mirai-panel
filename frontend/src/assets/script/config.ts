import { reactive, ref } from 'vue'
import type { Ref } from 'vue'


export const collapse: Ref<string[]> = ref(['chat', 'ai']);
export const settings = reactive({
  password: localStorage.getItem("password") || "",
  background: "https://s1.ax1x.com/2023/05/22/p9okyfs.jpg",
})
