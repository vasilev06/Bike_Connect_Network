from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms

from bike_connect_network.profiles.models import Profile

UserModel = get_user_model()


class ProfileUserCreationForm(auth_forms.UserCreationForm):
    age = forms.IntegerField()

    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = (UserModel.USERNAME_FIELD,)

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            user=user,
            age=self.cleaned_data['age'],
        )

        if commit:
            profile.save()

        return user


class ProfileUserChangeForm(auth_forms.UserChangeForm):
    class Meta(auth_forms.UserChangeForm.Meta):
        model = UserModel
        fields = '__all__'


class ProfileEditForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['age', 'first_name', 'last_name', 'profile_picture']

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
        }
