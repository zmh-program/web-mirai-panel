export const notify = (option: Record<string, any>): void => {
  // @ts-ignore
  // eslint-disable-next-line no-undef
  ElNotification(option);
}

export const message = (option: Record<string, any>): void => {
  // @ts-ignore
  // eslint-disable-next-line no-undef
  ElMessage(option);
}
