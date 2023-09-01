from django.urls import reverse_lazy
from django.templatetags.static import static
from django.views import generic as views
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views, get_user_model

from petstagram.accounts.forms import PetstagramUserCreateForm, LoginForm, PetstagramUserEditForm
from petstagram.accounts.models import PetstagramUser

UserModel = get_user_model()


class UserRegisterView(views.CreateView):
    model = PetstagramUser
    form_class = PetstagramUserCreateForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('login')


class UserLoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'accounts/login-page.html'
    next_page = reverse_lazy('home')


class UserLogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('login')


class UserDetailsView(views.DetailView):
    model = UserModel
    template_name = 'accounts/profile-details-page.html'

    profile_image = static('images/person.png')

    def get_profile_image(self):
        if self.object.profile_picture is not None:
            return self.object.profile_picture
        return self.profile_image

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        totals_like_count = sum(p.like_set_count() for p in self.object.photo_set.all())

        context.update({
            'totals_like_count': totals_like_count,
        })

        context['profile_image'] = self.get_profile_image()

        return context


class UserEditView(views.UpdateView):
    model = PetstagramUser
    form_class = PetstagramUserEditForm
    template_name = 'accounts/profile-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('profile_details', kwargs={'pk': self.object.pk})


class UserDeleteView(views.DetailView):
    model = PetstagramUser
    template_name = 'accounts/profile-delete-page.html'

    def post(self, *args, pk):
        self.request.user.delete()
        return redirect('home')
