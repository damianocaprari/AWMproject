import axios from 'axios'
import { baseURL } from '~/config'
import cookies from 'js-cookie'
import { setAuthToken, resetAuthToken } from '~/utils/auth'

axios.defaults.baseURL = baseURL

console.log('api/init.js')

const token = cookies.get('Authorization')
if (token) setAuthToken(token)
else resetAuthToken()
