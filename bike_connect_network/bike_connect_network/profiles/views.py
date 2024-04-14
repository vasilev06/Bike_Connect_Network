from django.contrib.auth import views as auth_views, get_user_model
from django.contrib.auth import mixins as auth_mixins

from django.shortcuts import redirect, render, get_object_or_404
from django.views import generic as views
from django.urls import reverse_lazy, reverse

from bike_connect_network.profiles.forms import ProfileUserCreationForm, ProfileEditForm
from bike_connect_network.profiles.models import Profile


UserModel = get_user_model()


class RegistrationUserView(views.CreateView):
    form_class = ProfileUserCreationForm
    template_name = 'profile/registration.html'
    success_url = reverse_lazy('index')


class LoginUserView(auth_views.LoginView):
    template_name = "web/index.html"
    success_url = reverse_lazy("index")


class LogoutUserView(auth_mixins.LoginRequiredMixin, auth_views.LogoutView):
    logout_url = reverse_lazy("index")


class DetailsUserView(auth_mixins.LoginRequiredMixin, views.DetailView):
    queryset = Profile.objects.prefetch_related('user').all()
    template_name = 'profile/profile_details.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        obj = Profile.objects.get(pk=pk)

        return obj


class EditUserView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = "profile/profile_edit.html"
    context_object_name = 'user'

    def get_success_url(self):
        return reverse("details_user", kwargs={
            "pk": self.object.pk,
        })

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        obj = Profile.objects.get(pk=pk)

        return obj


def delete_user_profile(request, pk):
    user = get_object_or_404(UserModel, pk=pk)
    if request.method == 'POST':
        if request.user == user:
            user.delete()
            return redirect('index')

    return render(request, 'profile/profile_delete.html')

