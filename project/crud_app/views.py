from django.shortcuts import render,redirect
from .models import Review
from .forms import ReviewForm
from django.views import View


class Add_Review(View):
    def get(self, request):
        template_name = 'crud_app/add.html'
        form = ReviewForm()
        context = {'form':form}
        return render(request, template_name, context)

    def post(self, request):
        form = ReviewForm()
        if request.method == "POST":
            form = ReviewForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('show_url')


class Show_Review(View):
    def get(self,request):
        template_name = 'crud_app/show.html'
        reviews = Review.objects.all()
        context = {'reviews':reviews}
        return render(request, template_name, context)

class Update_Review(View):
    def get(self,request,pk):
        template_name = 'crud_app/add.html'
        obj = Review.objects.get(id=pk)
        form = ReviewForm(instance=obj)
        context = {'form':form}
        return render(request, template_name, context)

    def post(self,request,pk):
        template_name = 'crud_app/Add.html'
        obj = Review.objects.get(id=pk)
        form = ReviewForm(instance=obj)
        if request.method == "POST":
            form = ReviewForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                return redirect('show_url')
        context = {'form': form}
        return render(request, template_name, context)


class Delete_Review(View):
    def get(self, request, pk):
        obj = Review.objects.get(id=pk)
        template_name = 'crud_app/confirm.html'
        return render(request, template_name)

    def post(self, request, pk):
        obj = Review.objects.get(id=pk)
        template_name = 'crud_app/confirm.html'
        if request.method == "POST":
            obj.delete()
            return redirect('show_url')
        return render(request, template_name)






