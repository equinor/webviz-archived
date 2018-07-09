(function webvizDefaultThemeMenu() {
    const map = collection => fn => Array.prototype.map.call(fn, collection)
    const get = document.querySelector.bind(document)
    const getAll = document.querySelectorAll.bind(document)

    const addClass = className => element => {
        element.classList.add(className)
        return element
    }

    const removeClass = className => element => {
        element.classList.remove(className)
        return element
    }

    const toggleClass = className => element => {
        element.classList.toggle(className)
        return element
    }

    const hasClass = className => element => element.classList.contains(className)

    /* partials */

    const hasMenuItemClass = hasClass('menuItem')

    const addExpandedClass = addClass('expanded')
    const toggleExpandedClass = toggleClass('expanded')

    const addSubExpandedClass = addClass('subexpanded')
    const removeSubExpandedClass = removeClass('subexpanded')

    const addShowSubmenuClass = addClass('showSubMenu')
    const removeShowSubmenuClass = removeClass('showSubMenu')

    function findParentWithMenuItemClass(el) {
        if (el.parentNode) {
            if (hasMenuItemClass(el.parentNode)) return el.parentNode
            return findParentWithMenuItemClass(el.parentNode)
        }
        return null
    }

    function init() {
        const menuItems = getAll('.menuItem')
        const menuToggleBtn = get('#menuToggleBtn')
        const menuCloseBtn = get('#menuCloseBtn')
        const menuOpenBtn = get('#menuOpenBtn')

        if (menuItems.length < 1) {
            /* no menuitems - remove buttons and abort */
            const buttons = [menuToggleBtn]
            const hideItems = map((menuItem) => {
                menuItem.style.visibility = 'hidden'
            })
            hideItems(buttons)
            return
        }

        const header = get('#header')
        const subMenuOpenBtns = getAll('.subMenuOpenBtn')
        const subMenuCloseBtns = getAll('.subMenuCloseBtn')

        const resetSubMenus = map(removeShowSubmenuClass)

        const openSubMenu = map((btn) => {
            btn.addEventListener('click', (event) => {
                event.preventDefault()
                resetSubMenus(menuItems)
                addExpandedClass(header)
                addSubExpandedClass(header)
                addShowSubmenuClass(findParentWithMenuItemClass(event.target))
            })
        })

        const closeSubMenu = map((btn) => {
            btn.addEventListener('click', (event) => {
                event.preventDefault()
                removeSubExpandedClass(header)
                resetSubMenus(menuItems)
            })
        })

        menuToggleBtn.addEventListener('click', () => toggleExpandedClass(header))
        menuCloseBtn.addEventListener('click', () => toggleExpandedClass(header))
        menuOpenBtn.addEventListener('click', () => toggleExpandedClass(header))

        openSubMenu(subMenuOpenBtns)
        closeSubMenu(subMenuCloseBtns)
    }

    window.addEventListener('DOMContentLoaded', init)
}())
