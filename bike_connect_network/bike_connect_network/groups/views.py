from django.urls import reverse_lazy
from django.views import generic as views

from django.shortcuts import redirect, get_object_or_404

from django.contrib.auth import mixins as auth_mixins

from bike_connect_network.groups.models import Group, Event


class GroupListView(views.ListView):
    model = Group
    template_name = "groups/group_list.html"
    context_object_name = "groups"


class GroupDetailView(views.DetailView):
    queryset = Group.objects.all()
    template_name = "groups/group_details.html"
    context_object_name = "group"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        group = self.get_object()
        context['events'] = Event.objects.filter(group=group)
        return context


class GroupCreateView(views.CreateView):
    model = Group
    template_name = "groups/group_create.html"
    fields = ["name", "description"]
    success_url = reverse_lazy("list_groups")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class GroupJoinView(auth_mixins.LoginRequiredMixin, views.View):
    model = Group

    def post(self, request, pk):
        group = get_object_or_404(Group, pk=pk)
        group.members.add(request.user)
        return redirect('detail_group', pk=pk)


class GroupLeaveView(auth_mixins.LoginRequiredMixin, views.View):
    model = Group

    def post(self, request, pk):
        group = get_object_or_404(Group, pk=pk)
        group.members.remove(request.user)
        return redirect('detail_group', pk=pk)


class EventCreateView(views.CreateView):
    model = Event
    fields = ['title', 'content']
    template_name = 'groups/group_event_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.group_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('detail_group', kwargs={'pk': self.kwargs['pk']})



