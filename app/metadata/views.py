from .models import Ontology, Concept

from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from .serializers import OntologySerializer, ConceptSerializer


class OntologyViewSet(viewsets.ModelViewSet):
    queryset = Ontology.objects.all()
    serializer_class = OntologySerializer

    @detail_route(methods=['get'])
    def get_whole_tree(self, request, pk=None):
        print(request.data)
        selected_ontology=Ontology.objects.get(pk=pk)
        all_concepts=Concept.objects.filter(ontology=selected_ontology)
        serializer = ConceptSerializer(all_concepts, many=True)

        return Response(serializer.data)

class ConceptViewSet(viewsets.ModelViewSet):
    queryset = Concept.objects.all()
    serializer_class = ConceptSerializer
