import { BASE_URL } from "@/constants/config";
import { request } from "@/utils/request";

export const POSITION_ENDPOINTS = {
    list: `${BASE_URL}api/position`,
};

class Positions {
    async getPositions() {
        const { data } = await request({
            url: POSITION_ENDPOINTS.list,
        });
        return data;
    }
}

export const positionService = new Positions();