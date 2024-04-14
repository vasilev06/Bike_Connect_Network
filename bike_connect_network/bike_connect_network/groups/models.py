from django.contrib.auth import get_user_model

from django.db import models

UserModel = get_user_model()


class Group(models.Model):
    name = models.CharField(max_length=100)

    description = models.TextField()

    created_by = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    members = models.ManyToManyField(UserModel, related_name='group_members')

    created_at = models.DateTimeField(auto_now_add=True)

    def join_group(self, user):
        """
        Method to allow a user to join the community.
        """
        self.members.add(user)

    def leave_group(self, user):
        """
        Method to allow a user to leave the community.
        """
        self.members.remove(user)

    @classmethod
    def create_group(cls, name, description, created_by):
        """
        Method to create a new community.
        """
        group = cls(name=name, description=description, created_by=created_by)
        group.save()
        return group

    @classmethod
    def search_groups(cls, query):
        """
        Method to search for communities by name.
        """
        return cls.objects.filter(name__icontains=query)


class Event(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    title = models.CharField(max_length=50, blank=False, null=False)

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

