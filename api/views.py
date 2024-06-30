from rest_framework import viewsets,request,status
from .models import Product, Rating
from .serializers import ProductSerializer, RatingSerializer

from rest_framework.decorators import action
from rest_framework.response import Response

from django.contrib.auth.models import User


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


    
    @action(detail=True, methods=['post'])
    def rate_product(self, request, pk=None):
        if 'stars' in request.data:
            '''
            create or update 
            '''
            product = Product.objects.get(id=pk)
            stars = request.data['stars']
            username = request.data['username']
            user = User.objects.get(username=username)

            try:
                # update
                rating = Rating.objects.get(user=user.id, product=product.id) # specific rate 
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                json = {
                    'message': 'Product Rate Updated',
                    'result': serializer.data
                }
                return Response(json , status=status.HTTP_202_ACCEPTED)

            except:
                # create if the rate not exist 
                rating = Rating.objects.create(stars=stars, product=product, user=user)
                serializer = RatingSerializer(rating, many=False)
                json = {
                    'message': 'Meal Rate Created',
                    'result': serializer.data
                }
                return Response(json , status=status.HTTP_201_CREATED)

        else:
            json = {
                'message': 'stars not provided'
            }
            return Response(json , status=status.HTTP_400_BAD_REQUEST)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer