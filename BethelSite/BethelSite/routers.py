from rest_framework import routers
from prejub.viewsets import SuggestionViewSet

router = routers.DefaultRouter()

router.register(r'sugerencias', SuggestionViewSet)
