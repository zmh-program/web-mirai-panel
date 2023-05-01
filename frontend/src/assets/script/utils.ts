import { ref } from 'vue'
import type { Ref } from 'vue'

export class Loader {
  public ref: Ref<boolean>;
  protected timeout: undefined | number;
  constructor() {
    this.ref = ref(false);
    this.timeout = undefined;
  }
  public trigger() {
    const _this = this;
    this.timeout = setTimeout(() => _this.ref.value = true, 250);
  }

  public close() {
    if (this.ref.value && typeof this.timeout !== undefined) clearTimeout(this.timeout);
    this.ref.value = false;
  }
}

export function Message(type: "success" | "warning" | "error" | "info", message: string) {
  // @ts-ignore
  // eslint-disable-next-line no-undef
  ElMessage({
    message: message,
    type: type,
  });
}