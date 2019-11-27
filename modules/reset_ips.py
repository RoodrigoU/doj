from shop.models import ModelIps

def reset_ips():
    ModelIps.objects.all().delete()

# reset_ips()
