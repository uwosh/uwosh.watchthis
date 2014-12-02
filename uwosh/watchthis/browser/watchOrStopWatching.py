from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView

def sendChangeEmail(object, event):##Object modified event will be passed in.... object that the object modified event occurs on will also be passed in
    ##pd = object.unrestrictedTraverse['pageDictionary']
    import pdb;pdb.set_trace()
    urltool = getToolByName(object, 'portal_url')
    pmtool = getToolByName(object, 'portal_membership')
    portal = urltool.getPortalObject()
    pd = portal.unrestrictedTraverse('pageDictionary')
    objectId = object.getId()##probably not correct
    objectTitle = object.Title()
    objectType = object.portal_type
    objectUrl = object.absolute_url()
            ##Potentially send the changes that were made?
    for users in pd[objectId]:
        if pmtool.getMemberById(users):
            user = pmtool.getMemberById(users)
            msgTo = user.getProperty('email')##actually have to get the user
            msgFrom = 'klotzj27@uwosh.edu' ##site.fromEmail##fix this
            msgSubj = 'A Page You Are Watching Has Changed'
            ##mSubj = 'The %s ''%s'' Has Changed' % (objectType, objectTitle)
            message = "%s has changed. Visit the updated object here %s" % (objectTitle, objectUrl)
            object.MailHost.simple_send(mto=msgTo, mfrom=msgFrom, subject=msgSubj, body=message) 
        
    return "Page Updated!"



class WatchThis(BrowserView):

    ##_template = ViewPageTemplateFile('docActions.pt')
    docDisplayTitle = "Watch This Object"#creating class attribute for what to display in the watchThis DA
##add browser view for watched pages---just iterate of over keys(pages) in BTree where user is a value and display in a pt
    ##check for attribute first
    def setDisplayTitle(self, displayTitle):
        self.docDisplayTitle = displayTitle

    def getDisplayTitle(self):##for use by KSS action
        return self.docDisplayTitle

    def showWatchThisAction(self):
        pm = getToolByName(self.context, 'portal_membership')
        user = pm.getAuthenticatedMember()
        show = False
        if not pm.isAnonymousUser() and user.has_role('Member'):
            show = True

        return show

    def getPageDictionary(self):
        pd = self.context.unrestrictedTraverse('pageDictionary')##need to get this
        return pd

    def getUserId(self):
        pm = getToolByName(self.context, 'portal_membership')
        user = pm.getAuthenticatedMember()
        catalog = getToolByName(self.context, 'portal_catalog')
        userId = user.getUserName()
        return userId
        
    def toggleWatching(self):##toggle the Watch This document action... append and remove from list of watchers and pages
        
        pd = self.getPageDictionary()
        userId = self.getUserId()
        page = self.context.getId()

###Options for toggling Watch This Document Action
	
        if page not in pd.keys():##if page is not in pageDictionary keys already then add it and user to it
            pd.insert(page, userId)#pd[page] = userId
            self.setDisplayTitle("Stop Watching This Page") ##what to display to the user

        elif page in pd.keys(): 
            usersCurrentlyWatchingThisPage = pd.get(page)
            if userId in usersCurrentlyWatchingThisPage:#if page is in pageDictionary and user is in values, check if the user is watching this page
                tempList = list()#list to use as value for this page key
                for users in usersCurrentlyWatchingThisPage:
                    if users != userId:
                        tempList.append(users)#add all other users to templist except the user that wanted to stop watching

                    pd[page] = tempList#can't use an insert since a key is already in the collection#pd[page] = tempList#set page entry to temp list which now doesn't include the user
                    self.setDisplayTitle("Watch This Page")
##pd.values gets list of values not list of values in the list.. moving to below function everytime because of this                            
            elif userId not in usersCurrentlyWatchingThisPage:#if page is in pageDictionary and user is not in values
                tempList = list()
                for values in pd[page]:
                    tempList.append(values)#add user to list watching this page
                tempList.append(userId)
                pd[page] = tempList#pd[page] = tempList#set page key to new list including the user
                self.setDisplayTitle("Stop Watching This Page") 

        if pd[page] == '':#if no value for page, remove from dict
            del pd[page]



        
        
        
        








                
