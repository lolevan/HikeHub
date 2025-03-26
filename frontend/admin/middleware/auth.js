export default function ({ store, redirect, route }) {
  // Если пользователь не залогинен и пытается открыть что-то кроме /login
  if (!store.state.auth.loggedIn && route.path !== '/login') {
    return redirect('/login')
  }
}
