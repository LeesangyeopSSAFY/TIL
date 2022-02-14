const menuData = require('@/views/main/menu.json')
const Tchr_menuData = require('@/views/main/Tchr_menu.json')
export function setPlatform (state, isDesktop) {
  state.isDesktopPlatform = isDesktop
}

export function setMenuActive (state, index) {
	console.log('setMenuActive',index)
	const keys = Object.keys(state.menus)
	state.activeMenu = keys[index]
}

export function setMenuActiveMenuName (state, menuName) {
	state.activeMenu = menuName
}

export function registerUser (state, id) {
	state.userid = id
}
export function removeUser (state, id) {
	state.userid = ''
}
export function logout (state) {
	state.authtoken = ''
}
export function jwtToken (state,jwt) {
	state.authtoken = jwt
}
export function checkTeacher (state) {
  state.whetherTchr = true
  state.menus = Tchr_menuData
}
export function checkStudent (state) {
  state.whetherTchr = false
  state.menus = menuData
}
export function changeClassName (state, className) {
  state.curClassName = className
}
export function changeClassId (state, classId) {
  state.curClassId = classId
}
