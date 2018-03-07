from django.db import models
from treebeard.mp_tree import MP_Node

class ConceptTypes(models.Model):
    TEXT = 'TXT'
    INT = 'INT'
    FLOAT = 'FLOAT'

    CONCEPT_TYPES = (
        (TEXT, 'Text'),
        (INT, 'Integer'),
        (FLOAT, 'Floating Point'),
    )


class Ontology(models.Model):
    name = models.CharField(max_length=200)


class Concept(models.Model):
    ontology = models.ForeignKey(Ontology, on_delete=models.DO_NOTHING)
    concept_path = models.CharField(max_length=500)
    concept_text = models.CharField(max_length=200)
    concept_type = models.CharField(max_length=25, choices=ConceptTypes.CONCEPT_TYPES)
    concept_depth = models.IntegerField()
