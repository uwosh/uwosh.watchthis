
def sendChangeEmail(object, event):##Object modified event will be passed in.... object that the object modified event occurs on will also be passed in
    objectId = object.getId()##probably not correct
    objectTitle = object.Title()
    objectType = object.portal_type()
    objectUrl = object.absolute_url()
            ##Potentially send the changes that were made?
    for users in pd[objectId]:
        mTo = users.getEmail()
        mFrom = 'klotzj27@uwosh.edu' ##site.fromEmail##fix this
        mSubj = 'The %s ''%s'' Has Changed' % (objectType, objectTitle)
        message = "Visit the updated object here %s" % (objectUrl)
        obj.MailHost.send(message, mTo, mFrom, mSubj) 
        
    return "Page Updated!"
