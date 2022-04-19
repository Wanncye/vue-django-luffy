import Vue from 'vue'

import Vuex from 'vuex'

Vue.use(Vuex);

export default new Vuex.Store({
  state:{
    cart_length: 0,
  },
  // 数据操作方法,类似vue里面的methods
  mutations: {
    add_cart(state,length,){
      state.cart_length = length;
    }
  },
})
