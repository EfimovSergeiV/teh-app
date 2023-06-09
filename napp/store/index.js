/* eslint-disable camelcase */

export const state = () => ({
    cts: [],
    selectedCategory: null,
    projects: [],
    files: [],
    toasts: [],
    historical_files: [],
    showCreateProject: false,
    showSearchForm: false,
    projectAuthors: [],
    searchResult: [],
    selectedAssembly: null,
    project_assembly: [],
    storageSpace: {},

  })
  
  export const getters = {
    isAuthenticated(state) {
      return state.auth.loggedIn
    },
    loggedInUser(state) {
      return state.auth.user
    }
  }

  export const mutations = {
    /// Категории
    selectCategory(state, id) {
      state.selectedCategory = id
    },
    addCategory(state, cts) {
      state.cts = cts
    },
    /// Проекты
    addProject(state, project) {
      state.projects.push(project)
    },
    cleanListProjects(state) {
      state.projects = []
    },
    /// Сборки
    cleanListAssembly(state) {
      state.project_assembly = []
    },
    addAssembly(state, assembly) {
      state.project_assembly.push(assembly)
    },
    selectAssembly(state, assembly) {
      /// Очистка отображений файлов и версий? потому что не выбрана сборка
      if (assembly) {
        state.selectedAssembly = assembly
      } else {
        state.selectedAssembly = assembly
        state.files = []
        state.historical_files = []
      }
        
    },

    /// Файлы и архивы
    addFile(state, file) {
      state.files.push(file)
    },
    cleanListFiles(state) {
      state.files = []
    },
    cleanHistoryFiles(state) {
      state.historical_files = []
    },
    addHistoryFile(state, file) {
      state.historical_files.push(file)
    },
    /// Уведомления
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
    /// Формочки (отображение)
    createProjectForm(state) {
      state.showCreateProject = !state.showCreateProject
    },
    searchForm(state) {
      state.showSearchForm = !state.showSearchForm
    },
    addAllAuthors(state, authors) {
      state.projectAuthors = authors
    },
    
    // addNewUploadFile(state, { id, file }) {
    //   console.log(id, file)
    //   const newFile = state.files.find((item) => item.id === id)
    //   newFile.upload = file.name

    // },
    updateStorageSpace(state, data) {
      state.storageSpace = data
    }
  }
  
  export const actions = {
    // Категории
    addCategory({commit}, cts) {
      commit('addCategory', cts)
    },
    selectCategory({commit}, id) {
      commit('selectCategory', id )
    },

    /// Проекты
    addProjects({ commit }, projects) {
      commit('cleanListProjects')
      for (const project in projects) {
        setTimeout(function() {
          commit('addProject', projects[project])
        }, project * 50)
      }
    },
    updateProjects({ commit }, id) {
      commit('cleanListProjects')
      this.$axios.$get(`s/projects/${id}/`).then((resp) => {
        commit('cleanListProjects')
        for (const project in resp) {
          setTimeout(function() {
            commit('addProject', resp[project])
          }, project * 50);
        }  
      }).catch(() => {})
    },
    updateProject({ commit }, id) {
      commit('cleanListFiles')
      this.$axios.$get(`s/projects/getone/${id}/`).then((resp) => {
        for (const file in resp.project_files) {
          setTimeout(function() {
            commit('addFile', resp.project_files[file])
          }, file * 100);
        }  
      }).catch(() => {})
    },

    /// Сборки и узлы
    addAssembly({ commit }, files ) {
      commit('cleanListAssembly')
      for (const file in files) {
        setTimeout(function() {
          commit('addAssembly', files[file])
        }, file * 100);
      }  
    },

    /// Добавление отображения последнего добавленного сборки
    /// МБ переименовать как Latest
    updateAssembly({commit}, id){
      // commit('cleanListAssembly')
      this.$axios.$get(`s/projects/getone/${id}/`).then((resp) => {
        if (resp.project_assembly.length > 1) {
          commit('addAssembly', resp.project_assembly.at(-1)) 
        } else {
          commit('addAssembly', resp.project_assembly[0]) 
        }
        
      }).catch(() => {})
    },
    selectAssembly({commit}, assembly) {
      commit('selectAssembly', assembly )
    },

    /// Файлы\Архивы
    updateFiles({ commit, state }, id) {
      commit('cleanListFiles')
      this.$axios.$get(`s/projects/get-latest-files/${state.selectedAssembly.id}/`).then((resp) => {
        for (const file in resp) {
          setTimeout(function() {
            commit('addFile', resp[file])
          }, file * 100);
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

    addHistoryFiles({ commit }, files) {
      commit('cleanHistoryFiles')
      for (const file in files) {
        setTimeout(function() {
          commit('addHistoryFile', files[file])
        }, file * 100);
      }
    },

    updateHistoryFiles({ commit }, id) {
      commit('cleanHistoryFiles')
      this.$axios.$get(`s/projects/get-history-files/${id}/`).then((resp) => {

        for (const file in resp) {
          setTimeout(function() {
            commit('addHistoryFile', resp[file])
          }, file * 200);
        }  

      }).catch(() => {})
    },

    updateStorageSpace({ commit }, data) {
      commit('updateStorageSpace', data)
    },


    /// Уведомления
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

    /// Формочки
    createProjectForm({ commit }) {
      commit('createProjectForm')
    },
    searchForm({ commit }) {
      commit('searchForm')
    },

    addAllAuthors({ commit }) {
      this.$axios.$get(`s/search/`).then((resp) => {

            commit('addAllAuthors', resp)

      }).catch(() => {})
    },
    // addNewUploadFile({ commit }, data) {
    //   commit('addNewUploadFile', { id: data.id, file: data.file })
    // }
  }
  
