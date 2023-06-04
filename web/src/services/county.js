import { BASE_URL } from "@/constants/config";
import { request } from "@/utils/request";

export const COUNTY_ENDPOINTS = {
    list: `${BASE_URL}api/county`,
    by_teryt: (teryt) => `${BASE_URL}api/county/${teryt}`,
    by_name: (name) => `${BASE_URL}api/county/name/${name}`,
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
}

export const countyService = new County()
