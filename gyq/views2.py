from django.shortcuts import render
from django.http import HttpResponse
import json
import os
import pandas as pd
def totojson(pdData,name,flag): #1=data.json,2=login.json
    if flag==2:
        with open(name, 'w',encoding='utf-8') as f:
            f.write("[\n")
            for i in range(len(pdData)):
                if i!= (len(pdData)-1):
                    tmp="{"+"\"username\":\""+pdData.loc[i]["username"]+"\",\"password\": \""+pdData.loc[i]["password"]+"\",\"authority\": \""+pdData.loc[i]["authority"]+"\",\"name\": \""+pdData.loc[i]["name"]+"\",\"address\": \""+pdData.loc[i]["address"]+"\",\"charger\" : \""+pdData.loc[i]["charger"]+"\",\"phone\": \""+pdData.loc[i]["phone"]+"\",\"email\": \""+pdData.loc[i]["email"]+"\"},\n"
                else:
                    tmp="{"+"\"username\":\""+pdData.loc[i]["username"]+"\",\"password\": \""+pdData.loc[i]["password"]+"\",\"authority\": \""+pdData.loc[i]["authority"]+"\",\"name\": \""+pdData.loc[i]["name"]+"\",\"address\": \""+pdData.loc[i]["address"]+"\",\"charger\" : \""+pdData.loc[i]["charger"]+"\",\"phone\": \""+pdData.loc[i]["phone"]+"\",\"email\": \""+pdData.loc[i]["email"]+"\"}"
                f.write(tmp)
            f.write("\n]")
    else:
        with open(name, 'w',encoding='utf-8') as f:
            f.write("[\n")
            for i in range(len(pdData)):
                if i!= (len(pdData)-1):
                    tmp="{"+"\"client_num\":\""+pdData.loc[i]["client_num"]+"\",\"education_level\": \""+pdData.loc[i]["education_level"]+"\",\"marital_status\": \""+pdData.loc[i]["marital_status"]+"\",\"income_category\": \""+pdData.loc[i]["income_category"]+"\",\"gender\": \""+pdData.loc[i]["gender"]+"\",\"age\" : \""+pdData.loc[i]["age"]+"\",\"credit_limit\": \""+pdData.loc[i]["credit_limit"]+"\",\"total_trans_amt\" : \""+pdData.loc[i]["total_trans_amt"]+"\",\"avg_utilization_ratio\": \""+pdData.loc[i]["avg_utilization_ratio"]+"\",\"flag\": \""+pdData.loc[i]["flag"]+"\"},\n"
                else:
                    tmp="{"+"\"client_num\":\""+pdData.loc[i]["client_num"]+"\",\"education_level\": \""+pdData.loc[i]["education_level"]+"\",\"marital_status\": \""+pdData.loc[i]["marital_status"]+"\",\"income_category\": \""+pdData.loc[i]["income_category"]+"\",\"gender\": \""+pdData.loc[i]["gender"]+"\",\"age\" : \""+pdData.loc[i]["age"]+"\",\"credit_limit\": \""+pdData.loc[i]["credit_limit"]+"\",\"total_trans_amt\" : \""+pdData.loc[i]["total_trans_amt"]+"\",\"avg_utilization_ratio\": \""+pdData.loc[i]["avg_utilization_ratio"]+"\",\"flag\": \""+pdData.loc[i]["flag"]+"\"}"
                f.write(tmp)
            f.write("\n]")
def index(request):
    return render(request, 'index.html')
def main_1(request):
    username_input=request.GET.get('username')
    return render(request, 'main_1.html', {"username_input":username_input})
def main_2(request):
    username_input=request.GET.get('username')
    return render(request, 'main_2.html', {"username_input":username_input})

def students_add(request):
    return render(request, 'students_add.html')
def allwords_add(request):
    return render(request, 'allwords_add.html')
def results_add(request):
    return render(request, 'results_add.html')
def testwords_add(request):
    return render(request, 'testwords_add.html')
def results_manage(request):
    username_input=request.GET.get('username')
    return render(request, 'results_manage.html', {"username_input":username_input})
def testwords_manage(request):
    username_input=request.GET.get('username')
    return render(request, 'testwords_manage.html', {"username_input":username_input})


def login_add(request):
    return render(request, 'login_add.html')

def students_manage(request):
    username_input=request.GET.get('username')
    return render(request, 'students_manage.html', {"username_input":username_input})
def allwords_manage(request):
    username_input=request.GET.get('username')
    return render(request, 'allwords_manage.html', {"username_input":username_input})
def exam_manage(request):
    username_input=request.GET.get('username')
    return render(request, 'exam_manage.html', {"username_input":username_input})
def results_manage(request):
    username_input=request.GET.get('username')
    return render(request, 'results_manage.html', {"username_input":username_input})
def testwords_manage(request):
    username_input=request.GET.get('username')
    return render(request, 'testwords_manage.html', {"username_input":username_input})


def login_manage(request):
    username_input=request.GET.get('username')
    return render(request, 'login_manage.html', {"username_input":username_input})
def persional(request):
    user=request.GET.get('username')
    file_name=os.path.dirname(os.path.abspath('__file__'))+"\\statics\\html\\data\\login.json"
    data = open(file_name,'r',encoding='utf-8')
    jsonData = json.load(data)
    pdData=pd.DataFrame(jsonData)
    user=str(user)
    a=list(pdData[pdData["username"]==user]["username"])[0]
    return_param={
        "username": list(pdData[pdData["username"]==user]["username"])[0],
        "password": list(pdData[pdData["username"]==user]["password"])[0],
        "authority": list(pdData[pdData["username"]==user]["authority"])[0],
        "name": list(pdData[pdData["username"]==user]["name"])[0],
        "address": list(pdData[pdData["username"]==user]["address"])[0],
        "charger" : list(pdData[pdData["username"]==user]["charger"])[0],
        "phone":list(pdData[pdData["username"]==user]["phone"])[0],
        "email": list(pdData[pdData["username"]==user]["email"])[0]
    }
    return render(request, 'grzl.html', return_param)
def xgmm(request):
    user=request.GET.get('username')
    file_name=os.path.dirname(os.path.abspath('__file__'))+"\\statics\\html\\data\\login.json"
    data = open(file_name,'r',encoding='utf-8')
    jsonData = json.load(data)
    pdData=pd.DataFrame(jsonData)
    user=str(user)
    a=list(pdData[pdData["username"]==user]["username"])[0]
    return_param={
        "username": list(pdData[pdData["username"]==user]["username"])[0],
        "password": list(pdData[pdData["username"]==user]["password"])[0],
        "authority": list(pdData[pdData["username"]==user]["authority"])[0],
        "name": list(pdData[pdData["username"]==user]["name"])[0],
        "address": list(pdData[pdData["username"]==user]["address"])[0],
        "charger" : list(pdData[pdData["username"]==user]["charger"])[0],
        "phone":list(pdData[pdData["username"]==user]["phone"])[0],
        "email": list(pdData[pdData["username"]==user]["email"])[0]
    }
    return render(request, 'xgmm.html', return_param)

def students_updata(request):
    xueshengbianhao = str(request.GET.get('xueshengbianhao'))
    file_name = os.path.dirname(os.path.abspath('__file__')) + "\\statics\\html\\data\\students.json"
    data = open(file_name, 'r', encoding='utf-8')
    jsonData = json.load(data)
    pdData = pd.DataFrame(jsonData)
    return_param = {
        "xueshengbianhao": list(pdData[pdData["xueshengbianhao"] == xueshengbianhao]["xueshengbianhao"])[0],
        "shengfen": list(pdData[pdData["xueshengbianhao"] == xueshengbianhao]["shengfen"])[0],
        "chengshi": list(pdData[pdData["xueshengbianhao"] == xueshengbianhao]["chengshi"])[0],
        "nianji": list(pdData[pdData["xueshengbianhao"] == xueshengbianhao]["nianji"])[0],
        "jiaocaibanben": list(pdData[pdData["xueshengbianhao"] == xueshengbianhao]["jiaocaibanben"])[0],
        "zhuceriqi": list(pdData[pdData["xueshengbianhao"] == xueshengbianhao]["zhuceriqi"])[0]
    }
    return render(request, 'students_updata.html', return_param)
def allwords_updata(request):
    cihuibianhao = str(request.GET.get('cihuibianhao'))
    file_name = os.path.dirname(os.path.abspath('__file__')) + "\\statics\\html\\data\\allwords.json"
    data = open(file_name, 'r', encoding='utf-8')
    jsonData = json.load(data)
    pdData = pd.DataFrame(jsonData)
    return_param = {
        "xueduan": list(pdData[pdData["cihuibianhao"] == cihuibianhao]["xueshengbianhao"])[0],
        "banben": list(pdData[pdData["cihuibianhao"] == cihuibianhao]["banben"])[0],
        "jiaocaimingcheng": list(pdData[pdData["cihuibianhao"] == cihuibianhao]["jiaocaimingcheng"])[0],
        "danyuan": list(pdData[pdData["cihuibianhao"] == cihuibianhao]["danyuan"])[0],
        "cihuibianhao": list(pdData[pdData["cihuibianhao"] == cihuibianhao]["cihuibianhao"])[0],
        "cizubianhao": list(pdData[pdData["cihuibianhao"] == cihuibianhao]["cizubianhao"])[0],
        "cihui": list(pdData[pdData["cihuibianhao"] == cihuibianhao]["cihui"])[0],
        "cixing": list(pdData[pdData["cihuibianhao"] == cihuibianhao]["cixing"])[0],
        "erjicixing": list(pdData[pdData["cihuibianhao"] == cihuibianhao]["erjicixing"])[0],
        "ciyi": list(pdData[pdData["cihuibianhao"] == cihuibianhao]["ciyi"])[0]
    }
    return render(request, 'students_updata.html', return_param)



def login_updata(request):
    username=str(request.GET.get('username'))
    file_name=os.path.dirname(os.path.abspath('__file__'))+"\\statics\\html\\data\\login.json"
    data = open(file_name,'r',encoding='utf-8')
    jsonData = json.load(data)
    pdData=pd.DataFrame(jsonData)
    return_param={
        "username": list(pdData[pdData["username"]==username]["username"])[0],
        "password": list(pdData[pdData["username"]==username]["password"])[0],
        "authority": list(pdData[pdData["username"]==username]["authority"])[0],
        "name": list(pdData[pdData["username"]==username]["name"])[0],
        "address": list(pdData[pdData["username"]==username]["address"])[0],
        "charger" : list(pdData[pdData["username"]==username]["charger"])[0],
        "phone":list(pdData[pdData["username"]==username]["phone"])[0],
        "email": list(pdData[pdData["username"]==username]["email"])[0]
    }
    return render(request, 'login_updata.html', return_param)

def students_json(request):
    file_name=os.path.dirname(os.path.abspath('__file__'))+"\\statics\\html\\data\\students.json"
    data = open(file_name,'r',encoding='utf-8')
    jsonData = json.load(data)
    #return_param={'status':["500"]}
    return HttpResponse(json.dumps(jsonData))

def login_json(request):
    file_name=os.path.dirname(os.path.abspath('__file__'))+"\\statics\\html\\data\\login.json"
    data = open(file_name,'r',encoding='utf-8')
    jsonData = json.load(data)
    #return_param={'status':["500"]}
    return HttpResponse(json.dumps(jsonData))
def axis_students(request): #"1"=新增 "2"="修改" "3"="删除"
    file_name=os.path.dirname(os.path.abspath('__file__'))+"\\statics\\html\\data\\students.json"
    data = open(file_name,'r',encoding='utf-8')
    jsonData = json.load(data)
    pdData=pd.DataFrame(jsonData)
    tag = str(request.POST.get('tag', 0))

    if tag == "1":
        xueshengbianhao = str(request.POST.get('xueshengbianhao', 0))
        shengfen = str(request.POST.get('shengfen', 0))
        chengshi = str(request.POST.get('chengshi', 0))
        nianji = str(request.POST.get('nianji', 0))
        jiaocaibanben = str(request.POST.get('jiaocaibanben', 0))
        zhuceriqi = str(request.POST.get('zhuceriqi', 0))

        new = pd.DataFrame({
            'xueshengbianhao': xueshengbianhao,
            'shengfen': shengfen,
            'chengshi': chengshi,
            'nianji': nianji,
            'jiaocaibanben': jiaocaibanben,
            'zhuceriqi': zhuceriqi
        }, index=[1])
        pdData = pdData.append(new, ignore_index=True)
    elif tag == "2":
        xueshengbianhao = str(request.POST.get('xueshengbianhao', 0))
        shengfen = str(request.POST.get('shengfen', 0))
        chengshi = str(request.POST.get('chengshi', 0))
        nianji = str(request.POST.get('nianji', 0))
        jiaocaibanben = str(request.POST.get('jiaocaibanben', 0))
        zhuceriqi = str(request.POST.get('zhuceriqi', 0))

        pdData.loc[pdData["xueshengbianhao"] == xueshengbianhao, "shengfen"] = shengfen
        pdData.loc[pdData["xueshengbianhao"] == xueshengbianhao, "chengshi"] = chengshi
        pdData.loc[pdData["xueshengbianhao"] == xueshengbianhao, "nianji"] = nianji
        pdData.loc[pdData["xueshengbianhao"] == xueshengbianhao, "jiaocaibanben"] = jiaocaibanben
        pdData.loc[pdData["xueshengbianhao"] == xueshengbianhao, "zhuceriqi"] = zhuceriqi
    else:
        xueshengbianhao = str(request.POST.get('xueshengbianhao', 0))
        xueshengbianhao = json.loads(xueshengbianhao)
        for i in range(len(xueshengbianhao)):
            index_num = pdData.loc[pdData['xueshengbianhao'] == xueshengbianhao[i]].index[0]
            pdData = pdData.drop(labels=index_num, axis=0)
        pdData = pdData.reset_index(drop=True)

        # 将修改后的数据写入JSON文件
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(pdData.to_dict(orient='records'), f, ensure_ascii=False, indent=4)
    return_param={"result": "1"}
    return HttpResponse(json.dumps(return_param))

def axis_manage_login(request): #"1"=新增 "2"="修改" "3"="删除"
    file_name=os.path.dirname(os.path.abspath('__file__'))+"\\statics\\html\\data\\login.json"
    data = open(file_name,'r',encoding='utf-8')
    jsonData = json.load(data)
    pdData=pd.DataFrame(jsonData)
    tag = str(request.POST.get('tag', 0))
    
    if(tag=="1"):
        username = str(request.POST.get('username', 0))
        password = str(request.POST.get('password', 0))
        authority = str(request.POST.get('authority', 0))
        name = str(request.POST.get('name', 0))
        address = str(request.POST.get('address', 0))
        charger = str(request.POST.get('charger', 0))
        phone = str(request.POST.get('phone', 0))
        email = str(request.POST.get('email', 0))
        new=pd.DataFrame({'username':username,
                  'password':password,
                  'authority':authority,
                  'name':name,
                  'address':address,
                 'charger':charger,
                  'phone':phone,
                  'email':email}, index=[1])
        pdData=pdData.append(new,ignore_index=True)
    elif(tag=="2"):
        username = str(request.POST.get('username', 0))
        password = str(request.POST.get('password', 0))
        authority = str(request.POST.get('authority', 0))
        name = str(request.POST.get('name', 0))
        address = str(request.POST.get('address', 0))
        charger = str(request.POST.get('charger', 0))
        phone = str(request.POST.get('phone', 0))
        email = str(request.POST.get('email', 0))

        pdData.loc[pdData["username"]==username,"password"]=password
        pdData.loc[pdData["username"]==username,"authority"]=authority
        pdData.loc[pdData["username"]==username,"name"]=name
        pdData.loc[pdData["username"]==username,"address"]=address
        pdData.loc[pdData["username"]==username,"charger"]=charger
        pdData.loc[pdData["username"]==username,"phone"]=phone
        pdData.loc[pdData["username"]==username,"email"]=email
    else:
        username = str(request.POST.get('username', 0))
        username=json.loads(username)
        for i in range(len(username)):
            index_num=pdData.loc[pdData['username']==username[i]].index[0]
            pdData=pdData.drop(labels=index_num,axis=0)
        pdData=pdData.reset_index(drop=True)

    totojson(pdData,file_name,2)
    return_param={"result": "1"}
    return HttpResponse(json.dumps(return_param))
def axis_login(request):
    return_param={'result':0,'authority':0}
    user = request.POST.get('username', 0)
    psd = request.POST.get('password', 0)
    file_name=os.path.dirname(os.path.abspath('__file__'))+"\\statics\\html\\data\\login.json"
    data = open(file_name,'r',encoding='utf-8')
    jsonData = json.load(data)
    pdData=pd.DataFrame(jsonData)
    try:
        if list(pdData[pdData["username"]==user]["password"]==psd)[0] :
            return_param={'result':1,'authority':list(pdData[pdData["username"]==user]['authority'])[0]}
        else:
            return_param={'result':0,'authority':0}
    except:
        return_param={'result':0,'authority':0}
    return HttpResponse(json.dumps(return_param))
def axis_persional(request):
    a = str(request.POST.get('username', 0))
    b = str(request.POST.get('password', 0))
    c = str(request.POST.get('authority', 0))
    d = str(request.POST.get('name', 0))
    e = str(request.POST.get('address', 0))
    f = str(request.POST.get('charger', 0))
    g = str(request.POST.get('phone', 0))
    h = str(request.POST.get('email', 0))
    file_name=os.path.dirname(os.path.abspath('__file__'))+"\\statics\\html\\data\\login.json"
    data = open(file_name,'r',encoding='utf-8')
    jsonData = json.load(data)
    pdData=pd.DataFrame(jsonData)
    pdData.loc[pdData["username"]==a,"password"]=b
    pdData.loc[pdData["username"]==a,"authority"]=c
    pdData.loc[pdData["username"]==a,"name"]=d
    pdData.loc[pdData["username"]==a,"address"]=e
    pdData.loc[pdData["username"]==a,"charger"]=f
    pdData.loc[pdData["username"]==a,"phone"]=g
    pdData.loc[pdData["username"]==a,"email"]=h
    totojson(pdData,file_name,2)
    return_param={"result": "1"}
    return HttpResponse(json.dumps(return_param))
def axis_xgmm(request):
    a = str(request.POST.get('username', 0))
    b = str(request.POST.get('password', 0))
    c = str(request.POST.get('authority', 0))
    d = str(request.POST.get('name', 0))
    e = str(request.POST.get('address', 0))
    f = str(request.POST.get('charger', 0))
    g = str(request.POST.get('phone', 0))
    h = str(request.POST.get('email', 0))
    file_name=os.path.dirname(os.path.abspath('__file__'))+"\\statics\\html\\data\\login.json"
    data = open(file_name,'r',encoding='utf-8')
    jsonData = json.load(data)
    pdData=pd.DataFrame(jsonData)
    pdData.loc[pdData["username"]==a,"password"]=b
    pdData.loc[pdData["username"]==a,"authority"]=c
    pdData.loc[pdData["username"]==a,"name"]=d
    pdData.loc[pdData["username"]==a,"address"]=e
    pdData.loc[pdData["username"]==a,"charger"]=f
    pdData.loc[pdData["username"]==a,"phone"]=g
    pdData.loc[pdData["username"]==a,"email"]=h
    totojson(pdData,file_name,2)
    return_param={"result": "1"}
    return HttpResponse(json.dumps(return_param))