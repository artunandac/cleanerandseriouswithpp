from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

from django.shortcuts import get_object_or_404
from django.http import Http404

from .models import Card


from django.core.files.uploadhandler import FileUploadHandler

# Create your views here.


def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password  = request.POST['password']

        user = auth.authenticate(username= username, password = password)
        if user is not None:
            auth.login(request, user)
            messages.add_message(request, messages.SUCCESS,'Oturum açıldı.')
            return redirect('index')
        else:
            messages.add_message(request, messages.ERROR, 'Hatalı username yada parola')
            return redirect('login')
    else:
        return render(request, 'card/login.html')

def register(request):
    if request.method == 'POST':
        
        # get form values
        username = request.POST['username']
        cardcode = request.POST['cardcode']
        name = request.POST['name']
        position = request.POST['position']
        company = request.POST['company']
        website =  request.POST['website']
        email = request.POST['email']
        gsm = request.POST['gsm']
        fax =  request.POST['fax']
        instagram = request.POST['instagramacc']
        twitter = request.POST['twitteracc']
        linkedin = request.POST['linkedinacc']
        email = request.POST['email']

        profilepic = request.FILES['profilephoto']
        
        password = request.POST['password']
        repassword = request.POST['repassword']
        if password == repassword:
            # Username
            if User.objects.filter(username = username).exists():
                messages.add_message(request, messages.WARNING, 'Bu kullanıcı adı daha önce alınmış.')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password= password,email=email)
                user.save()
                card = get_object_or_404(Card, cardcode = cardcode)#Card.objects.filter(cardcode = cardcode)
                card.owner, card.name, card.position, card.company, card.website, card.mail, card.gsm, card.fax, card.instagramacc, card.twitteracc, card.linkedinacc, card.profilepic = username, name, position, company, website, email, gsm, fax, instagram, twitter, linkedin, profilepic
                card.owner = username
                card.save()
                messages.add_message(request, messages.SUCCESS, 'Hesabınız oluşturuldu.')
                return redirect('login')
        else:            
            print('parolalar eşleşmiyor')
            return redirect('register')
    else:
        return render(request, 'card/register.html')
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.add_message(request, messages.SUCCESS, 'Oturumunuz kapatıldı.')
        return redirect('index')
def carddetail(request, card_id):
    card = get_object_or_404(Card, pk = card_id)
    # print(card.id)
    # card.id = 1
    # print(card.id)
    # card = Card.objects.get(cardid = card_id)
    if card.owner=="":
        return redirect('register')

    else:
        context = {
            'card': card
        }
        return render(request, 'pages/detail.html', context)

def editcard(request):
    if request.method == 'POST':
        # get form values
        name = request.POST['name']
        position = request.POST['position']
        company = request.POST['company']
        website =  request.POST['website']
        email = request.POST['email']
        gsm = request.POST['gsm']
        fax =  request.POST['fax']
        instagram = request.POST['instagramacc']
        twitter = request.POST['twitteracc']
        linkedin = request.POST['linkedinacc']
        email = request.POST['email']
        profilepic = request.FILES['profilepic']
        username = request.POST['username']
        password  = request.POST['password']
        #editcardinfos
        user = auth.authenticate(username= username, password = password)
        card = get_object_or_404(Card, owner = user)#Card.objects.filter(cardcode = cardcode)
        cardlist = [card.name, card.position, card.company, card.website, card.mail, card.gsm, card.fax, card.instagramacc, card.twitteracc, card.linkedinacc, card.profilepic]
        postlist =[name, position, company, website, email, gsm, fax, instagram, twitter, linkedin, profilepic]
        #card.name, card.position, card.company, card.website, card.mail, card.gsm, card.fax, card.instagramacc, card.twitteracc, card.linkedinacc = name, position, company, website, email, gsm, fax, instagram, twitter, linkedin
        for i in range(len(postlist)):
            if postlist[i] == '':
                None
            else:
                print(postlist[i])
                cardlist[i] = postlist[i]
        card.name, card.position, card.company, card.website, card.mail, card.gsm, card.fax, card.instagramacc, card.twitteracc, card.linkedinacc, card.profilepic = cardlist
        if user is not None:
            card.save()
            messages.add_message(request, messages.SUCCESS, 'Bilgiler Güncellendi.')
            return redirect('index')
        else:
            messages.add_message(request, messages.ERROR, 'Hatalı username yada parola')
            return redirect('editcardinfos')
    else:
        return render(request, 'card/editcardinfos.html')
    # # if request.method == 'POST':
    # #     form = CardEditForm(request.POST, request.FILES)
    # #     if form.is_valid():
    # #         print(form)
    # #         form.save()
    # #         messages.add_message(request, messages.SUCCESS, 'Bilgiler Güncellendi.')
    # #         return redirect('index')
    # # else:
    # #     form = CardEditForm()
    # #     return render(request, 'card/editcardinfos.html', {'form' : form})

