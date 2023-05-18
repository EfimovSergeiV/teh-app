/* eslint-disable camelcase */

export const state = () => ({
    projects: [],
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
    addProject(state, project) {
      state.projects.push(project)
    },
    cleanListProjects(state) {
      state.projects = []
    },
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
    addProjects({ commit }, projects) {
      commit('cleanListProjects')
      for (const project in projects) {
        setTimeout(function() {
          commit('addProject', projects[project])
        }, project * 50)
      }
    },
    updateProjects({ commit }, location) {
      this.$axios.$get('s/projects/getall/').then((resp) => {
        commit('cleanListProjects')
        for (const project in resp) {
          setTimeout(function() {
            commit('addProject', resp[project])
          }, project * 50);
        }  
      }).catch(() => {})
    },
    updateProject({ commit }, id) {
      this.$axios.$get(`s/projects/getone/${id}/`).then((resp) => {

        commit('cleanListFiles')
        for (const file in resp.project_files) {
          setTimeout(function() {
            commit('addFile', resp.project_files[file])
          }, file * 500);
        }  
      }).catch(() => {})
    },
    addFiles({ commit }, files ) {
      commit('cleanListFiles')
      for (const file in files) {
        setTimeout(function() {
          commit('addFile', files[file])
        }, file * 100);
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
  
