from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .models import Profile
from .forms import UserRegistrationForm, UserEditForm, ChangePasswordForm, ProfilePageForm


class UserRegisterView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEditView(UpdateView):
    form_class = UserEditForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('blog-home')

    def get_object(self):
        return self.request.user


class PasswordsChangeView(PasswordChangeView):
    form_class = ChangePasswordForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('edit-profile')


def password_changed(request):
    return render(request, 'registration/password_changed.html', {})


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context


class EditProfilePageView(UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = ['bio', 'profile_image', 'website_url', 'facebook_url', 'instagram_url', 'twitter_url', 'pinterest_url', 'linkedin_url']
    success_url = reverse_lazy('blog-home')

    def get_context_data(self, *args, **kwargs):
        context = super(EditProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context


class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_profile.html'
    success_url = reverse_lazy('blog-home')

    # Saving the form under the right user...
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
