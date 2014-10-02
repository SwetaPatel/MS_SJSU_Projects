# Create your views here.
#from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from djangobottle.app1.forms import ContactForm
from djangobottle.app1.LoginForm import LoginForm
from djangobottle.app1.createUserForm import createUserForm
from djangobottle.app1.updateUserForm import updateUserForm
from djangobottle.app1.createCategoryForm import createCategoryForm
from djangobottle.app1.createAnnouncementForm import createAnnouncementForm
from djangobottle.app1.addDiscussionForm import addDiscussionForm
from djangobottle.app1.DiscussionSuccessForm import DiscussionSuccessForm
from djangobottle.app1.forms import MoocForm
from bson.objectid import ObjectId
from bottle import route
from json import loads, dumps
import requests
from djangobottle.app1 import requestsUtil
import json
import ast


userloginEmail = None

def index(request):
    #return HttpResponse("Index Page")
    ctx = {}
    return render_to_response('loggedOutIndex.html', ctx, context_instance=RequestContext(request))

def login_index(request,teamName=None):

    if teamName != None:
        request.session['teamName'] = teamName

    r = requestsUtil.getCategoryList(request.session['teamName'])
    code = r.status_code
    ctx = {}
    if code == 200:
        data = ast.literal_eval(json.dumps(r.json()))
        print 'data is', data
        error_status = False
        ctx = {'data': data, 'error_status': error_status,"mooc_select":MoocForm(request.session['teamName'])}
    return render_to_response('loggedInIndex.html', ctx, context_instance=RequestContext(request))


def about(request):
    r = {'msg': 'fail'}

    login_form = LoginForm(request.POST)

    ctx = {'login_form': login_form}
    return render_to_response('about.html', ctx, context_instance=RequestContext(request))


def signIn(request):
    error_status = False
    login_status = False
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            request.session["contact_sent"] = True
            login_form_data = {'email': username, 'pwd': password}
            r = requestsUtil.makePostRequest("auth", data=json.dumps(login_form_data))
            code = r.status_code
            if code == 200:

                global userloginEmail
                userloginEmail = username
                request.session["username"]=username
                login_status = True
                return login_index(request)
            elif code == 500:
                error_status = True
                ctx = {'login_form': login_form, 'error_status': error_status, 'error': r.json()}
                return render_to_response('login.html', ctx, context_instance=RequestContext(request))
            elif code == 401:
                error_status = True
                ctx = {'login_form': login_form, 'error_status': error_status, 'error': r.json()}
                return render_to_response('login.html', ctx, context_instance=RequestContext(request))

    else:

        login_form = LoginForm()

    ctx = {'login_form': login_form, 'error_status': error_status}
    return render_to_response('login.html', ctx, context_instance=RequestContext(request))


def createUser(request):
    error_status = False
    login_status = False
    createUser_status = False
    if request.method == "POST":
        createUser_form = createUserForm(request.POST)
        if createUser_form.is_valid():
            email = createUser_form.cleaned_data['email']
            password = createUser_form.cleaned_data['password']
            fname = createUser_form.cleaned_data['fname']
            lname = createUser_form.cleaned_data['lname']
            request.session["contact_sent"] = True
            createUser_form_data = {'email': email, 'pwd': password, 'fname': fname, 'lname': lname}
            r = requestsUtil.makePostRequest("user", data=json.dumps(createUser_form_data))
            code = r.status_code
            if code == 201:
                login_status = False
                createUser_status = True
                request.session['teamName'] = 'Pinnacle'
                ctx = {'data': r.json(), 'error_status': error_status, 'createUser_status': createUser_status,
                       'login_status': login_status,"mooc_select":MoocForm(request.session['teamName'])}
                return render_to_response('loggedOutIndex.html', ctx, context_instance=RequestContext(request))
            elif code == 500:
                error_status = True
                ctx = {'createUser_form': createUser_form, 'error_status': error_status,
                       'error': 'Internal Error Occurs. Please try after sometime.'}
                return render_to_response('createUser.html', ctx, context_instance=RequestContext(request))
            elif code == 409:
                error_status = True
                ctx = {'createUser_form': createUser_form, 'error_status': error_status, 'error': r.json()}
                return render_to_response('createUser.html', ctx, context_instance=RequestContext(request))

    else:

        createUser_form = createUserForm()

    ctx = {'createUser_form': createUser_form, 'error_status': error_status}
    return render_to_response('createUser.html', ctx, context_instance=RequestContext(request))

def createCategory(request):
    error_status = False
    login_status = False
    createCategory_status = False
    if request.method == "POST":
        createCategory_form = createCategoryForm(request.POST)
        if createCategory_form.is_valid():
            name = createCategory_form.cleaned_data['name']
            description = createCategory_form.cleaned_data['description']
            createDate = createCategory_form.cleaned_data['createDate']
            status = createCategory_form.cleaned_data['status']
            request.session["contact_sent"] = True
            createCategory_form_data = {'name' : name, 'description' : description,
               'createDate' : createDate, 'status' : status}
            r = requestsUtil.createCategory(createCategory_form_data, request.session['teamName'])
            #r = requestsUtil.makePostRequest("category", data=json.dumps(createCategory_form_data))
            #r = requests.post("http://localhost:8080/category", data = json.dumps(createCategory_form_data))
            code = r.status_code
            print 'create category code value', code
            if code == 201:
                print 'In 201 area'
                login_status = False
                createCategory_status = True
                ctx = {'data': 'Category Added.', 'error_status': error_status, 'createCategory_status': createCategory_status}
                return render_to_response('loggedInIndex.html', ctx, context_instance=RequestContext(request))
            elif code == 500:
                error_status = True
                ctx = {'createCategory_form': createCategory_form, 'error_status': error_status,
                       'error': 'Internal Error Occurs. Please try after sometime.'}
                return render_to_response('createCategory.html', ctx, context_instance=RequestContext(request))
            elif code == 409:
                error_status = True
                ctx = {'createCategory_form': createCategory_form, 'error_status': error_status, 'error': r.json()}
                return render_to_response('createCategory.html', ctx, context_instance=RequestContext(request))

    else:

        createCategory_form = createCategoryForm()

    ctx = {'createCategory_form': createCategory_form, 'error_status': error_status}
    return render_to_response('createCategory.html', ctx, context_instance=RequestContext(request))


def createAnnouncement(request, courseId):
    print 'Create announcement is called'
    error_status = False
    #login_status = False
    createAnnouncement_status = False
    if request.method == "POST":
        createAnnouncement_form = createAnnouncementForm(request.POST)
        if createAnnouncement_form.is_valid():
            courseId1 = courseId
            title = createAnnouncement_form.cleaned_data['title']
            description = createAnnouncement_form.cleaned_data['description']
            postDate = createAnnouncement_form.cleaned_data['postDate']
            status = createAnnouncement_form.cleaned_data['status']
            request.session["contact_sent"] = True

            createAnnouncement_form_data = {'courseId': courseId1, 'title': title, 'description': description,
               'postDate': postDate, 'status': status}
            #r = requestsUtil.makePostRequest("category", data=json.dumps(createCategory_form_data))
           # r = requests.post("http://localhost:8080/announcements", data = json.dumps(createAnnouncement_form_data))
            r = requestsUtil.createAnnouncement(createAnnouncement_form_data, request.session['teamName'])

            code = r.status_code

            if code == 201:

                #login_status = False
                createAnnouncement_status = True
                ctx = {'error_status': error_status, 'createAnnouncement_status': createAnnouncement_status}
                return render_to_response('success.html', ctx, context_instance=RequestContext(request))
            elif code == 500:
                error_status = True
                ctx = {'createAnnouncement_form': createAnnouncement_form, 'error_status': error_status,
                       'error': 'Internal Error Occurs. Please try after sometime.'}
                return render_to_response('createAnnouncement.html', ctx, context_instance=RequestContext(request))


    else:

        createAnnouncement_form = createAnnouncementForm()

    ctx = {'courseId':courseId,'createAnnouncement_form': createAnnouncement_form, 'error_status': error_status}
    return render_to_response('createAnnouncement.html', ctx, context_instance=RequestContext(request))


def getUser(request):
    if request.method == "POST":
        #updateUser(request)
        login_status = True
        updateUser_status = False
        updateUser_form = updateUserForm(request.POST)
        if updateUser_form.is_valid():
            email = updateUser_form.cleaned_data['email']
            password = updateUser_form.cleaned_data['password']

            fname = updateUser_form.cleaned_data['fname']
            lname = updateUser_form.cleaned_data['lname']
            request.session["contact_sent"] = True
            updateUser_form_data = {'email': email, 'pwd': password, 'fName': fname, 'lName': lname}
            r = requestsUtil.makePutRequest("user/"+email, data=json.dumps(updateUser_form_data))
            code = r.status_code

            if code == 200:
                error_status = False
                updateUser_status = True

                ctx = {'data': r.json(), 'error_status': error_status, 'updateUser_status': updateUser_status, "mooc_select":MoocForm(request.session['teamName'])}
                return render_to_response('loggedInIndex.html', ctx, context_instance=RequestContext(request))
            elif code == 500:
                error_status = True
                #updateUser_form = updateUserForm()
                updateUser_status = False
                ctx = {'updateUser_form': updateUser_form, 'error_status': error_status, 'error.msg': 'Internal Error Occurs. Please try after sometime.'}
                return render_to_response('updateUser.html', ctx, context_instance=RequestContext(request))
            elif code == 201:
                error_status = False
                updateUser_status = True
                ctx = {'data': r.json(),'login_status': login_status, 'updateUser_status': updateUser_status, 'error': r.json()}
                return render_to_response('loggedInIndex.html', ctx, context_instance=RequestContext(request))

    else:
        error_status = False
        updateUser_status = False
        login_status = True
        r = requestsUtil.makeGetRequest("user/" + request.session["username"])
        code = r.status_code
        if code == 200:
            data = ast.literal_eval(json.dumps(r.json()))

            user_details = {'email': data['email'], 'password': data['pwd'], 'fname': data['fName'], 'lname': data['lName']}
            updateUser_form = updateUserForm(user_details)  #user_details, updateUser_form.__init__(user_details)


            ctx = {'updateUser_form': updateUser_form, 'error_status': error_status}
            return render_to_response('updateUser.html', ctx, context_instance=RequestContext(request))

        elif code == 404 or 500:
            error_status = True
            updateUser_form = updateUserForm()
            ctx = {'updateUser_form': updateUser_form, 'error_status': error_status, 'error.msg': 'Internal Error Occurs. Please try after sometime.'}
            return render_to_response('updateUser.html', ctx, context_instance=RequestContext(request))



def listCourses(request):
    if request.method == 'GET':
        r = requestsUtil.getCourseList(request.session['teamName'])
        code = r.status_code
        if code == 200:
            error_status = False
            ctx = {'data': r.json(), 'error_status': error_status, "mooc_select":MoocForm(request.session['teamName'])}
            return render_to_response('listCourses.html', ctx, context_instance=RequestContext(request))


def getCourse(request, courseId):
    if request.method == 'GET':
        userid = False
        global userloginEmail
        if userloginEmail is None:
            userCourse_status = False
        else:
            #r = requestsUtil.getCourse(courseId, request.session['teamName'])
            r = requestsUtil.makeGetRequest("user/" + request.session["username"])
            code = r.status_code
            if code == 200:
                data = ast.literal_eval(json.dumps(r.json()))
                own = data['own']
                userid = data['id']     # we will get user id.

                for i in own:

                    if i == courseId:
                        userCourse_status = True
                        break
                    else:
                        userCourse_status = False
            else:
                userCourse_status = False

        r = requestsUtil.getCourse(courseId, request.session['teamName'])
        r1 = requestsUtil.makeGetRequest("user/" + request.session["username"])
        userEnroll_status = False
        code = r1.status_code
        if code == 200:
                user_data = ast.literal_eval(json.dumps(r1.json()))
                enrolled = user_data['enrolled']
                userid = data['id']     # we will get user id.

                for i in enrolled:

                    if i == courseId:
                        userEnroll_status = True
                        break
                    else:
                        userEnroll_status = False
        else:
                userEnroll_status = False

        code = r.status_code
        if code == 200:
            error_status = False
            ctx = {'data': r.json(), 'error_status': error_status, 'userCourse_status': userCourse_status, 'userid': userid, 'courseId': courseId, 'userEnroll_status': userEnroll_status}
            return render_to_response('getCourse.html', ctx, context_instance=RequestContext(request))

        elif code == 500:
            error_status = True
            ctx = {'data': r.json(), 'error_status': error_status, 'error_msg': 'Internal Error: 500'}
            return render_to_response('getCourse.html', ctx, context_instance=RequestContext(request))

def listCategories(request):
    if request.method == 'GET':
        r = requestsUtil.getCategoryList()

        #r = requests.get("http://localhost:8080/category/list")
        code = r.status_code

        if code == 200:
            data = ast.literal_eval(json.dumps(r.json()))

            error_status = False
            ctx = {'data': data, 'error_status': error_status}
            return render_to_response('listCategories.html',ctx,context_instance=RequestContext(request))

def getCategory(request, categoryId):
    if request.method == 'GET':
        #r = requests.get("http://localhost:8080/category/"+categoryId)
        r = requestsUtil.getCategory(categoryId, request.session['teamName'])
        code = r.status_code
        if code == 200:
            error_status = False
            ctx = {'data': r.json(), 'error_status': error_status}
            return render_to_response('getCategory.html',ctx,context_instance=RequestContext(request))       

def listAnnouncements(request):
    if request.method == 'GET':

        r = requestsUtil.getAnnouncementList()

        #r = requests.get("http://localhost:8080/announcement/list")
        code = r.status_code

        if code == 200:
            data = ast.literal_eval(json.dumps(r.json()))

            error_status = False
            ctx = {'data': data, 'error_status': error_status}
            return render_to_response('listAnnouncements.html',ctx,context_instance=RequestContext(request))

def getAnnouncement(request, announcementId):
    if request.method == 'GET':
        #r = requests.get("http://localhost:8080/announcement/"+announcementId)
        r = requestsUtil.getAnnouncement(announcementId)
        code = r.status_code
        if code == 200:
            error_status = False
            ctx = {'data': r.json(), 'error_status': error_status}
            return render_to_response('getAnnouncement.html',ctx,context_instance=RequestContext(request))


def updateUser(request):
        #print 'in updateUser'
        login_status = True
        updateUser_form = updateUserForm(request.POST)
        if updateUser_form.is_valid():
            email = updateUser_form.cleaned_data['email']
            password = updateUser_form.cleaned_data['password']

            fname = updateUser_form.cleaned_data['fname']
            lname = updateUser_form.cleaned_data['lname']
            request.session["contact_sent"] = True
            updateUser_form_data = {'email': email, 'pwd': password, 'fName': fname, 'lName': lname}
            r = requestsUtil.makePutRequest("user/"+email, data=json.dumps(updateUser_form_data))
            code = r.status_code

            if code == 200:
                error_status = False
                updateUser_status = True
                ctx = {'data': r.json(), 'error_status': error_status, 'updateUser_status': updateUser_status, 'login_status': login_status,"mooc_select":MoocForm(request.session['teamName'])}
                return render_to_response('success.html', ctx, context_instance=RequestContext(request))
            elif code == 500:
                error_status = True
                ctx = {'updateUser_form': updateUser_form, 'error_status': error_status,'login_status': login_status, 'error': 'Internal Error Occurs. Please try after sometime.'}
                return render_to_response('success.html', ctx, context_instance=RequestContext(request))
            elif code == 201:
                error_status = False
                updateUser_status = True
                ctx = {'data': r.json(),'login_status': login_status, 'updateUser_status': updateUser_status, 'error': r.json()}
                return render_to_response('success.html', ctx, context_instance=RequestContext(request))


def addCourse(request):
    addCourse_status = False
    error_status = False
    if request.method == "POST":

        category = request.POST.__getitem__("category")     # comments in addCourse.html
        title = request.POST.__getitem__("title")
        section = request.POST.__getitem__("section")
        dept = request.POST.__getitem__("dept")
        term = request.POST.__getitem__("term")
        year = request.POST.__getitem__("year")
        insName = request.POST.__getitem__("insName")
        insEmail = request.POST.__getitem__("insEmail")
        days = request.POST.__getitem__("days")
        hour1 = request.POST.__getitem__("hour1")
        hour2 = request.POST.__getitem__("hour2")
        Description = request.POST.__getitem__("Description")
        attachment = request.POST.__getitem__("attachment")
        version = request.POST.__getitem__("version")
        global userloginEmail
        #addCourse_form_data = {"email": userloginEmail, "category": category, "title": title, "section": section, "dept": dept, "term": term, "year": year, "instructor": [{"name": insName, "email": insEmail}], "days": [days], "hours": [hour1, hour2], "Description": Description, "attachment": attachment, "version": version}
        addCourse_form_data = {"email": userloginEmail, "category": category, "title": title, "section": section, "dept": dept, "term": term, "year": year, "insName": insName, "insEmail": insEmail, "days": days, "hour1":hour1, "hour2":hour2, "Description": Description, "attachment": attachment, "version": version}
        #r = requestsUtil.makePostRequest("course", data=json.dumps(addCourse_form_data))
        r = requestsUtil.createCourse(addCourse_form_data, request.session['teamName'])
        code = r.status_code
        if code == 201:
            addCourse_status = True
            ctx = {'addCourse_status': addCourse_status, 'error_status': error_status, 'data': r.json()}
            return render_to_response('addCourse.html', ctx, context_instance=RequestContext(request))
        else:
            error_status = True
            addCourse_status = False
            ctx = {'addCourse_status': addCourse_status, 'error_status': error_status, 'error': r.json()} #look for errros
            return render_to_response('addCourse.html', ctx, context_instance=RequestContext(request))
    else:
        r1 = requestsUtil.getCategoryList()
        #r = requests.get("http://localhost:8080/category/list")
        code = r1.status_code
        lst = []
        if code == 200:
            data = ast.literal_eval(json.dumps(r1.json()))
            for record in data:
                temp = record["name"]
                lst.append(temp)
            ctx = {'array': lst }
            return render_to_response('addCourse.html', ctx, context_instance=RequestContext(request))

        else:
            error_status = True
            addCourse_status = False
            ctx = {'addCourse_status': addCourse_status, 'error_status': error_status, 'error': r1.json()} #look for errros
            return render_to_response('addCourse.html', ctx, context_instance=RequestContext(request))


def updateCourse(request):
    if request.method == 'GET':
        courseId = request.GET.__getitem__("courseId")
        r1 = requestsUtil.getCategoryList()
        #r = requests.get("http://localhost:8080/category/list")
        code = r1.status_code
        lst = []
        if code == 200:
            data1 = ast.literal_eval(json.dumps(r1.json()))
        for record in data1:
            temp = record["name"]
            lst.append(temp)

        r = requestsUtil.getCourse(courseId, request.session['teamName'])
        code = r.status_code
        if code == 200:
            error_status = False
            ctx = {'data': r.json(), 'error_status': error_status, 'courseId': courseId, 'array': lst}
            return render_to_response('updateCourse.html', ctx, context_instance=RequestContext(request))

        elif code == 500:
            error_status = True
            ctx = {'data': r.json(), 'error_status': error_status, 'error.msg': 'Internal Error: 500', 'courseId': courseId}
            return render_to_response('updateCourse.html', ctx, context_instance=RequestContext(request))

    elif request.method == 'POST':
        courseId = request.POST.__getitem__("courseId")
        category = request.POST.__getitem__("category")     # comments in addCourse.html
        title = request.POST.__getitem__("title")
        section = request.POST.__getitem__("section")
        dept = request.POST.__getitem__("dept")
        term = request.POST.__getitem__("term")
        year = request.POST.__getitem__("year")
        insName = request.POST.__getitem__("insName")
        insEmail = request.POST.__getitem__("insEmail")
        days = request.POST.__getitem__("days")
        Description = request.POST.__getitem__("Description")
        attachment = request.POST.__getitem__("attachment")
        version = request.POST.__getitem__("version")
        hour1 = request.POST.__getitem__("hour1")
        hour2 = request.POST.__getitem__("hour2")
        updateCourse_form_data = {"category": category, "title": title, "section": section, "dept": dept, "term": term, "year": year, "instructor": [{"name": insName , "email": insEmail}], "days": [days], "hours": [hour1, hour2], "Description": Description,  "attachment": attachment, "version": version}
        #r = requestsUtil.makePutRequest('course/update/'+courseId, data=json.dumps(updateCourse_form_data))
        r = requestsUtil.updateCourse(updateCourse_form_data, courseId, request.session['teamName'])
        code = r.status_code
        if code == 200:
            error_status = False
            ctx = {'data': r.json(), 'error_status': error_status, 'updateCourse_status': True}
            return render_to_response('updateCourse.html', ctx, context_instance=RequestContext(request))

        elif code == 500 or 400 or 404:
            error_status = True
            ctx = {'data': r.json(), 'error_status': error_status, 'error.msg': 'Internal Error: 500'}
            return render_to_response('updateCourse.html', ctx, context_instance=RequestContext(request))


def deleteCourse(request,courseId):
        request.method == 'DELETE'
        deleteCourse_status = False
        #r = requestsUtil.makeDeleteRequest('course/'+courseId)
        r = requestsUtil.deleteCourse(courseId, request.session['teamName'])
        code = r.status_code
        if code == 200:
            error_status = False
            deleteCourse_status = True
            ctx = {'data': r.json(), 'error_status': error_status, 'deleteCourse_status': deleteCourse_status}
            return render_to_response('loggedInIndex.html', ctx, context_instance=RequestContext(request))

        elif code == 500 or 400 or 404:
            error_status = True
            deleteCourse_status = False
            ctx = {'data': r.json(), 'error_status': error_status,'deleteCourse_status': deleteCourse_status, 'error.msg': 'Internal Error: 500'}
            return render_to_response('loggedInIndex.html', ctx, context_instance=RequestContext(request))

def enrollCourse(request):
    if request.method == "POST":
        courseId = request.POST.__getitem__("courseId")
        userEmail = request.POST.__getitem__("userEmail")
        payload = {"email": userEmail, "courseid": courseId}
        #r = requestsUtil.makePutRequest("course/enroll", data=json.dumps(payload))
        r = requestsUtil.enrollCourse(payload, request.session['teamName'])
        code = r.status_code

        if code == 200:
            enroll_status = True
            error_status = False
            r1 =  requestsUtil.getCourse(courseId, request.session['teamName'])
            ctx = {"data1": r.json(), "data": r1.json(), "enroll_status": enroll_status, "error_status": error_status, "courseId": courseId}
            return render_to_response('getCourse.html', ctx, context_instance=RequestContext(request))

        else:
            enroll_status = False
            error_status = True
            ctx = {"data": r.json(), "enroll_status": enroll_status, "error_status": error_status, "courseId": courseId}
            return render_to_response('getCourse.html', ctx, context_instance=RequestContext(request))




def archive(request):
    ctx = {}
    return render_to_response('archive.html', ctx, context_instance=RequestContext(request))



def logout(request):
    error_status = False
    login_status = False
    global userloginEmail
    userloginEmail = None
    ctx = {'error_status': error_status, 'login_status': login_status}
    return render_to_response('loggedOutIndex.html', ctx, context_instance=RequestContext(request))


@login_required
def profile(request):
    ctx = {}
    return render_to_response('profile.html', ctx, context_instance=RequestContext(request))

def addDiscussion(request):
    error_status = False
    login_status = False

    createDiscussion_status = False

    if request.method == "POST":
        addDiscussion_form = addDiscussionForm(request.POST)
        if addDiscussion_form.is_valid():
            courseId=request.POST.__getitem__("courseId")
            title = addDiscussion_form.cleaned_data['title']
            global userloginEmail
            createdby = userloginEmail
            request.session["contact_sent"] = True
            addDiscussion_form_data = {'course_id': courseId , 'title': title, 'created_by': createdby, 'created_at': "", 'updated_at':""}
            #r = requestsUtil.makePostRequest("discussions", data=json.dumps(addDiscussion_form_data))
            r = requestsUtil.createDiscussion(addDiscussion_form_data, request.session['teamName'])

            # r = requests.post("http://localhost:8080/discussions", data=json.dumps(addDiscussion_form_data))

            code = r.status_code

            if code == 201:
                login_status = False
                createDiscussion_status = True
                #r1 = requestsUtil.makeGetRequest("discussion/course/"+courseId)
                r1 = requestsUtil.getDiscussionByCourseId(courseId, request.session['teamName'])

                # r = requestsUtil.makeGetRequest("discussion/Pinnaclediscussion_20", data=json.dumps(addDiscussion_form_data))
                ctx = {'dataDiscussion': r1.json(), 'addDiscussion_form': addDiscussion_form,'error_status': error_status, 'createDiscussion_status': createDiscussion_status}

                return render_to_response('addDiscussion.html', ctx, context_instance=RequestContext(request))
            elif code == 500:
                error_status = True
                ctx = {'addDiscussion_form': addDiscussion_form, 'error_status': error_status,
                       'error': 'Internal Error Occurs. Please try after sometime.'}
                return render_to_response('addDiscussion.html', ctx, context_instance=RequestContext(request))
            elif code == 409:
                error_status = True
                ctx = {'addDiscussion_form': addDiscussion_form, 'error_status': error_status, 'error': r.json()}
                return render_to_response('addDiscussion.html', ctx, context_instance=RequestContext(request))

    else:
        courseId=request.GET.__getitem__("courseId")
        addDiscussion_form = addDiscussionForm()
        #addDiscussion_form_data = {'course_id': ""}
        #r2 = requestsUtil.makeGetRequest("discussion/course/"+courseId)
        r2 = requestsUtil.getDiscussionByCourseId(courseId, request.session['teamName'])
        # ' dataDiscussion': r1.json()
        ctx = {'dataDiscussion': r2.json(), 'addDiscussion_form': addDiscussion_form, 'error_status': error_status, 'courseId': courseId}
        return render_to_response('addDiscussion.html', ctx, context_instance=RequestContext(request))


def addMessage(request,discussionId):
    error_status = False
    login_status = False
    createDiscussion_status = False

    if request.method == "POST":
        DiscussionSuccess_form = DiscussionSuccessForm(request.POST)
        if DiscussionSuccess_form.is_valid():
            title = DiscussionSuccess_form.cleaned_data['title']
            content = DiscussionSuccess_form.cleaned_data['content']
            global userloginEmail
            createdby = userloginEmail
            request.session["contact_sent"] = True
            DiscussionSuccess_form_data = {'title':title , 'content':content, 'created_by': createdby, 'created_at':"",'updated_at':""}

            r = requestsUtil.createMessage(DiscussionSuccess_form_data, discussionId, request.session['teamName'])
            #r = requestsUtil.makePostRequest("discussion/"+discussionId+"/messages", data=json.dumps(DiscussionSuccess_form_data))
            code = r.status_code

            if code == 201:
                login_status = False
                createDiscussion_status = True

                #r2 = requestsUtil.makeGetRequest("discussion/"+discussionId)
                r2 = requestsUtil.getDiscussion(discussionId, request.session['teamName'])

                #r1 = requestsUtil.makeGetRequest("discussion/"+discussionId+"/messages")
                r1 = requestsUtil.getMessagesList(discussionId, request.session['teamName'])
                ctx = {'data':r2.json(),'dataMessage':r1.json(),'error_status': error_status, 'createDiscussion_status': createDiscussion_status}

                return render_to_response('DiscussionSuccess.html', ctx, context_instance=RequestContext(request))
            elif code == 500:
                error_status = True
                ctx = {'DiscussionSuccess_form': DiscussionSuccess_form, 'error_status': error_status,
                       'error': 'Internal Error Occurs. Please try after sometime.'}
                return render_to_response('addDiscussion.html', ctx, context_instance=RequestContext(request))
            elif code == 409:
                error_status = True
                ctx = {'DiscussionSuccess_form': DiscussionSuccess_form, 'error_status': error_status, 'error': r.json()}
                return render_to_response('addDiscussion.html', ctx, context_instance=RequestContext(request))

    else:

        DiscussionSuccess_form = DiscussionSuccessForm()

        #r3 = requestsUtil.makeGetRequest("discussion/"+discussionId)
        r3 = requestsUtil.getDiscussion(discussionId, request.session['teamName'])

        r1 = requestsUtil.getMessagesList(discussionId, request.session['teamName'])
        #r1 = requestsUtil.makeGetRequest("discussion/"+discussionId+"/messages")


    ctx = {'discussionId':discussionId,'data':r3.json(),'dataMessage':r1.json(),'DiscussionSuccess_form': DiscussionSuccess_form, 'error_status': error_status}
    return render_to_response('DiscussionSuccess.html', ctx, context_instance=RequestContext(request))


