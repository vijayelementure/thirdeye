from django.shortcuts import render


# Create your views here.
def dashboard(request):
    return render(request, "iplogger/dlayout.html")


def connectednode(request):
    # cnodes = [
    #     {
    #         "nodeid": "84e1a8f9-0122-48e6-8f6b-6f66f5a34b23",
    #         "gatewayid": "d95af6d6-10fd-4706-bafc-26129114cfc9",
    #         "projectid": "AQS2305A001",
    #         "loci_d": "AQS2305A001",
    #         "loc_name": "engrace",
    #         "p_source": "On Battery",
    #     },
    #     {
    #         "nodeid": "84e1a8f9-0122-48e6-8f6b-6f66f5a34b23",
    #         "gatewayid": "d95af6d6-10fd-4706-bafc-26129114cfc9",
    #         "projectid": "AQS2305A001",
    #         "loci_d": "AQS2305A001",
    #         "loc_name": "engrace",
    #         "p_source": "On Battery",
    #     },
    # ]
    # context = {"cnodes": cnodes}
    return render(request, "iplogger/cnlayout.html")

