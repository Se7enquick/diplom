from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .models import Task, Status
from .forms import AddTaskForm, UpdateStatusForm, UpdateTaskForm
from django.contrib.auth.mixins import LoginRequiredMixin

class TaskView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'main/index.html'
    context_object_name = 'tasks'
    login_url = '/login/'
    queryset = model.objects.all()
    
    def session_expired(self):
        if not self.request.user.is_superuser:
            self.request.session.set_expiry(5*60)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(object_list = None, **kwargs)
        performers_list = User.objects.exclude(id=1).filter(is_staff=False)
        self.session_expired()
        context.update({'delete': DeleteTask,
                        'create': AddTaskForm,
                        'performers_list': performers_list,
                        'status_list': Status.objects.all(), 
                        })
        return context
    

class CreateTask(CreateView):
    template_name = 'main/add.html'
    form_class = AddTaskForm
    success_url = '/'
    login_url = '/login/'

    def form_valid(self, form):
        form_create = form.save(commit=False)
        form_create.user_id = self.request.user.id
        if form.cleaned_data['performer']:
            form_create.performer = self.request.user
            form_create.performer = self.request.user.id
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

class UpdateStatus(UpdateView):
    model = Task
    template_name = 'main/update.html'
    success_url = '/'
    fields = ['status']

class UpdateTaskArticle(UpdateView):
    model = Task
    template_name = 'tasks_crud/update.html'
    success_url = '/'
    fields = ['article']

class UpdateTaskPerformer(UpdateView):
    model = Task
    template_name = 'tasks_crud/update.html'
    success_url = '/'
    fields = ['performer']

class DeleteTask(DeleteView):
    model = Task
    template_name = 'tasks_crud/delete.html'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        task = self.kwargs['pk']
        return super().dispatch(request, *args, **kwargs)
    