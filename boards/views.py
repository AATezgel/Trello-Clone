from rest_framework import viewsets
from .models import Board, List, Card
from .serializers import BoardSerializer, ListSerializer, CardSerializer

class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer

    def get_queryset(self):
        board_id = self.request.query_params.get('board')
        if board_id:
            return self.queryset.filter(board_id=board_id)
        return self.queryset

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def get_queryset(self):
        list_id = self.request.query_params.get('list')
        if list_id:
            return self.queryset.filter(list_id=list_id)
        return self.queryset
