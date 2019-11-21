from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from pitcaCom.models import PitcaCom

def regPitcaCom(request):
    return render(request, 'pitcaCom/registerPitcaCom.html')

def regConPitcaCom(request):
    name = request.POST['name']
    ip = request.POST['ip']
    cpu = request.POST['cpu']
    ram = request.POST['ram']
    storage = request.POST['storage']
    hdmi = request.POST['hdmi']

    qs = PitcaCom(pc_name=name, pc_ip=ip, pc_cpu=cpu, pc_ram=ram, pc_storage=storage, pc_hdmi=hdmi)
    qs.save()
    return HttpResponseRedirect(reverse('pitcaCom:comAll'))

def reaPitcaComAll(request):
    qs = PitcaCom.objects.all()
    context = {'com_list': qs}
    return render(request, 'pitcaCom/readPitcaCom.html', context)

def detPitcaCom(request, name):
    qs = PitcaCom.objects.get(pc_name=name)
    context = {'com_info': qs}
    return render(request, 'pitcaCom/detailPitcaCom.html', context)

def reaPitcaComOne(request, name):
    qs = PitcaCom.objects.get(pc_name=name)
    context = {'com_info': qs}
    return render(request, 'pitcaCom/modifyPitcaCom.html', context)

def modConPitcaCom(request):
    name = request.POST['name']
    ip = request.POST['ip']
    cpu = request.POST['cpu']
    ram = request.POST['ram']
    storage = request.POST['storage']
    hdmi = request.POST['hdmi']

    c_qs = PitcaCom.objects.get(pc_name=name)
    c_qs.pc_name=name
    c_qs.pc_ip=ip
    c_qs.pc_cpu=cpu
    c_qs.pc_ram=ram
    c_qs.pc_storage=storage
    c_qs.pc_hdmi=hdmi

    c_qs.save()
    return HttpResponseRedirect(reverse('pitcaCom:comAll'))

def delconPitcaCom(request, name):
    qs = PitcaCom.objects.get(pc_name=name)
    qs.delete()
    return HttpResponseRedirect(reverse('pitcaCom:comAll'))