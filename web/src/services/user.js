import { AUTH_ENDPOINTS } from "./auth";
import { users } from "@/services/users";
import { request } from "@/utils/request";

const userKey = "user";
const accessTokenKey = 'access_token';

class User {
  user = null;

  get() {
    if (this.user) {
      return this.user;
    }
    const savedUser = localStorage.getItem(userKey);
    if (savedUser) {
      this.user = JSON.parse(savedUser);
      return this.user;
    }
  }

  async clear() {
    this.user = null;
    const token = this.getToken();
    localStorage.removeItem(userKey);
    localStorage.removeItem(accessTokenKey);
    if (token && token.length)
    await request({
      url: AUTH_ENDPOINTS.logout,
      query: {
        token,
      },
      method: "POST",
    });
  }

  async set(value) {
    localStorage.setItem(userKey, JSON.stringify(value));
    if (value.accessToken) {
      localStorage.setItem("access_token", value.accessToken);
    }
    const userInfo = await users.getActiveUserInfo();
    const userData = { ...userInfo, ...value };
    localStorage.setItem(userKey, JSON.stringify(userData));
    this.user = userData;
  }

  getToken() {
    return this.get()?.accessToken;
  }

  setToken(token) {
    return this.set({ accessToken: token });
  }

  isAdministrator() {
    return this.get()?.is_superuser;
  }

  async getMeta() {
    const { data } = await request({
      url: AUTH_ENDPOINTS.currentUser,
    });

    return data;
  }

  getLanguage() {
    return this.get()?.language;
  }

  setLanguage(language) {
    language = language.toLowerCase()
    if (language !== this.getLanguage()) {
      return this.set({...this.get(), language});
    }
  }
}

export const ActiveUser = new User();