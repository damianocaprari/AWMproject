import cookies from 'js-cookie'
import { setAuthToken, resetAuthToken } from '~/utils/auth'

export default function ({ $axios }) {
  const token = cookies.get('Authorization')

  if (token)
    setAuthToken($axios, token)
  else
    resetAuthToken($axios)
}
