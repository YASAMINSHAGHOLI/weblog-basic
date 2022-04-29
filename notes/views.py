from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Note
# from .forms import NotesForm




# class NotesDeleteView(DeleteView):
#     model=Note
#     success_url = ''
#     template_name = ''


    
# class NotesUpdateView(UpdateView):
#     model = Note
#     success_url = ''
#     form_class = 
    
    

# class NotesCreateView(CreateView):
#     model = Note
#     success_url = ''
#     form_class = 

#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.user = self.request.user
#         self.object.save()
#         return HttpResponseRedirect(self.get_success_url())




class NotesListView(LoginRequiredMixin, ListView):
    model = Note
    context_object_name = "notes"
    template_name = "notes/notes.html"
    login_url = "/admin"

    # def get_queryset(self):
    #     return self.request.user.notes.all()
    
    

class NotesDetailView(DetailView):
    model = Note
    context_object_name = "note"
    template_name = "notes/notes_detail.html"
    



