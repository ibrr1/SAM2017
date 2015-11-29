from sam2017_app.models import paper
from sam2017_app.models.user_model import User
from sam2017_app.models import submission
from sam2017_app.forms.paper_updating_form import PaperSubmission
from django.shortcuts import render
from django.http import HttpResponseRedirect
from sam2017_app.views.session import __is_session_open
from sam2017_app.views.user_details import __add_general_content_to_context
import datetime
from django.contrib import messages


def paper_updating_event(request,paper_id):

       ## check if  the submition date is passed so he cannot  publish one
    last_month =  datetime.datetime.now() - datetime.timedelta(days=1)
    PaperDeadLine =paper.PaperDeadLine.objects.filter(date_deadline__gte=last_month)
    if  not PaperDeadLine  :
         return render(request, 'paper_dead_line.html')
#****************

    if not __is_session_open(request):
        return HttpResponseRedirect('/')

    user = User.objects.get(email=request.session['user_email'])
#get paper info that we want to update and put this info into the form op paper
    my_paper= paper.Paper.objects.get(id=paper_id)
    paper_submission_form = PaperSubmission(request.POST or None)
    paper_submission_form.fields["title"].initial=my_paper.title;
    paper_submission_form.fields["authors_list"].initial=my_paper.authors_list;
    paper_submission_form.fields["author_contact"].initial=my_paper.author_contact;
    paper_submission_form.fields["paper_format"].initial=my_paper.paper_format;
    my_Old_paper_path=my_paper.paper;
    paper_submission_form.fields["is_this_a_revision_of_a_previously_submitted_paper"].initial= "Yes" if my_paper.revision_paper==1  else "No"
  #  paper_submission_form.title=my_paper.title
    context = {
        'paper_submission_form': paper_submission_form,
    }

    context.update(__add_general_content_to_context(user))

    if request.method == "POST":
        paper_submission_form = PaperSubmission(request.POST, request.FILES)
        if paper_submission_form.is_valid():
            try:
              filename = request.FILES['paper'].name

              if not (filename.endswith('.pdf') or (filename.endswith('.doc')) or (filename.endswith('.docx'))):
                error = 'sorry!! you can only submit a PDF or Word document'
                context['error'] = error
              else:
                df = datetime.datetime.now()
                #file name is user last name + date + current time
                filename = user.last_name + '_' + str(df.month)+"_"+ str(df.day)+"_"+ str(df.year)+ "_" +str(df.hour)+ "_"+ str(df.minute) +"_" +str(df.second) +"_"+ filename

                #save the file in a folder name submitted_papers in the project main folder
                file_name='submitted_papers/'+ filename
                handle_uploaded_file(request.FILES['paper'],file_name)
                #----
            except:  # if he didnot submit new file keep old version
              filename=my_Old_paper_path
              #Update the paper info   submitted_paper = paper.Paper()
            my_paper.paper = filename
            my_paper.title = paper_submission_form.cleaned_data['title']
            my_paper.authors_list = paper_submission_form.cleaned_data['authors_list']
            my_paper.author_contact = paper_submission_form.cleaned_data['author_contact']
            my_paper.paper_format = paper_submission_form.cleaned_data['paper_format']
            my_paper.revision_paper= 1 if paper_submission_form.cleaned_data["is_this_a_revision_of_a_previously_submitted_paper"]=="Yes" else 0

            my_paper.save()


            messages.success(request, 'Thanks, You have successfully updated a paper')

            return HttpResponseRedirect('/user_profile')

    return render(request, 'paper_updating.html', context)

# End paper submission

def handle_uploaded_file(f, file_name):
    with open( file_name , 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
