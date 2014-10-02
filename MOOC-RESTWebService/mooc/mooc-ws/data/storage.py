"""
Storage interface
"""

import time
from pymongo import Connection
from bson import json_util
import json
import bottle
from bottle import response, Response
from bson.objectid import ObjectId
import ast



class Storage(object):
 
    def __init__(self):
      # initialize our storage, data is a placeholder
      self.data = {}
      # for demo
      self.data['created'] = time.ctime()
    '''  
    def insert(self, name, value):
      connection = Connection()
      db = connection['cmpe275']
      try:
          user = {"username": name, "password": value}
          users = db['users'] 
          users.insert(user)
          return "added"
      except:
         return "error: data not added"

    def remove(self, name):
       "---> remove:", name

    def names(self):
      #print "---> names:"
      for k in self.data.iterkeys():
        #print 'key:', k

    def find(self, name):
      #print "---> storage.find:", name
      connection = Connection()
      db = connection['cmpe275']
      c = db.users.find({"username":'john'}).count()
      #print "Count-->", c
      st = {"username":name}
      #print "String-->", st
      name1 = db.users.find(st)
      #print name1.count()
      for record in name1:
         #print "--> Inside Cursor"
         del record["_id"]
         json.dumps(record)
         #print "Record:", record
      if name > 0:
         return record
      else:
         return None
     '''
# def for sign in
    def auth(self, email, pwd):
        
        #print "---> storage.find:", email
        connection = Connection()
        db = connection['cmpe275']
        c = db.usercollection.find({"email": email}).count()
        if c == 1:
            st = {"email":email}
            name1 = db.usercollection.find(st)
            for record in name1:
                #print "--> Inside Cursor"
                del record["_id"]
                strPwd = record["pwd"]
                #print pwd
                #print strPwd
                if strPwd == pwd:
                    #print "Login Successfull"
                    msg = {"success": True, 'msg':'Login Successful'}
                    #response.status = 
                    return msg
                else:
                    response.status = 401
                    #print "Password Incorrect"
                    msg = {"success": False, 'msg':'Password Incorrect'}
                    return msg           
        else:
            response.status = 401
            msg = {"success": False, 'msg':'Login Failed - Email not found'}
            #print msg
            return msg  
 
        
    def catinsert(self, catname, catdesc, catcreatedate, catstatus):
        #print 'sweta: in storage -> category add'
        connection = Connection()
        
        db = connection['cmpe275']
        c = db.usercollection.find({"name": catname}).count()
        #print c
        if c == 0:
            try:
                categorycollection = db['categorycollection']
                #count = db.categorycollection.find().count()
                ##print "count is", count
                #newCount = count + 1
                ##print "new count is:", newCount
                #newid = "Pinnaclecategory_" + str(newCount)
                ##print "final id is", newid
                category = {"name": catname, "description": catdesc, "createDate": catcreatedate, "status": catstatus}
                obj_id = categorycollection.insert(category)
                obj_id = str(obj_id);
                #print "Successfully added"
                #print 'obj_id is:', obj_id
                output = {"success" : True, "id": obj_id}
                response.status = 201
                return output
            except:
                output = {"success" : False}
                response.status = 500
                return output
        else:
            response.status = 409
            #print "category already exists"
            output = {"success" : False, "msg":"Already Exists"}
            return output
        
    def deleteDiscussion(self, id):
            connection = Connection()
            db = connection['cmpe275']
            
            #print id                       
                         
            st = {"_Id":id}
            c = db.discussioncollection.find(st)
            #print c.count()
            if c.count() > 0:
                try:
                    db.discussioncollection.remove(st)
                    response.status = 200
                    #print "Delete discussion Success"
                    msg = {"success": True, 'msg':'Delete discussion Successful'}
                    return msg                    
                except:
                     response.status = 500
                     #print "Failed in deleting discussion", sys.exc_info()
                     msg = {"success": False, 'msg':'Delete discussion unsuccessful'}
                     return msg
            else:
                try:
                    response.status = 404
                    msg = {"success": False, 'msg':'discussion ID not found'}
                    return msg
                except:
                    response.status = 400
                    msg = {"success": False, 'msg':'discussion ID invaild'}
                    return msg
            
            
        
    def deleteAnnouncement(self, id):
            connection = Connection()
            db = connection['cmpe275']
            
            #print id                       
                         
            st = {"_Id":id}
            c = db.announcementcollection.find(st)
            #print c.count()
            if c.count() > 0:
                try:
                    db.announcementcollection.remove(st)
                    response.status = 200
                    #print "Delete announcement Success"
                    msg = {"success": True, 'msg':'Delete announcement Successful'}
                    return msg
                except:
                     response.status = 500
                     #print "Failed in deleting announcement", sys.exc_info()
                     msg = {"success": False, 'msg':'Delete announcement unsuccessful'}
                     return msg                    
            else:
                try:
                    response.status = 404
                    msg = {"success": False, 'msg':'announcement ID not found'}
                    return msg
                except:
                    response.status = 400
                    msg = {"success": False, 'msg':'announcement ID invaild'}
                    return msg
                    
                
                                          
                      
    def updateDiscussion(self, id, body):
        connection = Connection()
        db = connection['cmpe275']
        st = {"_Id":id}
        c = db.discussioncollection.find(st).count()
        if c > 0:
            try:
                db.discussioncollection.update(st, {'$set': body})
                response.status = 200
                #print "Delete announcement Success"
                msg = {"success": True, 'msg':'Update discussion Successful'}
                return msg
            except:
                 response.status = 500
                 #print "Failed in updating discussion", sys.exc_info()
                 msg = {"success": False, 'msg':'Update discussion  unsuccessful'}
                 return msg                    
        else:
            try:
                response.status = 404
                msg = {"success": False, 'msg':'Discussion ID not found'}
                return msg
            except:
                response.status = 400
                msg = {"success": False, 'msg':'Discussion ID invaild'}
                return msg
        
        
     
    def updateAnnoucement(self, id, body):
        connection = Connection()
        db = connection['cmpe275']
        st = {"_Id":id}
        c = db.annoucementcollection.find(st).count()
        if c > 0:
            try:
                db.annoucementcollection.update(st, {'$set': body})
                response.status = 200
                #print "Delete announcement Success"
                msg = {"success": True, 'msg':'Update announcement Successful'}
                return msg
            except:
                 response.status = 500
                 #print "Failed in updating announcement", sys.exc_info()
                 msg = {"success": False, 'msg':'Update announcement unsuccessful'}
                 return msg                    
        else:
            try:
                response.status = 404
                msg = {"success": False, 'msg':'announcement ID not found'}
                return msg
            except:
                response.status = 400
                msg = {"success": False, 'msg':'announcement ID invaild'}
                return msg
           
        
    def getCourse(self, id):
      #print "---> storage.getCourse:", id
      objid = ObjectId(id)
      #print 'new id is:', id
      connection = Connection()
      db = connection['cmpe275']
      c = db.coursecollection.find({"_id":objid}).count()
      #print "Count-->", c
      st = {"_id":objid}
      #print "String-->", st
      courseDetails = db.coursecollection.find(st)
      #print courseDetails.count()
      singleCourse = None
      for record in courseDetails:
         #print "--> Inside Cursor"
         del record["_id"]
         record["id"] = id
         json.dumps(record)
         #print "Record:", record
         singleCourse = record
      if c > 0:
          try:
              response.status = 200
              #print "Get course Success"
              return singleCourse
          except:
              response.status = 500
              #print "Failed in getting course", sys.exc_info()
              msg = {"success": False, 'msg':'Get course unsuccessful'}
              return msg                    
      else:
          try:
              response.status = 404
              msg = {"success": False, 'msg':'course ID not found'}
              return msg
          except:
              response.status = 400
              msg = {"success": False, 'msg':'course ID invaild'}
              return msg
     
     # Course list find 
    def listCourse(self):
        #print "---> storage category listCourse.find:"
        connection = Connection()
        db = connection['cmpe275']
        c = db.coursecollection.find().count()
        #print "Count-->", c
        courseList = db.coursecollection.find()
        #print courseList.count()
        lst = []
        for record in courseList:
            #print "--> Inside Cursor"
            temp = record["_id"]
            temp = str(temp)
            #print "temp value is", temp
            #record["_id"] = temp
            del record["_id"]
            record["id"] = temp
            lst.append(record)
        if c > 0:
            try:
                response.status = 200
                #print "List course Success"
                return json.dumps(lst)
            except:
                 #print "Failed in listing course", sys.exc_info()
                 msg = {"success": False, 'msg':'List course unsuccessful'}
                 return msg
                        
        else:
            #print "Failed in listing course", sys.exc_info()
            msg = {"success": False, 'msg':'List course unsuccessful'}
            return msg
 
    def deleteCourse(self, id):
            #print 'id is', id
            Objid = ObjectId(id)
            #print 'obj id is' , Objid
            connection = Connection()
            db = connection['cmpe275']
            
            
                           
            rowset1 = db.usercollection.find({'own':{'$all':[id]}})
            #print 'rowset is ' ,rowset1
            email = rowset1[0]['email']
            #print 'email is ' ,email

            result = db.usercollection.update({'email':email}, {'$pull':{'own':id}})
            #print 'result', result
            
            rowset2 = db.usercollection.find({'enrolled':{'$all':[id]}})
            #print 'rowset2 is', rowset2
            
            for r in rowset2:
                tempEmail = r['email']
                #print tempEmail
                db.usercollection.update({'email':tempEmail}, {'$pull':{'enrolled':id}})
         
            st = {"_id":Objid}
            #print 'string is', st
            c = db.coursecollection.find(st)
            #print c.count()
            if c.count() > 0:
                try:
                    db.coursecollection.remove(st)
                    response.status = 200
                    #print "Delete course Success"
                    msg = {"success": True, 'msg':'Delete course Successful'}
                    return msg
                except:
                     response.status = 500
                     #print "Failed in deleting course"
                     msg = {"success": False, 'msg':'Delete course unsuccessful'}
                     return msg
                    
            else:
                try:
                    response.status = 404
                    msg = {"success": False, 'msg':'course ID not found'}
                    return msg
                except:
                    response.status = 400
                    msg = {"success": False, 'msg':'course ID invaild'}
                    return msg

    def updateCourse(self, id, body):
        #print 'Inside Update storage'
        obj_id = ObjectId(id)
        connection = Connection()
        db = connection['cmpe275']
        #needs to convert from str to Object ID?
        st = {"_id":obj_id}
        c = db.coursecollection.find(st).count()
        if c > 0:
            try:
                db.coursecollection.update(st, {'$set': body})
                response.status = 200
                #print "Delete announcement Success"
                msg = {"success": True, 'msg':'Update course Successful'}
                return msg
            except:
                 response.status = 500
                 #print "Failed in updating course", sys.exc_info()
                 msg = {"success": False, 'msg':'Update course unsuccessful'}
                 return msg
                    
        else:
            try:
                response.status = 404
                msg = {"success": False, 'msg':'course ID not found'}
                return msg
            except:
                response.status = 400
                msg = {"success": False, 'msg':'course ID invaild'}
                return msg

    #def for Create User
    def addUser(self,name,value,fname,lname):
         #print 'add user in storage'
         connection=Connection()
         db=connection['cmpe275']
         c=db.usercollection.find({"email": name}).count()
         #print c
         if c == 0:
             try:
                 #user={"email": name, "pwd": value , "fName": fname, "lName": lname}
                 user={"email": name, "pwd": value, "fName": fname, "lName": lname,"own":[""],"enrolled":[""], "quizzes":[{"quiz":"", "grade":"", "submitDate":""}]}
                 #print 'user query is ', user
                 usercollection=db['usercollection']
                 usercollection.insert(user)
                 #print "Successfully added"
                 msg = {"success": True, 'msg':'Successfully added'}
                 response.status = 201
                 return msg  
             except:
                 response.status = 500
                 return {"success": False, 'msg': 'Data not added'}
         else:
             response.status = 409
             msg = {"success": False, 'msg':'Email already exists'}
             return msg
    
    #Update User
    def updateUser(self, email, body):
         connection = Connection()
         db = connection['cmpe275']
         st = {"email":email}
         c = db.usercollection.find(st).count()
         #print "Updated st " , st
         #print "Updated c" , c
         #print "Updated body" , body
         data = ast.literal_eval(json.dumps(body))
         
         if c > 0:
             ##print db.usercollection.update(st,{ '$set' : body })
             #for key,value in body:    #to add old password new password func.
                #data = json.loads(key)
             #oldpassword = db.usercollection.find(st,{'pwd':pwd})
             #if data["oldpassword"] == oldpassword["pwd"]:
                 #body = {'pwd': data['newpassword'], 'fName': data['fName'], 'lName': data['lName'] }
                
                 db.usercollection.update(st,{ '$set' : data })
                 #print "Updateddd"
                 msg = {"success": True, "msg":'Existing User Updated'}
                 response.status = 200
                 return msg
             
         else:
             #print "No User Found. It will create new User."
             for key,value in body:
                data1 = json.loads(key)
             data = ast.literal_eval(json.dumps(data1))
             msg = Storage.addUser(self, data['email'], data['newpassword'], data['fName'], data['lName'])
             response.status = 201  
             #msg = {"msg":'User Not Updateddd'}
             return msg
    
    
    #delete User 
    def deleteUser(self, email):
        connection = Connection()
        db = connection['cmpe275']
        c = db.usercollection.find({"email":email}).count()
        if c > 0:
            st = {"email":email}
            db.usercollection.remove(st)
            response.status = 200
            return {"success": True, 'msg':'Delete Success'}     #what about dependencies?? also log out n go to login page.
        elif c == 0:
             response.status = 404
             return {"success": False, 'msg': 'Email not found'}
        else:
            response.status = 400
            return {"success": False, 'msg': 'Bad Request. Please try again Later..'}
             
  
        
    def getUser(self, email):
        connection = Connection()
        db = connection['cmpe275']
        c = db.usercollection.find({"email":email}).count()
        if c > 0:
            st = {"email":email}
            records = db.usercollection.find(st)
            for record in records:
                obj_id = record["_id"]
                obj_id = str(obj_id)
                
                del record["_id"]
                record["id"] = obj_id
                json.dumps(record)
                #print "Record:", record
                response.status = 200
                return record
        else:
            response.status = 404
            return {"success": False, 'msg': 'No record found. Invalid Email Id'}
        
        '''
        if email <= 0:
            response.status = 400
            return {'msg': 'please insert email id. Bad Request'}   #what if other client do not provide validations
        '''

     
     
    def addCourse(self, body):
        # just run below query one time
        # db.coursecollection.ensureIndex( { "courseId": 1 }, { unique: true } )
        connection = Connection()
        db = connection['cmpe275']
        count = db.coursecollection.find().count()
        courseId = count + 1
        #print courseId
        try:
            #print body
            for key, value in body:
                data = json.loads(key)
            
            ##print 'Description from storage:' + data['Description']
            data1 = ast.literal_eval(json.dumps(data))
            #print data1
            
            #data2 = {"category" : "categ2", "title" : "intro to python", "section" : 2, "dept" : "eng", "term" : "spring", "year" : 2013, "instructor" : [ { "name" : "John", "email" : "gash@gash.com" } ], "days" : [ "Monday", "Wednesday", "Friday" ], "hours" : [ "8.00AM", "9.15AM" ], "Description" : "My Course", "attachment" : "Path", "version" : "1" }
            obj_id = db.coursecollection.insert({ "category" : data1['category'], "title" : data1['title'], "section" : data1['section'], "dept" : data1['dept'], "term" : data1['term'], "year" : data1['year'], "instructor" : [ { "name" : data1['insName'], "email" : data1['insEmail'] } ], "days" : [ data1['days'] ], "hours" : [ data1['hour1'], data['hour2' ]], "Description" : data1['Description'], "attachment" : data1['attachment'], "version" : data1['version'] })
            obj_id = str(obj_id)
            id = {"own": obj_id}
            
            st = {"email": data1['email']}
            db.usercollection.update(st,{ '$push' : id})
            #email = data1['email']
            ##print email
            response.status = 201
            return {"success": True, 'msg': 'Course Added'}
        except:
            response.status = 501
            return {"success": False, 'msg': 'Course not added'}

    def enrollCourse(self,email,courseId):
     #print 'in storage.enrollCourse'
     connection=Connection()
     db=connection['cmpe275']
     c = db.usercollection.find({"email": email}).count()
     #print c
     if c == 1:
         try:
             #print 'in try'
             st={"email": email}
             id = {"enrolled": courseId }
             #print 'before query', id
             db.usercollection.update(st,{ '$push' : id})
             #print "Successfully enrolled"
             msg = {"success": True, "msg":'Successfully enrolled'}
             response.status = 200
             return msg  
         except:
             response.status = 500
             return {"success": False, 'msg': 'Error data not added'}
     else:
         response.status = 404
         #print "No email "
         msg = {"success": False, 'msg':'No email'}
         return msg 


    def catfind(self, id):
      #print "---> storage.find:", id
      objid = ObjectId(id)
      #print 'new id is:', id 
      connection = Connection()
      db = connection['cmpe275']
      c = db.categorycollection.find({"_id":objid}).count()
      #print "Count-->", c
      st = {"_id":objid}
      #print "String-->", st
      name1 = db.categorycollection.find(st)
      #print name1.count()
      for record in name1:
         #print "--> Inside Cursor"
         del record["_id"]
         record["id"] = id
         json.dumps(record)
         #print "Record:", record
      if c > 0:
          try:
              response.status = 200
              #print "Get category Success"
              return record
          except:
              response.status = 500
              #print "Failed in getting category", sys.exc_info()
              msg = {"success": False, 'msg':'Get category unsuccessful'}
              return msg                    
      else:
          try:
              response.status = 404
              msg = {"success": False, 'msg':'category ID not found'}
              return msg
          except:
              response.status = 400
              msg = {"success": False, 'msg':'category ID invaild'}
              return msg
          
    def catlistfind(self):
      #print "---> storage category list.find:"
      connection = Connection()
      db = connection['cmpe275']
      c = db.categorycollection.find().count()
      #print "Count-->", c
      name1 = db.categorycollection.find()
      #print name1.count()
      lst = []
      for record in name1:
         #print "--> Inside Cursor"
         temp = record["_id"]
         temp = str(temp)
         #print "temp value is", temp
         #record["_id"] = temp
         del record["_id"]
         record["id"] = temp
         lst.append(record)
         #print "Record:", record
     
      if c > 0:
            try:
                response.status = 200
                #print "List category Success"
                return json.dumps(lst)
            except:
                response.status = 500
                #print "Failed in listing category", sys.exc_info()
                msg = {"success": False, 'msg':'List category unsuccessful'}
                return msg
      else:
            response.status = 500
            #print "Failed in listing category", sys.exc_info()
            msg = {"success": False, 'msg':'List category unsuccessful'}
            return msg
     
    def announcementfind(self, id):
      #print "---> storage.find:", id
      objid = ObjectId(id)
      #print 'new id is:', id 
      connection = Connection()
      db = connection['cmpe275']
      c = db.announcementcollection.find({"_id":objid}).count()
      #print "Count-->", c
      st = {"_id":objid}
      #print "String-->", st
      
      name1 = db.announcementcollection.find(st)
      #print name1.count()
      for record in name1:
         #print "--> Inside Cursor"
         del record["_id"]
         record["id"] = id
         json.dumps(record)
         #print "Record:", record
      if c > 0:
          try:
              response.status = 200
              #print "Get announcement Success"
              return record
          except:
              response.status = 500
              #print "Failed in getting announcement", sys.exc_info()
              msg = {"success": False, 'msg':'Get announcement unsuccessful'}
              return msg                    
      else:
          try:
              response.status = 404
              msg = {"success": False, 'msg':'annoncement ID not found'}
              return msg
          except:
              response.status = 400
              msg = {"success": False, 'msg':'announcement ID invaild'}
              return msg
     
    def announcementlistfind(self):
      #print "---> storage announcement list.find:"
      connection = Connection()
      db = connection['cmpe275']
      c = db.announcementcollection.find().count()
      #print "Count-->", c
      name1 = db.announcementcollection.find()
      #print name1.count()
      lst = []
      for record in name1:
         #print "--> Inside Cursor"
         temp = record["_id"]
         temp = str(temp)
         #print "temp value is", temp
         #record["_id"] = temp
         del record["_id"]
         record["id"] = temp
         lst.append(record)
         #print "Record:", record
      
      if c > 0:
            try:
                response.status = 200
                #print "List announcement Success"
                return json.dumps(lst)
            except:
                 response.status = 500
                 #print "Failed in listing announcement", sys.exc_info()
                 msg = {"success": False, 'msg':'List announcement unsuccessful'}
                 return msg
      else:
            response.status = 500
            #print "Failed in listing announcement", sys.exc_info()
            msg = {"success": False, 'msg':'List announcement unsuccessful'}
            return msg
     
    def announcementinsert(self, courseid, anntitle, anndesc, annpostdate, annstatus):
        connection = Connection()
        db = connection['cmpe275']
      
        try:
          #print "now herennnnnnnnnn"
          announcementcollection = db['announcementcollection']
         
          #count = db.announcementcollection.find().count()
          ##print "count is", count
          #newCount = count + 1
          
         # #print "new count is:", newCount
          #newid = "Pinnacleannouncement_" + str(newCount)
          
          ##print "final id is", newid
          
          announcement = {"courseId": courseid, "title": anntitle, "description": anndesc, "postDate": annpostdate, "status": annstatus}
          obj_id = announcementcollection.insert(announcement)
          
          obj_id = str(obj_id);
          #print "Successfully added"
          #print 'obj_id is:', obj_id
          output = {"success" : True, "id": obj_id}
          response.status = 201
          return output
        except:
          output = {"success" : False}
          response.status = 500
          return output
        
    def addDiscussion(self,course_id,title,createdby,createdAt,updatedAt):
    
      #print 'Str id in storage file in add discussin is',course_id 
      connection=Connection()
      db=connection['cmpe275']  
      Discussion=db['Discussion']
  
      c = db.Discussion.find().count()
      #print c

      createDate = "2013-05-07T23:24:40.132Z"
      updateDate = "2013-06-07T24:24:40.132Z"
      #print 'in add discussion'
      discussion= {"course_id": course_id, "title": title, "created_by": createdby,"created_at":createDate,"updated_at":updateDate}
      objid = db.Discussion.insert(discussion)
      discussionList = db.Discussion.find({"_id":objid})
      
      #print "Successfully added discssion"
      objid = str(objid);
      #print "Successfully added", objid
      #print 'obj_id is:', objid
      output = {"success" : True, "id": objid}
      response.status = 201
      #print 'output is', output
      for record in discussionList:
            #print "--> Inside Cursor"
            temp = record["_id"]
            temp = str(temp)
            #print "temp value is", temp
            del record["_id"]
            record["id"] = temp 
      
      return record

    # discussion find

    def getDiscussionFromId(self,id):

     #print "--> Inside getDiscussionFromId ----->>>>"

     connection=Connection()
     db=connection['cmpe275']
     objid = ObjectId(id)

     c=db.Discussion.find({"_id":objid}).count()
     #print "Count-->",c
     st={"_id":objid}
     #print "String-->",st
     name1=db.Discussion.find(st)
     #print name1.count()
     for record in name1:
        #print "--> Inside Cursor"
        del record["_id"]
        record["id"] = id

        json.dumps(record)
        #print "Record:", record
     if c > 0:
          try:
              response.status = 200
              #print "Get Discussion Success"
              return record
          except:
              response.status = 500
              #print "Failed in getting Discussion", sys.exc_info()
              msg = {"success": False, 'msg':'Get Discussion unsuccessful'}
              return msg                    
     else:
          try:
              response.status = 404
              msg = {"success": False, 'msg':'Discussion ID not found'}
              return msg
          except:
              response.status = 400
              msg = {"success": False, 'msg':'Discussion ID invaild'}
              return msg
    
    
    def addMessage(self,title,content,discussion_id,createdby,createdAt,updatedAt):
      connection=Connection()
      db=connection['cmpe275']    
      try:
         #print "now herennnnnnnnnn"
         Message=db['Message']
         count = db.Message.find().count()
         #print "count is", count
         newCount = count+1
         #print "new count is:", newCount
         newid = "Pinnaclemessage_" + str(newCount)
         
         createDate = "2013-05-07T23:24:40.132Z"
         updateDate = "2013-06-07T24:24:40.132Z"

         message= {"title":title, "content": content, "discussion_id": discussion_id, "created_by": createdby,"created_at":createDate,"updated_at":updateDate}
         Message.insert(message)

         msg = {"msg":newid}
         response.status = 201
         return msg  
      except:
             response.status = 500
             #print "message not added"
             msg = {"success": False, 'msg':'message not added'}
             return msg
    

    
         # getMessagesFromDiscussionId
    def getMessagesFromDiscussionId(self,discussion_id):
        #print "---> storage category listCourse.find:"
        connection = Connection()
        db = connection['cmpe275']
        c = db.Message.find().count()
        #print "Count-->", c
        st = {"discussion_id" : discussion_id}
        msgList = db.Message.find(st)
        #print msgList.count()
        lst = []
        for record in msgList:
            #print "--> Inside Cursor"
            del record["_id"]
            lst.append(record)
            #print "Record:", record
        if c > 0:
            try:
                response.status = 200
                #print "List messages Success"
                return json.dumps(lst)
            except:
                 #print "Failed in listing messages", sys.exc_info()
                 msg = {"success": False, 'msg':'List messages unsuccessful'}
                 return msg
                        
        else:
            #print "Failed in listing messages", sys.exc_info()
            msg = {"success": False, 'msg':'List messages unsuccessful'}
            return msg

             # getDiscussionFromCourseId
    def getDiscussionFromCourseId(self,course_id):
        #print "---> storage category listCourse.find:"
        connection = Connection()
        db = connection['cmpe275']
       
        c = db.Discussion.find().count()
        #print "Count-->", c
        st = {"course_id" : course_id}
        discList = db.Discussion.find(st)
        #print discList.count()
        lst = []
        for record in discList:
            #print "--> Inside Cursor of List Discusssionssss"
            temp = record["_id"]
            temp = str(temp)
            #print temp
            del record["_id"]
            record["id"] = temp

            lst.append(record)
            #print "Record:", record
        if c > 0:
            try:
                response.status = 200
                #print "List discusssions Success"
                return json.dumps(lst)
            except:
                 #print "Failed in listing discusssions", sys.exc_info()
                 msg = {"success": False, 'msg':'List discusssions unsuccessful'}
                 return msg
                        
        else:
            #print "Failed in listing discusssions", sys.exc_info()
            msg = {"success": False, 'msg':'List discusssions unsuccessful'}
            return msg     
        






