import Vue from 'vue'
import Router from 'vue-router'
import Home from '../components/Home'
import Login from '../components/Login'
import Register from '../components/Register'
import Course from '../components/Course'
import Detail from '../components/Detail'
import Cart from '../components/Cart'
import Order from '../components/Order'
import Success from '../components/Success'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/home',
      name: 'Home',
      component: Home
    },
    {
      path: '/user/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/user/register',
      name: 'Register',
      component: Register
    },
    {
      path: '/courses',
      name: 'Course',
      component: Course
    },
    {
      path: '/courses/detail/:id', //:id，路由传参
      name: 'Detail',
      component: Detail
    },
    {
      path: '/cart', 
      name: 'Cart',
      component: Cart
    },
    {
      path: '/order', 
      name: 'Order',
      component: Order
    },
    {
      path: '/payments/result',
      name: "Success",
      component: Success,
    },
    
  ]
})
