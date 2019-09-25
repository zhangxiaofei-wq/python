from django.shortcuts import render
from .models import HostGroup, Module, Host

# Create your views here.
def index(request):
    return render(request, 'polls_index.html')

def add_hosts(request):
    if request.method == 'POST':
        groupname = request.POST.get('group').strip()
        hostname = request.POST.get('host').strip()
        ip = request.POST.get('ip').strip()
        if groupname:  # 如果组字符串非空
            # get_or_create是取出或创建组，返回值是: (组实例，状态)
            group = HostGroup.objects.get_or_create(groupname=groupname)[0]
            if hostname and ip:  # 如果主机名和ip非空
                group.host_set.get_or_create(hostname=hostname, ipaddr=ip)

    groups = HostGroup.objects.all()
    return render(request, 'add_hosts.html', {'groups': groups})

def add_modules(request):
    if request.method == 'POST':
        mod_name = request.POST.get('mod').strip()
        arg = request.POST.get('param').strip()
        if mod_name:
            module = Module.objects.get_or_create(modulename=mod_name)[0]
            if arg:
                module.argument_set.get_or_create(arg_text=arg)

    modules = Module.objects.all()
    return render(request, 'add_modules.html', {'modules': modules})

def tasks(request):
    groups = HostGroup.objects.all()
    hosts = Host.objects.all()
    modules = Module.objects.all()
    context = {'hosts': hosts, 'groups': groups, 'modules': modules}
    return render(request, 'tasks.html', context)



