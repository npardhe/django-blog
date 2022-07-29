from secrets import choice
from attr import field
from django import forms
from .models import Post,Category,Comment

#choice=[('programing','programing'),('news','news'),('sport','sport'),('tech','tech')]
choice=Category.objects.all().values_list('name','name')
choice_lst=[]
for i in choice:
    choice_lst.append(i)
class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','title_tag','author','category','body','snippet','header_image')
        widgets={'title':forms.TextInput(attrs={'class':'form-control','placeholder':'This is title placeholder'}),
                'title_tag':forms.TextInput(attrs={'class':'form-control'}),
                'author':forms.TextInput(attrs={'class':'form-control','value':'','id':'elder','type':'hidden'}),
                #'author':forms.Select(attrs={'class':'form-control'}),
                'category':forms.Select(choices=choice_lst,attrs={'class':'form-control'}),
                'body':forms.Textarea(attrs={'class':'form-control'}),
                'snippet':forms.Textarea(attrs={'class':'form-control'})
                }

class EditPostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','title_tag','body','snippet')
        widgets={'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Thish is title placeholder'}),
                'title_tag':forms.TextInput(attrs={'class':'form-control'}),
                #'author':forms.Select(attrs={'class':'form-control'}),
                'body':forms.Textarea(attrs={'class':'form-control'})}



class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('name','body')
        widgets={'name':forms.TextInput(attrs={'class':'form-control'}),
                #'title_tag':forms.TextInput(attrs={'class':'form-control'}),
                #'author':forms.Select(attrs={'class':'form-control'}),
                'body':forms.Textarea(attrs={'class':'form-control'})}