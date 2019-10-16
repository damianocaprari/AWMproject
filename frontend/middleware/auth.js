export default function ({ store, redirect, route }) {
  console.log('middleware/auth.js export default function')
  const userIsLoggedIn = !!store.state.auth.user
  const urlRequiresAuth = /^\/admin(\/|$)/.test(route.fullPath)
  const urlRequiresNonAuth = /^\/login(\/|$)/.test(route.fullPath)
  console.log('middleware/auth.js route.fullPath', route.fullPath)
  console.log('middleware/auth.js userIsLoggedIn', userIsLoggedIn)
  console.log('middleware/auth.js urlRequiresAuth', urlRequiresAuth)
  console.log('middleware/auth.js urlRequiresNonAuth', urlRequiresNonAuth)
  if (!userIsLoggedIn && urlRequiresAuth) {
    console.log('middleware/auth.js redirect(/login)')
    return redirect('/login')
  }
  if (userIsLoggedIn && urlRequiresNonAuth) {
    console.log('middleware/auth.js redirect(/admin)')
    return redirect('/admin')
  }

  return Promise.resolve()
}
