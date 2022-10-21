from django.shortcuts import render
from rest_framework.viewsets import ViewSet

from extensions.handler import SuccessResponse, FailureResponse

from . import models
from . import serializers

# Create your views here.

class NoteView(ViewSet):

    """
        CRUD Operations:
        
        get_single (id) : GET    : returns single note
        get_all         : GET    : returns all notes
        create          : POST   : creates new note
        update (id)     : PUT    : updates a note
        delete (id)     : DELETE : deletes a note  
    """

    def get_single(self, request, id):

        query = models.Note.objects.filter(id=id)

        if(query):
            serializer = serializers.NoteSerializer(query.first(), many=False)
            return SuccessResponse(serializer.data, 200).response()
        return FailureResponse("Query object not found", 200).response()  


    def get_all(self, request):

        query = models.Note.objects.all()

        if(query):
            serializer = serializers.NoteSerializer(query, many=True)
            return SuccessResponse(serializer.data, 200).response()
        return FailureResponse("Empty Notes", 200).response()  


    def create(self, request):

        data = request.data
        title_param = data.get("title") 
        text_param = data.get("text")

        if not title_param or not text_param:
            return FailureResponse("Title or Text parameter missing", 200).response()

        query = models.Note.objects.filter(title=title_param)
        if(query):
            return FailureResponse("A note with this title already exists", 200).response()

        models.Note.objects.create(
            title = title_param,
            text = text_param,
        )

        return SuccessResponse("Created note successfully", 200).response()


    def update(self, request, id):

        query = models.Note.objects.filter(id=id)

        if(query.first()):
            data = request.data
            query_first = query.first()
            
            title_param = data.get("title", query_first.title)
            text_param = data.get("text", query_first.text)
            starred_param = data.get("starred", query_first.starred)

            query.update(
                title = title_param,
                text = text_param,
                starred = starred_param
            )

            return SuccessResponse("Note Updated Successfully", 200).response()
        return FailureResponse("Note not found", 200).response()  


    def delete(self, request, id):

        query = models.Note.objects.filter(id=id)
        
        if(query):
            target = query.first()
            target.delete()
            return SuccessResponse("Note deleted successfully", 200).response()
        return FailureResponse("Note not found", 200).response()  