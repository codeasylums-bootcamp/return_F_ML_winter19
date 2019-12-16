from commerce.viewsets import LaptopViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('laptops',LaptopViewset)

