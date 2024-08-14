from django.shortcuts import render
from django.http import Http404
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import OutfitPostScrap, OutfitItemScrap
from outfit_posts.models import OutfitPost, OutfitItem

class OutfitPostScrapDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_outfit_post(self, outfit_post_id):
        return OutfitPost.objects.filter(pk=outfit_post_id).first()

    def get_outfit_post_scrap(self, user, outfit_post):
        return OutfitPostScrap.objects.filter(user=user, outfit_post=outfit_post).first()

    def post(self, request, outfit_post_id):
        outfit_post = self.get_outfit_post(outfit_post_id)
        if not outfit_post:
          return Response({"message": "존재하지 않는 코디입니다."}, status=status.HTTP_404_NOT_FOUND)

        if self.get_outfit_post_scrap(request.user, outfit_post):
            return Response({"message": "이미 스크랩 되어있는 코디입니다."}, status=status.HTTP_409_CONFLICT)
            
        OutfitPostScrap.objects.create(user=request.user, outfit_post=outfit_post)
        return Response(status=status.HTTP_201_CREATED)

    def delete(self, request, outfit_post_id):
        outfit_post = self.get_outfit_post(outfit_post_id)
        if not outfit_post:
          return Response({"message": "존재하지 않는 코디입니다."}, status=status.HTTP_404_NOT_FOUND)

        outfit_post_scrap = self.get_outfit_post_scrap(request.user, outfit_post)
        if not outfit_post_scrap:
            return Response({"message": "스크랩 되어 있지 않은 코디입니다."}, status=status.HTTP_400_BAD_REQUEST)
          
        outfit_post_scrap.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OutfitItemScrapDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_outfit_item(self, outfit_item_id):
        return OutfitItem.objects.filter(pk=outfit_item_id).first()

    def get_outfit_item_scrap(self, user, outfit_item):
        return OutfitItemScrap.objects.filter(user=user, outfit_item=outfit_item).first()

    def post(self, request, outfit_item_id):
        outfit_item = self.get_outfit_item(outfit_item_id)
        if not outfit_item:
          return Response({"message": "존재하지 않는 코디 아이템입니다."}, status=status.HTTP_404_NOT_FOUND)

        if self.get_outfit_item_scrap(request.user, outfit_item):
            return Response({"message": "이미 스크랩 되어있는 코디 아이템입니다."}, status=status.HTTP_409_CONFLICT)
            
        OutfitItemScrap.objects.create(user=request.user, outfit_item=outfit_item)
        return Response(status=status.HTTP_201_CREATED)

    def delete(self, request, outfit_item_id):
        outfit_item = self.get_outfit_item(outfit_item_id)
        if not outfit_item:
          return Response({"message": "존재하지 않는 코디 아이템입니다."}, status=status.HTTP_404_NOT_FOUND)

        outfit_item_scrap = self.get_outfit_item_scrap(request.user, outfit_item)
        if not outfit_item_scrap:
            return Response({"message": "스크랩 되어 있지 않은 코디 아이템입니다."}, status=status.HTTP_400_BAD_REQUEST)
          
        outfit_item_scrap.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        