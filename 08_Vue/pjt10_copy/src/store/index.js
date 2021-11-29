import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    movieCards: [],
    toWatchs: [],
  },
  mutations: {
    LOAD_MOVIE_CARDS: function (state, results) {
      state.movieCards = results
    },
    CREATE_WISH: function (state, wishMovie) {
      state.toWatchs.push(wishMovie)
    },
    DELETE_WISH: function (state, wishMovie) {
      const index = state.toWatchs.indexOf(wishMovie)

      state.toWatchs.splice(index, 1)
    },
    UPDATE_WISH_STATUS: function (state,wishMovie) {
      state.toWatchs = state.toWatchs.map(toWatch => {
        if (toWatch === wishMovie) {
          return {
            ...toWatch,
            isWatched: !toWatch.isWatched
          }
        } else {
          return toWatch
        }
      })
    }
  },
  actions: {
    LoadMovieCards: function (context) {
      axios({
        method: 'get',
        // url: 'https://api.themoviedb.org/3/movie/top_rated',
        // url: 'https://api.themoviedb.org/3/movie/now_playing',
        url: 'https://api.themoviedb.org/3/movie/51608/similar',
        params: {
          api_key: '37178a9c5b2c52a9b92ab119386918ce',
          language: 'ko-KR',
        }
      })
        .then((res) => {
          console.log(res.data.results)
          context.commit('LOAD_MOVIE_CARDS', res.data.results)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    createWishList: function ({ commit }, wishMovie) {
      commit('CREATE_WISH', wishMovie)
    },
    deleteList: function ({ commit }, wishMovie) {
      commit('DELETE_WISH', wishMovie)
    },
    updateListStatus: function ({ commit }, wishMovie) {
      commit('UPDATE_WISH_STATUS', wishMovie)
    }
  },
  modules: {
  }
})
