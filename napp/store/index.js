/* eslint-disable camelcase */

export const state = () => ({
    files: [],
    toasts: [
      // {'id': 1, 'msg': "Архивы с паролем запрещены", 'type': 'error'},
      // {'id': 2, 'msg': "Не выбран файл", 'type': 'error'},
      // {'id': 3, 'msg': null, 'type': 'success'},
    ],
  })
  
//   export const getters = {
//     getCounter(state) {
//       return state.counter
//     }
//   }

  export const mutations = {
    addFile(state, file) {
      state.files.push(file)
    },
    cleanListFiles(state) {
      state.files = []
    },
    addToast(state, toast) {
      state.toasts.push(toast)
    },
    hideToast(state, id) {
      const toast = state.toasts.findIndex((item) => item.id === id)
      state.toasts.splice(toast, 1)
    },
    clearToast(state) {
      state.toasts.shift()
    },
  }
  
  export const actions = {
    addFiles({ commit }, files ) {
      commit('cleanListFiles')
      for (const file in files) {
        setTimeout(function() {
          commit('addFile', files[file])
        }, file * 50);
      }  
    },
    addToast({ commit }, toast ) {
      /// Сделать присваивание ID
      commit('addToast', toast)
  
      setTimeout(() => {
        commit('clearToast')
      }, "8000" )
  
    },
    hideToast({ commit }, toast ) {
      commit('hideToast', toast)
    },
  }
  
