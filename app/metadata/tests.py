from django.test import TestCase
from .models import Ontology, Concept, ConceptTypes
from rest_framework.test import APIClient


class OntologyTestCase(TestCase):

    def setUp(self):
        new_ontology = Ontology.objects.create(name="test_ontology")

        Concept.objects.create(ontology=new_ontology,
                               concept_path="/root/",
                               concept_text="Root",
                               concept_type=ConceptTypes.TEXT,
                               concept_depth=0)

        Concept.objects.create(ontology=new_ontology,
                               concept_path="/root/node1",
                               concept_text="Node 1",
                               concept_type=ConceptTypes.TEXT,
                               concept_depth=1)

        Concept.objects.create(ontology=new_ontology,
                               concept_path="/root/node2",
                               concept_text="Node 2",
                               concept_type=ConceptTypes.TEXT,
                               concept_depth=1)

        Concept.objects.create(ontology=new_ontology,
                               concept_path="/root/node1/node3/",
                               concept_text="Node 3",
                               concept_type=ConceptTypes.TEXT,
                               concept_depth=1)

        self.new_ontology = new_ontology

    def test_retrieve_ontology(self):
        client = APIClient()
        get_ontology_response = client.get('/ontology/')

        assert(get_ontology_response.status_code == 200)

    def test_full_tree(self):
        client = APIClient()

        get_ontology_response = client.get('/ontology/%s/get_whole_tree/' % self.new_ontology.id)
        print(get_ontology_response.content)
        assert (get_ontology_response.status_code == 200)

    def test_one_node(self):
        client = APIClient()

        get_ontology_response = client.get('/concept/get_child_nodes/' % self.new_ontology.id)
        print(get_ontology_response)
        assert (get_ontology_response.status_code == 200)
