import { BASE_URL } from "@/constants/config";
import { request } from "@/utils/request";

export const COUNTY_ENDPOINTS = {
    list: `${BASE_URL}api/county`,
    by_teryt: (teryt) => `${BASE_URL}api/county/${teryt}`,
    by_name: (name) => `${BASE_URL}api/county/name/${name}`,
    users: `${BASE_URL}api/county/users`,
}

class County {
    async getCountiesList() {
        const { data } = await request({
            url: COUNTY_ENDPOINTS.list
        });
        return data
    }

    async getCountyByTeryt(teryt) {
        const { data } = await request({
            url: COUNTY_ENDPOINTS.by_teryt(teryt)
        });
        return data
    }

    async addUser(teryt, user) {
        const { res } = await request({
            url: COUNTY_ENDPOINTS.users + "/add",
            method: "PATCH",
            body: {
                "teryt": teryt,
                "user": user
            }
        });
        return res
    }

    async getUsers() {
        const {res, data} = await request({
            url: COUNTY_ENDPOINTS.users + "/list",
        });
        if (res.status !== 200) {
            return alert("Error while fetching the data!")
        }
        return data;
    }
}

export const countyService = new County()
