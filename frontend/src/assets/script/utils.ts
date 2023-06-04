import axios from 'axios'

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


export async function authenticated(password: string): Promise<boolean> {
  try {
    const resp = await axios.get("api/auth", {
      headers: {
        auth: password,
      }
    })
    return resp.data.status;
  } catch (e) {
    console.log(e);
    return false;
  }
}
