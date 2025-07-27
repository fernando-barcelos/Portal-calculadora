from django import forms
from apps.login.models import Usuario  # Importando o modelo de usuário personalizado
from django.contrib.auth.hashers import make_password


#classe de referencia para usno formulario de login
class LoginForm(forms.Form):
    email_login = forms.CharField(
        label='Email de login.',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex fulano@gmail.com'
            }
        )
    )

    senha_login=forms.CharField(
        label='Senha',
        required=True,
        max_length=15,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha.',
            }
        )
    )

    class Meta:
        model = Usuario
        fields = ['email_login', 'senha_login']

#classe de referencia para ser usada no formulario de cadastro
class CadastroForm(forms.ModelForm):

    nome_cadastro=forms.CharField(
        label='Digite seu nome.',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'João Silva',
            }
        )
    )

    email_cadastro=forms.EmailField(
        label='Digite seu email.',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex fulano@gmail.com'
            }
        )
    )

    senha_cadastro1=forms.CharField(
        label='Senha',
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha.',
            }
        )
    )

    senha_cadastro2=forms.CharField(
        label='Confirme sua senha.',
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha novamente',
            }
        )
    )

    class Meta:
        model = Usuario
        fields = ['nome_cadastro', 'email_cadastro', 'senha_cadastro2']

    # Validações dos campos do formulario de cadastro que seram chamados automaticamente no is_valid()
    def clean(self):
        cleaned_data = super().clean()
        nome = cleaned_data.get('nome_cadastro')
        nome = nome.strip()
        email = cleaned_data.get('email_cadastro')
        email = email.strip()
        caracteresNaoPermitidosNome = [
        "'", '"', ';', ':', ',', '.', 
        '+', '-', '=', '*', '/', '%', 
        '(', ')', '[', ']', '{', '}', 
        '@', '#', '&', '|', '~', '^', ]

        for caractere in caracteresNaoPermitidosNome:
            if caractere in nome:
                raise forms.ValidationError(f"O caractere '{caractere}' não e permitido no campo nome.")
        
        caracteresNaoPermitidosEmail = [
        "'", '"', ';', ':', ',', 
        '+', '=', '*', '/', '%', 
        '(', ')', '[', ']', '{', '}', 
         '#', '&', '|', '~', '^', ]
        
        for caractere in caracteresNaoPermitidosEmail:
            if caractere in email:
                raise forms.ValidationError(f"O caractere '{caractere}' não e permitido no campo email.")
        

        senha1 = cleaned_data.get('senha_cadastro1')
        senha2 = cleaned_data.get('senha_cadastro2')
        if senha1 and senha2:
            if senha1 != senha2:
                raise forms.ValidationError('As senhas não são iguais')
           
        return cleaned_data
    
    def save(self, commit=True):
        cleaned_data = super().clean()
        usuario = Usuario()
        usuario.nome = cleaned_data.get('nome_cadastro')
        usuario.email = cleaned_data.get('email_cadastro')
        usuario.senha = make_password(cleaned_data.get('senha_cadastro2'))
        
        if commit:
            usuario.save()
        return usuario