from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import View

from question.models import Pregunta, Tag, Respuesta
from people.models import Colaborador
from .models import Post
from .forms import PostForm

from django.contrib.auth.decorators import login_required

from django.db.models import Count

class PostList(View):
	def get(self, request):
		colab =  Respuesta.objects.values('Colaborador','Colaborador__user__first_name', 'Colaborador__user__last_name').annotate(Count('Colaborador')).order_by('-Colaborador__count')[:5]#Colaborador.objects.all()[:5]
		for i in range(len(colab)):
			colab[i]['Colaborador'] = Colaborador.objects.get(pk=colab[i]['Colaborador'])
		tags = Tag.objects.all().order_by('name')
		posts = Post.objects.all().order_by('-id')[:10]

		return render(request, 'blog/post_list.html', {'post_list': Post.objects.all(), 'colaboradores_top': colab , 'tag_list': tags, 'posts' : posts,})


def post_detail(request, year, month, slug):
	colab =  Respuesta.objects.values('Colaborador','Colaborador__user__first_name', 'Colaborador__user__last_name').annotate(Count('Colaborador')).order_by('-Colaborador__count')[:5]#Colaborador.objects.all()[:5]
	for i in range(len(colab)):
		colab[i]['Colaborador'] = Colaborador.objects.get(pk=colab[i]['Colaborador'])
	tags = Tag.objects.all().order_by('name')
	posts = Post.objects.all().order_by('-id')[:10]

	post = get_object_or_404(Post, pub_date__year=year,pub_date__month=month,slug=slug)
	return render (request, 'blog/post_detail.html',{'post': post, 'colaboradores_top': colab , 'tag_list': tags, 'posts' : posts,})



class PostCreate(View):
	
	
	def get(self, request):
		colab =  Respuesta.objects.values('Colaborador','Colaborador__user__first_name', 'Colaborador__user__last_name').annotate(Count('Colaborador')).order_by('-Colaborador__count')[:5]#Colaborador.objects.all()[:5]
		for i in range(len(colab)):
			colab[i]['Colaborador'] = Colaborador.objects.get(pk=colab[i]['Colaborador'])
		tags = Tag.objects.all().order_by('name')
		posts = Post.objects.all().order_by('-id')[:10]
		return render(request, 'blog/post_form.html',{'form': PostForm, 'colaboradores_top': colab , 'tag_list': tags, 'posts' : posts,})

	
	def post(self, request):
		usu = request.user
		colaborator = Colaborador.objects.get(user=usu)
		colab =  Respuesta.objects.values('Colaborador','Colaborador__user__first_name', 'Colaborador__user__last_name').annotate(Count('Colaborador')).order_by('-Colaborador__count')[:5]#Colaborador.objects.all()[:5]
		for i in range(len(colab)):
			colab[i]['Colaborador'] = Colaborador.objects.get(pk=colab[i]['Colaborador'])
		tags = Tag.objects.all().order_by('name')
		posts = Post.objects.all().order_by('-id')[:10]

		bound_form = PostForm(request.POST)

		if bound_form.is_valid():
			new_post = bound_form.save(commit=False)
			new_post.colaboradores = colaborator
			new_post.save()
			return redirect(new_post)
		else:
			return render(request,'blog/post_form.html', {'form': bound_form, 'colaboradores_top': colab , 'tag_list': tags, 'posts' : posts,})


class PostUpdate(View):
	form_class = PostForm
	model = Post
	template_name='blog/post_form_update.html'

	def get(self, request,year, month, slug):
		post = self.get_object(year, month, slug)
		context = {'form': self.form_class(instance=post),'post': post,}
		return render(request, self.template_name, context)

	def post(self, request, year, month, slug):
		post = self.get_object(year, month, slug)
		bound_form = self.form_class(request.POST, instance=post)

		if bound_form.is_valid():
			new_post = bound_form.save()
			return redirect(new_post)
		else:
			context = {'form': bound_form, 'post': post,}
			return render(request,self.template_name, context)

	def get_object(self, year, month, slug):
		return get_object_or_404(self.model,pub_date__year=year,pub_date__month=month,slug=slug)

class PostDelete(View):

	def get(self, request, year, month, slug):
		post = get_object_or_404(Post, pub_date__year=year, pub_date__month = month, slug__iexact=slug)
		return render(request, 'blog/post_confirm_delete.html', {'post': post})

	def post(self, request, year, month, slug):
		post = get_object_or_404(Post, pub_date__year=year, pub_date__month = month, slug__iexact=slug)
		post.delete()
		return redirect('blog_post_list')
