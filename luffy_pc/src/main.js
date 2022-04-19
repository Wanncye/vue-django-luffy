// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router/index'
import setting from "./setting"
import axios from 'axios'; // 从node_modules目录中导入包
// 允许ajax发送请求时附带cookie
axios.defaults.withCredentials = false;

Vue.prototype.$axios = axios; // 把对象挂载vue中

Vue.config.productionTip = false

Vue.prototype.$settings = setting

//导入css初始化文件
import '../static/css/reset.css'

// elementUI 导入
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
// 调用插件
Vue.use(ElementUI);

// vue-video-player 视频播放器
require('video.js/dist/video-js.css');
require('vue-video-player/src/custom-theme.css');
import VideoPlayer from 'vue-video-player'
Vue.use(VideoPlayer);

import store from "./store/index"

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
