from rest_framework.routers import DefaultRouter
from chat.viewsets import ChatRoomViewSets, MessageViewSets

router = DefaultRouter()
router.register('chatroom', ChatRoomViewSets, basename='chatroom')
router.register('message', MessageViewSets, basename='message')
urlpatterns = router.urls
urlpatterns += [
    path('sum_numbers/', sumNumbersView, name='sum_numbers'),
]