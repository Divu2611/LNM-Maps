from unicodedata import name
from django.shortcuts import render
import json
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from bson import ObjectId
from .optimal_path import *
import time
import sys

# lnmiit_roads_nodes = [
#     [
#         (26.937066547706586, 75.92323972023897),
#         (26.937011849391904, 75.92277079247938),
#         (26.9367793812585, 75.92241142728045),
#         (26.936464864771967, 75.92224927463525),
#         (26.93536, 75.92215),
#         (26.93434332077833, 75.92213313830503),
#     ],
#     [(26.937066547706586, 75.92323972023897), (26.93657, 75.92321)],
#     [
#         (26.93434332077833, 75.92213313830503),
#         (26.934364809906914, 75.92143632034175),
#         (26.934073729453196, 75.92116898769376),
#         (26.934009261868507, 75.92109886765495),
#         (26.93395065494137, 75.92074607620965),
#         (26.934026843938625, 75.92026180964302),
#     ],
#     [(26.93434332077833, 75.92213313830503), (26.93433, 75.9232)],
#     [(26.93434332077833, 75.92213313830503), (26.93332, 75.92223)],
#     [
#         (26.93223, 75.92273),
#         (26.93118, 75.92214),
#         (26.93087, 75.92168),
#         (26.93091, 75.9213),
#     ],
#     [(26.93332, 75.92223), (26.93326, 75.92296)],
#     [(26.93332, 75.92223), (26.93254, 75.92225), (26.93223, 75.92273)],
#     [(26.93326, 75.92296), (26.93433, 75.9232)],
#     [(26.93433, 75.9232), (26.93432, 75.92421)],
#     [(26.93433, 75.9232), (26.93497, 75.92318)],
#     [(26.93497, 75.92318), (26.935, 75.9238)],
#     [(26.93497, 75.92318), (26.93564, 75.92315)],
#     [(26.935, 75.9238), (26.935, 75.92408), (26.93486, 75.92421)],
#     [(26.93432, 75.92421), (26.93486, 75.92421)],
#     [
#         (26.93486, 75.92421),
#         (26.93521, 75.92473),
#         (26.9355, 75.92511),
#         (26.93623, 75.9254),
#         (26.93651, 75.92531),
#         (26.9369, 75.92463),
#         (26.93741, 75.92351),
#     ],
#     [(26.93432, 75.92421), (26.93386, 75.92416), (26.93266, 75.92333)],
#     [
#         (26.93326, 75.92296),
#         (26.93303, 75.92295),
#         (26.93276, 75.92307),
#         (26.93266, 75.92333),
#     ],
# ]


@api_view(["POST"])
def api_home(request, *args, **kwargs):

    # country = Country()
    # country.name = "India"
    # country.coordinates = [
    #     Node(latitude=123.33, longitude=33.908),
    #     Node(latitude=13.33, longitude=3.908),
    #     Node(latitude=12.33, longitude=3223.908),
    # ]
    # country.save()
    # num = "62ee1339679f411219987a77"
    # entries = Country.objects.filter(id="62ee1339679f411219987a77")
    # print(entries)
    # print(sys.getsizeof(entries))
    # india_nodes = [
    #     Node(latitude=34.880853, longitude=76.931742),
    #     Node(latitude=25.079993, longitude=93.059672),
    #     Node(latitude=10.092576, longitude=77.503031),
    #     Node(latitude=28.027734, longitude=70.164164),
    # ]
    # rajasthan_nodes = [
    #     Node(latitude=29.874044, longitude=73.728406),
    #     Node(latitude=26.603316, longitude=77.364881),
    #     Node(latitude=23.870823, longitude=74.047010),
    #     Node(latitude=27.181409, longitude=70.388562),
    # ]
    # jaipur_nodes = [
    #     Node(latitude=26.945756, longitude=76.065207),
    #     Node(latitude=26.700037, longitude=75.804281),
    #     Node(latitude=26.935962, longitude=75.570135),
    #     Node(latitude=27.071167, longitude=75.801535),
    # ]
    # lnmiit_nodes = [
    #     Node(latitude=26.938949, longitude=75.922275),
    #     Node(latitude=26.930758, longitude=75.916818),
    #     Node(latitude=26.927894, longitude=75.925384),
    #     Node(latitude=26.936578, longitude=75.927698),
    # ]

    # lnmiit_graph = {}
    # for i in lnmiit_roads_nodes:
    #     n = len(i)
    #     for j in range(1, n):
    #         if lnmiit_graph.get(i[j]) == None:
    #             lnmiit_graph[i[j]] = []
    #         lnmiit_graph[i[j]].append(i[j - 1])
    #         if lnmiit_graph.get(i[j - 1]) == None:
    #             lnmiit_graph[i[j - 1]] = []
    #         lnmiit_graph[i[j - 1]].append(i[j])

    # graph = []
    # area = Area(
    #     name="The LNM Institute of Information Technology", coordinates=lnmiit_nodes
    # )
    # for par in lnmiit_graph:
    #     node = Node(latitude=par[0], longitude=par[1])
    #     tmp = []
    #     for child in lnmiit_graph[par]:
    #         tmp.append(Node(latitude=child[0], longitude=child[1]))
    #     lst = List(parent_node=node, children=tmp)
    #     graph.append(lst)
    # print(graph)
    # area.graph = graph
    # area.save()

    # city = City(name="Jaipur", areas=[area.id], coordinates=jaipur_nodes)
    # city.save()

    # state = State(name="Rajasthan", cities=[city.id], coordinates=rajasthan_nodes)
    # state.save()

    # country = Country(name="Hindustan", states=[state.id], coordinates=india_nodes)
    # country.save()

    # ll = []
    # for i in nodes:
    #     coo = Node(latitude=i[0], longitude=i[1])
    #     coo.save()
    #     ll.append(coo.id)

    # entries = Country(name="Hindustan")
    # entries.coordinates = [coo.id]
    # entries.save()
    # val = Country.objects(name="Hindustan").first()
    # print(val.id)

    # coor = Coordinate(x=26.935179, y=75.923564)
    # print(coor.Address)
    # return HttpResponse("Hello ")

    if request.method == "POST":
        start_time = time.time()
        path = Path(
            startX=request.data["startX"],
            startY=request.data["startY"],
            endX=request.data["endX"],
            endY=request.data["endY"],
        )
        cnt = 1
        while cnt > 0:
            cnt -= 1
            ans = path.getOptimalPath()
        response = {"path": ans[0], "distance": ans[1]}
        print("--- %s seconds ---" % (time.time() - start_time))
        return JsonResponse(response)
