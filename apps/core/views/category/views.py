from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator

from apps.core.forms import CategoryForm
from apps.core.models import Category


class CategoryListView(ListView):
    model = Category
    template_name = 'category/list.html'

    # def get_queryset(self):
    #     return Category.objects.filter(name__startswith='A')
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = Category.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Cateogry List'
        context['create_url'] = reverse_lazy('create')
        context['list_url'] = reverse_lazy('category_list')
        context['entity'] = 'Category'
        return context


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/create.html'
    success_url = reverse_lazy('category_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creating a Cateogry'
        context['list_url'] = reverse_lazy('category_list')
        context['entity'] = 'Category'
        context['action'] = 'add'
        return context

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = CategoryForm(request.POST)
                data = form.save()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
    # form = CategoryForm(request.POST)
    # if form.is_valid():
    #     form.save()
    #     return HttpResponseRedirect(self.success_url)
    # self.object = None
    # context = self.get_context_data(**kwargs)
    # context['form'] = form
    # return render(request, self.template_name, context)


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/create.html'
    success_url = reverse_lazy('category_list')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'update':
                form = self.get_form()
                data = form.save()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Updating a Cateogry'
        context['list_url'] = reverse_lazy('category_list')
        context['entity'] = 'Category'
        context['action'] = 'update'
        return context


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category/list.html'
    success_url = reverse_lazy('category_list')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete a Cateogry'
        context['list_url'] = reverse_lazy('category_list')
        context['entity'] = 'Category'
        return context
