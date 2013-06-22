from django.conf import settings

def AddModuleList(request):
  module_list = list()
  for module in settings.MODULE_LIST:
    if request.path.find(module) != -1:
      module_list.append( (module, module+'_home', True) )
    else:
      module_list.append( (module, module+'_home', False) )
  return {'module_list': module_list}
