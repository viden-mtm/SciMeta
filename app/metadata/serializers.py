from rest_framework import serializers

from .models import Ontology, Concept


class OntologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ontology
        fields = ('id', 'name')


class ConceptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concept
        fields = ('concept_path', 'concept_text', 'concept_type', 'concept_depth')
