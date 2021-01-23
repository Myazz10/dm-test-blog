from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from .models import Post, Category, Comment
from django.http import HttpResponseRedirect
from .forms import AddPostForm, UpdatePostForm, AddCategoryForm, AddCommentForm
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView


# DEALING WITH POSTS
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    # ordering = ['-id']  # --> The hackie way to order the post by the latest.
    ordering = ['-date_posted']  # --> This the way how to order posts by the latest post by date.

    # Passing another variable to the home page.
    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(PostListView, self).get_context_data(*args, **kwargs)

        context['category_menu'] = category_menu
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_details.html'

    # Passing another variable to the home page.
    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked = False

        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['category_menu'] = category_menu
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context


class AddPostView(CreateView):
    model = Post
    form_class = AddPostForm  # Instantiating a add post post form.
    template_name = 'blog/add_post.html'

    # fields = '__all__'  # --> This will return all the fields of a Post model.
    # fields = ['title', 'content']  # Only display the fields listed in the list.

    # Passing another variable to the home page.
    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(AddPostView, self).get_context_data(*args, **kwargs)

        context['category_menu'] = category_menu
        return context


class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdatePostForm  # Instantiating a add post post form.
    template_name = 'blog/update_post.html'

    # fields = ['title', 'title_tag', 'content']

    # Passing another variable to the home page.
    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(UpdatePostView, self).get_context_data(*args, **kwargs)

        context['category_menu'] = category_menu
        return context


class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('blog-home')

    # Passing another variable to the home page.
    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(DeletePostView, self).get_context_data(*args, **kwargs)

        context['category_menu'] = category_menu
        return context


# DEALING WITH CATEGORIES
class AddCategoryView(CreateView):
    model = Category
    form_class = AddCategoryForm  # Instantiating a add post post form.
    template_name = 'blog/add_category.html'

    # fields = '__all__'
    # fields = ['title', 'content']

    # Passing another variable to the home page.
    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(AddCategoryView, self).get_context_data(*args, **kwargs)

        context['category_menu'] = category_menu
        return context


'''
class PostByCategoryListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']  # --> This the way how to order posts by the latest post by date.
'''


def post_by_category_list_view(request, pk):
    try:
        category = Category.objects.get(pk=pk)
        category_posts = Post.objects.filter(category=category).order_by('-date_posted')
        category_menu = Category.objects.all()
        context = {
            'category': category,
            'category_posts': category_posts,
            'category_menu': category_menu,
        }
    except Exception:
        context = {
            'category': '404 error, this page does not exist!',
        }

    return render(request, 'blog/post_by_category.html', context)


def like_view(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('post-detail', args=(str(pk))))


class AddCommentView(CreateView):
    model = Comment
    form_class = AddCommentForm
    template_name = 'blog/add_comment.html'

    # Saving the form under the right user...
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)


