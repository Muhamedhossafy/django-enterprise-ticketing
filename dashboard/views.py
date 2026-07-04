from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ticket.models import *
# Create your views here.

@login_required()
def dashboard(request):
    # Customer  
    all_tickets_for_customer = Ticket.objects.filter(created_by=request.user).order_by('-id')[:5]
    all_tickets =  Ticket.objects.filter(created_by=request.user).count()
    pending_tickets = Ticket.objects.filter(created_by=request.user, status='Pending').count()
    Active_tickets = Ticket.objects.filter(created_by=request.user, status='Active').count()
    closed_tickets = Ticket.objects.filter(created_by=request.user, status='Completed').count()

    # Admin 
    all_tickets_for_admin = Ticket.objects.all().order_by('-id')[:5]
    all_tickets_n =  Ticket.objects.all().count()
    pending_tickets_n = Ticket.objects.filter(status='Pending').count()
    Active_tickets_n = Ticket.objects.filter(status='Active').count()
    closed_tickets_n = Ticket.objects.filter(status='Completed').count()

    context = {
        'all_tickets_for_customer': all_tickets_for_customer,
        'all_tickets': all_tickets,
        'pending_tickets': pending_tickets,
        'Active_tickets': Active_tickets,
        'closed_tickets': closed_tickets,

        'all_tickets_for_admin': all_tickets_for_admin,
        'all_tickets_n': all_tickets_n,
        'pending_tickets_n': pending_tickets_n,
        'Active_tickets_n': Active_tickets_n,
        'closed_tickets_n': closed_tickets_n
    }
    return render(request, 'dashboard.html', context)