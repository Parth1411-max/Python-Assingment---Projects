from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models  import *
from random import randint



# Create your views here.

def home(request):

    if "email" in request.session:
        uid=user.objects.get(email=request.session["email"])
        if uid.role=="chairman":
            cid = chairman.objects.get(user_id = uid)

            context={
                "uid":uid,
                "cid":cid,
            }
            return render(request,'myapp/index.html',context)
        else:
            pass
    else:
        return render(request,'myapp/login.html')


def login(request):
    if "email" in request.session:
        return redirect("home")

    if request.POST:
        p_email = request.POST['email']   # p_email is python varibale /////  email is HTML variable # 
        p_password = request.POST['password']

        try:
            uid=user.objects.get(email = p_email)
            if uid.password == p_password:
                cid = chairman.objects.get(user_id = uid)
                print("---> firstname =",cid.firstname)
                request.session["email"]=p_email
                
                context={
                    "uid":uid,
                    "cid":cid,
                }
                return render(request,"myapp/index.html",context)
            else:
                context={
                    "e_msg":"INVALID PASSWORD"
                }
                return render(request,"myapp/login.html",context)

        except Exception as e:
            print("--->exception",e)
            context={
                "e_msg":"INVALID EMAIL ADDRESS"
             }
            return render(request,"myapp/login.html",context)
        
        # except user.DoesNotExist:
        #      print(" User Does Not Exist here")
        #      return render(request,"myapp/login.html")


        # print("----> Email", p_email)
        # print("--->Password",p_password)
        
    else:
        print("---> Page Just Loaded")
        return render(request,'myapp/login.html')


def logout(request):
    if "email" in request.session:
        del request.session["email"]
        return render(request,'myapp/login.html')
    else:
        return render(request,'myapp/login.html')


def profile(request):
    if "email" in request.session:
        uid=user.objects.get(email=request.session['email'])
        
        if uid.role=="chairman":
            cid=chairman.objects.get(user_id=uid)
            context={
                "uid":uid,
                "cid":cid,
            }

            return render(request,'myapp/profile.html',context)


def change_password(request):
    if 'email' in request.session:


        if request.POST:
            currentpassword=request.POST['currentpassword']
            new_password=request.POST['new_password']

            uid=user.objects.get(email=request.session['email'])
            cid=chairman.objects.get(user_id=uid)

            if uid.password == currentpassword:
                uid.password=new_password
                uid.save()

                context={
                    'uid':uid,
                    'cid':cid,
                    'msg':"Successfully password reset"
                }
                return render(request,'myapp/profile.html',context)

            else:
                cid=chairman.objects.get(user_id=uid)
                context={
                "uid":uid,
                "cid":cid,
                'msg':" INVALID PASSWORD "
            }
            return render(request,'myapp/profile.html',context)
        else:
            return redirect("login")


def edit_profile(request):
    if request.POST:
        uid=user.objects.get(email=request.session['email'])
       

        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        contect=request.POST['contect']
        block_no=request.POST['block_no']
        house_no=request.POST['house_no']
        about_me=request.POST['about_me']
        pic =request.FILES['pic']
        
        cid=chairman.objects.get(user_id=uid)

        if cid:
            cid.firstname=firstname
            cid.lastname=lastname
            cid.contect=contect
            cid.block_no=block_no
            cid.house_no=house_no
            cid.about_me=about_me
            if "pic" in request.FILES:
                cid.pic=pic
                cid.save()
            context={
                'uid':uid,
                'cid':cid,
            }

            return render(request, 'myapp/profile.html',context)
        else:
            print("Chairmn not found")
            return redirect("profile")
    else:
        print("DATA not found")
        return redirect("login")


def add_member(request):    

        if "email" in request.session:
            uid=user.objects.get(email=request.session['email'])
            cid=chairman.objects.get(user_id=uid)

            if request.POST:
                    firstname=request.POST['firstname']
                    lastname=request.POST['lastname']
                    email=request.POST['email']
                    contect=request.POST['contect']
                    DOB=request.POST['DOB']
                    totalvehicle=request.POST['totalvehicle']
                    familymember=request.POST['familymember']
                    gender=request.POST['gender']
                    workinfo=request.POST['workinfo']
                    pic=request.POST['pic']

                    addmember=member.objects.create(firstname=firstname,
                                                    lastname=lastname,
                                                    email=email,
                                                    contect=contect,
                                                    DOB=DOB,
                                                    totalvehicle=totalvehicle,
                                                    familymember=familymember,
                                                    gender=gender,
                                                    workinfo=workinfo,
                                                    pic=pic)
                    
                    context={
                                'uid':uid,
                                'cid':cid,
                                'addmember':addmember
                            }
                    return render(request,'myapp/add_member.html',context)

            else:
                     context={
                                'uid':uid,
                                'cid':cid,
                            }
            
            return render(request,'myapp/add_member.html',context)


def add_notice(request):

    if 'email' in request.session:

        uid=user.objects.get(email=request.session['email'])
        cid=chairman.objects.get(user_id=uid)

        if request.POST:
            notice_title = request.POST["notice_title"]
            notice_content = request.POST["notice_content"]
            img = request.FILES.get('img')
            video = request.FILES.get('video')
            
            nid=notice.objects.create(user_id=chairman.objects.get(firstname=cid.firstname),
                                         notice_title=notice_title,
                                         notice_content=notice_content,
                                         img=img,
                                         video=video
                                        )
            if nid:
                
                context={
                    'uid':uid,
                    'cid':cid,
                }

                return render(request,'myapp/add_notice.html',context)

            else:
                context={
                    'uid':uid,
                    'cid':cid,
                }

                return render(request,'myapp/add_notice.html')

        else:
            context={
                    'uid':uid,
                    'cid':cid,
                    }            
            return render(request,'myapp/add_notice.html',context)

    else:
        return render(request, "myapp/login.html")


def all_notice(request):

    if 'email' in request.session:
        uid=user.objects.get(email=request.session['email'])

        if uid.role == "chairman":

            cid=chairman.objects.get(user_id=uid)
        
            nid=notice.objects.all()
            
            context={
                'uid':uid,
                'cid':cid,
                'nid':nid
                }
            return render(request,'myapp/all_notice.html',context)
        
        else:
            return render(request,'myapp/all_notice.html',context)
    else:
        return redirect("login")


def add_events(request):

    if 'email' in request.session:

        uid=user.objects.get(email=request.session['email'])
        cid=chairman.objects.get(user_id=uid)

        if request.POST:
            events_title = request.POST["events_title"]
            events_content = request.POST["events_content"]
            img = request.FILES.get('img')
            video = request.FILES.get('video')
            
            eid=events.objects.create(user_id=chairman.objects.get(firstname=cid.firstname),
                                         events_title=events_title,
                                         events_content=events_content,
                                         img=img,
                                         video=video
                                        )
            if eid:
                
                context={
                    'uid':uid,
                    'cid':cid,
                }

                return render(request,'myapp/add_events.html',context)

            else:
                context={
                    'uid':uid,
                    'cid':cid,
                }

                return render(request,'myapp/add_events.html')

        else:
            context={
                    'uid':uid,
                    'cid':cid,
                    }            
            return render(request,'myapp/add_events.html',context)

    else:
        return render(request, "myapp/login.html")

def all_events(request):

    if 'email' in request.session:
        uid=user.objects.get(email=request.session['email'])

        if uid.role == "chairman":

            cid=chairman.objects.get(user_id=uid)
        
            eid=events.objects.all()
            
            context={
                'uid':uid,
                'cid':cid,
                'eid':eid
                }
            return render(request,'myapp/all_events.html',context)
        
        else:
            return render(request,'myapp/all_events.html',context)
    else:
        return redirect("login")

   
def member(request):
    return render(request,'myapp/member.html')

   

        

