import axios from "axios";


const bkClient = axios.create({baseURL: import.meta.env.VITE_APP_BACKEND_BASE_URL});

bkClient.interceptors.request.use(config => {
    return config;
}, error => {
    console.log(error);
    throw(error);
});

bkClient.interceptors.response.use(
    response => {
        return response;
    },
    error => {
        console.log(error)
    }
);

export default bkClient;