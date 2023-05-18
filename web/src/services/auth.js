import { request } from "@/utils/request";
import { BASE_URL } from '@/constants/config';
import { ActiveUser } from "@/services/user";

export const AUTH_ENDPOINTS = {
  login: `${BASE_URL}auth/jwt/login`,
  logout: `${BASE_URL}auth/jwt/logout`,
  forgotPassword: `${BASE_URL}auth/forgot-password`,
  resetPassword: `${BASE_URL}auth/reset-password`,
  currentUser: `${BASE_URL}users/me`
};

class Auth {
  async forgotPassword(email) {
    return await request({
      url: AUTH_ENDPOINTS.forgotPassword,
      method: "POST",
      skipRedirect: true,
      body: {
        email,
      },
    });
  }

  async resetPassword({ password, token }) {
    return await request({
      url: AUTH_ENDPOINTS.resetPassword,
      method: "POST",
      skipRedirect: true,
      body: {
        password,
        token,
      },
    });
  }

  async login({ email, password }) {
    const formData = new FormData();
    formData.append("password", password);
    formData.append("username", email);
    const { data, res } = await request({
      url: AUTH_ENDPOINTS.login,
      method: "POST",
      skipRedirect: true,
      formData,
    });
    if (res.status === 200) {
      const accessToken = data.access_token;
      await ActiveUser.set({ ...data, accessToken });
    }
    return {
      data,
      res,
    };
  }
}

export const AuthService = new Auth();