import axios from 'axios'

const AxiosInstance = axios.create({
  timeout: 1000,
  headers: {'Content-Type': 'text/json'}
})

export default AxiosInstance
