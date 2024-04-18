from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views import generic as views

from django.contrib.auth import mixins as auth_mixin
from django.core.paginator import Paginator
from bike_connect_network.web.models import UserStatus, Comment


def index(request):
    posts_list = UserStatus.objects.prefetch_related('comments').all()
    paginator = Paginator(posts_list, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'web/index.html', {'page_obj': page_obj})


class UserStatusListView(views.ListView):
    queryset = UserStatus.objects.prefetch_related('comments').all()
    template_name = 'web/index.html'
    context_object_name = 'user_statuses'
    ordering = ['-created_at']


class UserStatusCreateView(auth_mixin.LoginRequiredMixin, views.CreateView):
    model = UserStatus
    template_name = 'web/user_status_create.html'
    fields = ['status', 'image']
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def add_comment(request, status_id):
    if request.method == 'POST':
        status = UserStatus.objects.get(pk=status_id)
        comment_text = request.POST.get('comment_text')
        Comment.objects.create(status=status, user=request.user, text=comment_text)
    return redirect('index')


def like_user_status(request, status_id):
    status = UserStatus.objects.get(pk=status_id)
    if request.user in status.likes.all():
        status.likes.remove(request.user)
    else:
        status.likes.add(request.user)
    return redirect('index')


