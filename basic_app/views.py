from django.views.generic import ListView , TemplateView , View, DetailView
from . import models
from django.db.models import Q
from django.core.paginator import Paginator
from basic_app.models import Post , Ingredients
from django.shortcuts import get_object_or_404, render ,reverse


class home(ListView):
    template_name = 'basic_app/home.html'
    context_object_name = 'posts' 
    model = Post
   
    def get_queryset(self):
        return Post.objects.order_by('-id')[:6]
       
    
class postlist(ListView):
    context_object_name = 'postlist'
    model = Post
    template_name = 'basic_app/postlist.html'
    paginate_by = 10
      

       
class postdetail(DetailView):
    context_object_name = 'postdetail'
    model = Post
    template_name = 'basic_app/postdetail.html'
 

    
class randomlist(ListView):
    context_object_name = 'randomlist'
    model = Post
    template_name = 'basic_app/randomlist.html'
        
    def get_queryset(self):
        return Post.objects.order_by('?')
       


class contact(TemplateView):
     template_name = 'basic_app/contact.html'
     




class ingredients_list(ListView): 
    context_object_name = 'inglist'
    model = Ingredients
    template_name = 'basic_app/ingredients.html'


class ingredients_detail(ListView):
     model = Post
     template_name = 'basic_app/ingredients_detail.html'
     context_object_name = 'posts'

     
     def get_queryset(self):
        self.ing = get_object_or_404(Ingredients,pk=self.kwargs['pk'])
        return  Post.objects.filter(ingredients =self.ing)


     def get_context_data(self , **kwargs):
         context = super(ingredients_detail , self).get_context_data(**kwargs)
         context['ingredients'] = self.ing 
         return context

 
def search(request):
     template = 'basic_app/search.html'
     query = request.GET.get('q')
     if query :
         results = Post.objects.filter(Q(title__icontains=query)|
          Q(ingredients_list__icontains=query) )
     else:     
          results = Post.objects.all()
     paginator = Paginator(results, 11)
     
     page_number = request.GET.get('page')
     page_obj = paginator.get_page(page_number)

     return render(request, template , {'page_obj': page_obj , 'query':query})