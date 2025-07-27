from django.shortcuts import redirect, render
from django.contrib.auth.hashers import check_password

from django.contrib import auth, messages
from apps.login.models import Usuario as User

from apps.login.forms import CadastroForm, LoginForm

# Create your views here.
def login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            email_login = form.cleaned_data['email_login']
            senha_login = form.cleaned_data['senha_login']

            try:
                usuario = User.objects.get(email=email_login) # Obtendo o usuário pelo email
                if not check_password(senha_login, usuario.senha): 
                    messages.error(request, 'Senha incorreta.')
                    return redirect('login')
                
                request.session['usuario_id'] = usuario.idusuario
                return redirect('index')
            except User.DoesNotExist:
                form.add_error('email_login', 'Usuário não encontrado.')
        
    return render(request, 'login/index.html', {"form": form}) # passandi o form para pagina de login

#cria o cadastro do usuario baseado no form modelo
def cadastro(request):
    form = CadastroForm()

    if request.method == "POST":
        form = CadastroForm(request.POST)
        
        if form.is_valid():
            email = form['email_cadastro'].value()

            if User.objects.filter(email=email).exists():
                messages.error(request, 'Usuário já existente.')
                return redirect('cadastro')
            
            usuario = form.save(commit=False)

            usuario.save()

        
            messages.success(request, 'Cadastro efetuado com sucesso!')
            return redirect('login')
        else:
            for erro in form.errors:
                messages.error(request, form.errors[erro])
    return render(request, 'login/cadastro.html', {"form": form})

def logout(request):
    if request.method == 'GET':
        request.session.flush()  # Clear the session data
        messages.success(request, 'Logout efetuado com sucesso!')
    return redirect('login')  # Redirect to the index page after logout

  # Render a protected page