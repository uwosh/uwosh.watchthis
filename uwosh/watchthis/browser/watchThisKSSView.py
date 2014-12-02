##very much incomplete
from kss.core import KSSView, kssaction
from Products.CMFCore.utils import getToolByName
from watchOrStopWatching import WatchThis

class toggleWatchThisTitleKSS(KSSView):

    @kssaction
    def KSStoggle(self):
        ##get current browser view
        #my_view = MyAnotherView(self.context, self.request); another_value = my_view.function()
        watchThisView = WatchThis(self.context, self.request)
        watchThisView.toggleWatching()#have to call to initialize docDisplayTitle if its not initialized yet
        displayTitle = watchThisView.getDisplayTitle()
        pa = getToolByName(self, 'portal_actions')
        da = pa.document_actions
        wt = da.watchThis
        
        #get the current browser view, pass it to getDisplayTitle to get the title
        WTDescription = wt.description
        WTHref = self.context.absolute_url() + "/toggleWatching"
        WTTitle = displayTitle#get WatchThis Browser View
        ksscore = self.getCommandSet('core')
        selector = ksscore.getHtmlIdSelector('document-action-watchthis')
        content = '<a title="%s" href="%s">%s</a>' % (WTDescription, WTHref, WTTitle)
        ksscore.replaceInnerHTML(selector, content)

        
    def setWatchThisTitle(self):
        watchThisView = WatchThis(self.context, self.request)
        pd = watchThisView.getPageDictionary()
        userId = watchThisView.getUserId()
        page = self.context.getId()
        
        if page in pd.keys(): 
            usersCurrentlyWatchingThisPage = pd.get(page)
            if userId in usersCurrentlyWatchingThisPage:
                displayTitle = "Stop Watching This Page"
            elif userId not in usersCurrentlyWatchingThisPage:
                displayTitle = "Watch This Page"

        elif page not in pd.keys():
            displayTitle = "Watch This Page"
        #get pageDictionary
        #if current user is watching this page
        #display Stop Watching This Page
        #else display Watch This Page
        pa = getToolByName(self, 'portal_actions')
        da = pa.document_actions
        wt = da.watchThis
        
        #get the current browser view, pass it to getDisplayTitle to get the title
        WTDescription = wt.description
        WTHref = self.context.absolute_url() + "/toggleWatching"
        ksscore = self.getCommandSet('core')
        selector = ksscore.getHtmlIdSelector('document-action-watchthis')
        content = '<a title="%s" href="%s">%s</a>' % (WTDescription, WTHref, displayTitle)
        ksscore.replaceHTML(selector, content)##won't render new title, is getting assigned to displayTitle however

        

