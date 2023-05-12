/* eslint-disable camelcase */

export const state = () => ({
    files: [], 
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
    }
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

  }
  
