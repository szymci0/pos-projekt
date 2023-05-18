import { BASE_URL } from "@/constants/config";
import { request } from "@/utils/request";

export const USER_ENDPOINTS = {
  list: `${BASE_URL}api/users/`,
  register: `${BASE_URL}auth/register`,
  me: `${BASE_URL}users/me`,
  detail: (id) => `${BASE_URL}users/${id}`,
};

class Users {
  async getActiveUserInfo() {
    const { data } = await request({
      url: USER_ENDPOINTS.me,
    });
    return data;
  }

  async getUser(id) {
    const { data } = await request({
      url: USER_ENDPOINTS.detail(id),
    });
    return data;
  }

  async createUser(userData) {
    const { data } = await request({
      url: USER_ENDPOINTS.register,
      method: "POST",
      body: userData,
    });
    return data;
  }

  async editUser(id, userData) {
    const { data } = await request({
      url: USER_ENDPOINTS.detail(id),
      method: "PATCH",
      body: userData,
    });
    return data;
  }

  async deleteUser(id) {
    return await request({
      url: USER_ENDPOINTS.detail(id),
      method: "DELETE",
    });
  }
}

export const users = new Users();