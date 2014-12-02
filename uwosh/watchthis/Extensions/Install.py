from plone.app.contentrules.browser.traversal import RuleNamespace
from BTrees.OOBTree import OOBTree
from Products.CMFCore.utils import getToolByName

def install(portal):
    setup_tool = getToolByName(portal, 'portal_setup')
    setup_tool.runAllImportStepsFromProfile('profile-uwosh.watchthis:default')
    ##add pageDictionary if not already there
    if portal.getAttribute('pageDictionary') is None:
        portal.pageDictionary = OOBTree()
        portal.pageDictionary.insert('page', 'user')
    return "Ran all import steps."

def uninstall(portal):
    setup_tool = getToolByName(portal, 'portal_setup')
    ##setup_tool.runAllImportStepsFromProfile('profile-uwosh.watchthis:uninstall')    
    return "Ran all uninstall steps."
    ##delete pageDictionary

