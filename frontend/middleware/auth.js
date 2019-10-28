export default function ({ store, redirect, route }) {
  const userIsLoggedIn = !!store.state.auth.user
  const urlRequiresAuth = /^\/account\/?$/.test(route.fullPath)
  const urlRequiresNonAuth = /(^\/account\/login\/?$)|(^\/account\/register\/?$)/.test(route.fullPath)
  //console.log('middleware/auth.js route.fullPath', route.fullPath)
  //console.log(`middleware/auth.js userIsLoggedIn ${userIsLoggedIn} | urlRequiresAuth ${urlRequiresAuth} | urlRequiresNonAuth ${urlRequiresNonAuth}`)
  if (!userIsLoggedIn && urlRequiresAuth) {
    //console.log('middleware/auth.js redirect(/account/login)')
    return redirect('/account/login')
  }
  if (userIsLoggedIn && urlRequiresNonAuth) {
    //console.log('middleware/auth.js redirect(/)')
    return redirect('/')
  }

  return Promise.resolve()
}
