/* eslint-disable camelcase */

export const state = () => ({
    files: [],
    toasts: [],
    showCreateProject: false
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
    createProject(state) {
      state.showCreateProject = !state.showCreateProject
    },
    // addNewUploadFile(state, { id, file }) {
    //   console.log(id, file)
    //   const newFile = state.files.find((item) => item.id === id)
    //   newFile.upload = file.name

    // },
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
    createProject({ commit }) {
      commit('createProject')
    },
    // addNewUploadFile({ commit }, data) {
    //   commit('addNewUploadFile', { id: data.id, file: data.file })
    // }
  }
  
