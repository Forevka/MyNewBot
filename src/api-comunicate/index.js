import axios from 'axios'

const AxiosInstance = axios.create({
  baseURL: 'https://forevka.serveo.net',
  timeout: 1000,
  headers: {'Content-Type': 'text/json'}
})

export default AxiosInstance
