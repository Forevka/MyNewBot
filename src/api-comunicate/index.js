import axios from 'axios'

const AxiosInstance = axios.create({
  timeout: 1000
})

export default AxiosInstance
