# from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request,'home.html')


def count(request):
    user_text=request.GET['text']
    total_count=len(user_text)
    word_dict={}
    for word in user_text:
        if word not in word_dict:
            word_dict[word]=1
        else:
            word_dict[word]+=1
    sorted_dict=\
            sorted(word_dict.items(),key=lambda x:x[1],reverse=True)#按第二个元素排序


    return render(request,'count1.html',
                 {'count':total_count,'text':user_text,'worddict':word_dict,'sorted':sorted_dict})
##通过字典传递值给html文件。

def about(request):
    return render(request,'about.html')