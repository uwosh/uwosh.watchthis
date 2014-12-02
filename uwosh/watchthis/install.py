from Products.CMFCore.utils import getToolByName
from plone.app.contentrules.browser.traversal import RuleNamespace
from BTrees.OOBTree import OOBTree #object keys, any object, BTree structure for faster transactions
from browser.watchOrStopWatching import WatchThis
#from persistent.dict import PersistentDict

def import_all(context):

    site = context.getSite()
    if 'pageDictionary' not in site.objectIds():
        pageDictionary = OOBTree()
        pageDictionary.insert('page','users')##make users a list?


#if site.getAttribute('pageDictionary') is None:
#        rule.pageDictionary = PersistentDict() use Btree, otherwise every time an item is changed, the entire dict will be versioned
#        self.pageDictionary = OOBTree()
#        self.pageDictionary.insert('page', 'users')##correct?


#    watchThisView = WatchThis(self.context, self.request)
#    if watchThisView.getAttribute('docDisplayTitle') is None:
#        watchThisView.docDisplayTitle = "Watch This Object"

#     actionsTool = getToolByName(self, 'portal_actions', None)
#     if actionsTool is not None:
#         for action in actionsTool.listActions():
#             if action.getId() == 'watchthis':
#                 break 
#         else:
#             actionsTool.addAction('watchthis',
#                 name='Watch This Page',
#                 action='''string:$object_url/WatchThis''',
#                 condition='',
#                 permission='',
#                 category='document_actions',
#                 visible=1,
#                 )

#    memberDataTool = getToolByName(self, 'portal_memberdata', None)
#
#    if memberDataTool is not None:
#        for property in memberDataTool.propertyIds():
#            if property.getId() == 'watchedPages':
#                break
#
#        else:
#            memberDataTool.manage_addProperty('watchedPages', 'Watch This Page', 'lines')




#    if 'watchedPages' not in pmd.propertyIds():
#    pmd.manage_addProperty('watchedPages', 'Watch This Page', 'lines')


#    site = context.getSite()
#    portal_actions = site.portal_actions

#    portal_actions = getToolByName(self.context, 'portal_actions')
#    PAObjectIds = portal_actions.objectIds_d()#this line

#    if 'watchthis' not in portal_actions.objectIds(): portal_actions.listActions()
#    for objectIds in PAObjectIds:
#        if objectIds == 'watchthis':
#            break
#        elif objectIds != 'watchthis':

#    if 'watchthis' not in PAObjectIds:
#    portal_actions.addAction('watchthis','Watch This','string:$object_url/watchOrStopWatching','','','document_actions',1)
#    portal_actions.changeActions()

##add Watched Pages Property To Members

#    pmd = site.portal_memberdata
    
#    pmd = getToolByName(self.context, 'portal_memberdata')

#    if 'watchedPages' not in pmd.propertyIds():
#    pmd.manage_addProperty('watchedPages', 'Watch This Page', 'lines')
